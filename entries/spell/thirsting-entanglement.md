+++
id = "ref/spell/thirsting-entanglement"
kind = "spell"
title = "Thirsting Entanglement"
aon = "SpellDisplay.aspx?ItemName=Thirsting%20Entanglement"
source_ids = ["core-rulebook", "villain-codex", "advanced-class-guide", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thirsting_entanglement", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/entangle" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "17"

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

### Thirsting Entanglement

This spell functions as [entangle](ref/spell/entangle), except the plants latch on to targets and
drain away their vitality. Any creature that fails a save to avoid becoming entangled or fails a
check to break free takes 1d2 points of Constitution damage.
