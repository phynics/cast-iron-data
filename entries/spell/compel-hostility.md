+++
id = "ref/spell/compel-hostility"
kind = "spell"
title = "Compel Hostility"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "compel_hostility", path = "json/spells12.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "226"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of your blood)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Cleric, Hunter, Inquisitor, Medium, Mesmerist, Oracle, Paladin, Psychic, Ranger, Skald, Summoner, Unchained Summoner, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (a drop of your blood)
Range: personal
Duration: 1 round/level
Saving throw: see text
Spell resistance: see text
Target: you
Subschool: Compulsion
Descriptors: mind-affecting
:::

Whenever a creature you can see that threatens you makes an attack against one of your allies, as an
immediate action, you can compel that creature to attack you instead. When you compel a creature to
attack you, you must first overcome that creature's [spell resistance](ref/rule/spell-resistance),
and the creature can attempt a Will saving throw to ignore the compulsion.

A summoner casting this spell can choose his eidolon as the target of the spell.
