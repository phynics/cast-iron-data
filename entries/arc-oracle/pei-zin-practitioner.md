+++
id = "ref/arc-oracle/pei-zin-practitioner"
kind = "archetype"
title = "Pei Zin Practitioner"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Pei%20Zin%20Practitioner"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pei_zin_practitioner", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "healers-handbook"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "master-herbalist" },
  { anchor = "healer-s-way", level = 1 },
  { anchor = "master-healing-technique", level = 7 },
]
trades = [
  { replaces = "The additional class skills the oracle gains from her mystery", feature = "mystery", power = "class skills", by = ["master-herbalist"] },
  { replaces = "Revelation gained at 1st level", feature = "revelation", levels = [1], by = ["healer-s-way"] },
  { replaces = "Revelation gained at 7th level", feature = "revelation", levels = [7], by = ["master-healing-technique"] },
]
+++

In distant Tian Xia, herbalists practice an obscure alchemical art known as
[Pei Zin herbalism](ref/rule/pei-zin-herbalism), which involves medicinal and restorative techniques
that are used throughout much of that continent. A few practitioners develop a talent for Pei Zin
that transcends ordinary alchemy, allowing them to blur the line between applying alchemical
medicine and coaxing divine miracles.

Like other masters of the art, Pei Zin practitioners can use the
[Profession (herbalist)](ref/skill/profession-any) skill in place of Craft (alchemy) to create
alchemical remedies with recipes that include certain plant-derived reagents. More information is on
pages 24–25 of _Pathfinder Player Companion: Alchemy Manual._

## Master Herbalist (Su) {#master-herbalist}

A Pei Zin practitioner has mastered countless alchemical techniques that supplement her divine
powers and greatly aid her when she heals the sick and wounded. She gains a competence bonus on
Profession (herbalist) checks equal to 1/2 her oracle level (minimum 1), and uses her Charisma
modifier in place of her Wisdom modifier when attempting Profession (herbalist) checks.
Additionally, a Pei Zin practitioner can identify potions as if via
_[detect magic](ref/spell/detect-magic)_ using Profession (herbalist) instead of Spellcraft, and she
can attempt such a check after holding a potion for 1 round.

This ability replaces the additional class skills the oracle gains from her mystery.

## Healer's Way (Su) {#healer-s-way}

A Pei Zin practitioner combines alchemy, acupuncture, and divine magic to heal wounds by touch. She
can use this ability a number of times per day equal to 1 + her Charisma modifier. With one use of
this ability, she uses positive energy to heal the target of 1d6 hit points for every 2 oracle
levels she has. Using this ability is a standard action unless the oracle targets herself, in which
case it is a swift action. Using this ability requires only one free hand. This ability counts as a
paladin's [lay on hands](ref/ability/lay-on-hands) ability for the purposes of feats, spells, and
effects that work with that class feature when it is used for healing purposes. Unlike lay on hands,
this ability cannot be used to harm undead.

This ability replaces the revelation gained at 1st level.

## Master Healing Technique (Su) {#master-healing-technique}

At 7th level, whenever a Pei Zin practitioner heals a living creature with her healer's way ability,
as a free action she can attempt a Profession (herbalist) check to remove a condition from the
target, with each condition having an accompanying Profession (herbalist) DC (see the list below).
She cannot take 10 or 20 on this check, nor can she receive aid from any creature except another Pei
Zin practitioner (though the practitioner need not be an oracle; see pages 24–25 of _Pathfinder
Player Companion: Alchemy Manual_). Failure by 5 or more causes the target to become
[sickened](ref/misc/sickened) for 1 round (if the Pei Zin practitioner is attempting to remove the
sickened condition, this extends it by 1 round). Similarly, failure by 10 or more instead causes the
target to become [nauseated](ref/misc/nauseated) for 1 round or to have its existing nauseated
condition extended by 1 round. A creature that cannot be sickened or nauseated cannot have
conditions removed by this ability.

- Minor Conditions (DC 20): Fatigued, shaken, and sickened.
- Major Conditions (DC 25): Dazed and staggered.
- Severe Conditions (DC 30): Confused, exhausted, frightened, and nauseated.
- Dire Conditions (DC 35): Blinded, deafened, paralyzed, and stunned.

This ability replaces the revelation gained at 7th level.

- Minor Conditions (DC 20): Fatigued, shaken, and sickened.
- Major Conditions (DC 25): Dazed and staggered.
- Severe Conditions (DC 30): Confused, exhausted, frightened, and nauseated.
- Dire Conditions (DC 35): Blinded, deafened, paralyzed, and stunned.

This ability replaces the revelation gained at 7th level.

## Recommended Mysteries {#recommended-mysteries}

[Life](ref/mystery/life), [nature](ref/mystery/nature), [succor](ref/mystery/succor).
