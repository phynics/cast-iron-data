+++
id = "ref/spell/power-word-stun"
kind = "spell"
title = "Power Word Stun"
aon = "SpellDisplay.aspx?ItemName=Power%20Word%20Stun"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "power_word_stun", path = "json/spells14.json" },
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
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature with 150 hp or less" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: none
Spell resistance: yes
Target: one creature with 150 hp or less
Subschool: Compulsion
Descriptors: mind-affecting
:::

You utter a single word of power that instantly causes one creature of your choice to become
stunned, whether the creature can hear the word or not. The duration of the spell depends on the
target's current hit point total. Any creature that currently has 151 or more hit points is
unaffected by power word stun.

|Hit Points|Duration|
| --- | --- |
|50 or less|4d4 rounds|
|51 to 100|2d4 rounds|
|101 to 150|1d4 rounds|
