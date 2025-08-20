const fs = require('fs')
const filePath = process.platform === 'linux' ? '/dev/stdin' : "BJ18352_input.txt"
const input = fs.readFileSync(filePath).toString().trim().split('\n')

/*
  input 첫 번째 줄
  N : 도시의 개수 (노드)
  M : 도로의 개수 (간선)
  K : 거리 정보 (최단 경로 거리 목표)
  X : 출발 도시 정보
*/
const [N, M, K, X] = input[0].split(' ').map(Number) 

const adjList = Array.from({length: N+1}, () => []) // 간선 정보 담는 배열
for (let i=1; i <= M; i++) {
  const [start, end] = input[i].split(' ').map(Number) 
  adjList[start].push(end)
}
const dist = new Array(N+1).fill(-1)  // 방문 체크


function bfs(start) {
  const q = [start]
  let front = 0
  const result = []
  dist[start] = 0
  
  while (q.length > front) { 
    
    const cur = q[front++]

     // 길이가 K면 종료
    if (dist[cur] === K) {
      result.push(cur)
      continue
    }

    for (const nxt of adjList[cur]) {
      // 방문하지 않은 노드만 q에 담음
      if (dist[nxt] === -1) {
        dist[nxt] = dist[cur] + 1
        q.push(nxt)
      }
    }
  }
  return result.length > 0 ? result.sort((a,b)=>a-b).join('\n') : -1
}

console.log(bfs(X))


