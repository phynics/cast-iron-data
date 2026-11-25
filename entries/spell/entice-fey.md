+++
id = "ref/spell/entice-fey"
kind = "spell"
title = "Entice Fey"
aon = "SpellDisplay.aspx?ItemName=Entice%20Fey"
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
subschools = ["calling"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Druid", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Skald", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 1,250 gp plus payment)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one or two called fey, totaling no more than 12 Hit Dice, which can't appear more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Bard, Skald\
7: Druid, Shaman
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 1,250 gp plus payment)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one or two called fey, totaling no more than 12 Hit Dice, which can't appear more than 30 ft. apart
Subschool: calling
:::

### Entice Fey

This spell functions as [lesser entice fey](ref/spell/entice-fey-lesser), except that the spell's
whimsical calling can produce a single fey of 12 Hit Dice or less, or two fey of the same kind whose
Hit Dice total no more than 12.
