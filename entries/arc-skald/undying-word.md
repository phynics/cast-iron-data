+++
id = "ref/arc-skald/undying-word"
kind = "archetype"
title = "Undying Word"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Undying%20Word"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undying_word", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "5"

[fields]
kind = "archetype"
replaces = ["Scribe scroll", "lore master", "Inspired rage", "Song of strength", "Dirge of doom", "Spell kenning"]
replaces_features = ["scribe-scroll", "lore-master", "inspired-rage", "song-of-strength", "dirge-of-doom", "spell-kenning"]
+++

Some who have survived the Mana Wastes cannot accept defeat, and those who have learned to speak the
undying word can lend others the strength to endure.

**Bonus Feat**

**Ability:** An undying word gains a bonus feat in addition to those gained from normal advancement.
He must meet the prerequisites for the feat, and it must include Endurance as a prerequisite or be
selected from the following list: [Endurance](ref/feat/endurance),
[Great Fortitude](ref/feat/great-fortitude), or
[Improved Great Fortitude](ref/feat/improved-great-fortitude).

**Gained:** At 1st Level

**Repeat:** He gains another bonus feat, following the restrictions above., 7, 6

**Replaces:** Scribe scroll, lore master

**Undying Song (Su)**

**Info:** An undying word gains the following _raging songs,_ granting his allies the ability to
withstand punishment.

**Inspire Resilience (Su)**

**Ability:** The undying word can grant his companions supernatural endurance. This functions as
_inspired rage,_ but it grants neither a bonus to his allies' Strength nor a -1 penalty to their AC.

**Gained:** At 1st Level

**Replaces:** Inspired rage

**Song of Defiance (Su)**

**Ability:** By expending 1 round of _raging song,_ the undying word grants all allies within 60
feet the effects of [endure elements](ref/spell/endure-elements) for the next hour. The undying word
must continue to perform for the remainder of the hour; otherwise its effects end, but only 1 round
of _raging song_ is expended for that hour.

**Flavor:** An undying word can shield his allies against the environment.

**Gained:** At 6th Level

**Replaces:** Song of strength

**Dirge of Determination (Su)**

**Flavor:** An undying word can urge his allies within 30 feet to overcome hardships.

**Gained:** At 10th Level

**Passive:** Affected allies treat [ability damage, ability drain](ref/rule/ability-damage-drain),
and penalties to ability scores as though each were 2 lower.

**Replaces:** Dirge of doom

**Special:** The undying word can never reduce a penalty below 0 or increase an ability score beyond
its original value in this manner.

At 15th level: This reduction 4.

At 20th level: This reduction 6.

**Endurance Power (Su)**

**Ability:** An undying word learns an additional rage power that affects him and any allies under
the influence of his _inspire resilience._ This rage power must be selected from the following list:
[clear mind](ref/ragepower/clear-mind), [energy absorption](ref/ragepower/energy-absorption),
[energy resistance](ref/ragepower/energy-resistance), [flesh wound](ref/ragepower/flesh-wound),
[greater energy resistance](ref/ragepower/greater-energy-resistance),
[greater guarded life](ref/ragepower/greater-guarded-life),
[guarded life](ref/ragepower/guarded-life),
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[internal fortitude](ref/ragepower/internal-fortitude), or
[superstition](ref/ragepower/superstition). This otherwise functions as the skald's _rage powers_
ability.

**Gained:** At 5th Level

**Repeat:** He learns another rage power, following the restrictions above., 11, 6

**Replaces:** Spell kenning
