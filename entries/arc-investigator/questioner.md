+++
id = "ref/arc-investigator/questioner"
kind = "archetype"
title = "Questioner"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Questioner"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "questioner", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiration-for-subterfuge", level = 1 },
  { anchor = "spells", level = 1 },
  { anchor = "know-it-all", level = 2 },
  { anchor = "restricted-talents", level = 3 },
]
trades = [
  { replaces = "Alchemy", feature = "alchemy", by = ["spells"] },
  { replaces = "Poison lore", feature = "poison-lore", by = ["know-it-all"] },
  { alters = "Inspiration", feature = "inspiration", by = ["inspiration-for-subterfuge"] },
  { alters = "Investigator talents", feature = "investigator-talent", by = ["restricted-talents"] },
]
+++

Dabblers in arcane magic and masters of stealth and guile, questioners are investigators who often
find themselves mucking about in cases for less-than-savory clientele or that require an extra bit
of subtlety. Although questioners are found in nearly every major city in the Inner Sea region,
Ustalav has the highest concentration; many belong to the famed Sleepless Detectives, while others
have trained to evade the notice of that acclaimed agency.

## Inspiration for Subterfuge (Ex) {#inspiration-for-subterfuge}

A questioner can use inspiration on any Knowledge, Linguistics, or Stealth checks he attempts
without expending a use of inspiration, provided he's trained in that skill.

This ability alters inspiration.

## Spells {#spells}

A questioner casts arcane spells drawn from the [bard](ref/class/bard) spell list. He can cast any
spell he knows without preparing it ahead of time. To learn or cast a spell, a questioner must have
an Intelligence score equal to at least 10 + the spell's level. The saving throw DC against a
questioner's spell is equal to 10 + the spell's level + the questioner's Intelligence modifier.

Like other spellcasters, a questioner can cast only a certain number of spells of each spell level
per day. He knows the same number of spells and receives the same number of spell slots per day as a
bard of his investigator level, including for cantrips. In addition, he receives
[bonus spells per day](ref/rule/determine-bonuses) if he has a high Intelligence score.

At 5th level and every 3 investigator levels thereafter, a questioner can learn a new spell in place
of one he already knows, using the same rules as a bard. In effect, the questioner loses the old
spell in exchange for the new one. The new spell's level must be the same as that of the spell being
exchanged, and it must be at least 1 level lower than the highest-level spell the questioner can
cast.

A questioner need not prepare his spells in advance. He can cast any bard spell he knows at any
time, assuming he has not yet used up his allotment of spells per day for the spell's level.

This ability replaces alchemy.

## Know-It-All (Ex) {#know-it-all}

At 2nd level, a questioner receives a +1 bonus on skill checks for all Knowledge skills in which he
is trained. This bonus increases by 1 at 5th level and every 3 investigator levels thereafter, to a
maximum of +6 at 17th level. If he has the [perceptive tracking](ref/invtalent/perceptive-tracking)
investigator talent, he also adds this bonus on Perception checks to find and follow tracks. At 5th
level, the questioner gains the [eidetic recollection](ref/invtalent/eidetic-recollection)
investigator talent as a bonus talent, ignoring its prerequisites.

This ability replaces poison lore.

## Restricted Talents {#restricted-talents}

A questioner selects investigator talents as normal, except he cannot select the
[alchemist discovery](ref/invtalent/alchemist-discovery) investigator talent.

This ability alters investigator talents.

## Investigator Talents {#investigator-talents}

The following investigator talents complement the questioner archetype particularly well:
[expanded inspiration](ref/invtalent/expanded-inspiration),
[inspirational expertise](ref/invtalent/inspirational-expertise), perceptive tracking,
[rogue talent](ref/invtalent/rogue-talent), and
[underworld inspiration](ref/invtalent/underworld-inspiration).
