+++
id = "ref/spell/transmute-metal-to-wood"
kind = "spell"
title = "Transmute Metal to Wood"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transmute_metal_to_wood", path = "json/spells10.json" },
]
[[sources]]
publication = "core-rulebook"
page = "361"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "all metal objects within a 40-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes (object; see text)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Druid
Casting time: 1 standard action
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes (object; see text)
Area: all metal objects within a 40-ft.-radius burst
:::

This spell enables you to change all metal objects within its area to wood. Weapons, armor, and
other metal objects carried by creatures are affected as well. A magic object made of metal
effectively has [spell resistance](ref/rule/spell-resistance) equal to 20 + its caster level against
this spell. Artifacts cannot be transmuted. Weapons converted from metal to wood take a -2 penalty
on attack and damage rolls. The armor bonus of any armor converted from metal to wood is reduced
by 2. Weapons changed by this spell splinter and break on any natural attack roll of 1 or 2, and
armor changed by this spell loses an additional point of armor bonus every time it is struck with a
natural attack roll of 19 or 20.

Only [limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), [wish](ref/spell/wish),
or similar magic can restore a transmuted object to its metallic state.
