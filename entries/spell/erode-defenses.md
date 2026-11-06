+++
id = "ref/spell/erode-defenses"
kind = "spell"
title = "Erode Defenses"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "erode_defenses", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Magus", level = 2 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Magus\
3: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (see below)
Spell resistance: yes
Target: one creature
:::

**Sources:** Dragonslayer's Handbook pg 29

Your spell slowly begins to eat away at the defenses of your target. If the target fails its saving
throw, it loses 1 point from any [damage reduction](ref/rule/damage-reduction) and natural armor
bonus it may have. If the initial save was not successful, the target may attempt a new saving throw
each round for the duration of the spell or continue to suffer cumulative losses. If the first save
fails but a subsequent save succeeds, the eroding effects stop at that point, though any of the
penalties already accrued remain until the spell expires. At the end of the spell's duration, the
target's damage reduction and natural armor bonus immediately return to normal. Only one erode
defenses spell can affect a particular target at any one time.
