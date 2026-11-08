+++
id = "ref/spell/polymorph-any-object"
kind = "spell"
title = "Polymorph Any Object"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "polymorph_any_object", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/polymorph-greater" },
]

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (mercury, gum arabic, and smoke)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature, or one nonmagical object of up to 100 cu. ft./level" },
]
duration = "see text"
saving_throw = "Fortitude negates (object); see text"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (mercury, gum arabic, and smoke)
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: Fortitude negates (object); see text
Spell resistance: yes (object)
Target: one creature, or one nonmagical object of up to 100 cu. ft./level
Subschool: Polymorph
:::

**Sources:** PRPG Core Rulebook pg 323

This spell functions like [greater polymorph](ref/spell/polymorph-greater), except that it changes
one object or creature into another. You can use this spell to transform all manner of objects and
creatures into new forms-you aren't limited to transforming a living creature into another living
form. The duration of the spell depends on how radical a change is made from the original state to
its transmuted state. The duration is determined by using the following guidelines.

|Changed Subject Is...|Increase to Duration Factor^[1](ref/spell/polymorph-any-object#footnote-n)^|
| --- | --- |
|Same kingdom (animal, vegetable, mineral)|+5|
|Same class (mammals, fungi, metals, etc.)|+2|
|Same size|+2|
|Related (twig is to tree, wolf fur is to wolf, etc.)|+2|
|Same or lower Intelligence|+2|

|Duration Factor|Duration|Example|
| --- | --- | --- |
|0|20 minutes|Pebble to human|
|2|1 hour|Marionette to human|
|4|3 hours|Human to marionette|
|5|12 hours|Lizard to manticore|
|6|2 days|Sheep to wool coat|
|7|1 week|Shrew to manticore|
|9+|Permanent|Manticore to shrew|

If the target of the spell does not have physical ability scores (Strength, Dexterity, or
Constitution), this spell grants a base score of 10 to each missing ability score. If the target of
the spell does not have mental ability scores (Intelligence, Wisdom, or Charisma), this spell grants
a score of 5 to such scores. Damage taken by the new form can result in the injury or death of the
polymorphed creature. In general, damage occurs when the new form is changed through physical force.
A nonmagical object cannot be made into a magic item with this spell. Magic items aren't affected by
this spell.

This spell cannot create material of great intrinsic value, such as copper, silver, gems, silk,
gold, platinum, mithral, or adamantine. It also cannot reproduce the special properties of cold iron
in order to overcome the [damage reduction](ref/rule/damage-reduction) of certain creatures.

This spell can also be used to duplicate the effects of baleful polymorph, greater polymorph, flesh
to stone, stone to flesh, transmute mud to rock, transmute metal to wood, or transmute rock to mud.

###### ^1^ {#footnote-n}

Add all that apply. Look up the total on the next table.
