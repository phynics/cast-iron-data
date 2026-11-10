+++
id = "ref/spell/magic-circle-against-technology"
kind = "spell"
title = "Magic Circle Against Technology"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_circle_against_technology", path = "json/spells6.json" },
]
[[sources]]
publication = "technology-guide"
page = "9"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a 3-ft.-diameter circle of powdered copper)"
range = "touch"
effects = [
  { label = "Area", value = "10-ft.-radius emanation from touched creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless), see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a 3-ft.-diameter circle of powdered copper)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless), see text
Spell resistance: no
Area: 10-ft.-radius emanation from touched creature
:::

All creatures within the area gain the effects of a protection from technology spell. Creatures in
the area, or that later enter the area, receive only one attempt to suppress technological effects
that are controlling them. If a creature succeed at this save, such effects are suppressed as long
as the creature remains in the area. Creatures that leave the area and then return are not
protected. Robots receive a saving throw and [spell resistance](ref/rule/spell-resistance) to avoid
being kept at bay, but the deflection and resistance bonuses and the protection from mental control
apply to non-technological creatures in the area even if a robot succeeds at its saving throw and is
thus able to enter the area.

This spell is not cumulative with protection from technology and vice versa.
