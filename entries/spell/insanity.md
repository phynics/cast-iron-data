+++
id = "ref/spell/insanity"
kind = "spell"
title = "Insanity"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "insanity", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "301"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Mesmerist\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

The affected creature suffers from a continuous [confusion](ref/spell/confusion) effect, as the
spell.

[Remove curse](ref/spell/remove-curse) does not remove insanity.
[Greater restoration](ref/spell/restoration-greater), [heal](ref/spell/heal),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), or [wish](ref/spell/wish) can
restore the creature.
