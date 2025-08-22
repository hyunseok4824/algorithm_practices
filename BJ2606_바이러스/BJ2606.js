const fs = require('fs')
const filePath = process.platform === 'linux'? 'dev/stdin' : 'BJ2606_input.txt'
const input = fs.readFileSync(filePath).toString().trim().split('\n')

const N = parseInt(input[0])
const M = parseInt(input[1])

const visited = Array(N+1).fill(0)
const adjList = Array.from({length: N+1}, () => [])

for (let i=2; i<= M+1; i++) {
  const [v1, v2] = input[i].split(' ').map(Number)
  adjList[v1].push(v2)
  adjList[v2].push(v1)
}

function bfs(start) {
  const q = [start]
  let front = 0
  visited[start] = 1
  let cnt = 0
  while (q.length > front) {
    const v = q[front++]
    for (const nxt of adjList[v]) {
      if (visited[nxt] === 0) {
        cnt ++
        visited[nxt] = 1
        q.push(nxt)
      }
    }
  }
  return cnt
}

console.log(bfs(1))