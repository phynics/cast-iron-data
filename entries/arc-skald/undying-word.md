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
features = [
  { anchor = "bonus-feat", level = 1 },
  { anchor = "inspire-resilience", level = 1 },
  { anchor = "song-of-defiance", level = 6 },
  { anchor = "dirge-of-determination", level = 10 },
  { anchor = "endurance-power", level = 5 },
]
trades = [
  { replaces = "Scribe scroll", feature = "scribe-scroll", by = ["bonus-feat"] },
  { replaces = "lore master", feature = "lore-master", by = ["bonus-feat"] },
  { replaces = "Inspired rage", feature = "inspired-rage", by = ["inspire-resilience"] },
  { replaces = "Song of strength", feature = "song-of-strength", by = ["song-of-defiance"] },
  { replaces = "Dirge of doom", feature = "dirge-of-doom", by = ["dirge-of-determination"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["endurance-power"] },
]
+++

Some who have survived the Mana Wastes cannot accept defeat, and those who have learned to speak the
undying word can lend others the strength to endure.

## Bonus Feat {#bonus-feat}

At 1st level and every 6 skald levels thereafter, an undying word gains a bonus feat in addition to
those gained from normal advancement. He must meet the prerequisites for the feat, and it must
include [Endurance](ref/feat/endurance) as a prerequisite or be selected from the following list:
Endurance, [Great Fortitude](ref/feat/great-fortitude), or
[Improved Great Fortitude](ref/feat/improved-great-fortitude).

This replaces scribe scroll and lore master.

## Undying Song (Su) {#undying-song}

An undying word gains the following raging songs, granting his allies the ability to withstand
punishment.

## Inspire Resilience (Su) {#inspire-resilience}

At 1st level, the undying word can grant his companions supernatural endurance. This functions as
inspired rage, but it grants neither a bonus to his allies' Strength nor a -1 penalty to their AC.

This raging song replaces inspired rage.

## Song of Defiance (Su) {#song-of-defiance}

At 6th level, an undying word can shield his allies against the environment. By expending 1 round of
raging song, the undying word grants all allies within 60 feet the effects of
_[endure elements](ref/spell/endure-elements)_ for the next hour. The undying word must continue to
perform for the remainder of the hour; otherwise its effects end, but only 1 round of raging song is
expended for that hour.

This raging song replaces song of strength.

## Dirge of Determination (Su) {#dirge-of-determination}

At 10th level, an undying word can urge his allies within 30 feet to overcome hardships. Affected
allies treat [ability damage, ability drain](ref/rule/ability-damage-drain), and penalties to
ability scores as though each were 2 lower. This reduction increases to 4 at 15th level, and to 6 at
20th level. The undying word can never reduce a penalty below 0 or increase an ability score beyond
its original value in this manner.

This raging song replaces dirge of doom.

## Endurance Power (Su) {#endurance-power}

At 5th level and every 6 skald levels thereafter, an undying word learns an additional rage power
that affects him and any allies under the influence of his inspire resilience. This rage power must
be selected from the following list: [clear mind](ref/ragepower/clear-mind),
[energy absorption](ref/ragepower/energy-absorption),
[energy resistance](ref/ragepower/energy-resistance), [flesh wound](ref/ragepower/flesh-wound),
[greater energy resistance](ref/ragepower/greater-energy-resistance),
[greater guarded life](ref/ragepower/greater-guarded-life),
[guarded life](ref/ragepower/guarded-life),
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[internal fortitude](ref/ragepower/internal-fortitude), or
[superstition](ref/ragepower/superstition). This otherwise functions as the skald's rage powers
ability.

This replaces spell kenning.
