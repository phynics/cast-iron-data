+++
id = "ref/spell/rage"
kind = "spell"
title = "Rage"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rage", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "329"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one willing living creature per three levels, no two of which may be more than 30 ft. apart" },
]
duration = "concentration+ 1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Skald\
3: Alchemist, Arcanist, Bloodrager, Investigator, Psychic, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level (D)
Saving throw: none
Spell resistance: yes
Targets: one willing living creature per three levels, no two of which may be more than 30 ft. apart
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

Each affected creature gains a +2 morale bonus to Strength and Constitution, a +1 morale bonus on
Will saves, and a -2 penalty to AC. The effect is otherwise identical with a
[barbarian's](ref/class/barbarian) rage except that the subjects aren't fatigued at the end of the
rage.
