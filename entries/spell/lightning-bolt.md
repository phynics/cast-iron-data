+++
id = "ref/spell/lightning-bolt"
kind = "spell"
title = "Lightning Bolt"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lightning_bolt", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (fur and a glass rod)"
range = "120 ft."
effects = [
  { label = "Area", value = "120-ft. line" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Adept, Arcanist, Bloodrager, Magus, Occultist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (fur and a glass rod)
Range: 120 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 120-ft. line
Descriptors: electricity
:::

**Sources:** PRPG Core Rulebook pg 304

You release a powerful stroke of electrical energy that deals 1d6 points of electricity damage per
caster level (maximum 10d6) to each creature within its area. The bolt begins at your fingertips.

The lightning bolt sets fire to combustibles and damages objects in its path. It can melt metals
with a low melting point, such as lead, gold, copper, silver, or bronze. If the damage caused to an
interposing barrier shatters or breaks through it, the bolt may continue beyond the barrier if the
spell's range permits; otherwise, it stops at the barrier just as any other spell effect does.

### Mythic Lightning Bolt

**Sources:** Mythic Adventures pg 100\
The damage dealt increases to 1d8 points of electricity damage per caster level (maximum 10d8). Any
creature that fails its save is staggered for 1 round.

_Augmented (3rd):_ If you expend two uses of mythic power, you can bend the line of the spell once
up to 90 degrees. Any creature that fails its save is stunned for 1 round.
