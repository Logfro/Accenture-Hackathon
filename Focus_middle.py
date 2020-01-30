def reward_function(param):

    distance_from_center = param['distance_from_center']

    marker_1 = 0.1 * param['track_width']
    marker_2 = 0.25 * param['track_width']
    marker_3 = 0.4 * param['track_width']
    marker_4 = 0.6 * param['track_width']
    marker_5 = 0.8 * param['track_width']

    if distance_from_center <= marker_1:
        reward = 4.0
    elif distance_from_center <= marker_2:
        reward = 2.0
    elif distance_from_center <= marker_3:
        reward = 1.0
    elif distance_from_center <= marker_4:
        reward = 0.5
    elif distance_from_center <= marker_5:
        reward = 0.25
    else:
        reward = 1e-3  # likely crashed / close to off track


    all_wheels_on_track = param['all_wheels_on_track']
    speed = param['speed']

    SPEED_THRESHOLD = 2.0 
    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward *= 0.8
    else:
        # High reward if the car stays on track and goes fast
        reward += 1.0


    steering = abs(param['steering_angle']) # We don't care whether it is left or right steering
    # Penalize if car steer too much to prevent zigzag
    STEERING_THRESHOLD = 20.0
    if steering > STEERING_THRESHOLD:
        reward *= 0.8
    else:
        reward += 1.0
    return reward   