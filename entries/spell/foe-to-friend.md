+++
id = "ref/spell/foe-to-friend"
kind = "spell"
title = "Foe to Friend"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "foe_to_friend", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "224"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 5 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Skald\
7: Psychic
Casting time: 1 immediate action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

Cast this spell when an enemy is about to make an attack against an ally. The creature makes the
attack against a valid target of your choice instead or the attack is negated. In addition, the
target is considered an ally for determining flanking for 1 round.
