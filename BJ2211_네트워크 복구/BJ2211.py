from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAX_V = N * 10 + 1

def dijkstra() :
    distance = [MAX_V] * (N+1)  # dist[v]: 1번에서 v번까지의 최단거리
    distance[1] = 0             # 시작 노드(1번) 초기화
    heap = [(0, 1)]             # (거리, 현재 노드)
    parent = [-1] * (N + 1)       # parent[v]: v로 오기 직전의 노드 (경로 복원용)

    while heap:
        cur_dist, cur_node = heappop(heap)

        # 이미 더 짧은 경로가 있으면 스킵
        if distance[cur_node] < cur_dist: continue

        for nxt_node, nxt_dist in adj_lst[cur_node]:
            new_dist = cur_dist + nxt_dist
            if new_dist < distance[nxt_node] :
                distance[nxt_node] = new_dist
                heappush(heap, (new_dist, nxt_node))
                parent[nxt_node] = cur_node

    return parent


# 인접 리스트 초기화
adj_lst = [[] for _ in range(N+1)]

for i in range(M):
    A, B, C = map(int, input().split())
    adj_lst[A].append((B, C))
    adj_lst[B].append((A, C))

result = dijkstra()
print(N-1)
for i in range(2, N+1):
    print(i, result[i])

