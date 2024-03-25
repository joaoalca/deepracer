import math

 

def reward_function(params):  

    waypoints = params['waypoints']

    closest_waypoints = params['closest_waypoints']

    heading = params['heading']
    all_wheels_on_track = params['all_wheels_on_track']

    progress = params['progress']
    steps = params['steps']

    reward = 1.0
    next_point = waypoints[closest_waypoints[1]]

    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    DIRECTION_THRESHOLD = 10.0

    if direction_diff > DIRECTION_THRESHOLD:

        reward *= 0.5

    acuracy = (progress / steps) * 10


    if not all_wheels_on_track:
        return 1e-3

    return float(reward*acuracy)