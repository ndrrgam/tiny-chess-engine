# tiny-chess-engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ndrrgam/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ndrrgam/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python: iterative-deepening
alpha-beta on a fixed node budget (no clock, no random), a transposition
table, null-move pruning, quiescence search, MVV-LVA + killer + history
move ordering, and incremental material + piece-square evaluation. One file,
standard library only, deterministic move for move.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 -P -s main.py
```

It plays the make.fun tiny-chess-01 gauntlet through the env's HTTP routes
(`POST /game`, `POST /move`) until the env answers `done`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xv38kktf&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
