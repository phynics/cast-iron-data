+++
id = "ref/arc-druid/nature-priest"
kind = "archetype"
title = "Nature Priest"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Nature%20Priest"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nature_priest", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "healers-handbook"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "faithful" },
  { anchor = "studious-piety", level = 1 },
  { anchor = "chosen-druid" },
  { anchor = "shepherd-of-the-faithful", level = 4 },
  { anchor = "divine-servants", level = 9 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["studious-piety"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["shepherd-of-the-faithful"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["divine-servants"] },
  { alters = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "Nature bond", feature = "nature-bond", by = ["chosen-druid"] },
  { alters = "Class skills" },
]
+++

Nature priests serve two masters: their deities and nature itself, and can call upon the power of
both to fuel their divine abilities.

## Faithful {#faithful}

Like a cleric, a nature priest must worship a deity and her alignment must be within one step of her
deity's (_Pathfinder RPG Core Rulebook_ 166).

## Class Skills {#class-skills}

A nature priest adds Knowledge (religion) to her list of class skills instead of Knowledge
(geography).

This alters the druid's class skills.

## Weapon Proficiencies {#weapon-proficiencies}

A nature priest is proficient with her deity's favored weapon in addition to a druid's typical
weapon proficiencies.

This alters the druid's weapon proficiencies.

## Studious Piety (Ex) {#studious-piety}

A nature priest gains a +1 bonus on Knowledge (religion) checks. This bonus increases to +2 when
attempting checks that involve knowledge of her deity or her faith.

This ability replaces nature sense.

## Chosen Druid (Ex) {#chosen-druid}

If a nature priest chooses a domain for her nature bond, she must choose one of her deity's domains
(or subdomains) in place of those typically available to a druid.

This ability alters nature bond.

## Shepherd of the Faithful (Su) {#shepherd-of-the-faithful}

At 4th level, a nature priest and all allies within 60 feet that can see or hear her gain a +2
insight bonus on skill checks to notice or avoid natural hazards, difficult terrain, and rough winds
or water, as well as on saving throws against natural hazards. This ability offers no protection
against the abilities of creatures or the effects of spells or items.

This ability replaces resist nature's lure.

## Divine Servants (Su) {#divine-servants}

At 9th level, a nature priest adds the spells _[lesser planar ally](ref/spell/planar-ally-lesser)_,
_[planar ally](ref/spell/planar-ally)_, and _[greater planar ally](ref/spell/planar-ally-greater)_
to her druid spell list at their cleric spell levels. When she casts these spells, the planar allies
summoned require half the payment described in those spells.

This ability replaces the venom immunity ability.
