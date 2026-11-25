+++
id = "ref/arc-oracle/purifier"
kind = "archetype"
title = "Purifier"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Purifier"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "purifier", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-race-guide"
page = "86"

[fields]
kind = "archetype"
features = [
  { anchor = "recommended-mysteries" },
  { anchor = "diminished-spellcasting" },
  { anchor = "revelations" },
  { anchor = "see-sin", level = 3 },
  { anchor = "celestial-armor", level = 7 },
  { anchor = "sin-eater", level = 11 },
  { anchor = "sacred-scourge", level = 5 },
  { anchor = "holy-terror", level = 9 },
  { anchor = "celestial-master", level = 13 },
]
trades = [
  { replaces = "Revelations from her mystery gained at 3rd, 7th, and 11th levels", feature = "revelation", levels = [3, 7, 11], by = ["revelations"] },
]
+++

The purifier seeks out signs of possession or mind control that manifest from unwilling (and often
unwitting) servants for fiendish corruptors and their mortal minions. A purifier seeks liberation of
mind, body, and spirit from the bondage of sin and the taint of the unholy. A purifier gains the
following class features.

## Recommended Mysteries {#recommended-mysteries}

ancestor, battle, heavens, lore.

## Bonus Spells {#bonus-spells}

_veil of heaven_ (2nd), _confess_ (_Advanced Player's Guide_ 212; 4th), _cast out_ (_Advanced
Player's Guide_ 210; 6th), _denounce_ (_Advanced Player's Guide_ 215; 8th), _dispel evil_ (10th),
_banishment_ (12th), _holy word_ (14th), _mind blank_ (16th), _freedom_ (18th).

## Diminished Spellcasting {#diminished-spellcasting}

A purifier can use one fewer spell per day of each level and does not automatically learn cure or
inflict spells. Her number of oracle spells known is unchanged.

## Revelations {#revelations}

A purifier must take the following revelations at the listed levels.

## See Sin (Sp) {#see-sin}

At 3rd level, a purifier gains a bonus equal to 1/2 her oracle level on Sense Motive checks to sense
enchantments, which she can make as a full-round action. She also gains a bonus equal to 1/2 her
oracle level on Spellcraft checks to identify enchantment school spells and spells with the curse or
emotion descriptor (see page 251 of _Ultimate Magic_ for spells in the _Pathfinder RPG Core
Rulebook_ and _Advanced Player's Guide_ that have the curse or emotion descriptor).

## Celestial Armor (Su) {#celestial-armor}

At 7th level, a purifier's armor takes on a golden or silvery sheen and becomes light as a feather.
Her armor weighs half as much as long as she wears it, and she also gains armor training as a
[fighter](ref/class/fighter) 4 levels lower than her oracle level. At 11th level, a purifier gains
[heavy armor proficiency](ref/feat/armor-proficiency-heavy).

## Sin Eater (Su) {#sin-eater}

At 11th level, a purifier can consume a curse, enchantment, or emotion effect by touch as a
full-round action. She can do this a number of times per day equal to her Charisma modifier, and
must make a Charisma check with a bonus equal to her oracle level against a DC of 11 + the caster
level of the effect (or the Hit Dice of the creator for a supernatural effect). If the check
succeeds, the effect is negated; however, the purifier is [sickened](ref/misc/sickened) for 1d4
rounds.

If the target is possessed (such as by a _[magic jar](ref/spell/magic-jar)_ effect or a
[ghost's](ref/template/ghost) malevolence ability), the possessor is forced out on a successful
check. Whether the check succeeds or fails, the possessor is sickened for 2d4 rounds.

## Sacred Scourge (Su) {#sacred-scourge}

At 5th level, a purifier may channel holy power to harm evil outsiders as a cleric of her level
using the [Alignment Channel](ref/feat/alignment-channel) feat. She may use this ability a number of
times per day equal to 1 + her Charisma modifier.

## Holy Terror (Su) {#holy-terror}

At 9th level, a purifier may use her sacred scourge to panic evil outsiders as if using the
[Turn Undead](ref/feat/turn-undead) feat against undead.

## Celestial Master (Su) {#celestial-master}

At 13th level, a purifier may use her sacred scourge to compel good outsiders to serve her, as if
using the [Command Undead](ref/feat/command-undead) feat against undead.
