+++
id = "ref/spell/find-quarry"
kind = "spell"
title = "Find Quarry"
aon = "SpellDisplay.aspx?ItemName=Find%20Quarry"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "find_quarry", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "230"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Hunter, Inquisitor, Ranger\
5: Occultist
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You sense whether a well-known creature you can clearly visualize is within a 20-mile radius of your
current location, as well as the distance and direction to the creature in relation to you. You also
discern whether the creature is moving, and its direction, speed, and mode of movement. The radius
you can sense increases by 5 miles for every two caster levels you have above 10th (to a maximum of
a 45-mile radius at 20th level). Anything that would prevent locate creature from finding a creature
also prevents find quarry from doing so.
