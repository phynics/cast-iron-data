+++
id = "ref/arc-bard/savage-skald"
kind = "archetype"
title = "Savage Skald"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Savage%20Skald"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "savage_skald", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "84"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiring-blow", level = 1 },
  { anchor = "incite-rage", level = 6 },
  { anchor = "song-of-the-fallen", level = 10 },
  { anchor = "berserkergang", level = 12 },
  { anchor = "battle-song", level = 18 },
]
trades = [
  { replaces = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["inspiring-blow"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["incite-rage"] },
  { replaces = "Jack of all trades", feature = "jack-of-all-trades", by = ["song-of-the-fallen"] },
  { replaces = "Soothing performance", feature = "bardic-performance", power = "soothing performance", by = ["berserkergang"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["battle-song"] },
]
+++

Far from civilization, furious tribes have their own war-singers, work-chanters, and lore-keepers,
savaging enemies with song and sword alike.

## Bardic Performance {#bardic-performance}

A savage skald gains the following types of bardic performance.

## Inspiring Blow (Su) {#inspiring-blow}

A savage skald roars his war-cries with each telling blow. When he confirms a critical hit, he can
start this performance as an immediate action (ending any other performances). He gains
[temporary hit points](ref/rule/temporary-hit-points) equal to his Charisma modifier (if positive),
and all allies within 30 feet gain a +1 morale bonus on their next attack roll prior to the start of
his next turn. These temporary hit points remain until the bard ends his performance. This
performance replaces fascinate.

## Incite Rage (Su) {#incite-rage}

At 6th level, a savage skald can induce a furious [rage](ref/spell/rage) in one creature within 30
feet. This effect functions as a _rage_ spell that lasts as long as the target can hear the bard's
performance; however, unwilling creatures can be affected if they fail a Will save (DC 10 + 1/2 the
bard's level + the bard's Cha modifier). Success renders the target immune to this power for 24
hours. The bard cannot target himself with this ability. If the target has the rage class feature,
it can instead immediately rage and stay in this rage without consuming rounds of rage per day as
long as the bard continues performing. This mind-affecting effect requires audible components. This
performance replaces suggestion.

## Song of the Fallen (Sp) {#song-of-the-fallen}

At 10th level, a savage skald can duplicate the effect of a
_[horn of Valhalla](ref/magic-wondrous/horn-of-valhalla)_. This effect requires 10 continuous rounds
of performance and summons barbarians as a silver horn at 10th level, as a brass horn at 13th level,
as a bronze horn at 16th level, and as an iron horn at 19th level. The warriors remain only as long
as the bard continues his performance. This ability requires audible components. This performance
replaces jack of all trades.

## Berserkergang (Ex) {#berserkergang}

At 12th level, a savage skald can inspire a rapturous battle trance that suppresses pain, stunning,
and fear effects for one creature, plus one additional creature per three levels after 12th.
Affected creatures also gain DR 5/— (DR 10/— against nonlethal damage); this benefit stacks with the
[damage reduction](ref/rule/damage-reduction) class ability of barbarians. This mind-affecting
ability requires audible components. This performance replaces soothing performance.

## Battle Song (Su) {#battle-song}

At 18th level, a savage skald can affect all allies within 30 feet when using performance to incite
rage. This performance replaces mass suggestion.
