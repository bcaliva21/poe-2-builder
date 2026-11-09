# Ailments

Ailments are debuffs tied to damage types. Exact numbers can shift by patch - verify against `sources.md` and in-game tooltips when precision matters.

## Family

| Ailment | Typical association | Notes |
|---|---|---|
| Bleeding | Physical | Damaging; usually needs an explicit bleed chance |
| Ignite | Fire | Damaging DoT from fire hits / flammability rules |
| Poison | Chaos (+ phys contribution rules) | Damaging; usually needs poison chance |
| Chill | Cold | Non-damaging slow; magnitude vs threshold |
| Freeze | Cold | Buildup / threshold crowd control |
| Shock | Lightning | Non-damaging; target takes increased damage |
| Electrocute | Lightning | CC-style; often needs specific skill contribution |

## Damaging vs non-damaging

- Damaging ailments (bleed, ignite, poison) deal damage over time. Crit usually does not apply to those DoTs unless an effect says otherwise.
- Non-damaging ailments (chill, freeze, shock, electrocute) alter the target without being a DoT DPS line themselves. Shock still increases *other* damage taken.

## Chance / buildup vs magnitude

Keep these separate in every answer:

- **Chance or buildup** - can you apply it reliably?
- **Magnitude / effect** - how strong is it when applied?
- **Duration / uptime** - does it stay up on the targets you care about?

A magnitude upgrade is weak if uptime is near zero. Chance upgrades are weak if you already permanently maintain the ailment on relevant targets and only magnitude/duration still moves DPS.

## Thresholds

Many ailments compare hit contribution to the target's **ailment threshold**. Trash mobs often track life closely; rares/uniques/bosses may use adjusted thresholds. Boss uptime can diverge from pack uptime - say so when advising.

## Cross-type contribution

By default, only the associated damage type contributes to an ailment. Mods/skills that let other damage types contribute change both application and (for some ailments) magnitude math. Always check the character's conversion and "contributes to" modifiers before dismissing an ailment path.
