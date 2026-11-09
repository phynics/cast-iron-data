+++
id = "ref/spell/lightning-arc"
kind = "spell"
title = "Lightning Arc"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lightning_arc", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "227"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (fur and two glass figurines)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Targets", value = "two creatures or objects which must be no more than 60 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (fur and two glass figurines)
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes (see text)
Targets: two creatures or objects which must be no more than 60 ft. apart
Descriptors: electricity
:::

You generate an arc of lightning between two targets. The lightning deals 1d6 points of electricity
damage per caster level (maximum 15d6) to both targets and any creatures in a line connecting them.
The spell fails if there is no line of effect between the targets. Lightning arc sets fire to
combustibles and damages objects in its path. It can melt metals that have a low melting point, such
as lead, gold, copper, silver, or bronze.
