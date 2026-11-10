+++
id = "ref/spell/siphon-might"
kind = "spell"
title = "Siphon Might"
aon = "SpellDisplay.aspx?ItemName=Siphon%20Might"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siphon_might", path = "json/spells9.json" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "27"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Druid, Hunter, Magus, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude half
Spell resistance: yes
Target: one creature
:::

You drain the might of the target and transfer that power to another creature. The subject takes a
penalty to Strength equal to 1d6 + 1 per 2 caster levels (maximum 1d6 + 5). This effect can't cause
the subject's Strength score to drop below 1. A successful Fortitude save halves this penalty. This
penalty doesn't stack with itself or the penalty applied from ray of enfeeblement.

You can grant any one creature adjacent to you (including yourself) an enhancement bonus to Strength
equal to the Strength penalty imposed by this spell.
