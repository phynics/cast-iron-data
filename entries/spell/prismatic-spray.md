+++
id = "ref/spell/prismatic-spray"
kind = "spell"
title = "Prismatic Spray"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prismatic_spray", path = "json/spells14.json" },
]

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

**Sources:** PRPG Core Rulebook pg 325

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

### Mythic Prismatic Spray

**Sources:** Mythic Adventures pg 104\
The spell automatically blinds creatures with up to 12 Hit Dice instead of 8 Hit Dice. Attempt one
[bull rush](ref/rule/bull-rush) combat maneuver and apply its results to each creature in the area.
Your CMB for this bull rush is equal to your caster level plus your Intelligence, Wisdom, or
Charisma modifier, whichever is highest. This bull rush doesn't provoke an attack of opportunity.

_Augmented (6th):_ If you expend two uses of mythic power, the area changes from a cone into a line.
Creatures in the line are struck by two beams (or three, if the creature rolls an 8 on the table).
The spell bypasses energy resistance and immunity.
