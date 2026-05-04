import os
import xacro
import subprocess
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction, SetEnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
    pkg = get_package_share_directory('mobilebot_description')
    xacro_file = os.path.join(pkg, 'urdf', 'mobilebot.xacro')

    # Generate URDF from xacro
    robot_description = xacro.process_file(xacro_file).toxml()

    # Write URDF to tmp
    urdf_file = '/tmp/mobilebot.urdf'
    with open(urdf_file, 'w') as f:
        f.write(robot_description)

    # Convert URDF to SDF
    sdf_file = '/tmp/mobilebot.sdf'
    subprocess.run(['gz', 'sdf', '-p', urdf_file],
                   stdout=open(sdf_file, 'w'),
                   stderr=subprocess.DEVNULL)

    return LaunchDescription([
        SetEnvironmentVariable('GZ_VERSION', 'harmonic'),

        # 1. Start Gazebo
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', 'empty.sdf'],
            output='screen'
        ),

        # 2. Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
            output='screen'
        ),

        # 3. Spawn from SDF after 10 seconds
        TimerAction(
            period=10.0,
            actions=[
                ExecuteProcess(
                    cmd=['gz', 'service', '-s', '/world/empty/create',
                         '--reqtype', 'gz.msgs.EntityFactory',
                         '--reptype', 'gz.msgs.Boolean',
                         '--timeout', '5000',
                         '--req', f'sdf_filename: "{sdf_file}", name: "mobilebot", pose: {{position: {{z: 0.05}}}}'],
                    output='screen'
                ),
            ]
        ),

        # 4. Bridge after 12 seconds
        TimerAction(
            period=12.0,
            actions=[
                Node(
                    package='ros_gz_bridge',
                    executable='parameter_bridge',
                    arguments=[
                        '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
                        '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
                        '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
                        '/lidar@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
                    ],
                    output='screen'
                ),
            ]
        ),
    ])
