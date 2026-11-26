+++
id = "ref/arc-barbarian/urban-barbarian"
kind = "archetype"
title = "Urban Barbarian"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Urban%20Barbarian"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_barbarian", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "31"

[fields]
kind = "archetype"
features = [
  { anchor = "crowd-control", level = 1 },
  { anchor = "controlled-rage" },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["crowd-control"] },
  { alters = "Rage", feature = "rage", by = ["controlled-rage"] },
]
+++

Every barbarian knows that city life can soften the spirit and the body, but some barbarians take on
the trappings and ways of their adoptive homes and bend their savage powers to its challenges. While
these urban barbarians' rough edges are smoothed into civility, they can use their primal nature and
upbringing to move with the ebb and flow of civilization's natural rhythms.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An urban barbarian is not proficient with medium armor.

## Skills {#skills}

An urban barbarian does not gain Handle Animal (Cha), Knowledge (nature) (Int), or Survival (Wis) as
class skills; instead, she gains Diplomacy (Cha), Knowledge (local) (Int), Knowledge (nobility)
(Int), Linguistics (Int), and Profession (Wis) as class skills.

## Crowd Control (Ex) {#crowd-control}

At 1st level, an urban barbarian gains a +1 bonus on attack rolls and a +1 dodge bonus to AC when
adjacent to two or more enemies. In addition, her movement is not impeded by
[crowds](ref/rule/city-streets), and she gains a bonus equal to 1/2 her barbarian level on
Intimidate checks to influence crowds. This ability replaces fast movement.

## Controlled Rage (Ex) {#controlled-rage}

When an urban barbarian rages, instead of making a normal rage she applies a +4 morale bonus to her
Strength, Dexterity, or Constitution. This bonus increases to +6 when she gains greater rage and +8
when she gains mighty rage. She may apply the full bonus to one ability score or may split the bonus
between several scores in increments of +2. When using a controlled rage, an urban barbarian gains
no bonus on Will saves, takes no penalties to AC, and can still use Intelligence-, Dexterity-, and
Charisma-based skills. This ability otherwise follows the normal rules for rage. This ability alters
rage.

## Rage Powers {#rage-powers}

The following rage powers complement the urban barbarian archetype:
[boasting taunt](ref/ragepower/boasting-taunt), [clear mind](ref/ragepower/clear-mind),
[deadly accuracy](ref/ragepower/deadly-accuracy), [guarded stance](ref/ragepower/guarded-stance),
[intimidating glare](ref/ragepower/intimidating-glare),
[lethal accuracy](ref/ragepower/lethal-accuracy), [no escape](ref/ragepower/no-escape),
[quick reflexes](ref/ragepower/quick-reflexes), [perfect clarity](ref/ragepower/perfect-clarity),
[sharpened accuracy](ref/ragepower/sharpened-accuracy),
[surprise accuracy](ref/ragepower/surprise-accuracy), and
[unexpected strike](ref/ragepower/unexpected-strike).
