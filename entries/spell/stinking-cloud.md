+++
id = "ref/spell/stinking-cloud"
kind = "spell"
title = "Stinking Cloud"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stinking_cloud", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "349"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a rotten egg or cabbage leaves)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bloodrager, Magus, Shaman, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a rotten egg or cabbage leaves)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates; see text
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: Creation
Descriptors: poison
:::

Stinking cloud creates a bank of fog like that created by fog cloud, except that the vapors are
nauseating. Living creatures in the cloud become nauseated. This condition lasts as long as the
creature is in the cloud and for 1d4+1 rounds after it leaves. (Roll separately for each nauseated
character.) Any creature that succeeds on its save but remains in the cloud must continue to save
each round on your turn. This is a poison effect.

Stinking cloud can be made permanent with a [permanency](ref/spell/permanency) spell. A permanent
stinking cloud dispersed by wind reforms in 10 minutes.
