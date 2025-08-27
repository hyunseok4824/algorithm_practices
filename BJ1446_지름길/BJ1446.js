const fs = require('fs')
const filePath = process.platform === 'linux' ? '/dev/stdin' : 'BJ1446_input.txt'
const input = fs.readFileSync(filePath).toString().trim().split('\n')

const [N, D] = input[0].split(' ').map(Number)

// start → [[end, dist], ...]
const g = Array.from({ length: D + 1 }, () => [])

for (let i = 1; i <= N; i++) {
  const [s, e, w] = input[i].split(' ').map(Number)
  if (e > D) continue
  if (e - s <= w) continue
  g[s].push([e, w])
}

const INF = 1e15
const dp = Array(D + 1).fill(INF)
dp[0] = 0

for (let i = 0; i < D; i++) {
  // 일반 도로 한 칸 전진
  dp[i + 1] = Math.min(dp[i + 1], dp[i] + 1)
  // i에서 시작하는 지름길들 완화
  for (const [e, w] of g[i]) {
    dp[e] = Math.min(dp[e], dp[i] + w)
  }
}

console.log(dp[D])