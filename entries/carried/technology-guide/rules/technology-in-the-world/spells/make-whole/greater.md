+++
id = "ref/carried/technology-guide/rules/technology-in-the-world/spells/make-whole/greater"
kind = "spell"
title = "Make Whole, Greater"
source_ids = ["technology-guide"]
section = ["Rules", "Technology in the world", "Spells", "Make Whole"]
tags = ["transmutation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Technology Guide/Rules/Technology in the world/Spells/Make Whole/Greater", path = "technology_guide/spell/make_whole_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "10 ft."
effects = [
  { label = "Target", value = "one object of up to 5 lb./level" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless, object)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
School: transmutation
Level: 4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting Time: 1 standard action
Components: V, S
Range: 10 ft.
Target: one object of up to 5 lb./level
Duration: instantaneous
Saving Throw: Will negates (harmless, object)
Spell Resistance: yes (harmless, object)
:::

This spell repairs 1d6 points of damage plus 1 point per level when cast on a construct creature
(maximum 10d6+10). _[Greater make whole](ref/spell/make-whole-greater)_ can fix destroyed magic
items or technological items (items at 0 hit points or fewer), and restores the magic properties of
the item if your caster level at least equal to that of the item. This spell otherwise functions as
_[make whole](ref/spell/make-whole)_.
