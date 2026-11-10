+++
id = "ref/spell/power-word-blind"
kind = "spell"
title = "Power Word Blind"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "power_word_blind", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "324"

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
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature with 200 hp or less" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Mesmerist\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: none
Spell resistance: yes
Target: one creature with 200 hp or less
Subschool: Compulsion
Descriptors: mind-affecting
:::

You utter a single word of power that causes a creature to become blinded, whether the creature can
hear the word or not. The duration of the spell depends on the target's current hit point total. Any
creature that currently has 201 or more hit points is unaffected.

|Hit Points|Duration|
| --- | --- |
|50 or less|Permanent|
|51 to 100|1d4+1 minutes|
|101 to 200|1d4+1 rounds|
