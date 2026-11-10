+++
id = "ref/spell/protection-from-chaos-communal"
kind = "spell"
title = "Communal Protection from Chaos"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_chaos_communal", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/protection-from-chaos" },
]
[[sources]]
publication = "ultimate-combat"
page = "240"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Adept, Arcanist, Bloodrager, Cleric, Inquisitor, Medium, Oracle, Paladin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no; see text
Target: creature touched
Descriptors: good
:::

### Communal Protection from Chaos

This spell functions like _[protection from chaos](ref/spell/protection-from-chaos),_ except you
divide the duration in 1-minute intervals among the creatures touched.
