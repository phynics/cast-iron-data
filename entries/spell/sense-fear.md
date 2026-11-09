+++
id = "ref/spell/sense-fear"
kind = "spell"
title = "Sense Fear"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sense_fear", path = "json/spells15.json" },
]
[[sources]]
publication = "horror-adventures"
page = "127"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a patch of fur)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Antipaladin, Bloodrager, Medium\
2: Cleric, Druid, Hunter, Inquisitor, Mesmerist, Occultist, Oracle, Psychic, Ranger, Shaman, Spiritualist, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a patch of fur)
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

You sense the fear of those nearby, feeling it in the air around you. You can detect
[spooked, shaken, scared, frightened, panicked, terrified, and horrified](ref/rule/lesser-fear-and-greater-fear)
creatures within 30 feet, and you immediately know what level of fear they are experiencing. You
determine the creatures' approximate direction from you, though you do not sense a given creature's
identity or know which squares the creatures occupy. If you're within 5 feet of a creature whose
fear you sense, you pinpoint that creature's location, as if using
[blindsense](ref/rule/blindsight-and-blindsense).
