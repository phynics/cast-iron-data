+++
id = "ref/spell/entice-fey-greater"
kind = "spell"
title = "Greater Entice Fey"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entice_fey_greater", path = "json/spells4.json" },
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
  { class = "Druid", level = 9 },
  { class = "Shaman", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 2,500 gp plus payment, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "up to three called fey, totaling no more than 18 Hit Dice, no two of which can appear more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Druid, Shaman
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 2,500 gp plus payment, see text)
Range: close (25 ft. + 5 ft./2 levels)
Effect: up to three called fey, totaling no more than 18 Hit Dice, no two of which can appear more than 30 ft. apart
Duration: instantaneous
Saving throw: none
Spell resistance: no
Subschool: Calling
:::

### Greater Entice Fey

This spell functions as [lesser entice fey](ref/spell/entice-fey-lesser), except the spell's
whimsical calling can produce a single fey of 18 Hit Dice or less, or up to three fey of the same
kind whose Hit Dice total no more than 18.
