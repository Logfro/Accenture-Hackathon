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
  
  #Middle
  if distance_from_center <= marker:
    reward = 2
  else:
    reward = 0.75

  if speed > max_speed:
    reward *= 0.5
  
  if min_steering <= steering_angle <= max_steering:
    reward += 3
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

def get_test_params2():
    return {
        'x': 0.7,
        'y': 1.05,
        'heading': 160.0,
        'track_width': 0.45,
        'is_reversed': False,
        'steering_angle': 1,
        'closest_waypoints': [1, 2],
        'distance_from_center': 4,
        'speed': 5,
        'waypoints': [
            [0, 0],
            [1, 1],
            [2.2638341785858, 1.2382063662274],
            [3.4327786150719, 0.5126546470291],
            [4.8032651957797, -0.6159813606126],
            [6.5365276360867, -0.2128970721691],
            [7.7860889302614, 0.7545052200952],
            [9.0759586532806, 1.8025243700483],
            [10.3255199474553, 2.8908519488457],
            [11.2929222397197, 3.979179527643],
        ]
    }

print("Reward: "+str(reward_function(get_test_params2())))
print (calculate_angle([0.48, 0.8], [0.15, 0.95], [-0.1, 1.0]))