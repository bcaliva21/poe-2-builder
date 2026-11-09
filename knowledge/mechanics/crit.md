# Critical strikes

## What crit scales

- Crit chance raises the fraction of hits that use crit damage.
- Crit multi (critical damage bonus) raises how strong those crits are.
- Crit generally matters for **hits**. Pure DoT setups often gain little from crit chance unless something makes the DoT crit or the build still has an important hitting component (ailment application via hits, etc.).

## Expected value intuition

If effective crit chance is `c` (0-1) and crit hits deal `m` times a non-crit (where `m` includes base crit bonus):

`crit_dps_factor = (1 - c) + c * m`

Marginal value of more chance is highest when `c` is mid-range and `m` is large. If already near 100% effective chance, more chance is weak and multi (or other multipliers) is usually better.

## Common pitfalls

- "Crit chance on tree/gear" is not always the same as effective chance for the skill you care about (local weapon crit, spell vs attack, supports, blind, enemy aversion, etc.).
- Crit does **not** automatically mean higher Shock magnitude. Crit can help Shock **chance** indirectly if it makes lightning hits bigger (and chance depends on damage vs threshold), but magnitude is a separate stat. See `shock.md`.
- Lucky / unlucky / extra crit rolls change effective chance; don't assume sheet chance equals real chance without noting those effects.

## When answering crit questions

Require or request from the session when possible:

- effective crit chance for the main skill
- crit multi / critical damage bonus
- whether the main damage is hit or DoT
- any "never crit" or "always crit" effects
