def on_segment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and 
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False
 
def orientation(p, q, r):
    val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
    if val > 0:
        return 1
    elif val < 0:
        return 2
    else:
        return 0
 
def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    if o1 != o2 and o3 != o4:
        return True
    
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True
    
    return False
 
def intersects_polygon(x1, y1, x2, y2, polygon):
    n = len(polygon)
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        if do_intersect((x1, y1), (x2, y2), p1, p2):
            return True
    return False
 
# Example usage:
polygon = [(4, 2), (4, 1), (3, 1), (3, 2)]
# Example polygon vertices
x1, y1 = 0, 0  # Line segment start point
x2, y2 = 3, 3  # Line segment end point
 
if intersects_polygon(x1, y1, x2, y2, polygon):
    print("The line segment intersects the polygon.")
else:
    print("The line segment does not intersect the polygon.")