+++
id = "ref/spell/song-of-discord"
kind = "spell"
title = "Song of Discord"
aon = "SpellDisplay.aspx?ItemName=Song%20of%20Discord"
source_ids = ["core-rulebook", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "song_of_discord", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "345"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting", "sonic"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "creatures within a 20-ft.-radius spread" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Psychic, Skald
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Area: creatures within a 20-ft.-radius spread
Subschool: Compulsion
Descriptors: mind-affecting, sonic
:::

This spell causes those within the area to turn on each other rather than attack their foes. Each
affected creature has a 50% chance to attack the nearest target each round. (Roll to determine each
creature's behavior every round at the beginning of its turn.) A creature that does not attack its
nearest neighbor is free to act normally for that round. Creatures forced by a song of discord to
attack their fellows employ all methods at their disposal, choosing their deadliest spells and most
advantageous combat tactics. They do not, however, harm targets that have fallen unconscious.
