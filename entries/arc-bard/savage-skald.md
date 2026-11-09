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
replaces = ["Fascinate", "Suggestion", "Jack of all trades", "Soothing performance", "Mass suggestion"]
+++

Far from civilization, furious tribes have their own war-singers, work-chanters, and lore-keepers,
savaging enemies with song and sword alike.

**Bardic Performance**

**Info:** A savage skald gains the following types of bardic performance.

**Inspiring Blow (Su)**

**Flavor:** A savage skald roars his war-cries with each telling blow.

**Immediate:** When he confirms a critical hit, he can start this performance (ending any other
performances). He gains [temporary hit points](ref/rule/temporary-hit-points) equal to his Charisma
modifier (if positive), and all allies within 30 feet gain a +1 morale bonus on their next attack
roll prior to the start of his next turn. These temporary hit points remain until the bard ends his
performance.

**Replaces:** Fascinate

**Incite Rage (Su)**

**Ability:** A savage skald can induce a furious rage in one creature within 30 feet. This effect
functions as a [rage](ref/spell/rage) spell that lasts as long as the target can hear the bard's
performance; however, unwilling creatures can be affected if they fail a Will save (DC 10 +
[half](ref/misc/fractions-and-rounding) the bard's level + the bard's Cha modifier). Success renders
the target immune to this power for 24 hours. The bard cannot target himself with this ability.

**Gained:** At 6th Level

**Replaces:** Suggestion

**Special:** If the target has the rage class feature, it can instead immediately rage and stay in
this rage without consuming rounds of rage per day as long as the bard continues performing. This
mind-affecting effect requires audible components.

**Song of the Fallen (Sp)**

**At 10th Level:** A savage skald can duplicate the effect of a
[horn of Valhalla](ref/magic-wondrous/horn-of-valhalla). This effect requires 10 continuous rounds
of performance. This summons barbarians as a silver horn.

**At 13th Level:** This summons barbarians as a brass horn.

**At 16th Level:** This now summons as a bronze horn.

**At 19th Level:** This now summons as an iron horn.

**Replaces:** Jack of all trades

**Special:** The warriors remain only as long as the bard continues his performance. This ability
requires audible components.

**Berserkergang (Ex)**

**At 12th Level:** A savage skald can inspire a rapturous battle trance that suppresses pain,
stunning, and fear effects for one creature.

**At 15th Level:** This affects two creatures at once.

**At 18th Level:** This now affects three creatures at once.

**Replaces:** Soothing performance

**Special:** Affected creatures also gain DR 5/- (DR 10/- against nonlethal damage); this benefit
stacks with the [damage reduction](ref/rule/damage-reduction) class ability of barbarians. This
mind-affecting ability requires audible components.

**Battle Song (Su)**

**At 18th Level:** A savage skald can affect all allies within 30 feet when using performance to
_incite rage._

**Replaces:** Mass suggestion
