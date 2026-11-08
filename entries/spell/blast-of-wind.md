+++
id = "ref/spell/blast-of-wind"
kind = "spell"
title = "Blast of Wind"
source_ids = ["core-rulebook", "mythic-adventures", "elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blast_of_wind", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/gust-of-wind" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Effect", value = "line-shaped gust of severe wind emanating out from you to the extreme of the range" },
]
duration = "1 round"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Druid, Hunter, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Duration: 1 round
Saving throw: Fortitude negates
Spell resistance: yes
Effect: line-shaped gust of severe wind emanating out from you to the extreme of the range
Descriptors: air
:::

### Mythic Gust of Wind

**Sources:** Mythic Adventures pg 97

The force of the wind increases to [windstorm](ref/rule/winds) (approximately 70 mph). All effects
described in the spell affect creatures one size larger. Ranged attacks can't be attempted in the
area of the spell. The wind automatically blows out unprotected flames and has a 75% chance of
blowing out protected flames.

_Augmented (2nd):_ If you expend two uses of mythic power, the spell lasts for 1 additional round
and the range increases by 30 feet. As a swift action at the start of your turn, you can expend
another use of mythic power to extend the duration by 1 round and the range by another 30 feet.

### Blast of Wind

**Sources:** Elemental Master's Handbook pg 17

With a spiraling gesture of your hand and a forceful exhalation, you create a brief but fierce (90
mph) blast of wind. This spell functions as [gust of wind](ref/spell/gust-of-wind), except all
creatures within the area are treated as though they were one size category smaller for the purpose
of determining how the spell affects them. For every 4 caster levels beyond 7th, creatures in the
area are treated as an additional size category smaller (to a maximum of three size categories
smaller at 15th level).
