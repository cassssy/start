def orientation(p, q, r):
    # Calculate the orientation of three points (p, q, r).
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def on_segment(p, q, r):
    # Check if point q lies on line segment pr.
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

def do_intersect(p1, q1, p2, q2):
    # Check if line segment p1q1 intersects with p2q2.

    # Find the 4 orientations needed for general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

def find_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    p1 = (x1, y1)
    q1 = (x2, y2)
    p2 = (x3, y3)
    q2 = (x4, y4)

    if do_intersect(p1, q1, p2, q2):
        return "Intersect"
    else:
        return "Do not intersect"

result = find_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
print(result)
