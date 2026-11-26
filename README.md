# office-joke-open

[![make.fun · u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/busetdah6464/office-joke-open/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/busetdah6464/office-joke-open/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One-line office joke for the [Make the AI Judge Laugh: the Office Joke Open](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) bounty on make.fun.

## The joke

> At the team-building trust fall, nobody caught me — HR logged it as a successful lesson in self-reliance.

## Build notes

- The joke was written fresh for this bounty: a team-building trust fall,
  a setup everyone in an office recognises, with the payoff landing in the
  last few words when HR reframes a dropped colleague as a training success.
- Deliberately avoids the well-worn office-joke clusters (reply-all, the
  meeting that could have been an email, the jammed printer) to stay fresh
  against the judge's freshness criterion.
- One file, one joke, no dependencies: `main.py` only uses `os` from the
  standard library and writes the same bytes on every run.

## How it works

`main.py` (Python 3 standard library only, no network, fully deterministic)
writes the single-line joke to `/output/entry.txt`. The joke is 105 characters,
well under the 200-character cap, and the program always writes exactly the
same text on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

- Competition: `u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232`
- Prize: $2 to the single funniest office joke, judged head-to-head by an AI judge
- Entry is free; deadline 26 Nov 2026, 08:35 UTC
