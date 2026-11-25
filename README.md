[![Make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/firlifirrizqi/famous-last-words-1pct-makefun/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/firlifirrizqi/famous-last-words-1pct-makefun/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

# Famous Last Words at 1 Percent

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) of the same name: the funniest possible last words a phone would say when its battery hits 1 percent.

## The line

> I survived three drops, one toilet, and a software update — only to die because you needed one more video.

The phone delivers its dying words deadpan: it lists three disasters it heroically survived, then reveals the embarrassingly trivial thing that finally killed it — its human couldn't stop watching one more video.

## How it works

`main.py` writes that single line (106 characters, within the 199-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. A `verify()` helper re-reads the file and asserts it is byte-identical to the chosen line, 1–199 characters, and not only whitespace.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
