+++
id = "ref/spell/ill-omen"
kind = "spell"
title = "Ill Omen"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ill_omen", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (hair from a black cat)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level or until discharged"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Medium, Mesmerist, Psychic, Witch
Casting time: 1 standard action
Components: V, S, M (hair from a black cat)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until discharged
Saving throw: none
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse, mind-affecting
:::

**Sources:** Advanced Player's Guide pg 229

You afflict the target with bad luck. On the next d20 roll the target makes, it must roll twice and
take the less favorable result. For every five caster levels you have, the target must roll twice on
an additional d20 roll (to a maximum of five rolls at 20th level).

A target who can speak and has at least one free hand and who is aware of the spell and its effects
(such as from a Spellcraft check to identify the spell as it is cast) can negate one reroll by
spending a move action to utter a brief prayer or good luck charm to appease the spirits of ill
fortune.
