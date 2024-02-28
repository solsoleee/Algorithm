def point_line_distance(x1, y1, x2, y2, x3, y3):
    
    return abs((y2 - y1) * x3 - (x2 - x1) * y3 + x2 * y1 - y2 * x1) / ((y2 - y1)**2 + (x2 - x1)**2)**0.5

def min_triangle_height(points, N):
    min_height = float('inf')
    
    for i in range(N):
        for j in range(i + 1, N):
            max_height = 0
            for k in range(N):
                if k != i and k != j:
                    height = point_line_distance(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1])
                    max_height = max(max_height, height)
            min_height = min(min_height, max_height)
    
    return min_height


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]


min_h = min_triangle_height(points, N)


if min_h == float('inf'):
    print(0)
else:
    print(f"{min_h:.7f}")
