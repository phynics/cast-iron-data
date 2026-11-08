+++
id = "ref/spell/planar-ally-greater"
kind = "spell"
title = "Greater Planar Ally"
source_ids = ["core-rulebook", "adventurers-guide", "arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_ally_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/planar-ally-lesser" },
]

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Calling"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Shaman", level = 8 },
]
casting_time = "10 minutes"
components = "V, S, M (offerings worth 2,500 plus payment), DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "up to three called outsiders, totaling no more than 18 HD, no two of which can be more than 30 ft. apart when they appear." },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 8: Cleric, Oracle, Psychic, Shaman
Casting time: 10 minutes
Components: V, S, M (offerings worth 2,500 plus payment), DF
Range: close (25 ft. + 5 ft./2 levels)
Effect: up to three called outsiders, totaling no more than 18 HD, no two of which can be more than 30 ft. apart when they appear.
Duration: instantaneous
Saving throw: none
Spell resistance: no
Subschool: Calling
:::

### Greater Planar Ally

**Sources:** PRPG Core Rulebook pg 320

This spell functions like [lesser planar ally](ref/spell/planar-ally-lesser), except that you may
call a single creature of 18 HD or less, or up to three creatures of the same kind whose Hit Dice
total no more than 18. The creatures agree to help you and request your return payment together.
