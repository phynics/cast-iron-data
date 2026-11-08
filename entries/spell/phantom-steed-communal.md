+++
id = "ref/spell/phantom-steed-communal"
kind = "spell"
title = "Communal Phantom Steed"
source_ids = ["core-rulebook", "wilderness-origins", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantom_steed_communal", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/phantom-steed" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one quasi-real, horse-like creature" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Summoner, Unchained Summoner\
3: Arcanist, Bloodrager, Bard, Magus, Occultist, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 10 minutes
Components: V, S
Range: 0 ft.
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: one quasi-real, horse-like creature
Subschool: Creation
:::

### Communal Phantom Steed

**Sources:** Ultimate Combat pg 239

This spell functions like [phantom steed](ref/spell/phantom-steed), except you can summon up to six
steeds, and you divide the duration in 1-hour intervals among the steeds summoned.
