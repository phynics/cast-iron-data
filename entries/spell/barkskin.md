+++
id = "ref/spell/barkskin"
kind = "spell"
title = "Barkskin"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "barkskin", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "246"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Druid, Hunter, Investigator, Ranger, Shaman, Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: yes
Target: living creature touched
:::

Barkskin toughens a creature's skin. The effect grants a +2 enhancement bonus to the creature's
existing natural armor bonus. This enhancement bonus increases by 1 for every three caster levels
above 3rd, to a maximum of +5 at 12th level.

The enhancement bonus provided by barkskin stacks with the target's natural armor bonus, but not
with other enhancement bonuses to natural armor. A creature without natural armor has an effective
natural armor bonus of +0.
