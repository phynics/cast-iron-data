+++
id = "ref/arc-shifter/weretouched"
kind = "archetype"
title = "Weretouched"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Weretouched"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weretouched", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "83"

[fields]
kind = "archetype"
features = [
  { anchor = "lycanthrope-aspect", level = 1 },
  { anchor = "lycanthropic-empathy", level = 1 },
  { anchor = "lycanthropic-wild-shape", level = 4 },
]
trades = [
  { alters = "Shifter aspect and all of its improvements", feature = "shifter-aspect", by = ["lycanthrope-aspect"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["lycanthropic-empathy"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["lycanthropic-wild-shape"] },
]
+++

Weretouched shifters are scions of lycanthropic forces, whether hereditary or supernaturally
imposed. They can assume both animal and hybrid forms, as a lycanthrope does.

## Lycanthrope Aspect (Su) {#lycanthrope-aspect}

At 1st level, a weretouched gains the shifter aspect ability, except the animal aspect chosen is the
only animal aspect the weretouched can gain. This alters her other class features, as detailed in
each relevant class feature. Otherwise, this ability functions identically to shifter aspect.

At 5th level, a weretouched gains DR/silver equal to [half](ref/misc/fractions-and-rounding) her
shifter level, to a maximum of DR 10/silver at 20th level. Additionally, a weretouched shifter
becomes immune to a lycanthrope's [curse of lycanthropy](ref/umr/curse-of-lycanthropy).

This alters shifter aspect and all of its improvements.

## Lycanthropic Empathy (Ex) {#lycanthropic-empathy}

At 1st level, a weretouched gains wild empathy and a +4 bonus on wild empathy checks, but this
ability works only on the type of animal she chose for her lycanthrope aspect.

This alters wild empathy.

## Lycanthropic Wild Shape (Su) {#lycanthropic-wild-shape}

At 4th level, when a weretouched uses wild shape, she can assume only the form of an animal of the
same type as her lycanthrope aspect. However, instead of assuming a major form, she can assume a
hybrid form that mixes the traits of her natural form and the major form of her aspect. While in a
hybrid form, she gain a +2 size bonus to her Strength score, a +2 natural armor bonus to her AC, and
all of the natural attacks and abilities listed by her major form. A weretouched also counts as
being in her natural form for the purpose of determining whether she can extend her shifter claws. A
weretouched's hybrid form is roughly the same size and shape as her natural form, albeit with
bestial qualities such as digitigrade legs or shaggy fur, so her equipment does not merge into her
new form when she shifts between her natural form and hybrid form. In addition, the size of a
weretouched's hybrid form is the same as the size of her natural form. This otherwise counts as
assuming a major form using wild shape.

This alters wild shape.
