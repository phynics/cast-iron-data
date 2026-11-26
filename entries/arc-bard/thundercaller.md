+++
id = "ref/arc-bard/thundercaller"
kind = "archetype"
title = "Thundercaller"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Thundercaller"
source_ids = ["ultimate-wilderness", "varisia-birthplace-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thundercaller", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "41"
[[sources]]
publication = "varisia-birthplace-of-legends"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "bound-to-the-land", level = 1 },
  { anchor = "thunder-call", level = 3 },
  { anchor = "incite-rage", level = 6 },
  { anchor = "call-lightning", level = 8 },
  { anchor = "call-lightning-storm", level = 14 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["bound-to-the-land"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["thunder-call"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["incite-rage"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["incite-rage"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["call-lightning"] },
  { replaces = "Frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["call-lightning-storm"] },
]
+++

Thundercallers bear the knowledge of the ancients, wielding it like a weapon to protect the land for
which they care so deeply. Their voices ring like thunder, calling the sky's wrath down upon their
enemies and summoning furious rage to bolster their allies.

## Bound to the Land (Ex) {#bound-to-the-land}

A thundercaller gains a bonus equal to [half](ref/misc/fractions-and-rounding) her level on Handle
Animal checks, Knowledge (nature) checks, and Survival checks.

This replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

A thundercaller gains the following types of bardic performance.

## Thunder Call (Su) {#thunder-call}

At 3rd level, the thundercaller can start a performance to unleash a deafening peal of thunder. This
allows the thundercaller to spend a round of performance to create an effect similar to the spell
_[sound burst](ref/spell/sound-burst)_ (having the same range and area and allowing the same saving
throw). At 7th level, the sonic damage dealt by this blast of sound increases to 3d8. This damage
further increases by 2d8 at 11th level, and every 4 levels thereafter. A creature that succeeds at
its saving throw against thunder call is immune to the stunning effect but still takes sonic damage.
Beginning this performance is always a standard action.

This performance replaces inspire competence.

## Incite Rage (Su) {#incite-rage}

At 6th level, the thundercaller can induce a furious [rage](ref/spell/rage) in one creature within
30 feet. This effect functions as the _rage_ spell and lasts as long as the target can hear the
thundercaller's performance. Any unwilling creature targeted is affected if it fails a Will saving
throw (DC = 10 + half the thundercaller's level + the thundercaller's Charisma modifier). A target
that succeeds at its saving throw is immune to this power for 24 hours. The thundercaller cannot
target herself with this ability. If the target has the rage class feature, it can instead
immediately rage and stay in this rage without consuming rounds of rage per day as long as the
thundercaller continues performing. This performance is a mind-affecting effect and relies on
audible components.

This replaces suggestion and mass suggestion.

## Call Lightning (Su) {#call-lightning}

At 8th level, the thundercaller can use her performance to summon bolts of lightning, as per the
spell _[call lightning](ref/spell/call-lightning)_. The lightning storm lasts for as long as she
continues her performance, calling down one bolt of lightning per round as a standard action. The
damage of these lightning bolts can be increased in stormy areas or can be limited as
_[call lightning](ref/spell/call-lightning)_ describes.

This performance replaces dirge of doom.

## Call Lightning Storm (Su) {#call-lightning-storm}

At 14th level, the thundercaller can use her performance to summon bolts of lightning, as per the
spell _[call lightning storm](ref/spell/call-lightning-storm)_. The lightning storm lasts for as
long as she continues her performance, calling down one bolt of lightning per round as a standard
action. The damage of these lightning bolts can be increased in stormy areas or can be limited as
_[call lightning](ref/spell/call-lightning)_ describes.

This performance replaces frightening tune.
