+++
id = "ref/spell/planar-ally"
kind = "spell"
title = "Planar Ally"
aon = "SpellDisplay.aspx?ItemName=Planar%20Ally"
source_ids = ["core-rulebook", "adventurers-guide", "arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_ally", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planar-ally-lesser" },
]
[[sources]]
publication = "core-rulebook"
page = "320"
[[sources]]
publication = "adventurers-guide"
page = "125"
[[sources]]
publication = "arcane-anthology"
page = "14"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["calling"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 1,250 gp plus payment)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one or two called outsiders, totaling no more than 12 HD, which cannot be more than 30 ft. apart when they appear" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text for lesser planar ally\]
Level: 6: Cleric, Oracle, Psychic, Shaman, Warpriest
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 1,250 gp plus payment)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one or two called outsiders, totaling no more than 12 HD, which cannot be more than 30 ft. apart when they appear
Subschool: calling
:::

### Planar Ally

This spell functions like [lesser planar ally](ref/spell/planar-ally-lesser), except you may call a
single creature of 12 HD or less, or two creatures of the same kind whose HD total no more than 12.
The creatures agree to help you and request your return payment together.
