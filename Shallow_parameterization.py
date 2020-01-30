def reward_function(param):

    distance_from_center = param['distance_from_center']

    marker_1 = 0.1 * param['track_width']
    
    if distance_from_center <= marker_1:
        reward = 1.0
    else:
        reward = 1e-3  # likely crashed / close to off track

    all_wheels_on_track = param['all_wheels_on_track']
    speed = param['speed']

    MIN_SPEED_THRESHOLD = 2.0 
    MAX_SPEED_THRESHOLD = 5.0 
    if not all_wheels_on_track:
        # Penalize if the car goes off track
        reward = 1e-3
    elif speed < MIN_SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward *= 0.8
    elif speed > MAX_SPEED_THRESHOLD:
        # Penalize if the car goes too slow
        reward *= 0.6
    else:
        # High reward if the car stays on track and goes fast
        reward += 1.0

    steering = abs(param['steering_angle']) # We don't care whether it is left or right steering
    # Penalize if car steer too much to prevent zigzag
    STEERING_THRESHOLD = 18.0
    if steering > STEERING_THRESHOLD:
        reward *= 0.8
    else:
        reward += 1.0

    isofftrack = param['is_offtrack']
    if isofftrack
        reward = 1e-3
    else:
        reward += 0.1
        
    isreversed = param['is_reversed']
    if isreversed
        reward = 1e-3
    else:
        reward += 0.1

    isCrashed = param['is_crashed']
    if isCrashed
        reward = 1e-3
    else:
        reward += 0.1

    isleftofcenter = param['is_left_of_center']
    if isleftofcenter
        reward = 1e-3
    else:
        reward += 0.1    

    return reward   