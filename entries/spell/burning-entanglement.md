+++
id = "ref/spell/burning-entanglement"
kind = "spell"
title = "Burning Entanglement"
source_ids = ["core-rulebook", "mythic-adventures", "villain-codex", "advanced-class-guide", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_entanglement", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/entangle" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "plants in a 40-ft.-radius spread" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex partial; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level (D)
Saving throw: Reflex partial; see text
Spell resistance: no
Area: plants in a 40-ft.-radius spread
:::

### Mythic Entangle

**Sources:** Mythic Adventures pg 93

The spell functions in areas without any vegetation, causing plants to spring up out of the ground.
These plants can reach creatures that are up to 10 feet in the air. Plants affected or created by
the spell sprout thorns that deal 1d6 points of damage each round to creatures in the area.

### Burning Entanglement

**Sources:** Villain Codex pg 140

This spell functions as per [entangle](ref/spell/entangle), except it sets the foliage on fire. A
creature that begins its turn entangled by the spell takes 4d6 points of fire damage (Reflex half),
and a creature that begins its turn in the area but is not entangled takes 2d6 points of fire damage
(Reflex negates). Smoke rising from the vines partially obscures visibility. Creatures can see
things in the smoke within 5 feet clearly, but attacks against anything farther away in the smoke
must contend with concealment (20% miss chance). When the spell's duration expires, the vines burn
away entirely.
