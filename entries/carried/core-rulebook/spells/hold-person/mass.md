+++
id = "ref/carried/core-rulebook/spells/hold-person/mass"
kind = "spell"
title = "Hold Person, Mass"
aon = "SpellDisplay.aspx?ItemName=Hold%20Person%2C%20Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Hold Person"]
tags = ["enchantment", "compulsion", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Hold Person/Mass", path = "core_rulebook/spell/hold_person_mass.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a small, straight piece of iron)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one or more humanoid creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (D); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
School: enchantment (compulsion) \[mind-affecting\]
Level: 7: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S, F/DF (a small, straight piece of iron)
Range: medium (100 ft. + 10 ft./level)
Targets: one or more humanoid creatures, no two of which can be more than 30 ft. apart
Duration: 1 round/level (D); see text
Saving Throw: Will negates; see text
Spell Resistance: yes
:::

_As hold person, but all within 30 ft._

This spell functions like _[hold person](ref/spell/hold-person)_, except as noted above.
