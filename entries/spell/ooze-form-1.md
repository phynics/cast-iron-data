+++
id = "ref/spell/ooze-form-1"
kind = "spell"
title = "Ooze Form I"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ooze_form_1", path = "json/spells7.json" },
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

**Sources:** Ultimate Wilderness pg 232

You assume the form of a Small or Medium ooze. Regardless of the type of ooze you transform into,
you gain base speed 10 feet, climb speed 10 feet, swim speed 20 feet, and
[blindsense](ref/rule/blindsight-and-blindsense) 30 feet. You gain a +4 resistance bonus on saving
throws against mind-affecting effects and poison. A wood or metal weapon that strikes you takes acid
damage as if from your slam unless the wielder succeeds at a Reflex saving throw.

_Small Ooze:_ If you assume this form, you gain a +4 size bonus to your Constitution score, a slam
attack (1d3 plus 1d3 acid), and constrict (1d3), and take, a -4 penalty to your Dexterity score.

_Medium Ooze:_ If you assume this form, you gain a +6 size bonus to your Constitution score, a -6
penalty to your Dexterity score, a slam attack (1d4 plus 1d4 acid), and constrict (1d4).
