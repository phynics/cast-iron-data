+++
id = "ref/spell/scrying-greater"
kind = "spell"
title = "Greater Scrying"
aon = "SpellDisplay.aspx?ItemName=Scrying%2C%20Greater"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scrying_greater", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/scrying" },
]
[[sources]]
publication = "core-rulebook"
page = "337"

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "magical sensor" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Bard, Mesmerist, Occultist, Skald\
7: Arcanist, Cleric, Druid, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Effect: magical sensor
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Scrying
:::

### Greater Scrying

This spell functions like [scrying](ref/spell/scrying), except as noted above. Additionally, all of
the following spells function reliably through the sensor: [detect chaos](ref/spell/detect-chaos),
[detect evil](ref/spell/detect-evil), [detect good](ref/spell/detect-good),
[detect law](ref/spell/detect-law), [detect magic](ref/spell/detect-magic),
[message](ref/spell/message), [read magic](ref/spell/read-magic), and [tongues](ref/spell/tongues).
