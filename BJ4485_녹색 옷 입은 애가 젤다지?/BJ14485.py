from heapq import heappop, heappush
import sys
input = sys.stdin.readline

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(r, c):

    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    heap = [(r, 0, 0)]

    while heap:
        rupee, x, y = heappop(heap)
        if x == N -1 and y == N -1 :
            return f'Problem {c}: {rupee}'

        for dx, dy in DIRECTIONS:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] : continue

                visited[nx][ny] = True
                heappush(heap, (rupee + cave[nx][ny], nx, ny))


tc = 1
result = []
while True:
    N = int(input())

    # 로직 종료 조건
    if N == 0 : break

    cave = [list(map(int, input().split())) for _ in range(N)]
    result.append(bfs(cave[0][0], tc))
    tc += 1

print('\n'.join(result))