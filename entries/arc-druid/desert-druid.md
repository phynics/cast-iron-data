+++
id = "ref/arc-druid/desert-druid"
kind = "archetype"
title = "Desert Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Desert%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "desert_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "99"

[fields]
kind = "archetype"
features = [
  { anchor = "desert-native", level = 2 },
  { anchor = "sandwalker", level = 3 },
  { anchor = "desert-endurance", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "shaded-vision", level = 9 },
  { anchor = "dunemeld", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["desert-native"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["sandwalker"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["desert-endurance"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["shaded-vision"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["dunemeld"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

Not all climates are verdant paradises, but even in the sere deserts there is life—though often
hidden from the sun and rarely friendly—and raw, desolate beauty. Here desert druids come to pay
homage, protect and maintain the few habitable locales, and witness nature's majesty in all its
burning, merciless glory.

## Desert Native (Ex) {#desert-native}

At 2nd level, a desert druid gains a bonus on Initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks equal to 1/2 her druid level in desert terrain, and she
cannot be tracked in such environments. This ability replaces woodland stride.

## Sandwalker (Ex) {#sandwalker}

At 3rd level, a desert druid suffers no penalty to speed or on Acrobatics or Stealth checks when
moving through sandy or desert terrain. This ability replaces trackless step.

## Desert Endurance (Ex) {#desert-endurance}

At 4th level, a desert druid ignores the effects of a hot climate as if using
_[endure elements](ref/spell/endure-elements)_. She also has a reduced need to eat and drink, as if
wearing a _[ring of sustenance](ref/magic-ring/ring-of-sustenance)_ (though normal sleep is still
required). This ability replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

A desert druid gains this ability at 6th level, except that her effective druid level for the
ability is equal to her druid level - 2. A desert druid cannot use wild shape to adopt a plant form.
At 10th level she can assume the form of a Small or Medium vermin, at 12th level a Tiny or Large
vermin, and at 14th level a Diminutive or Huge vermin. This effect functions as
_[beast shape IV](ref/spell/beast-shape-4)_ (treating the vermin as an animal to determine its
ability and natural armor modifiers).

## Shaded Vision (Ex) {#shaded-vision}

At 9th level, a desert druid becomes immune to blinding and dazzling effects and gains a +2 bonus on
saving throws against [gaze](ref/umr/gaze) attacks and illusions of the figment and pattern
subschools. This ability replaces venom immunity.

## Dunemeld (Ex) {#dunemeld}

At 13th level, a desert druid can assume the form of a swirling mass of sand at will. This is
equivalent to _[gaseous form](ref/spell/gaseous-form)_, but the druid gains a land and burrow speed
of 10 feet rather than a fly speed. While in this form, the druid gains a circumstance bonus on
Stealth checks made in desert terrain equal to her druid level. This ability replaces a thousand
faces.
