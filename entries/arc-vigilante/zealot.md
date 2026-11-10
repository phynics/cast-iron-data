+++
id = "ref/arc-vigilante/zealot"
kind = "archetype"
title = "Zealot"
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
replaces = ["4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents", "Vigilante specialization"]
alters = ["Weapon proficiencies", "Vigilante talents"]
+++

Dedicated to a single deity, the zealot hunts the enemies of his faith in secret, often because his
religion is outlawed or persecuted in the region.

**Gained class skills:** kr, spc

**Lost class skills:** dd, ke, perf, soh

**Skill Ranks per Level**

**Info:** A zealot gains a number of skill ranks equal to 4 + his Intelligence modifier at each
level, instead of 6 + his Intelligence modifier skill ranks.

**Weapon Proficiencies**

**Ability:** A zealot is also proficient in his deity's favored weapon, even if it is an exotic
weapon, and if the deity's favored weapon is unarmed strike, he gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat.

**Alters:** Weapon proficiencies

**Spellcasting**

**Ability:** A zealot casts divine spells and orisons as an [inquisitor](ref/class/inquisitor) and
uses the inquisitor's spell list.

**Replaces:** 4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents

**Chaotic, Evil, Good, and Lawful Spells**

**Info:** Zealots can't cast spells of an alignment opposed to his vigilante identity's alignment or
that of his deity. Spells associated with particular alignments are indicated by the chaotic, evil,
good, and lawful descriptors in their spell descriptions.

**Alignment**

**Info:** A zealot's alignment must be within one step of his deity's, along either the law/chaos
axis or the good/evil axis, but only when in his vigilante identity. If his social identity's
alignment isn't within one step of his deity's, he can't cast spells in his social identity.

**Aura (Ex)**

**Info:** A zealot of a chaotic, evil, good, or lawful deity has a particularly powerful aura
corresponding to the deity's alignment (see [detect evil](ref/spell/detect-evil) spell for details),
but only when in his vigilante identity.

**Inquisition (Ex)**

**Choice:** A zealot picks a deity and picks a single [inquisition](ref/ability/inquisitions) tied
to that deity.

**Replaces:** Vigilante specialization

**Special:** He uses his vigilante level as his inquisitor level to determine level dependent
inquisition abilities.

**Zealot Talents**

**Alters:** Vigilante talents

**Info:** A zealot can select from any of the following vigilante talents, in addition to general
vigilante talents.

**Channel Energy (Su)**

**Ability:** A zealot who takes this talent can [channel energy](ref/ability/channel-energy) with an
effective cleric level equal to his vigilante level - 4 (minimum 1) while in his vigilante identity.
If good in his vigilante identity (or if he worships a good deity), the vigilante channels positive
energy and can choose to deal damage to undead creatures or to heal living creatures. If evil in his
vigilante identity (or if he worships an evil deity), the vigilante channels negative energy and can
choose to deal damage to living creatures or to heal undead creatures. If the vigilante is neutral
in his vigilante identity and worships a neutral deity, the vigilante must choose whether he
channels positive or negative energy. Once this choice is made, it can't be reversed.

**Discern Lies (Sp)**

**Immediate:** The zealot can use [discern lies](ref/spell/discern-lies) as a
[spell-like ability](ref/umr/spell-like-abilities) for a number of rounds per day equal to his
vigilante level. The rounds need not be consecutive.

**Prereq:** 6th-level vigilante

**Empower Symbol (Su)**

**At 10th Level:** The zealot treats his holy symbol as a permanent fixture for the purpose of
determining the consecration or desecration effects.

**Prereq:** 6th-level vigilante

**Standard:** The zealot can empower his holy symbol. If the zealot is of good alignment while in
his vigilante identity (or worships a good deity), this works as if the holy symbol was the center
of a [consecrate](ref/spell/consecrate) effect. If the zealot is of evil alignment in his vigilante
identity (or worships an evil deity), this works as if the holy symbol was the center of a
[desecrate](ref/spell/desecrate) effect. If the zealot is neutral in his vigilante identity and
worships a neutral deity, he can choose whether this ability acts as per consecrate or desecrate,
but once the choice is made, it cannot be changed.

**Harsh Judgment (Su)**

**Ability:** A vigilante with this talent can pronounce _judgment_ upon his foes as per the
[inquisitor](ref/class/inquisitor) class feature. He can choose from among the following inquisitor
judgments: _destruction, piercing, purity,_ and _smiting._ For the purpose of determining the
bonuses provided by this ability, the vigilante's level stacks with levels in any other classes that
grant _judgment_ or _harsh judgment._

**Usage:** 1 time/day + 1 per 3 vigilante levels beyond 1st

**Stalwart (Ex)**

**Ability:** If he succeeds at a Fortitude or Will saving throw against an attack that has a reduced
effect on a successful save, he avoids the effect entirely. A [helpless](ref/misc/helpless) zealot
doesn't gain the benefit of this ability.

**Flavor:** A zealot with this talent can use mental and physical resilience to avoid certain
attacks.

**Prereq:** 12th-level vigilante

**Stern Gaze (Ex)**

**Flavor:** A zealot with this talent is skilled at sensing deception and intimidating his foes.

**Passive:** The zealot gains a morale bonus on all Intimidate and Sense Motive checks equal to half
his vigilante level (minimum +1).

**Zealot Smite (Su)**

**Flavor:** A zealot with this talent can use this power to smite a foe.

**Info:** Zealots that are good in their vigilante identity (or worship a good deity) can _smite_
evil creatures, those that are evil in their vigilante identity (or worship an evil deity) can
_smite_ good creatures, those that are chaotic in their vigilante identity (or worship a chaotic
deity) can _smite_ lawful creatures, and those that are lawful in their vigilante identity (or
worship a lawful deity) can _smite_ chaotic creatures. A zealot that is neutral when in his
vigilante identity and that worships a neutral deity can pick to _smite_ any one of the four
alignments; other zealots must select from the alignments available based on their own alignment or
their deity's. Once that choice is made, it can't be changed.

**Swift:** The zealot chooses one target within sight to _smite._ If this target is of the proper
alignment, the zealot adds his Charisma bonus on his attack rolls (to a maximum of half his
vigilante level) and his vigilante level on all damage rolls against the target of his _smite._ If
the target of _smite_ is an outsider with an alignment subtype of the _zealot's smite,_ a similarly
aligned dragon, or an undead creature (if the _zealot's smite_ is against evil creatures), a
good-aligned cleric or paladin (if the _zealot's smite_ is against good creatures), a chaotic
aberration (if the _zealot's smite_ is against chaotic creatures), or a lawful-aligned cleric or
paladin (if the _zealot's smite_ is against lawful creatures), the bonus to damage on the first
successful attack increases to 2 points of damage per vigilante level. Regardless of the target, the
_zealot's smite_ attacks bypass the creature's DR as if it were a weapon with a +5 enhancement
bonus.

**Usage:** 1 time/day + 1 per 3 vigilante levels beyond 2nd
