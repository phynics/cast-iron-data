+++
id = "ref/spell/tactical-miscalculation"
kind = "spell"
title = "Tactical Miscalculation"
aon = "SpellDisplay.aspx?ItemName=Tactical%20Miscalculation"
source_ids = ["pathfinder-society-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tactical_miscalculation", path = "json/spells10.json" },
]
[[sources]]
publication = "pathfinder-society-primer"
page = "15"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Hunter, Inquisitor, Ranger, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: see text
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

The target becomes fixated on avoiding damage and fails to spot even the most opportune moments to
attack. Whenever a creature the target threatens would provoke an attack of opportunity from the
target, the target must succeed at a Will save or be unable to make the attack of opportunity
against that creature.
