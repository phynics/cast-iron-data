+++
id = "ref/spell/burning-entanglement"
kind = "spell"
title = "Burning Entanglement"
aon = "SpellDisplay.aspx?ItemName=Burning%20Entanglement"
source_ids = ["core-rulebook", "villain-codex", "advanced-class-guide", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_entanglement", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/entangle" },
]
[[sources]]
publication = "villain-codex"
page = "140"

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

### Burning Entanglement

This spell functions as per [entangle](ref/spell/entangle), except it sets the foliage on fire. A
creature that begins its turn entangled by the spell takes 4d6 points of fire damage (Reflex half),
and a creature that begins its turn in the area but is not entangled takes 2d6 points of fire damage
(Reflex negates). Smoke rising from the vines partially obscures visibility. Creatures can see
things in the smoke within 5 feet clearly, but attacks against anything farther away in the smoke
must contend with concealment (20% miss chance). When the spell's duration expires, the vines burn
away entirely.
