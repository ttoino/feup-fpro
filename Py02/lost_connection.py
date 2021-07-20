import math
def time_until_lost_connection(direction_a, direction_b):
    angle = direction_a - direction_b
    
    cos = math.cos(angle/360*math.tau)
    
    d = 35 / math.sqrt((1 - cos) * 2)
    
    t = d/5*60
    
    return round(t, 3)
