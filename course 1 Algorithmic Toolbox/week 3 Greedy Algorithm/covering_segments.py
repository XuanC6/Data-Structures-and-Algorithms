# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    n = len(segments)
    
    if n == 1:
        points.append(segments[0].end)
        return points

    l = []
    for i in range(n):
        l.append(segments[i].start)
        
    segments_sort = []
    for i in range(n):
        k = l.index(min(l))
        segments_sort.append(segments[k])
        l.pop(k)
        segments.pop(k)
    
    a = segments_sort[0]
    b = segments_sort[1]

    i = 0
    while i<=n-2:
        
        if a[1]>=b[0]:
            c = (b[0],min(a[1],b[1]))
            a = c
        else:
            points.append(a[1])
            a = b
        if i == n-2:
            break
        b = segments_sort[i+2]
        i = i+1
    
    points.append(a[1])
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
