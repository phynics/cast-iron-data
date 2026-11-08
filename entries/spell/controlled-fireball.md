+++
id = "ref/spell/controlled-fireball"
kind = "spell"
title = "Controlled Fireball"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "controlled_fireball", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fireball" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a ball of bat guano and sulfur)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a ball of bat guano and sulfur)
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 20-ft.-radius spread
Descriptors: fire
:::

### Mythic Fireball

**Sources:** Mythic Adventures pg 94

The damage dealt increases to 1d10 points of fire damage per caster level (maximum 10d10). Any
creature that fails its Reflex saving throw catches on fire, taking 2d6 points of fire damage each
round until the fire is extinguished. Attempts to extinguish this fire use the spell's save DC.

_Augmented (6th):_ If you expend two uses of mythic power, the maximum damage increases to 20d10,
the area increases to a 40-foot radius spread, and any fire damage dealt by the spell bypasses fire
resistance and fire immunity.

### Controlled Fireball

**Sources:** Ultimate Intrigue pg 208

This spell functions as [fireball](ref/spell/fireball) except you can cause the bead of fire to
originate from anywhere you can see within range. You can choose a number of squares within the area
up to your Intelligence bonus (for magi, occultists, or wizards) or Charisma bonus (for bloodragers
or sorcerers) to be struck by weaker flames; the controlled fireball deals minimum damage in those
squares.

Attempts to identify controlled fireball with a skill check incorrectly identify it as fireball (see
the [ruse](ref/spelldef/ruse) descriptor).
