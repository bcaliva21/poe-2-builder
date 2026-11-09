# Shock

Shock is the non-damaging lightning ailment that makes the target take increased damage.

Values below are the commonly documented EA defaults. If a patch or tooltip disagrees, prefer the newer source and update this file.

## Base rules

- Default Shock effect: target takes **20% increased damage**.
- Default duration: often cited as **8s** on monsters / **4s** on players (confirm if answering duration-sensitive questions).
- Only the **highest magnitude** Shock normally applies at once (unless an ascendancy/effect like Stormweaver "Strike Twice" says otherwise).
- Shock magnitude has a **hard cap** commonly documented at **100% increased damage taken** from Shock.
- Magnitude modifiers multiply the base effect. Example: `30% increased magnitude of Shock` → `20% * 1.30 = 26%` increased damage taken.
- Magnitude mods do not, by themselves, change duration.

## Chance to Shock

Documented default model:

- Lightning damage from a hit has a chance to Shock based on lightning damage dealt relative to the target's ailment threshold.
- Commonly cited: **1% chance to Shock per 4% of ailment threshold** dealt as lightning by that hit (community guides describe this after mitigation on the target).
- `increased chance to Shock` and `increased chance to inflict Ailments` scale that chance; they are not a flat "base chance" unrelated to the hit.
- No meaningful lightning contribution → no meaningful natural Shock from hits unless another effect forces Shock.

Because chance depends on hit size vs threshold, bigger hits (including crits) can improve Shock **application**, but that is still separate from Shock **magnitude**.

## Ascendancy / special cases (examples)

- **Strike Twice** (Stormweaver): can allow more than one Shock magnitude instance to matter, often with a duration penalty. Read the current notable text before advising.
- **Shaper of Storms** (Stormweaver): changes how Shock is inflicted / calculated. Do not use default chance assumptions blindly if this is allocated - read the notable and session tree.

## Comparing Shock magnitude vs other stats

Use this checklist instead of a fixed FAQ:

1. Does the build apply Shock at all on the content that matters (packs vs bosses)?
2. What is current Shock effect vs the 100% cap?
3. What is Shock uptime on that content?
4. Is the alternative stat (crit chance, lightning damage, cast speed, etc.) entering a different bucket with more headroom?
5. Estimate relative gain:
   - More magnitude ≈ raises the on-enemy increased-damage-taken multiplier while Shock is up.
   - More crit chance ≈ raises average hit damage for crittable hits (and may indirectly help application via larger hits).
6. If session lacks shock effect, crit chance, or damage profile, ask for those PoB lines before a firm verdict.

## Worked intuition

Suppose Shock is up permanently and current effect is 40% increased damage taken (i.e. target takes `1.40x` from the Shock bucket, ignoring other damage-taken mods).

- Raising effect to 48% is `1.48 / 1.40 ≈ +5.7%` more damage while shocked, before other additive damage-taken peers.
- If other increased damage-taken mods already exist, Shock's contribution is additive with them - compute with the combined sum when known.

Always recompute with the character's actual numbers when present.
