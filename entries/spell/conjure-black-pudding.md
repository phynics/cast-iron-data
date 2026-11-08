+++
id = "ref/spell/conjure-black-pudding"
kind = "spell"
title = "Conjure Black Pudding"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conjure_black_pudding", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["acid"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 round"
components = "V, S, M (a flask of acid worth 10 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned black pudding" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Summoner, Unchained Summoner\
6: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (a flask of acid worth 10 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned black pudding
Subschool: Summoning
Descriptors: acid
:::

**Sources:** Ultimate Magic pg 211

You summon a black pudding that immediately attacks creatures near it. You have no control over the
creature, and it may attack you if there are no more obvious opponents. The black pudding is treated
as a summoned creature and has the extraplanar subtype. The black pudding's split ability works
normally, but all puddings derived from the summoned one disappear when the spell ends.
