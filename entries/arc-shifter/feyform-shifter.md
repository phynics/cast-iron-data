+++
id = "ref/arc-shifter/feyform-shifter"
kind = "archetype"
title = "Feyform Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Feyform%20Shifter"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feyform_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "wilderness-origins"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "fey-aspect" },
  { anchor = "fey-shape", level = 4 },
  { anchor = "fey-shifter", level = 9 },
  { anchor = "greater-fey-shifter", level = 14 },
  { anchor = "final-aspect", level = 20 },
]
trades = [
  { replaces = "All improvements to shifter aspect", feature = "shifter-aspect", by = ["fey-aspect"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["fey-shape"] },
  { alters = "Chimeric aspect", feature = "chimeric-aspect", by = ["fey-shifter"] },
  { alters = "Greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["greater-fey-shifter"] },
  { alters = "Final aspect", feature = "final-aspect", by = ["final-aspect"] },
]
+++

Feyform shifters are intimately linked to the First World, and can draw from it to gain otherworldly
powers.

## Fey Aspect (Su) {#fey-aspect}

A feyform shifter can take on a First World aspect and assume fey traits as a swift action. While in
this form, she gains [low-light vision](ref/rule/low-light-vision) (or
[darkvision](ref/rule/darkvision) with a range of 30 feet, if she already has low-light vision) and
DR 1/cold iron. Her body outline becomes indistinct; she is treated as though she has
[concealment](ref/rule/concealment), except that she cannot use this concealment to attempt Stealth
checks. She can maintain this form for a number of minutes per day equal to 3 + her shifter level.
The duration does not need to be consecutive, but it must be spent in 1-minute increments.

At 5th level, the feyform shifter's DR increases to 2/cold iron, and she grows a pair of
butterfly-like wings that grant her a fly speed of 30 feet with average maneuverability.

At 10th level, the feyform shifter's DR increases to 5/cold iron, and she gains a +4 bonus on saving
throws against enchantment spells and effects.

At 15th level, the feyform shifter's DR increases to 7/cold iron, and her fly speed maneuverability
increases to good.

At 20th level, the feyform shifter's DR increases to 10/cold iron. She becomes resistant to
movement-impairing effects (as _[freedom of movement](ref/spell/freedom-of-movement)_) and gains
[spell resistance](ref/rule/spell-resistance) equal to 10 + her level.

This alters and replaces all improvements to shifter aspect.

## Fey Shape (Su) {#fey-shape}

At 4th level, a feyform shifter can use her wild shape ability to become a fey creature. The fey
shifter must spend at least one use of wild shape to transform into a fey creature; this ability
functions as _[fey form I](ref/spell/fey-form-1)_, except that it lasts for only 1 minute per use of
wild shape spent. Using fey shape or reverting back is a standard action that does not cause attacks
of opportunity. At 8th level this ability instead functions as
_[fey form II](ref/spell/fey-form-2)._ At 10th level this ability functions as
_[fey form III](ref/spell/fey-form-3)_, and at 14th level it functions as
_[fey form IV](ref/spell/fey-form-4)_.

This alters wild shape.

## Fey Shifter (Su) {#fey-shifter}

At 9th level, a feyform shifter gains a second shifter aspect, chosen from the animal aspects
normally available to shifters. When she uses her shifter aspect ability to take on her fey aspect,
she can choose a second aspect and assume the minor form of that aspect, alongside her fey aspect,
allowing her to combine her fey aspect with the animal aspects available to her.

This modifies chimeric aspect.

## Greater Fey Shifter (Su) {#greater-fey-shifter}

At 14th level, a feyform shifter gains a third aspect. When she uses her shifter aspect ability to
take on her fey aspect, she can choose two aspects and assume the minor form of each aspect,
alongside her fey aspect.

This modifies greater chimeric aspect.

## Final Aspect (Su) {#final-aspect}

At 20th level, a feyform shifter gains access to a fourth aspect. When she uses shifter aspect, she
can assume the minor forms of all her aspects in addition to her fey aspect, and she can use her
major and minor forms at will.

This alters final aspect.
