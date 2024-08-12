def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def distance2(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

def distance3(c1, c2):
    d = distance2(c1[:2], c2[:2])
    return d, c1[2]+c2[2] >= d

def perimeter(points):
    sgm = 0
    sz_points = len(points)
    for i in range(sz_points):
        sgm += distance2(points[i], points[(i+1)%(sz_points)])
    return sgm

exec(input().strip())