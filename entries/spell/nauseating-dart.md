+++
id = "ref/spell/nauseating-dart"
kind = "spell"
title = "Nauseating Dart"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nauseating_dart", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "189"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one poisonous stinger" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Druid, Hunter, Witch
Casting time: 1 standard action
Components: S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: no
Effect: one poisonous stinger
Subschool: Creation
Descriptors: poison
:::

You spit a poisonous stinger around the size of a quill at a creature within range, as though you
had fired a dart from a blowgun. You must succeed at a ranged attack to hit your target. The stinger
deals 1d2 points of piercing damage and poisons the target, causing it to become nauseated for 1
round unless it succeeds at a Fortitude save.
