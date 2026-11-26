+++
id = "ref/arc-shifter/dragonblood-shifter"
kind = "archetype"
title = "Dragonblood Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Dragonblood%20Shifter"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragonblood_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "wilderness-origins"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "draconic-aspect" },
  { anchor = "wyrmshifter", level = 9 },
  { anchor = "improved-wyrmshifter", level = 14 },
  { anchor = "greater-wyrmshifter", level = 20 },
]
trades = [
  { replaces = "Shifter aspect and all improvements to shifter aspect", feature = "shifter-aspect", by = ["draconic-aspect"] },
  { replaces = "Chimeric aspect", feature = "chimeric-aspect", by = ["wyrmshifter"] },
  { replaces = "Greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["improved-wyrmshifter"] },
  { replaces = "Final aspect", feature = "final-aspect", by = ["greater-wyrmshifter"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wyrmshifter"] },
]
+++

Dragonblood shifters draw upon the inherent strength and majesty of the true dragons, gaining a
measure of their powers from their association.

## Draconic Aspect (Su) {#draconic-aspect}

A dragonblood shifter can temporarily imbue her body with draconic majesty as a swift action. When
activating this ability, the shifter must select one of the chromatic or metallic dragon types from
the table on page 6. Her draconic aspect abilities grant resistances and deal a type of damage based
on the chosen dragon type. While shifted into this form, she gains the [scent](ref/umr/scent)
ability and energy [resistance](ref/umr/resistance) 5 against the energy type that corresponds to
her selected dragon type. She can maintain this form for a number of minutes per day equal to 3 +
her shifter level. The duration does not need to be consecutive, but it must be spent in 1-minute
increments. The shifter can select a different dragon type every time she uses this ability, but she
must end her current draconic aspect and activate this ability again in order to change her chosen
dragon type.

|Dragon Type|Energy Type|
| --- | --- |
|Black|Acid|
|Blue|Electricity|
|Green|Acid|
|Red|Fire|
|White|Cold|
|Brass|Fire|
|Bronze|Electricity|
|Copper|Acid|
|Gold|Fire|
|Silver|Cold|

At 5th level, the energy resistance granted by the dragonblood shifter's draconic aspect increases
to 10.

At 10th level, the energy resistance granted by the dragonblood shifter's draconic aspect increases
to 15, and she gains a [breath weapon](ref/umr/breath-weapon) of her energy type that deals 1d6
points of damage per shifter level within a 30-foot cone. A target can attempt a Reflex save (DC =
10 + half the dragonblood shifter's level + her Charisma modifier) to reduce damage by half. The
dragonblood shifter can use her breath weapon once per day.

At 15th level, the energy resistance granted by the dragonblood shifter's draconic aspect increases
to 20, and she can use her breath weapon twice per day.

At 20th level, the dragonblood shifter becomes [immune](ref/umr/immunity) to the energy type that
corresponds to her selected dragon type while in her draconic aspect. In addition, she gains
[spell resistance](ref/rule/spell-resistance) equal to 10 + her shifter level, and she can use her
breath weapon three times per day.

This replaces shifter aspect and all improvements to shifter aspect.

## Wyrmshifter (Su) {#wyrmshifter}

At 9th level, a dragonblood shifter can push her form closer to that of a true dragon. She gains a
+2 racial bonus on saving throws against sleep and paralysis effects. She does not gain the wild
shape ability until 9th level. When using the ability, she takes on the form of a true dragon; this
ability functions as _[form of the dragon I](ref/spell/form-of-the-dragon-1)_ instead of
_[beast shape II](ref/spell/beast-shape-2)_. A dragonblood shifter can use wild shape for a number
of minutes each day equal to her shifter level + her Wisdom modifier. This duration doesn't need to
be consecutive, but it must be spent in 1-minute increments. For abilities that function based on
uses of wild shape, each minute of wild shape counts as a use.

This alters wild shape and replaces chimeric aspect.

## Improved Wyrmshifter (Su) {#improved-wyrmshifter}

At 14th level, a dragonblood shifter's ties to her draconic abilities grow stronger. Her bonus on
saves against sleep and paralysis effects increases to +4. Her wild shape ability now functions as
_[form of the dragon II](ref/spell/form-of-the-dragon-2)_, and she can use it for a number of
minutes each day equal to twice her shifter level + her Wisdom modifier, though it still must be
used in 1-minute increments.

This replaces greater chimeric aspect.

## Greater Wyrmshifter (Su) {#greater-wyrmshifter}

At 20th level, a dragonblood shifter's tie to her draconic abilities reaches its peak. She becomes
immune to sleep and paralysis effects. She can use wild shape to transform into a dragon for a
number of hours each day equal to her shifter level + her Wisdom modifier. This duration does not
need to be consecutive, but it must be spent in 1-hour increments. For abilities that function based
on uses of wild shape, each hour of wild shape counts as a use.

This replaces final aspect.
