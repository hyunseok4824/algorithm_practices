import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = 1000 * 200_000 + 1  # 넉넉하게

def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, cur = heappop(hq)
        if d != dist[cur]:
            continue
        for nxt, w in adj[cur]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heappush(hq, (nd, nxt))
    return dist

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())

d1  = dijkstra(1)
dV1 = dijkstra(v1)
dV2 = dijkstra(v2)

# 1 -> v1 -> v2 -> N  /  1 -> v2 -> v1 -> N
path1 = d1[v1] + dV1[v2] + dV2[N]
path2 = d1[v2] + dV2[v1] + dV1[N]

ans = min(path1, path2)
print(-1 if ans >= INF else ans)