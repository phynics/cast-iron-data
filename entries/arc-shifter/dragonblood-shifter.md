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
replaces = ["Shifter aspect", "Chimeric aspect", "Greater chimeric aspect", "Final aspect"]
alters = ["Wild shape"]
replaces_features = ["shifter-aspect", "chimeric-aspect", "greater-chimeric-aspect", "final-aspect"]
alters_features = ["wild-shape"]
+++

Dragonblood shifters draw upon the inherent strength and majesty of the true dragons, gaining a
measure of their powers from their association.

**Dragon Attacks**

**Ability:** A shifter that uses **alternate natural attacks** can choose from Bite (B, P, S), Tail
slap (B), or Wing (B).

**Draconic Aspect (Su)**

**Action:** Swift Action

**At 10th Level:** The energy resistance granted by the dragonblood shifter's draconic aspect
increases to 15, and she gains a [breath weapon](ref/umr/breath-weapon) of her energy type that
deals 1d6 points of damage per shifter level within a 30-foot cone. A target can attempt a Reflex
save (DC = 10 + half the dragonblood shifter's level + her Charisma modifier) to reduce damage by
half. The dragonblood shifter can use her breath weapon once per day.

**At 15th Level:** The energy resistance granted by the dragonblood shifter's draconic aspect
increases to 20, and she can use her breath weapon twice per day.

**At 20th Level:** The dragonblood shifter becomes [immune](ref/umr/immunity) to the energy type
that corresponds to her selected dragon type while in her draconic aspect. In addition, she gains
[spell resistance](ref/rule/spell-resistance) equal to 10 + her shifter level, and she can use her
breath weapon three times per day.

**At 5th Level:** The energy resistance granted by the dragonblood shifter's draconic aspect
increases to 10.

**Replaces:** Shifter aspect

**Special:** The shifter can select a different dragon type every time she uses this ability, but
she must end her current draconic aspect and activate this ability again in order to change her
chosen dragon type.

**Usage:** 1 minute/day per shifter3 level; these minutes need not be consecutive, but must be spent
in 1-minute increments

A dragonblood shifter can temporarily imbue her body with draconic majesty. When activating this
ability, the shifter must select one of the chromatic or metallic dragon types from the table below.
Her draconic aspect abilities grant resistances and deal a type of damage based on the chosen dragon
type. While shifted into this form, she gains the [scent](ref/umr/scent) ability and energy
[resistance](ref/umr/resistance) 5 against the energy type that corresponds to her selected dragon
type.

|Dragon Type|Energy Type|
| --- | --- |
|Black, Green, or Copper|Acid|
|Blue or Bronze|Electricity|
|Red, Brass, or Gold|Fire|
|White or Silver|Cold|

**Wyrmshifter (Su)**

**Ability:** She does not gain the _wild shape_ ability until 9th level. When using the ability, she
takes on the form of a true dragon; this ability functions as
[form of the dragon I](ref/spell/form-of-the-dragon-1) instead of
[beast shape II](ref/spell/beast-shape-2).

**Alters:** Wild shape

**Flavor:** A dragonblood shifter can push her form closer to that of a true dragon.

**Gained:** At 9th Level

**Passive:** She gains a +2 racial bonus on saving throws against sleep and paralysis effects.

**Replaces:** Chimeric aspect

**Special:** For abilities that function based on uses of _wild shape,_ each minute of this ability
counts as a use.

**Usage:** shifter level + Wisdom modifier minutes/day; these minutes need not be consecutive, but
must be spent in 1-minute increments

**Improved Wyrmshifter (Su)**

**Ability:** Her _wild shape_ ability now functions as
[form of the dragon II](ref/spell/form-of-the-dragon-2), and she can use it for a number of minutes
each day equal to twice her shifter level + her Wisdom modifier, though it still must be used in
1-minute increments.

**Flavor:** A dragonblood shifter's ties to her draconic abilities grow stronger.

**Gained:** At 14th Level

**Passive:** Her bonus on saves against sleep and paralysis effects increases to +4.

**Replaces:** Greater chimeric aspect

**Greater Wyrmshifter (Su)**

**Ability:** She can use _wild shape_ to transform into a dragon for a number of hours each day
equal to her shifter level + her Wisdom modifier. This duration does not need to be consecutive, but
it must be spent in 1-hour increments.

**Flavor:** A dragonblood shifter's tie to her draconic abilities reaches its peak.

**Gained:** At 20th Level

**Passive:** She becomes immune to sleep and paralysis effects.

**Replaces:** Final aspect

**Special:** For abilities that function based on uses of _wild shape,_ each hour of this ability
counts as a use.
