+++
id = "ref/spell/entice-fey"
kind = "spell"
title = "Entice Fey"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entice_fey", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/entice-fey-lesser" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "213"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Calling"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 500 gp plus payment, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one called fey, with 6 Hit Dice or fewer" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium\
4: Bard, Hunter, Ranger, Skald\
5: Druid, Shaman
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 500 gp plus payment, see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one called fey, with 6 Hit Dice or fewer
Subschool: Calling
:::

### Entice Fey

This spell functions as [lesser entice fey](ref/spell/entice-fey-lesser), except that the spell's
whimsical calling can produce a single fey of 12 Hit Dice or less, or two fey of the same kind whose
Hit Dice total no more than 12.
