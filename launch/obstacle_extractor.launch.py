from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='obstacle_detector',
            executable='obstacle_extractor_node',
            name='obstacle_extractor',
            remappings=[
                ('/scan', '/merged_scan'),
                ('/pcl', '/truck1/front_lidar'),
                ('/pcl2', '/truck1/front_lidar'),
            ],
            parameters=[{
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
                'max_circle_radius': 2.4, #0.6
                'radius_enlargement': 0.3,
                'frame_id': 'map',
            }],
            output='screen'
        )
    ])