+++
id = "ref/spell/changestaff"
kind = "spell"
title = "Changestaff"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "changestaff", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 7 },
]
casting_time = "1 round"
components = "V, S, F (a quarterstaff that has been carved and polished for 28 days)"
range = "touch"
effects = [
  { label = "Target", value = "your touched staff" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Druid
Casting time: 1 round
Components: V, S, F (a quarterstaff that has been carved and polished for 28 days)
Range: touch
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: your touched staff
:::

**Sources:** PRPG Core Rulebook pg 253

You change a specially prepared quarterstaff into a Huge treant-like creature, about 24 feet tall.
When you plant the end of the staff in the ground and speak a special command to conclude the
casting of the spell, your staff turns into a creature that looks and fights just like a treant. The
staff-treant defends you and obeys any spoken commands. However, it is by no means a true treant; it
cannot converse with actual treants or control trees. If the staff-treant is reduced to 0 or fewer
hit points, it crumbles to powder and the staff is destroyed. Otherwise, the staff returns to its
normal form when the spell duration expires (or when the spell is dismissed), and it can be used as
the focus for another casting of the spell. The staff-treant is always at full strength when
created, despite any wounds it may have incurred the last time it appeared.

### Mythic Changestaff

**Sources:** Mythic Adventures pg 88\
The treant-like creature created with this spell is considered a mythic creature, and it gains DR
10/epic and slashing instead of gaining DR 10/slashing.

_Augmented (7th):_ If you expend two uses of mythic power, the creature gains the savage
[mythic template](ref/rule/mythic-simple-templates).
