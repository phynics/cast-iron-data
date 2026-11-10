+++
id = "ref/spell/ooze-form-3"
kind = "spell"
title = "Ooze Form III"
aon = "SpellDisplay.aspx?ItemName=Ooze%20Form%20III"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ooze_form_3", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ooze-form-2" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "233"

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

### Ooze Form III

This spell functions as [ooze form II](ref/spell/ooze-form-2) except you can also assume the form of
a Huge ooze. You gain [blindsight](ref/rule/blindsight-and-blindsense) 60 feet and a +8 resistance
bonus on saving throws against mind-affecting effects and poison as well.

_Huge Ooze:_ If you assume this form, you gain a +4 size bonus to your Strength, a +10 size bonus to
your Constitution score, a -10 penalty to your Dexterity score, base speed 20 feet, climb speed 20
feet, swim speed 30 feet, a slam attack (2d6 plus 2d6 acid and grab), and constrict (2d6).
