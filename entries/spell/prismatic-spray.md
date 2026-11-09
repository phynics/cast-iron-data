+++
id = "ref/spell/prismatic-spray"
kind = "spell"
title = "Prismatic Spray"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prismatic_spray", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "325"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Duration: instantaneous
Saving throw: see text
Spell resistance: yes
Area: cone-shaped burst
:::

This spell causes seven shimmering, multicolored beams of light to spray from your hand. Each beam
has a different power. Creatures in the area of the spell with 8 HD or less are automatically
[blinded](ref/misc/blinded) for 2d4 rounds. Every creature in the area is randomly struck by one or
more beams, which have additional effects.

|1d8|Color of Beam|Effect|
| --- | --- | --- |
|1|Red|20 points fire damage (Reflex half)|
|2|Orange|40 points acid damage (Reflex half)|
|3|Yellow|80 points electricity damage (Reflex half)|
|4|Green|[Green prismatic poison](ref/eq-poison/green-prismatic-poison)|
|5|Blue|[Flesh to stone](ref/spell/flesh-to-stone) (Fortitude negates)|
|6|Indigo|Insane, as [insanity](ref/spell/insanity) spell (Will negates)|
|7|Violet|Sent to another plane (Will negates)|
|8|Struck by two rays|Roll twice more, ignoring any "8" results|
