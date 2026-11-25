+++
id = "ref/arc-swashbuckler/picaroon"
kind = "archetype"
title = "Picaroon"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Picaroon"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "picaroon", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "127"

[fields]
kind = "archetype"
features = [
  { anchor = "panache" },
  { anchor = "deeds" },
  { anchor = "melee-shooter", level = 1 },
  { anchor = "quick-clear", level = 3 },
  { anchor = "gun-feint", level = 7 },
  { anchor = "lightning-reload", level = 11 },
  { anchor = "two-weapon-finesse", level = 1 },
]
trades = [
  { replaces = "Weapon proficiency", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Opportune parry and riposte", feature = "deeds", power = "opportune parry and riposte", by = ["melee-shooter"] },
  { replaces = "Kip-up", feature = "deeds", power = "kip-up", by = ["quick-clear"] },
  { replaces = "Superior feint", feature = "deeds", power = "superior feint", by = ["gun-feint"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["lightning-reload"] },
  { replaces = "Swashbuckler finesse", feature = "swashbuckler-finesse", by = ["two-weapon-finesse"] },
  { alters = "Panache", feature = "panache", by = ["panache"] },
]
+++

While some swashbucklers take pride in their ability to wear down an opponent with great skill at
arms and clever positioning, there are those who use firearms to get in close and hit hard.

## Weapon Proficiency {#weapon-proficiency}

A picaroon gains proficiency with all simple weapons and martial weapons, as well as one-handed
firearms. This replaces the swashbuckler's weapon proficiency.

## Panache {#panache}

Unlike other swashbucklers, a picaroon regains panache when she confirms a critical hit or makes a
killing blow with a light or one-handed piercing melee weapon or a one-handed firearm. This ability
alters panache.

## Deeds {#deeds}

The picaroon gains the following deeds, each of which replaces an existing deed.

## Melee Shooter (Ex) {#melee-shooter}

At 1st level, as a swift action when wielding both a light or one-handed piercing melee weapon and a
one-handed firearm, the picaroon can spend 1 panache point to avoid provoking attacks of opportunity
with the first ranged attack made by the one-handed firearm during her turn. This deed replaces
opportune parry and riposte.

## Quick Clear (Ex) {#quick-clear}

At 3rd level, as a standard action the picaroon can spend 1 panache point to remove the
[broken](ref/misc/broken) condition from a single one-handed firearm she is currently wielding, as
long as the firearm gained that condition through a misfire. This deed replaces kip-up.

## Gun Feint (Ex) {#gun-feint}

At 7th level, a picaroon can use the ferocious reputation of firearms to her advantage. A picaroon
with at least 1 panache point can [feint](ref/skill/bluff) instead of attacking with her firearm as
part of a full attack. She can spend 1 panache point to gain a +5 bonus on this check. This deed
replaces superior feint.

## Lightning Reload (Ex) {#lightning-reload}

At 11th level, once per round the picaroon can spend 1 panache point to reload a single barrel of a
one-handed firearm as a swift action. If she has the [Rapid Reload](ref/feat/rapid-reload) feat or
is using an alchemical cartridge, she can instead reload a single barrel of the weapon as a free
action each round. Using this deed doesn't provoke attacks of opportunity. This deed replaces
bleeding wound.

## Two-Weapon Finesse (Ex) {#two-weapon-finesse}

A picaroon gains the benefits of the [Weapon Finesse](ref/feat/weapon-finesse) feat with light or
one-handed piercing melee weapons. She also gains the effects of the
[Two-Weapon Fighting](ref/feat/two-weapon-fighting) feat as long as she is wielding a light or
one-handed piercing melee weapon in one hand and one-handed firearm in the other hand. This ability
counts as having both the Weapon Finesse and Two-Weapon Fighting feats for the purposes of meeting
feat requirements. This ability replaces swashbuckler finesse.
