+++
id = "ref/arc-shifter/oozemorph"
kind = "archetype"
title = "Oozemorph"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Oozemorph"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oozemorph", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]

[fields]
kind = "archetype"
features = [
  { anchor = "compression" },
  { anchor = "fluidic-body", level = 1 },
  { anchor = "morphic-weaponry", level = 1 },
  { anchor = "ooze-empathy", level = 1 },
  { anchor = "damage-reduction", level = 2 },
  { anchor = "clinging-ooze", level = 4 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Chimeric form", feature = "chimeric-aspect", by = ["fluidic-body"] },
  { replaces = "Greater chimeric form", feature = "greater-chimeric-aspect", by = ["fluidic-body"] },
  { replaces = "wild shape", feature = "wild-shape", by = ["fluidic-body"] },
  { replaces = "Shifter aspect, and all improvements of shifter aspect", feature = "shifter-aspect", by = ["fluidic-body"] },
  { replaces = "Shifter claws", feature = "shifter-claws", by = ["morphic-weaponry"] },
  { replaces = "Defensive instinct", feature = "defensive-instinct", by = ["damage-reduction"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["clinging-ooze"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["ooze-empathy"] },
]
+++

While most shifters are trained in druidic traditions that allow them to tap into animalistic
powers, others look instead to the simplest forms of life for inspiration. Known as oozemorphs,
these shifters focus on the ooze—a form of life as simple in construction as it is dangerous in
combat. While some shifters consider the oozemorph to be unsettling or even vile, these shifters
merely embrace a stranger form of life than most. They are not inherently evil, yet they are often
misunderstood by druidic circles and these circles' shifter champions.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An oozemorph is proficient with all simple weapons and light armor.

This replaces a shifter's normal weapon and armor proficiencies.

## Compression (Ex) {#compression}

An oozemorph gains [compression](ref/umr/compression) as per the universal monster rule. This
ability can be used regardless of the current form the oozemorph has taken.

## Fluidic Body (Su) {#fluidic-body}

An oozemorph's base form is not that of her race but rather that of a protoplasmic blob that has the
same volume and weight. An oozemorph treats her creature type as both [ooze](ref/type/ooze) and her
base creature type from her race for the purposes of effects targeting creatures by type (such as
_[bane](ref/magic-enh/bane)_ weapons and a ranger's [favored enemy](ref/ability/favored-enemy)). In
this form, the oozemorph is immune to critical hits and precision damage and can't be flanked.
However, she has no magic item slots and she cannot benefit from armor; cast spells; hold objects;
speak; or use any magic item that requires activation, is held, or is worn on the body.

An oozemorph reverts to this formless state whenever she is unconscious or in an area of antimagic.
This is treated as a [polymorph](ref/spelldef/polymorph) effect.

A number of times per day equal to half her level (minimum 1), an oozemorph can assume a humanoid
form as a move action. This transformation is identical to _[alter self](ref/spell/alter-self)_,
except the oozemorph can maintain the form for a number of hours equal to her level. Each hour after
this duration, the oozemorph must succeed at a DC 15 Fortitude save or revert back to her fluidic
body until she rests for at least 8 hours. This save DC increases by 1 for each additional hour
spent maintaining the form.

At 8th level, the oozemorph can treat this ability as _[beast shape I](ref/spell/beast-shape-1)_,
and at 15th level, she can treat this ability as _[beast shape II](ref/spell/beast-shape-2)_ or
_giant shape I_.

Ending this transformation at any time reverts the oozemorph back to her ooze form and renders her
[fatigued](ref/misc/fatigued) for a number of minutes equal to the number of hours she maintained
the form.

This replaces chimeric form, greater chimeric form, wild shape, shifter aspect, and all improvements
of shifter aspect.

## Morphic Weaponry (Ex) {#morphic-weaponry}

An oozemorph can create a number of natural weapons to fight with from any portion of her body,
regardless of her current form. At 1st level, as a move action, an oozemorph can form two primary
natural attacks that each deal 1d6 points of bludgeoning, piercing, or slashing damage, chosen by
the oozemorph when she forms them. An oozemorph can change the damage type of any number of her
natural weapons as a swift action. An oozemorph gains one additional primary natural attack at 6th
level and another at 15th level.

The total number of natural attacks an oozemorph has at any given time includes those gained via her
current form. For example, an 8th-level oozemorph who has taken the form of a wolf with
_[beast shape I](ref/spell/beast-shape-1)_ has a bite attack as part of that form; she can create
only two additional natural attacks via morphic weaponry, for a total of three attacks available to
her at that level. If the oozemorph later reverts to a humanoid form with no natural weapons, she
can instead create three morphic weapons.

This replaces shifter claws.

## Ooze Empathy (Ex) {#ooze-empathy}

An oozemorph gains the shifter's wild empathy class feature, but she can use it only to influence
the attitude of oozes with an Intelligence score of 2 or lower. An oozemorph can use this ability on
mindless oozes; when she does so, she imparts a modicum of intellect to the ooze to allow it to
respond to her commands.

This alters wild empathy.

## Damage Reduction (Ex) {#damage-reduction}

At 2nd level, an oozemorph gains DR 4/slashing while unencumbered and either wearing no armor or
wearing light nonmetal armor. This [damage reduction](ref/rule/damage-reduction) increases by 2 at
4th level and every 4 levels thereafter, to a maximum of DR 14/slashing at 20th level.

This replaces defensive instinct.

## Clinging Ooze (Ex) {#clinging-ooze}

At 4th level, when in her natural form, an oozemorph gains a climb speed of 10 feet.

This replaces woodland stride.
