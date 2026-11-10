+++
id = "ref/spell/song-of-discord-greater"
kind = "spell"
title = "Greater Song of Discord"
aon = "SpellDisplay.aspx?ItemName=Song%20of%20Discord%2C%20Greater"
source_ids = ["core-rulebook", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "song_of_discord_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/song-of-discord" },
]
[[sources]]
publication = "chronicle-of-legends"
page = "14"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting", "sonic"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Skald", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "creatures within a 20-ft.-radius spread" },
]
duration = "1 round/level"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Mesmerist, Skald\
8: Psychic
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Area: creatures within a 20-ft.-radius spread
Duration: 1 round/level
Saving throw: Will partial
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting, sonic
:::

### Greater Song of Discord

This spell functions as [song of discord](ref/spell/song-of-discord) except that affected creatures
automatically attack the nearest target each round. In addition, all affected creatures gain a +4
morale bonus to Strength for the duration of the spell. A creature that succeeds at the Will save
reduces the effect's duration to 1 round.
