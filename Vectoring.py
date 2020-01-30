import math

def reward_function(params):
  distance_from_center = params['distance_from_center']
  marker = 0.4 * params['track_width']
  reward = 0
  
  #Vectors
  waypoints = params['waypoints'] + params['waypoints']
  closest_waypoints = params['closest_waypoints']
  i = closest_waypoints[1]
  angle = calculate_angle(waypoints[i], waypoints[i+1], waypoints[i+2])
  print("Angle: "+str(angle))
  steering_angle = params['steering_angle']
  
  #Speed
  speed = params['speed']
  straight = 160 <= angle
  max_speed = 0
  max_steering = 0
  min_steering = 0
  if straight:
    max_speed = 5
    max_steering = 3
    min_steering = 0
  else:
    max_speed = 2
    max_steering = 25
    min_steering = 10
  
  print ("Speed: "+str(max_speed))
  print ("Max Steering: "+str(max_steering))
  print ("Min Steering: "+str(min_steering))
  if speed > max_speed:
    reward *= 0.5
  
  #Mitte
  if distance_from_center <= marker:
    reward += 1
  else:
    reward *= 0.6
  
  if min_steering <= steering_angle <= max_steering:
    reward += 1.0
  else:
    reward = 1e-3
  
  return reward

# Returns the angle between three points
# https://onlinemschool.com/math/library/vector/angl/
def calculate_angle(point_a, point_b, point_c):
  v_ba = [point_b[0]-point_a[0],point_b[1]-point_a[1]]
  v_bc = [point_b[0]-point_c[0],point_b[1]-point_c[1]]
  return int(math.degrees(angle(v_ba,v_bc)))

def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def get_test_params():
    return {
        'x': 0.7,
        'y': 1.05,
        'heading': 160.0,
        'track_width': 0.45,
        'is_reversed': False,
        'steering_angle': 0.0,
        'closest_waypoints': [0, 1],
        'distance_from_center': 0,
        'speed': 5,
        'waypoints': [
            [0.75, -0.7],
            [1.0, 0.0],
            [0.7, 0.52],
            [0.58, 0.7],
            [0.48, 0.8],
            [0.15, 0.95],
            [-0.1, 1.0],
            [-0.7, 0.75],
            [-0.9, 0.25],
            [-0.9, -0.55],
        ]
    }

def get_test_params2():
    return {
        'x': 0.7,
        'y': 1.05,
        'heading': 160.0,
        'track_width': 0.45,
        'is_reversed': False,
        'steering_angle': 0.0,
        'closest_waypoints': [6, 7],
        'distance_from_center': 0,
        'speed': 5,
        'waypoints': [
            [0.0, 0.0],
            [1, 1],
            [2.2, 1.2],
            [3.4, 0.5],
            [4.8, -0.6],
            [6.5, -0.2],
            [7.7, 0.7],
            [9.0759586532806, 1.8025243700483],
            [10.3255199474553, 2.8908519488457],
            [11.2929222397197, 3.979179527643],
        ]
    }

print("Reward: "+str(reward_function(get_test_params2())))
print (calculate_angle([0.48, 0.8], [0.15, 0.95], [-0.1, 1.0]))