+++
id = "ref/spell/planar-ally"
kind = "spell"
title = "Planar Ally"
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

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Calling"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 500 gp plus payment, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one called outsider of 6 HD or less" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 3: Medium\
4: Cleric, Oracle, Psychic, Shaman, Warpriest
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 500 gp plus payment, see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one called outsider of 6 HD or less
Subschool: Calling
:::

### Planar Ally

This spell functions like [lesser planar ally](ref/spell/planar-ally-lesser), except you may call a
single creature of 12 HD or less, or two creatures of the same kind whose HD total no more than 12.
The creatures agree to help you and request your return payment together.
