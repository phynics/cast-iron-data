+++
id = "ref/spell/rebuke-technology"
kind = "spell"
title = "Rebuke Technology"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rebuke_technology", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (powdered fragments of technology)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one technological object or creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (powdered fragments of technology)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: one technological object or creature
:::

**Sources:** Technology Guide pg 10

You shroud the targeted technological object or creature (such as a robot or a nanotech swarm) with
magical energy. If the targeted creature fails to resist the spell, it is rendered inert and
unusable (or unconscious in the case of creatures) for the spell's duration. A creature can attempt
a new Fortitude saving throw to end the effect early at the end of its turn after the first full
round it is affected by this spell.
