+++
id = "ref/arc-oracle/elementalist-oracle"
kind = "archetype"
title = "Elementalist Oracle"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Elementalist%20Oracle"
source_ids = ["ultimate-wilderness", "people-of-the-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elementalist_oracle", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "68"
[[sources]]
publication = "people-of-the-sands"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "revelations" },
  { anchor = "elemental-linguist", level = 1 },
  { anchor = "elemental-form", level = 11 },
  { anchor = "elemental-revelation", level = 20 },
]
trades = [
  { replaces = "The oracle's mystery bonus spells at these levels", feature = "mystery", levels = [4, 6, 8, 10, 12, 18], power = "bonus spells" },
  { replaces = "Final revelation", feature = "final-revelation", by = ["elemental-revelation"] },
]
+++

An elementalist oracle shares an affinity with the elements and elemental creatures. She can
communicate with elemental creatures and can eventually become an elemental herself. She sees
perfection in manifestations of elemental fury in the natural world, be they the thunderous wrath of
the storm, the churning waters of the ocean's tides or a flooding river, the terrain-shaping power
of a landslide or earthquake, or the apocalyptic fury of a volcanic eruption.

## Recommended Mysteries {#recommended-mysteries}

Flame, stone, waves, wind.

## Bonus Spells {#bonus-spells}

_Elemental touch_ (4th), _protection from energy_ (6th), _elemental body_ (8th), _summon monster V_
(elementals only; 10th), _elemental body III_ (12th), _elemental swarm_ (18th). These bonus spells
replace the oracle's mystery bonus spells at these levels.

## Revelations {#revelations}

An elementalist oracle must take the following revelations at the listed levels.

## Elemental Linguist (Su) {#elemental-linguist}

At 1st level, you gain a bonus language of your choice from the following list: Aquan, Auran, Ignan,
or Terran. At 5th, 10th, and 15th levels, you gain another language chosen from this list.

## Elemental Form (Su) {#elemental-form}

At 11th level, you gain the [air](ref/subtype/air), [earth](ref/subtype/earth),
[fire](ref/subtype/fire), or [water](ref/subtype/water) subtype and an associated ability: • Air:
Fly speed of 30 feet with perfect maneuverability. • Earth: [Tremorsense](ref/umr/tremorsense) with
a range of 30 feet. • Fire: Immunity to fire and vulnerability to cold. • Water: Swim speed of 30
feet and the ability to breathe underwater.

## Elemental Revelation (Su) {#elemental-revelation}

At 20th level, you fully harness the power of the elements. You can apply the
[Elemental Spell](ref/feat/elemental-spell) metamagic feat (_Pathfinder RPG Advanced Player's Guide_
158) to spells you cast without increasing the level or casting time. You can choose acid, cold,
electricity, or fire each time you use this ability. Whenever you score a critical hit with an
attack that deals energy damage, you ignore the target's energy resistance (if any). If you score
such a critical hit against a creature that has immunity to the energy type you are attacking with,
the creature takes half damage from the attack.

This replaces final revelation.
