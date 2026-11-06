+++
id = "ref/spell/cone-of-cold"
kind = "spell"
title = "Cone of Cold"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cone_of_cold", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a small crystal or glass cone)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Magus, Occultist, Sorcerer, Wizard\
6: Shaman, Witch
Casting time: 1 standard action
Components: V, S, M (a small crystal or glass cone)
Range: 60 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: cone-shaped burst
Descriptors: cold
:::

**Sources:** PRPG Core Rulebook pg 258

Cone of cold creates an area of extreme cold, originating at your hand and extending outward in a
cone. It drains heat, dealing 1d6 points of cold damage per caster level (maximum 15d6).

### Mythic Cone of Cold

**Sources:** Mythic Adventures pg 89\
The damage dealt increases to 1d10 points of cold damage per caster level (maximum 15d10). Any
creature that fails its save is partially encased in ice, reducing its speed by half. Creatures with
the cold or incorporeal subtype or immunity to being grappled are immune to this effect. The reduced
movement lasts until the ice is destroyed. Destroying the ice requires a successful Strength or
dispel check against the spell's DC, or dealing bludgeoning or fire damage equal to 1 point per
caster level to the creature.

_Augmented:_ You can expend two uses of mythic power to transform the spell's cold into a barrage of
giant hailstones, icicles, or shards. Half the spell's damage is your choice of bludgeoning,
piercing, or slashing damage, and the other half is cold damage.
