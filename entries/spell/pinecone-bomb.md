+++
id = "ref/spell/pinecone-bomb"
kind = "spell"
title = "Pinecone Bomb"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pinecone_bomb", path = "json/spells7.json" },
]
[[sources]]
publication = "wilderness-origins"
page = "13"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinecone)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "10-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Druid, Hunter, Shaman, Witch\
3: Ranger
Casting time: 1 standard action
Components: V, S, M (a pinecone)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 10-ft.-radius spread
:::

Created by Ghorus when he was working to create the [ghorans](ref/monster/ghoran), pinecone bomb
infuses a small pinecone with power, causing it to detonate with explosive force when thrown. You
throw the pinecone at a target or point within range and it detonates immediately upon landing,
dealing 1d6 points of piercing damage per 2 caster levels you have (maximum 5d6) to each creature
caught in the spread.
