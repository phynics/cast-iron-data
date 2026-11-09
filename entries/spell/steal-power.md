+++
id = "ref/spell/steal-power"
kind = "spell"
title = "Steal Power"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steal_power", path = "json/spells9.json" },
]
[[sources]]
publication = "mythic-adventures"
page = "114"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one mythic creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Mesmerist\
5: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one mythic creature
:::

You sap the power from a mythic creature, using it to restore your own. The target loses 1d4 uses of
mythic power. If you have the ability to expend mythic power, you regain one use for each use the
target loses.
