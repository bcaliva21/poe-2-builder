# Damage overview

Use this chapter to locate *where* a scaling option lands before comparing options.

## Hit vs DoT

- **Hits** can crit (unless something says otherwise) and can inflict many ailments based on hit damage / chance rules.
- **Damage over time** generally does not crit unless a specific effect says it can.
- A build that is mostly DoT often cares less about crit chance than a hit build does.

## Rough evaluation order for advice

When comparing two damage stats for a character:

1. Confirm the skill's damage profile (hit, DoT, minion, totem, etc.).
2. Confirm which damage types are actually present after conversion.
3. Confirm defensive mitigation of the *target* only when chance-to-ailment depends on it.
4. Apply offensive multipliers (increased/more) and crit expectation if hits matter.
5. Apply on-enemy effects (Shock, Exposure, Wither, marks, etc.) with correct stacking.
6. Multiply by uptime / coverage (ailment uptime, fortify uptime, etc.).

## Expected hit damage with crit

For ordinary critting hits:

`average_hit ≈ base_hit * (1 + non_crit_multipliers...) * (crit_chance * crit_multi + (1 - crit_chance) * 1)`

Use the character's effective crit chance and crit multi from the session when present. If only "crit chance on tree" is known and not effective chance vs the relevant skill, say so.

## Enemy damage taken

Effects like Shock make the target take increased damage. These are not the same as your "increased damage" mods. They are often additive with other increased damage-taken effects. See `ailments.md` and `shock.md`.

## Do not fake PoB

This repo does not replace Path of Building's full calc engine. For exact DPS, prefer PoB numbers from the session export. Use these chapters for relative decisions and sanity checks.
