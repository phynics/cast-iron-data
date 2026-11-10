+++
id = "ref/spell/thunderous-footfalls"
kind = "spell"
title = "Thunderous Footfalls"
source_ids = ["pathfinder-91-battle-of-bloodmarch-hills"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thunderous_footfalls", path = "json/spells10.json" },
]
[[sources]]
publication = "pathfinder-91-battle-of-bloodmarch-hills"
page = "71"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one Large or larger creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "no (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: no (harmless)
Target: one Large or larger creature
:::

This spell makes the target creature's footfalls shake the ground violently as he trundles, which
may knock down smaller creatures as he passes by, though it also makes the target slower on land.
The target's land speed is reduced by half (round down to the nearest 5-foot increment), but each
time he moves overland adjacent to a creature that is at least one size category smaller than he is,
that creature must succeed at a Fortitude saving throw or be knocked prone.
