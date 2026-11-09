+++
id = "ref/spell/gird-ally"
kind = "spell"
title = "Gird Ally"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gird_ally", path = "json/spells5.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "22"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one summoned creature you control/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: one summoned creature you control/level, no two of which can be more than 30 ft. apart
:::

You create a magical field around summoned creatures you control that deflects attacks made against
them. The targets gain a deflection bonus to their AC equal to 1 + 1 for every 6 caster levels you
possess (maximum +4 deflection bonus at 18th level). A summoner can target his eidolon with this
spell.
