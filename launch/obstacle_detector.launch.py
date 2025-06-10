import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, Shutdown
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_nodes(context, *, num_trucks):
    nodes = []

    for i in range(1, int(num_trucks)):
        node = Node(
            package='obstacle_detector',
            executable='obstacle_extractor_node',
            name=f'obstacle_extractor_{i}',
            remappings=[
                ('/scan', '/merged_scan'),
                ('/pcl', '/truck1/front_lidar'),
                ('/pcl2', f'/truck{i}/front_lidar/roi'),
            ],
            parameters=[{
                'truck_id': i,
                'active': True,
                'use_scan': False,
                'use_pcl': False,
                'use_pcl2': True,
                'use_sim_time': True,
                'use_split_and_merge': True,
                'circles_from_visibles': True,
                'discard_converted_segments': True,
                'transform_coordinates': True,
                'min_group_points': 7, #10
                'max_group_distance': 0.5, #0.1
                'distance_proportion': 0.01628,
                'max_split_distance': 0.2, #0.2
                'max_merge_separation': 0.2,
                'max_merge_spread': 0.2,
                'max_circle_radius': 6.0, #0.6
                'radius_enlargement': 0.3,
                'frame_id': 'lidar_frame',
            }],
            output='screen'
        )
        nodes.append(node)
        
    return nodes

def launch_setup(context):
    num_trucks = LaunchConfiguration('NumTrucks').perform(context)
    return generate_nodes(context, num_trucks=num_trucks)

def generate_launch_description():
    declare_num_trucks = DeclareLaunchArgument(
        'NumTrucks',
        default_value='1',
        description='Number of trucks to launch'
    )

    return LaunchDescription([
        declare_num_trucks,
        OpaqueFunction(function=launch_setup)
    ])
