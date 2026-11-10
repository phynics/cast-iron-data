+++
id = "ref/arc-summoner/blood-summoner"
kind = "archetype"
title = "Blood Summoner"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Blood%20Summoner"
source_ids = ["champions-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_summoner", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "champions-of-corruption"
page = "24"

[fields]
kind = "archetype"
replaces = ["Shield ally", "Transposition", "Greater shield ally", "Merge forms"]
replaces_features = ["shield-ally", "transposition", "greater-shield-ally", "merge-forms"]
+++

A blood summoner conjures an eidolon born from violence and blood. These cruel spellcasters are
common among the god-callers of now-shattered Sarkoris, where the influence of the Worldwound has
warped them into beings of chilling malevolence.

**Gained class skills:** heal

**Blood Offering (Su)**

**Gained:** At 4th Level

**Replaces:** Shield ally

**Special:** This blood can be extracted from a willing or helpless creature as a **full-round
action** that deals 1 point of [Constitution damage](ref/rule/ability-damage-drain). The bonuses
last for 10 minutes. The offering cannot be made to the same fiend twice in the same day.

**Standard:** The blood summoner can sacrifice a flask of blood, extracted up to 1 day ago from a
living creature or a corpse that's been dead no longer than 1 minute, to aid and appease an evil
outsider within 30 feet. The offering grants the outsider a +2 enhancement bonus to the ability
score of the blood summoner's choice and grants the blood summoner a +4 circumstance bonus on
Diplomacy checks and Charisma checks to bargain with it.

**Blood Travel (Su)**

**Ability:** A blood summoner can use his _maker's call_ ability to allow his eidolon to travel
through the blood of other creatures instead of bringing it to his side. The eidolon can either
emerge from the blood of a living creature within range that has fewer than its maximum hit points
remaining, or burst from the corpse of a Small or larger creature within range that has been dead
for no longer than 1 minute. If the eidolon emerges from an injured creature, that creature takes
4d6 points of damage, which is halved if the creature succeeds at a Fortitude save (DC = 10 + 1/2
the blood summoner's level + his Charisma modifier). The eidolon appears in its choice of the
nearest unoccupied square to the creature or corpse it emerged from, and is
[staggered](ref/misc/staggered) for 1 round.

**Gained:** At 8th Level

**Replaces:** Transposition

**Fiendish Calling (Su)**

**At 10th Level:** The blood summoner's _[summon monster](ref/spell/summon-monster)_ ability can
additionally be used as [lesser planar binding](ref/spell/planar-binding-lesser) as a **standard
action**, but only to call evil outsiders.

**At 13th Level:** He can instead use it as [planar binding](ref/spell/planar-binding).

**At 16th Level:** He can instead use it as
[greater planar binding](ref/spell/planar-binding-greater).

**Replaces:** Greater shield ally

**Blood Possession (Su)**

**Fullround:** A blood summoner's eidolon can enter and control the body of any corporeal creature
that has blood. This ability functions as [marionette possession](ref/spell/marionette-possession),
except that the eidolon's body also enters the target and the target can be unwilling. A successful
Will save (DC = 10 + 1/2 the blood summoner's level + his Charisma modifier) negates this effect.
The eidolon can end this possession at any time as a **standard action**.

**Gained:** At 16th Level

**Replaces:** Merge forms

**Special:** If the host body is slain while the eidolon is possessing it, the eidolon is
immediately ejected, takes 4d6 points of damage, and is [stunned](ref/misc/stunned) for 1 round.

**Usage:** 1 time/day + 1 per 2 summoner levels beyond 16th
