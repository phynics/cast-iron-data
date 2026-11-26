+++
id = "ref/arc-paladin/tempered-champion"
kind = "archetype"
title = "Tempered Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Tempered%20Champion"
source_ids = ["weapon-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tempered_champion", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "weapon-masters-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "divine-weapon-specialization", level = 4 },
  { anchor = "divine-bond", level = 5 },
]
trades = [
  { replaces = "Spellcasting", feature = "spells", by = ["divine-weapon-specialization"] },
]
+++

Tempered champions are trained in the Tempering Hall in Absalom to master their deities' favored
weapons.

## Divine Weapon Specialization (Ex) {#divine-weapon-specialization}

At 4th level and every 4 levels thereafter, a tempered champion gains a bonus feat from the
following list: [Disruptive](ref/feat/disruptive),
[Divine Fighting Technique](ref/feat/divine-fighting-technique) (see page 10),
[Greater Penetrating Strike](ref/feat/greater-penetrating-strike),
[Greater Weapon Focus](ref/feat/greater-weapon-focus),
[Greater Weapon Specialization](ref/feat/greater-weapon-specialization),
[Penetrating Strike](ref/feat/penetrating-strike), [Weapon Focus](ref/feat/weapon-focus),
[Weapon Specialization](ref/feat/weapon-specialization), and [Weapon Trick](ref/feat/weapon-trick)
(see page 8). If a feat requires choosing a weapon or weapon group, the tempered champion must
choose her deity's favored weapon, or its group. The tempered champion must meet the feat's
prerequisites, but treats her tempered champion levels as fighter levels for this purpose.

In addition, the 4th-level tempered champion gains the increased base weapon damage of the
[warpriest's](ref/class/warpriest) sacred weapon ability at her tempered champion level. This
ability replaces spellcasting.

## Divine Bond (Su) {#divine-bond}

At 5th level, a tempered champion must select a weapon for her divine bond. If she is out of daily
uses, she can expend a use of lay on hands to activate this ability.
