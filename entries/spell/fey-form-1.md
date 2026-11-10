+++
id = "ref/spell/fey-form-1"
kind = "spell"
title = "Fey Form I"
aon = "SpellDisplay.aspx?ItemName=Fey%20Form%20I"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_form_1", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "229"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
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
Level: 3: Alchemist, Bloodrager, Druid, Hunter, Investigator, Shaman\
4: Arcanist, Magus, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

You assume the form of a Small or Medium creature of the fey type. Your base speed changes to match
the new form's base speed, with a maximum speed of 60 feet (even if the chosen fey form has a base
speed in excess of that speed). If the form you assume has any of the following abilities, you gain
those abilities: climb speed 30 feet, fly speed 30 feet (average maneuverability), swim speed 30
feet, [darkvision](ref/rule/darkvision) 60 feet, [low-light vision](ref/rule/low-light-vision),
scent, and boot stomp. If the form you assume has the aquatic subtype, you can breathe air and
water. If the creature has any weaknesses, you gain those weaknesses. If a listed ability depends on
an item (as is the case with boot stomp), this spell transforms the nearest counterpart among your
worn gear into that item.

You can more easily cast spells that the creature has as
[spell-like abilities](ref/umr/spell-like-abilities), although you must still cast them as normal
for your class. When you cast a spell that the creature has as a spell-like ability, it requires no
verbal or somatic components and can't be countered.

_Small Fey:_ If you assume this form, you gain a +2 size bonus to your Dexterity and Constitution
scores.

_Medium Fey:_ If you assume this form, you gain a +2 size bonus to your Strength and Constitution
scores.
