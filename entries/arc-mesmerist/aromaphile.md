+++
id = "ref/arc-mesmerist/aromaphile"
kind = "archetype"
title = "Aromaphile"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aromaphile", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "18"

[fields]
kind = "archetype"
replaces = ["Hypnotic stare", "painful stare", "towering ego", "Bold stare", "Mental potency"]
alters = ["Touch treatment"]
+++

Rather than employ the baleful glares of the typical mesmerist, aromaphiles hypnotize others using
an array of sickeningly sweet scents developed from their unique ghoran physiology.

**Prerequisites:** Ghoran

**Hypnotic Aroma (Su)**

**At 8th Level:** This penalty becomes -3.

**Replaces:** Hypnotic stare, painful stare, towering ego

**Special:** The hypnotic aroma must be inhaled to be effective, and creatures that choose to
[hold their breath](ref/misc/hold-your-breath), do not breathe, or are immune to inhaled poisons are
immune to its effect.

**Swift:** An aromaphile can use unique aspects of ghoran biology to release intoxicating aromas in
a 10-foot-radius [burst](ref/misc/burst) centered on him. All creatures within this area, as well as
creatures with [scent](ref/umr/scent) within 30 feet, take a -2 penalty on Will saving throws. The
aroma hovers around the aromaphile, moving with him, and lasts for 1 minute.

**Debilitating Aroma (Su)**

**Ability:** An aromaphile can imbue his hypnotic aroma with another effect, chosen from those
listed within the _bold stare_ mesmerist class feature. However, they affect creatures affected by
his _hypnotic aroma_ for as long as they are affected by that ability.

**Gained:** At 3rd Level

**Repeat:** The aromaphile selects a new _debilitating aroma._, 7, 4

**Replaces:** Bold stare

**Special:** The aromaphile chooses one option each time he gains a new debilitating aroma
improvement, and the choice can't be changed later. The aromaphile can't choose the same
debilitating aroma more than once unless otherwise noted.

**Aromatic Manipulation (Su)**

**Action:** Ability

**Alters:** Touch treatment

**At 10th Level:** His touch can cause the target to become [stunned](ref/misc/stunned).

**At 14th Level:** His touch can cause the target to fall asleep (as per
[deep slumber](ref/spell/deep-slumber), except the Hit Die limit is equal to the aromaphile's
level + 2).

**At 6th Level:** His touch can deaden the target's emotions (as per
[calm emotions](ref/spell/calm-emotions)).

**Gained:** At 3rd Level

**Replaces:** Mental potency

**Special:** The target can attempt a Will save to negate these ill effects (DC = 10 + half the
aromaphile's level + the aromaphile's Charisma modifier). On a failed save, the target gains the
chosen condition for a number of rounds equal to the aromaphile's level. Each round that the target
is affected, it can attempt a new Will save at the same DC to end the effect early. If the target
succeeds at such a save, its turn immediately ends.

The aromaphile can touch a creature affected by his _hypnotic aroma_ to alter its mental state. This
functions as the _touch treatment_ class feature, except the aromaphile cannot remove the _confused,
cowering,_ or _stunned_ conditions, and he cannot _break enchantments_ using this ability. Instead,
he can remove the [fatigued](ref/misc/fatigued) condition at 3rd level and the
[exhausted](ref/misc/exhausted) condition at 10th level.

An aromaphile can also use this ability to inflict hampering conditions on a target by touching it.
Initially, he can cause his target to become [fascinated](ref/misc/fascinated) by his _aroma,_ but
he gains more abilities as he gains levels.
