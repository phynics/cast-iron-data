+++
id = "ref/spell/power-word-kill"
kind = "spell"
title = "Power Word Kill"
aon = "SpellDisplay.aspx?ItemName=Power%20Word%20Kill"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "power_word_kill", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "324"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["death", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature with 100 hp or less" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one living creature with 100 hp or less
Subschool: Compulsion
Descriptors: death, mind-affecting
:::

You utter a single word of power that instantly kills one creature of your choice, whether the
creature can hear the word or not. Any creature that currently has 101 or more hit points is
unaffected by power word kill.
