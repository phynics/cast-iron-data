+++
id = "ref/arc-mesmerist/aromaphile"
kind = "archetype"
title = "Aromaphile"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Aromaphile"
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
features = [
  { anchor = "hypnotic-aroma", level = 1 },
  { anchor = "debilitating-aroma", level = 3 },
  { anchor = "aromatic-manipulation", level = 3 },
]
trades = [
  { replaces = "Hypnotic stare", feature = "hypnotic-stare", by = ["hypnotic-aroma"] },
  { replaces = "painful stare", feature = "painful-stare", by = ["hypnotic-aroma"] },
  { replaces = "towering ego", feature = "towering-ego", by = ["hypnotic-aroma"] },
  { replaces = "Bold stare", feature = "bold-stare", by = ["debilitating-aroma"] },
  { replaces = "Mental potency", feature = "mental-potency", by = ["aromatic-manipulation"] },
  { alters = "Touch treatment", feature = "touch-treatment", by = ["aromatic-manipulation"] },
]
+++

Rather than employ the baleful glares of the typical mesmerist, aromaphiles hypnotize others using
an array of sickeningly sweet scents developed from their unique ghoran physiology.

## Hypnotic Aroma (Su) {#hypnotic-aroma}

As a swift action, an aromaphile can use unique aspects of ghoran biology to release intoxicating
aromas in a 10-foot-radius [burst](ref/misc/burst) centered on him. All creatures within this area,
as well as creatures with [scent](ref/umr/scent) within 30 feet, take a -2 penalty on Will saving
throws. This penalty becomes -3 at 8th level. The aroma hovers around the aromaphile, moving with
him, and lasts for 1 minute. The hypnotic aroma must be inhaled to be effective, and creatures that
choose to [hold their breath](ref/misc/hold-your-breath), do not breathe, or are immune to inhaled
poisons are immune to its effect.

This replaces hypnotic stare, painful stare, and towering ego.

## Debilitating Aroma (Su) {#debilitating-aroma}

At 3rd level and every 4 levels thereafter, an aromaphile can imbue his hypnotic aroma with other
effects. These effects are the same as those listed within the bold stare mesmerist class feature,
but they affect creatures affected by his hypnotic aroma for as long as they are affected by that
ability. The aromaphile chooses one option each time he gains a new debilitating aroma improvement,
and the choice can't be changed later. The aromaphile can't choose the same debilitating aroma more
than once unless otherwise noted.

This replaces bold stare.

## Aromatic Manipulation (Su) {#aromatic-manipulation}

At 3rd level, the aromaphile can touch a creature affected by his hypnotic aroma to alter its mental
state. This functions as the touch treatment class feature, except the aromaphile cannot remove the
confused, cowering, or [stunned](ref/misc/stunned) conditions, and he cannot break enchantments
using this ability.

Instead, he adds [fatigued](ref/misc/fatigued) to his list of minor conditions and
[exhausted](ref/misc/exhausted) to his list of greater conditions.

An aromaphile can also use this ability to inflict hampering conditions on a target by touching it.
At 3rd level, he can cause his target to become [fascinated](ref/misc/fascinated) by his aroma. At
6th level, he can deaden the target's emotions (as per _[calm emotions](ref/spell/calm-emotions)_).
At 10th level, he can cause the target to become stunned. At 14th level, he can cause the target to
fall asleep (as per _[deep slumber](ref/spell/deep-slumber)_, except the Hit Die limit is equal to
the aromaphile's level + 2). The target can attempt a Will save to negate these effects (DC = 10 +
half the aromaphile's level + the aromaphile's Charisma modifier). On a failed save, the target
gains the chosen condition for a number of rounds equal to the aromaphile's level. Each round that
the target is affected, it can attempt a new Will save at the same DC to end the effect early. If
the target succeeds at such a save, its turn immediately ends.

This alters touch treatment and replaces mental potency.
