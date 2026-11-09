+++
id = "ref/spell/revealing-light"
kind = "spell"
title = "Revealing Light"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "revealing_light", path = "json/spells8.json" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "31"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (piece of a mirror)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Bard, Medium, Skald\
2: Arcanist, Cleric, Inquisitor, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (piece of a mirror)
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: light
:::

The touched object emits a shimmering light (as per light) that causes shadows to shift constantly
in a 20-foot radius. Creatures lose any racial bonus on Stealth checks while in the area, and the
light suppresses any bonuses on Stealth checks granted by visual camouflage (such as from camouflage
netting or the camouflage rogue talent). The unpredictable light patterns also interfere with spells
and effects of the pattern subschool, granting all creatures in the area a +2 bonus on saves against
such effects.
