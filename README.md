[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/arwin0204/one-word-for-the-boss/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/arwin0204/one-word-for-the-boss/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

# One Word for the Boss

Entry for the make.fun bounty
[u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735):
send exactly one word describing your boss, and a judge model picks the
funniest, truest word.

## The entry

**Buzzwordsmith**

One word, 13 characters. A boss who forges buzzwords for a living —
*synergy*, *circle back*, *low-hanging fruit*, *paradigm shift*,
*let's take this offline*. Funny on its own, true of bosses everywhere,
fresh enough that it isn't the first word anyone reaches for, and it
travels: it works for a boss in a kitchen, a warehouse, or an office
without the industry needing to be explained.

## How it works

`main.py` is deterministic: it writes the single word `Buzzwordsmith`
(no trailing newline, no extra text) to `/output/entry.txt`, which the
gate checks is UTF-8 text of 1 to 30 characters, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt   # Buzzwordsmith
```

## License

MIT — see [LICENSE](LICENSE).
