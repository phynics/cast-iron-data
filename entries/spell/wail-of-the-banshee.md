+++
id = "ref/spell/wail-of-the-banshee"
kind = "spell"
title = "Wail of the Banshee"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wail_of_the_banshee", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "sonic"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature/level within a 40-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature/level within a 40-ft.-radius spread
Descriptors: death, sonic
:::

**Sources:** PRPG Core Rulebook pg 365

When you cast this spell, you emit a terrible, soul-chilling scream that possibly kills creatures
that hear it (except for yourself). The spell affects up to one creature per caster level,
inflicting 10 points of damage per caster level. Creatures closest to the point of origin are
affected first.
