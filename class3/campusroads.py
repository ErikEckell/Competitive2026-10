from dataclasses import dataclass
import math
import sys

EPS = 1e-12

@dataclass
class point:
    x: float
    y: float

    def __add__(self, t):
        return point(self.x + t.x, self.y + t.y)
    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)
    def dot(self, a):
        return self.x*a.x + self.y*a.y

    def norm(self):
        return math.sqrt(self.dot(self))
    
    def rotate(self, theta):
        return point(
            self.x * math.cos(theta) - self.y * math.sin(theta),
            self.x * math.sin(theta) + self.y * math.cos(theta),
        )
    
    def angle(self, a, c):
        s1 = a - self
        d1 = s1.norm()

        s2 = c - self
        d2 = s2.norm()

        return math.acos(s1.dot(s2)/(d1*d2))

    def cross(self, p):
        return self.x*p.y - p.x*self.y


def find_point_at_distance(points, target_distance):
    current_distance = 0.0
    
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        
        segment_length = (p2 - p1).norm()
        
        if current_distance + segment_length >= target_distance:
            remaining = target_distance - current_distance
            if segment_length < EPS:
                return p1
            
            t = remaining / segment_length
            return point(
                p1.x + t * (p2.x - p1.x),
                p1.y + t * (p2.y - p1.y)
            )
        
        current_distance += segment_length
    
    return points[-1]


def read_input(infile):
    num_roads = int(infile.readline())
    
    for _ in range(num_roads):
        parts = infile.readline().split()
        n_points = int(parts[0])
        n_trees = int(parts[1])
        
        points = []
        for _ in range(n_points):
            coords = list(map(float, infile.readline().split()))
            points.append(point(coords[0], coords[1]))
        
        yield points, n_trees


def solver(road_num, points, n_trees):
    total_length = 0.0
    for i in range(len(points) - 1):
        total_length += (points[i + 1] - points[i]).norm()
    
    tree_distance = total_length / (n_trees - 1) if n_trees > 1 else 0
    
    print(f"Road #{road_num}:")
    
    for tree_idx in range(n_trees):
        distance = tree_idx * tree_distance
        tree_point = find_point_at_distance(points, distance)
        print(f"{tree_point.x:.2f} {tree_point.y:.2f}")
    
    print()


road_num = 1
for points, n_trees in read_input(sys.stdin):
    solver(road_num, points, n_trees)
    road_num += 1