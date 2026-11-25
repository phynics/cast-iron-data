+++
id = "ref/arc-vigilante/zealot"
kind = "archetype"
title = "Zealot"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Zealot"
source_ids = ["ultimate-intrigue", "inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "zealot", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "62"
[[sources]]
publication = "inner-sea-intrigue"
page = "33"

[fields]
kind = "archetype"
features = [
  { anchor = "spellcasting" },
  { anchor = "chaotic-evil-good-and-lawful-spells" },
  { anchor = "aura" },
  { anchor = "inquisition", level = 1 },
  { anchor = "zealot-talents" },
]
trades = [
  { replaces = "4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents", feature = "vigilante-talent", levels = [4, 8, 10, 14, 16], by = ["spellcasting"] },
  { replaces = "Vigilante specialization", feature = "vigilante-specialization", by = ["inquisition"] },
  { alters = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "Vigilante talents", feature = "vigilante-talent", by = ["zealot-talents"] },
]
+++

Dedicated to a single deity, the zealot hunts the enemies of his faith in secret, often because his
religion is outlawed or persecuted in the region.

## Class Skills {#class-skills}

A zealot adds Knowledge (religion) and Spellcraft to his list of class skills, instead of Disable
Device, Knowledge (engineering), Perform, and Sleight of Hand.

This alters the vigilante's class skills.

## Skill Ranks per Level {#skill-ranks-per-level}

A zealot gains a number of skill ranks equal to 4 + his Intelligence modifier at each level, instead
of 6 + his Intelligence modifier skill ranks.

This alter's the vigilante's skill ranks per level.

## Weapon Proficiencies {#weapon-proficiencies}

A zealot is also proficient in his deity's favored weapon, even if it is an exotic weapon, and if
the deity's favored weapon is unarmed strike, he gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat.

This alters the vigilante's weapon proficiencies.

## Spellcasting {#spellcasting}

A zealot casts divine spells and orisons as an [inquisitor](ref/class/inquisitor) and uses the
inquisitor's spell list.

This replaces the 4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents.

## Chaotic, Evil, Good, and Lawful Spells {#chaotic-evil-good-and-lawful-spells}

Zealots can't cast spells of an alignment opposed to his vigilante identity's alignment or that of
his deity. Spells associated with particular alignments are indicated by the chaotic, evil, good,
and lawful descriptors in their spell descriptions.

## Alignment {#alignment}

A zealot's alignment must be within one step of his deity's, along either the law/chaos axis or the
good/evil axis, but only when in his vigilante identity. If his social identity's alignment isn't
within one step of his deity's, he can't cast spells in his social identity.

## Aura (Ex) {#aura}

A zealot of a chaotic, evil, good, or lawful deity has a particularly powerful aura corresponding to
the deity's alignment (see _[detect evil](ref/spell/detect-evil)_ spell for details), but only when
in his vigilante identity.

## Inquisition (Ex) {#inquisition}

A zealot picks a deity and picks a single [inquisition](ref/ability/inquisitions) tied to that
deity. He uses his vigilante level as his inquisitor level to determine level dependent inquisition
abilities.

This ability replaces vigilante specialization.

## Zealot Talents {#zealot-talents}

A zealot can select from any of the following vigilante talents, in addition to general vigilante
talents.

This alters vigilante talents.

### Channel Energy (Su) {#channel-energy}

A zealot who takes this talent can [channel energy](ref/ability/channel-energy) with an effective
cleric level equal to his vigilante level - 4 (minimum 1) while in his vigilante identity. If good
in his vigilante identity (or if he worships a good deity), the vigilante channels positive energy
and can choose to deal damage to undead creatures or to heal living creatures. If evil in his
vigilante identity (or if he worships an evil deity), the vigilante channels negative energy and can
choose to deal damage to living creatures or to heal undead creatures. If the vigilante is neutral
in his vigilante identity and worships a neutral deity, the vigilante must choose whether he
channels positive or negative energy. Once this choice is made, it can't be reversed.

### Discern Lies (Sp) {#discern-lies}

The zealot can use _[discern lies](ref/spell/discern-lies)_ as a
[spell-like ability](ref/umr/spell-like-abilities) for a number of rounds per day equal to his
vigilante level. The rounds need not be consecutive. Activating this ability is an immediate action.
A zealot must be 6th level before taking this talent.

### Empower Symbol (Su) {#empower-symbol}

As a standard action, the zealot can empower his holy symbol. If the zealot is of good alignment
while in his vigilante identity (or worships a good deity), this works as if the holy symbol was the
center of a _[consecrate](ref/spell/consecrate)_ effect. If the zealot is of evil alignment in his
vigilante identity (or worships an evil deity), this works as if the holy symbol was the center of a
_[desecrate](ref/spell/desecrate)_ effect. If the zealot is neutral in his vigilante identity and
worships a neutral deity, he can choose whether this ability acts as per _consecrate_ or
_desecrate_, but once the choice is made, it cannot be changed. At 10th level, the zealot treats his
holy symbol as a permanent fixture for the purpose of determining the consecration or desecration
effects. A zealot must be at least 6th level to select this talent.

### Stalwart (Ex) {#stalwart}

A zealot with this talent can use mental and physical resilience to avoid certain attacks. If he
succeeds at a Fortitude or Will saving throw against an attack that has a reduced effect on a
successful save, he avoids the effect entirely. A [helpless](ref/misc/helpless) zealot doesn't gain
the benefit of this ability. A zealot must be 12th level before selecting this talent.

### Stern Gaze (Ex) {#stern-gaze}

A zealot with this talent is skilled at sensing deception and intimidating his foes. The zealot
gains a morale bonus on all Intimidate and Sense Motive checks equal to half his vigilante level
(minimum +1).

### Zealot Smite (Su) {#zealot-smite}

Once per day, a zealot with this talent can use this power to smite a foe. Zealots that are good in
their vigilante identity (or worship a good deity) can smite evil creatures, those that are evil in
their vigilante identity (or worship an evil deity) can smite good creatures, those that are chaotic
in their vigilante identity (or worship a chaotic deity) can smite lawful creatures, and those that
are lawful in their vigilante identity (or worship a lawful deity) can smite chaotic creatures. A
zealot that is neutral when in his vigilante identity and that worships a neutral deity can pick to
smite any one of the four alignments; other zealots must select from the alignments available based
on their own alignment or their deity's. Once that choice is made, it can't be changed.

As a swift action, the zealot chooses one target within sight to smite. If this target is of the
proper alignment, the zealot adds his Charisma bonus on his attack rolls (to a maximum of half his
vigilante level) and his vigilante level on all damage rolls against the target of his smite. If the
target of smite is an outsider with an alignment subtype of the zealot's smite, a similarly aligned
dragon, or an undead creature (if the zealot's smite is against evil creatures), a good-aligned
cleric or paladin (if the zealot's smite is against good creatures), a chaotic aberration (if the
zealot's smite is against chaotic creatures), or a lawful-aligned cleric or paladin (if the zealot's
smite is against lawful creatures), the bonus to damage on the first successful attack increases to
2 points of damage per vigilante level. Regardless of the target, the zealot's smite attacks bypass
the creature's DR as if it were a weapon with a +5 enhancement bonus.

At 5th level, and every 3 vigilante levels thereafter, a zealot can smite one additional time per
day, to a maximum of seven times per day at 20th level.

### Harsh Judgment (Su) (Inner Sea Intrigue page 33) {#harsh-judgment}

A vigilante with this talent can pronounce _judgment_ upon his foes as per the
[inquisitor](ref/class/inquisitor) class feature (see page 38 of the _Pathfinder RPG Advanced
Player's Guide_). He can choose from among the following inquisitor judgments: _destruction,
piercing, purity,_ and _smiting._ For the purpose of determining the bonuses provided by this
ability, the vigilante's level stacks with levels in any other classes that grant _judgment_ or
_harsh judgment._ The vigilante can use this ability once per day plus an additional time per day at
4th level and every 3 levels thereafter (up to a maximum of seven times per day at 19th level). Only
a vigilante with the zealot archetype can select this talent.
