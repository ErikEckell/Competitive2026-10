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

@dataclass
class segment:
    p: point
    q: point

    def point_on_segment(self, point):
        cross = (point - self.p).cross(self.q - self.p)
        if abs(cross) > EPS:
            return False
        if abs((self.q - self.p).x) > EPS:
            return min(self.p.x, self.q.x) <= point.x <= max(self.p.x, self.q.x)
        else:
            return min(self.p.y, self.q.y) <= point.y <= max(self.p.y, self.q.y)

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)
        
        standard_intersect = ( #la que ya existia
            (cross1 * cross2 < 0 or
                (include_p and math.fabs(cross2) < EPS)
                or (include_q and math.fabs(cross1) < EPS))
            and (cross3 * cross4 < 0
                or (include_p and math.fabs(cross4) < EPS)
                or (include_q and math.fabs(cross3) < EPS))
        )
        
        if standard_intersect:
            return True
        if self.point_on_segment(seg2.p) or self.point_on_segment(seg2.q):
            return True
        if seg2.point_on_segment(self.p) or seg2.point_on_segment(self.q):
            return True
        return False
    
def read_input(infile):
    num_cases = int(infile.readline())
    
    for _ in range(num_cases):
        num_segments = int(infile.readline())
        segments = []
        
        for _ in range(num_segments):
            segment = list(map(int, infile.readline().split()))
            segments.append(segment)
        
        yield segments

def solver(segments):
    segments_object = [] #lista de segmentos creados
    isolated_count = 0 #contador aislados

    for value in segments:
        p1 = point(value[0], value[1])
        p2 = point(value[2], value[3])
        segments_object.append(segment(p1, p2))
    
    for i in range(len(segments_object)):
        is_isolated = True
        for j in range(len(segments_object)):
            if i != j:
                if segments_object[i].does_intersect(segments_object[j]):
                    is_isolated = False
                    break
        if is_isolated:
            isolated_count += 1
                    
    print(isolated_count)

for case in read_input(sys.stdin):
    solver(case)
