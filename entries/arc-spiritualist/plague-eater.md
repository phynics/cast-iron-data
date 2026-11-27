+++
id = "ref/arc-spiritualist/plague-eater"
kind = "archetype"
title = "Plague Eater"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Plague%20Eater"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plague_eater", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "heroes-of-golarion"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "plague-ward", level = 1 },
  { anchor = "spiritual-inoculation", level = 4 },
  { anchor = "remove-sickness", level = 5 },
  { anchor = "disfiguring-touch", level = 7 },
  { anchor = "remove-disease", level = 9 },
  { anchor = "fused-well-being", level = 10 },
  { anchor = "greater-spiritual-inoculation", level = 12 },
  { anchor = "withdraw-affliction", level = 16 },
]
trades = [
  { replaces = "Detect undead", feature = "detect-undead", by = ["remove-sickness"] },
  { replaces = "Calm spirit", feature = "calm-spirit", by = ["disfiguring-touch"] },
  { replaces = "See invisibility", feature = "see-invisibility", by = ["remove-disease"] },
  { replaces = "Fused consciousness", feature = "fused-consciousness", by = ["fused-well-being"] },
  { replaces = "Call spirit", feature = "call-spirit", by = ["withdraw-affliction"] },
  { alters = "Phantom", feature = "phantom", by = ["plague-ward"] },
  { alters = "shared consciousness", feature = "shared-consciousness", by = ["plague-ward"] },
  { alters = "Spiritual interference", feature = "spiritual-interference", by = ["spiritual-inoculation"] },
  { alters = "Greater spiritual interference", feature = "greater-spiritual-interference", by = ["greater-spiritual-inoculation"] },
]
+++

Iobaria has been ravaged by plague for centuries, and many of its dead do not rest. These ghosts
often flock around specialized spiritualists called plague eaters. Such a spiritualist bears the
weight of many souls within her consciousness, spirits that remember the devastation of disease and
seek to protect their host from infections, cleanse others of plague, and use disease itself as a
weapon.

## Plague Ward {#plague-ward}

A plague eater does not bond with a single spirit, but rather a group of spirits gathered around her
psychic presence. The spiritualist can meditate on an emotional focus during her 8-hour rest and
bond with a spirit from her community with a matching focus. A spirit associated with the chosen
emotion links with the spiritualist and acts as her phantom until the plague eater changes her
emotional focus with another 8-hour rest. The changing roster of spirits dilutes the bond between
the plague eater and her community, and the manifesting phantom has a level 1 lower than the
spiritualist's level (minimum level 1).

While a phantom is confined in a plague eater's consciousness (but not while it's fully manifested
or banished to the Ethereal Plane), it grants a +4 bonus on saving throws against disease. At 12th
level, this bonus increases to +8. In addition, the phantom grants the plague eater the
[Skill Focus](ref/feat/skill-focus) feat in one of the skills determined by the phantom's emotional
focus. This skill is chosen by the plague eater the first time she confines the phantom tied to that
particular emotional focus. Once this choice is made for a given emotional focus, it cannot be
changed.

This alters phantom and shared consciousness.

## Spiritual Inoculation (Su) {#spiritual-inoculation}

At 4th level, whenever a plague eater is within reach of her ectoplasmic manifested phantom, she
gains a +4 circumstance bonus on saving throws against disease.

This alters spiritual interference.

## Remove Sickness (Sp) {#remove-sickness}

At 5th level, a plague eater's understanding of disease grows to the point where she can cast
_[remove sickness](ref/spell/remove-sickness)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her spiritualist
level.

This replaces detect undead.

## Disfiguring Touch (Sp) {#disfiguring-touch}

At 7th level, a plague eater can inflict upon others the superficial disfigurement associated with
plague by casting _[disfiguring touch](ref/spell/disfiguring-touch)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day. At 11th level and every 4 levels
thereafter, the spiritualist can use this ability an additional time per day (to a maximum of four
times per day at 19th level).

This replaces calm spirit.

## Remove Disease (Sp) {#remove-disease}

At 9th level, a plague eater gains the ability to purge disease from herself and others. She gains
the ability to cast _[remove disease](ref/spell/remove-disease)_ as a
[spell-like ability](ref/umr/spell-like-abilities) three times per day.

This ability replaces see invisibility

## Fused Well-Being (Su) {#fused-well-being}

At 10th level, a plague eater always gains the benefits of bonded senses when her phantom is
manifested. She also gains the skill ranks and bonus to resist disease granted by the spirit's
emotional focus, even when her phantom is manifested.

This replaces fused consciousness.

## Greater Spiritual Inoculation (Su) {#greater-spiritual-inoculation}

At 12th level, the plague eater becomes immune to disease, including supernatural and magical
diseases. In addition, whenever a manifested phantom is in ectoplasmic form, each of the plague
eater's allies within the phantom's reach gains a +4 circumstance bonus on saving throws against
disease.

This ability alters greater spiritual interference.

## Withdraw Affliction (Sp) {#withdraw-affliction}

At 16th level, a plague eater can reach into a body, remove an affliction directly from the flesh,
and use the diseased matter as a weapon. She can cast
_[withdraw affliction](ref/spell/withdraw-affliction)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her spiritualist
level.

This replaces call spirit.
