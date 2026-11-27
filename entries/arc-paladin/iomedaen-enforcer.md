+++
id = "ref/arc-paladin/iomedaen-enforcer"
kind = "archetype"
title = "Iomedaean Enforcer"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Iomedaen%20Enforcer"
source_ids = ["divine-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iomedaen_enforcer", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "divine-anthology"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "detect-chaos", level = 1 },
  { anchor = "smite-chaos", level = 1 },
  { anchor = "aura-of-order", level = 14 },
  { anchor = "armor-of-law", level = 17 },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["detect-chaos"] },
  { replaces = "Smite evil", feature = "smite-evil", by = ["smite-chaos"] },
  { alters = "Aura of faith", feature = "aura-of-faith", by = ["aura-of-order"] },
  { alters = "Aura of righteousness", feature = "aura-of-righteousness", by = ["armor-of-law"] },
  { alters = "holy champion", feature = "holy-champion", by = ["armor-of-law"] },
  { replaces = "The paladin's class skills list" },
]
+++

Since the publication of _The Majestic Book of the Prime Ascended_, certain paladins have taken
"Prime Commander" to heart and have developed their own methods of upholding the teachings in this
book. Iomedaean enforcers have altered abilities that allow them to stand against the forces of
chaos. They seek to maintain order and uphold the laws of just rulers and governments, pursuing any
who break those laws or otherwise disrupt the peace. Still, they remain lawful good servants of
[Iomedae](ref/faith/iomedae), and as such always seek to temper the justice they deliver with mercy.

## Class Skills {#class-skills}

The Iomedaean enforcer's class skills are Craft (Int), Handle Animal (Cha), Heal (Wis), Intimidate
(Cha), Knowledge (local) (Int), Knowledge (religion) (Int), Profession (Wis), Ride (Dex), Sense
Motive (Wis), and Spellcraft (Int).

This replaces the paladin's class skills list.

## Detect Chaos (Sp) {#detect-chaos}

At will, an Iomedaean enforcer can use _[detect chaos](ref/spell/detect-chaos)_, as per the spell.
The Iomedaean enforcer can, as a move action, concentrate on a single item or individual within 60
feet and determine whether it is chaotic, learning the strength of its aura as if she had studied it
for 3 rounds. While focusing on one individual or object, the Iomedaean enforcer can't use
_[detect chaos](ref/spell/detect-chaos)_ on any other object or individual within range.

This ability replaces _detect evil_.

## Smite Chaos (Su) {#smite-chaos}

This ability functions as the paladin's smite evil ability, but against chaotic-aligned creatures.
Smite chaos is twice as effective against chaotic-aligned aberrations, outsiders with the chaotic
subtype, and fey.

This ability replaces smite evil.

## Aura of Order {#aura-of-order}

At 14th level, the paladin's weapons are treated as lawful-aligned for the purposes of overcoming
[damage reduction](ref/rule/damage-reduction). Any attack made against an enemy within 10 feet of
the Iomedaean enforcer is treated as if it were lawful-aligned for the purpose of overcoming damage
reduction.

This ability alters aura of faith.

## Armor of Law (Su) {#armor-of-law}

When an enforcer gains [damage reduction](ref/rule/damage-reduction) from aura of righteousness, it
is DR 5/chaos instead of DR 5/evil. When that DR increases from the holy champion class feature, it
increases to DR 10/chaos.

This ability alters the aura of righteousness and holy champion class features.
