from dataclasses import dataclass
import sys

EPS = 1e-12

@dataclass(frozen=True)
class point:
    x: float
    y: float

    def __sub__(self, t):
        return point(self.x - t.x, self.y - t.y)

    def cross(self, p):
        return self.x*p.y - p.x*self.y

@dataclass
class segment:
    p: point
    q: point

    def does_intersect(self, seg2, *, include_p=False, include_q=False):
        cross1 = (seg2.q - self.p).cross(self.q - self.p)
        cross2 = (seg2.p - self.p).cross(self.q - self.p)
        cross3 = (self.q - seg2.p).cross(seg2.q - seg2.p)
        cross4 = (self.p - seg2.p).cross(seg2.q - seg2.p)
        
        return (
            (cross1 * cross2 < 0 or
                (include_p and abs(cross2) < EPS)
                or (include_q and abs(cross1) < EPS))
            and (cross3 * cross4 < 0
                or (include_p and abs(cross4) < EPS)
                or (include_q and abs(cross3) < EPS))
        )

def hull(points):
    points = sorted(set(points), key=lambda p: (p.x, p.y))
    if len(points) <= 2:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and (lower[-1] - lower[-2]).cross(p - lower[-2]) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and (upper[-1] - upper[-2]).cross(p - upper[-2]) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def polygon_area(polygon):
    if len(polygon) < 3:
        return 0
    area = 0
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        area += polygon[i].x * polygon[j].y
        area -= polygon[j].x * polygon[i].y
    return abs(area) / 2

def point_in_polygon(q, polygon):
    if len(polygon) < 3:
        return False

    p = min(polygon, key=lambda v: v.x) - point(1, 0)
    ray = segment(p, q)
    crosses = 0

    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        if ray.does_intersect(segment(polygon[i], polygon[j]), include_p=True):
            crosses += 1

    return crosses % 2 == 1

def read_input(infile):
    kingdoms = []
    missiles = []

    while True:
        line = infile.readline()
        if not line:
            break

        n = int(line.strip())
        if n == -1:
            break

        x, y = map(int, infile.readline().split())
        ps = point(x, y)

        points = [ps]
        for _ in range(n - 1):
            x, y = map(int, infile.readline().split())
            points.append(point(x, y))

        kingdoms.append(points)

    for line in infile:
        missile_parts = line.strip().split()
        if missile_parts:
            missiles.append(point(int(missile_parts[0]), int(missile_parts[1])))

    return kingdoms, missiles

def solver(kingdoms, missiles):
    kingdom_data = []
    for points in kingdoms:
        kingdom_hull = hull(points)
        area = polygon_area(kingdom_hull)
        kingdom_data.append((kingdom_hull, area, False))
    
    for missile in missiles:
        for i, (kingdom_hull, area, _) in enumerate(kingdom_data):
            if point_in_polygon(missile, kingdom_hull):
                kingdom_data[i] = (kingdom_hull, area, True)

    return sum(area for _, area, destroyed in kingdom_data if destroyed)

kingdoms_list, missiles_list = read_input(sys.stdin)

total_area = solver(kingdoms_list, missiles_list)
print(f"{total_area:.2f}")