+++
id = "ref/spell/matchmaker"
kind = "spell"
title = "Matchmaker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "matchmaker", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "220"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "S, M (a rose petal)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "two living creatures" },
]
duration = "1 hour/level"
saving_throw = "Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Skald\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S, M (a rose petal)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level
Saving throw: Will partial, see text
Spell resistance: yes
Target: two living creatures
Subschool: Charm
Descriptors: mind-affecting
:::

You entice the target creatures to become romantically interested in one another. Each creature
saves and applies [spell resistance](ref/rule/spell-resistance) separately. Both must be affected
for the spell to have an effect. If either creatures has a prior unfriendly or hostile attitude
toward the other, it receives a +4 bonus on its saving throw.

This spell doesn't override the targets' normal sexual preferences or other limitations. If romantic
feelings are incompatible for this reason, the creature instead feels an intimate platonic bond with
the other.
