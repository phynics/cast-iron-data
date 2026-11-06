+++
id = "ref/spell/know-direction"
kind = "spell"
title = "Know Direction"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "know_direction", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Occultist", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Shaman", level = 0 },
  { class = "Skald", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
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
Level: 0: Bard, Druid, Hunter, Occultist, Psychic, Shaman, Skald
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 304

When you cast this spell, you instantly know the direction of north from your current position. The
spell is effective in any environment in which "north" exists, but it may not work in extraplanar
settings. Your knowledge of north is correct at the moment of casting, but you can get lost again
within moments if you don't find some external reference point to help you keep track of direction.
