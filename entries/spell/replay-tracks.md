+++
id = "ref/spell/replay-tracks"
kind = "spell"
title = "Replay Tracks"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "replay_tracks", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "233"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Ranger", level = 2 },
]
casting_time = "3 rounds"
components = "V, S, F (a track or other sign of a creature's passing found with Perception or Survival)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "concentration, up to 1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Hunter, Ranger\
3: Medium, Occultist\
4: Inquisitor\
5: Druid, Psychic
Casting time: 3 rounds
Components: V, S, F (a track or other sign of a creature's passing found with Perception or Survival)
Range: personal
Duration: concentration, up to 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

This spell allows you to reconstruct past events that occurred in your current location based on the
tracks and other signs left behind. Replay tracks reveals events that occurred while the tracks that
serve as the focus for the spell were being left, revealing events in the order they happened in
real time or in reverse, depending on whether you are following the tracks forward or backward,
although the image isn't clear enough to make out details (such as a creature's exact identity). You
can attempt Survival checks to follow tracks as part of concentrating on the spell, but only events
connected to the tracks used as the focus of the spell are revealed by the spell. Elements that left
no trace detectable by you, such as creatures benefitting from pass without trace, are absent from
the events you visualize.
