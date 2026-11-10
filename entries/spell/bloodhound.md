+++
id = "ref/spell/bloodhound"
kind = "spell"
title = "Bloodhound"
aon = "SpellDisplay.aspx?ItemName=Bloodhound"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloodhound", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "206"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of blood and a pinch of cinnamon)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Hunter, Inquisitor, Ranger\
3: Alchemist, Investigator, Occultist
Casting time: 1 standard action
Components: V, S, M (a drop of blood and a pinch of cinnamon)
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

You gain the scent special quality, including the ability to track by scent. You receive a +8
competence bonus on Perception checks involving smell and a +4 competence bonus on Survival checks
to track using scent. You take a -4 penalty on saving throws against odor-related effects such as
the stench ability and stinking cloud. A creature under the effects of bloodhound can detect poison
by scent with a DC 20 Perception check.
