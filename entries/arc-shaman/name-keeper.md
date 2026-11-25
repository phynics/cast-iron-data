+++
id = "ref/arc-shaman/name-keeper"
kind = "archetype"
title = "Name-Keeper"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Name-Keeper"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "name_keeper", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "adventurers-guide"
page = "145"

[fields]
kind = "archetype"
features = [
  { anchor = "inherited-wayfinder", level = 1 },
  { anchor = "keeper-spirit-magic" },
  { anchor = "pathfinders-past", level = 4 },
  { anchor = "versatile-hex", level = 6 },
]
trades = [
  { replaces = "Spirit animal", feature = "spirit-animal", by = ["inherited-wayfinder"] },
  { replaces = "Spirit magic spells gained from the shaman's spirit", feature = "spirit-magic", by = ["keeper-spirit-magic"] },
  { replaces = "Wandering spirit", feature = "wandering-spirit", by = ["pathfinders-past"] },
  { replaces = "Wandering hex", feature = "wandering-hex", by = ["versatile-hex"] },
  { alters = "Class skills" },
]
+++

Pathfinders who perish in the pursuit of greater knowledge are commemorated on the Wall of Names, a
curving monument of black glass at the Grand Lodge. Originally started as a humble memorial, the
Wall of Names is now a moving testament to all those who have given their lives to further the cause
of the [Pathfinder Society](ref/rule/aff-scholars), and for many agents, an expedition to Absalom is
as much a chance to visit the Wall of Names and seek out a vanished loved one, relation, or departed
friend as it is an opportunity to visit the place where it all began.

A decade ago, a small cadre of agents began studying the fallen names, correlating these adventurers
with the quests they were on when they perished or went missing, and then took it upon themselves to
finish these incomplete missions —but in so doing these agents made an unexpected discovery. In
delving into the storied histories etched into the Wall of Names, these agents have discovered how
to commune with the departed spirits of those whose names are memorialized on the monument. These
mystical agents soon became known as name-keepers, and they pride themselves on helping their
predecessors find peace while preventing other Pathfinders' names from being added to the wall.

## Class Skills {#class-skills}

A name-keeper gains Knowledge (engineering), Knowledge (history), and Linguistics as class skills,
instead of Knowledge (nature), Knowledge (planes), and Survival.

This alters the shaman's class skills.

## Inherited Wayfinder (Su) {#inherited-wayfinder}

A name-keeper forms a powerful bond with a damaged _[wayfinder](ref/magic-wondrous/wayfinder)_ (see
pages 148–149) inherited from another Pathfinder. It functions for her alone. This functions as a
[wizard's](ref/class/wizard) bonded object except it can be used to cast shaman spells (instead of
wizard spells).

This ability replaces spirit animal.

## Keeper Spirit Magic {#keeper-spirit-magic}

The name-keeper adds the following spells to the list of spells she can cast using spirit magic:
_stone shield_ (1st), _object reading_ (2nd), _speak with dead_ (3rd), _wall of stone_ (4th),
_breath of life_ (5th), _stone tell_ (6th), _vision_ (7th), _word of recall_ (8th), and _true
resurrection_ (9th).

This ability replaces the spirit magic spells gained from the shaman's spirit.

## Pathfinders Past (Su) {#pathfinders-past}

At 4th level, a name-keeper can form a temporary bond with a deceased Pathfinder who is commemorated
on the Wall of Names. The name-keeper must make this selection each day when preparing her spells.
While this feature is active, she gains one or more benefits tied to the Pathfinder's former focus
in the Society: Scrolls, Spells, or Swords. Each allows her to select one or more options (such as a
weapon or shaman spirit), and she can choose different options each time she forms this bond.

### Scrolls {#scrolls}

The name-keeper selects an oracle [mystery](ref/ability/mysteries). She can use any of the mystery's
associated skills untrained, and she treats them as class skills. For any of those skills that were
already class skills, she instead gains a +2 sacred bonus on those checks. At 12th level, she gains
[Skill Focus](ref/feat/skill-focus) for one of the associated skills as a bonus feat. At 20th level,
she gains Skill Focus a second time as a bonus feat, and she always counts as having at least 10
ranks in those skills for calculating these temporary feats' benefits.

### Spells {#spells}

The name-keeper selects a second shaman spirit and adds the spells granted by that spirit to her
list of spells that she can cast using spirit magic. She gains one additional spirit magic spell
slot of her highest spell level. At 12th level, she selects two shaman spirits and adds both their
granted spells to the list of spells she can cast using spirit magic. At 20th level, her number of
spirit magic spell slots at each spell level increases to two.

### Swords {#swords}

The name-keeper gains proficiency in all martial weapons and one exotic weapon of her choice. At
12th level, whenever she makes a full attack, she gains one additional attack at her highest base
attack bonus; this ability stacks with the extra attack from _[haste](ref/spell/haste)_, but it
doesn't stack with other abilities that grant extra attacks. At 20th level, she gains two combat
feats for which she qualifies.

This ability replaces wandering spirit.

## Versatile Hex (Su) {#versatile-hex}

At 6th level, a name-keeper can temporarily gain a shaman hex or one of the hexes that her spirit
has when she prepares her spells, lasting until the next time she prepares spells. At 14th level,
she can select two such hexes each day.

This ability replaces wandering hex.
