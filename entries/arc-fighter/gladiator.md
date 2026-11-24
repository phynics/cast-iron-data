+++
id = "ref/arc-fighter/gladiator"
kind = "archetype"
title = "Gladiator"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Gladiator"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gladiator", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "fame", level = 2 },
]
trades = [
  { alters = "Proficiency with heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor" },
  { alters = "tower shields", feature = "weapon-and-armor-proficiencies", power = "shields" },
  { replaces = "Bravery", feature = "bravery", by = ["fame"] },
]
+++

Most fighters battle out of necessity, with each battle a contest of life and death. Some, however,
fight for glory and for the adulation of the crowd. The gladiator is both a cunning warrior and a
consummate performer, knowing life and death are balanced not only on a sword's edge, but also on
the cheers or jeers of the crowd.

## Skills {#skills}

A gladiator gains Perform (act, comedy, and dance) (Cha) as class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A gladiator is not proficient with heavy armor or tower shields. Instead he gains the
[Performance Weapon Mastery](ref/feat/performance-weapon-mastery) feat (see page 112) at 1st level
as a bonus feat. This bonus feat is in addition to the bonus feat a fighter gains at 1st level.
Furthermore, a gladiator using [piecemeal armor](ref/rule/piecemeal-armor) is considered to be
wearing a suit of armor as long as he wearing two or three armor pieces, gaining the +1 to armor
bonus but still taking the +5% chance of arcane spell failure if the pieces are mixed.

## Bonus Feats {#bonus-feats}

A gladiator may choose to take combat or performance feats as bonus feats.

## Fame (Ex) {#fame}

At 2nd level, when a gladiator begins a [performance combat](ref/rule/performance-combat) (see page
153), he always starts with at least 1 victory point. If he already has victory points, he gains 1
extra victory point. At 10th level, the gladiator starts out with at least 2 victory points. If he
already has victory points, he gains 2 extra victory points. This ability replaces bravery.
