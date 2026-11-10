+++
id = "ref/spell/fear-the-sun"
kind = "spell"
title = "Fear the Sun"
aon = "SpellDisplay.aspx?ItemName=Fear%20the%20Sun"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fear_the_sun", path = "json/spells4.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "15"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a drow eyelash)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "up to one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Antipaladin, Bloodrager\
2: Arcanist, Cleric, Druid, Hunter, Inquisitor, Occultist, Oracle, Psychic, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drow eyelash)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: up to one creature/level, no two of which can be more than 30 ft. apart
:::

Each target that fails its saving throw gains [light blindness](ref/umr/light-blindness). When
exposed to bright light, affected targets are blinded for 1 full round and are dazzled in successive
rounds. If you cast this spell in the presence of bright light, any target that fails its save is
blinded immediately, and dazzled starting at the beginning of its first turn.
