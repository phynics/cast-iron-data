+++
id = "ref/spell/serenity"
kind = "spell"
title = "Serenity"
aon = "SpellDisplay.aspx?ItemName=Serenity"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "serenity", path = "json/spells15.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "236"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Mesmerist, Skald\
5: Cleric, Oracle, Psychic, Warpriest\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You fill the targets' minds with feelings of tranquility. Those attempting to commit violence become
stricken with wracking pain and take 3d6 points of nonlethal damage each round they attempt to harm
another creature. If attacked, affected individuals can defend themselves and may participate in
combat by using [Combat Expertise](ref/feat/combat-expertise), fighting defensively, or taking the
total defense action without triggering the spell's nonlethal damage.
