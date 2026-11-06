+++
id = "ref/spell/awaken-the-devoured"
kind = "spell"
title = "Awaken the Devoured"
source_ids = ["book-of-the-damned", "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "awaken_the_devoured", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["pain"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one daemon per 4 caster levels" },
]
duration = "instantaneous and 1 round/level"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Inquisitor\
5: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous and 1 round/level
Saving throw: Will partial (see text)
Spell resistance: yes
Target: one daemon per 4 caster levels
Descriptors: pain
:::

**Sources:** Book of the Damned pg 183, Book of the Damned - Volume 3: Horsemen of the Apocalypse pg
38

This spell is often used by conjurers as a method to torment daemons and force compliance, for it
awakens the broken, anguished memories of the countless souls that the target daemons have consumed.
All daemons targeted by awaken the devoured must be within 30 feet of each other. The fragmented
memories haunt and afflict the daemons, dealing 1d8 points of damage per caster level (maximum 15d8)
and making the daemons confused for 1 round per level. A daemon that succeeds at a Will save halves
the damage and negates the confusion effect.
