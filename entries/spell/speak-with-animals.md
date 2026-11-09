+++
id = "ref/spell/speak-with-animals"
kind = "spell"
title = "Speak with Animals"
aon = "SpellDisplay.aspx?ItemName=Speak%20with%20Animals"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_with_animals", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "346"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 3 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Druid, Hunter, Ranger\
2: Psychic\
3: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

You can ask questions of and receive answers from animals, but the spell doesn't make them any more
friendly than normal. Wary and cunning animals are likely to be terse and evasive, while the more
stupid ones make inane comments. If an animal is friendly toward you, it may do some favor or
service for you.
