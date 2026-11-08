+++
id = "ref/spell/ooze-form-2"
kind = "spell"
title = "Ooze Form II"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ooze_form_2", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ooze-form-1" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a bit of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Alchemist, Arcanist, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a bit of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

### Ooze Form II

**Sources:** Ultimate Wilderness pg 233

This spell functions as [ooze form I](ref/spell/ooze-form-1) except you can also assume the form of
a Large ooze. You gain [blindsight](ref/rule/blindsight-and-blindsense) 30 feet and immunity to
critical hits and precision damage as well.

_Large Ooze:_ If you assume this form, you gain a +2 size bonus to your Strength score, a +8 size
bonus to your Constitution score, a slam attack (2d4 plus 1d6 acid and grab), and constrict (2d4),
and you take a -8 penalty to your Dexterity score.
