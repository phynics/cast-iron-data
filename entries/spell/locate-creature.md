+++
id = "ref/spell/locate-creature"
kind = "spell"
title = "Locate Creature"
aon = "SpellDisplay.aspx?ItemName=Locate%20Creature"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "locate_creature", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/locate-object" },
]
[[sources]]
publication = "core-rulebook"
page = "305"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (fur from a bloodhound)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "circle, centered on you, with a radius of 400 ft. + 40 ft./level" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium, Summoner\
4: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (fur from a bloodhound)
Range: long (400 ft. + 40 ft./level)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Area: circle, centered on you, with a radius of 400 ft. + 40 ft./level
:::

This spell functions like [locate object](ref/spell/locate-object), except this spell locates a
known creature. You slowly turn and sense when you are facing in the direction of the creature to be
located, provided it is within range. You also know in which direction the creature is moving, if
any.

The spell can locate a creature of a specific kind or a specific creature known to you. It cannot
find a creature of a certain type. To find a kind of creature, you must have seen such a creature up
close (within 30 feet) at least once.

Running water blocks the spell. It cannot detect objects. It can be fooled by mislead, nondetection,
and polymorph spells.
