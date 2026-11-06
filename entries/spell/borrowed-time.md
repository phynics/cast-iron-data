+++
id = "ref/spell/borrowed-time"
kind = "spell"
title = "Borrowed Time"
source_ids = ["mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "borrowed_time", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Alchemist, Arcanist, Bard, Investigator, Magus, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Mythic Origins pg 14

A creation of the archmage Nex, this spell allows you to reach ahead in time and draw alacrity from
the future at the expense of your own health. For the duration of this spell, you gain an extra
swift action you can use only during your turn. You can't use this swift action to take a second
immediate action between turns, but you can use it to take a swift action the turn after you've
taken an immediate action. Each time you take an extra swift action in this fashion you take 1 point
of Constitution damage. If you're immune to ability damage, you take 5 points of hit point damage
instead. When the spell ends, you are staggered for 1d4+1 rounds from the temporal backlash.

### Mythic Borrowed Time

**Sources:** Mythic Origins pg 14\
If you expend one use of mythic power, instead of taking an extra swift action, you can take either
an extra move or an extra swift action each round. You can use this extra swift action to take two
immediate actions between your turns; this consumes your extra swift action in your next round. Each
extra action you take still deals damage to you as described above.
