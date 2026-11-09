+++
id = "ref/spell/challenge-evil"
kind = "spell"
title = "Challenge Evil"
aon = "SpellDisplay.aspx?ItemName=Challenge%20Evil"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "challenge_evil", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "210"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Paladin", level = 1 },
]
casting_time = "1 standard action"
components = "V, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one evil creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Paladin
Casting time: 1 standard action
Components: V, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one evil creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You challenge an evil creature to bring the fight to you, or suffer the consequences. You gain a +2
sacred bonus on all melee attacks against the subject of the spell. At the end of its turn, if the
target has not made at least one attack on you, it becomes sickened. If you move away from the
target, the spell ends.
