+++
id = "ref/arc-monk/weapon-adept"
kind = "archetype"
title = "Weapon Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Weapon%20Adept"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weapon_adept", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "114"

[fields]
kind = "archetype"
features = [
  { anchor = "perfect-strike", level = 1 },
  { anchor = "way-of-the-weapon-master", level = 2 },
  { anchor = "evasion", level = 9 },
  { anchor = "uncanny-initiative", level = 17 },
  { anchor = "pure-power", level = 20 },
]
trades = [
  { replaces = "Stunning Fist", feature = "stunning-fist", by = ["perfect-strike"] },
  { replaces = "Evasion", feature = "evasion", by = ["way-of-the-weapon-master", "evasion"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["evasion"] },
  { replaces = "Timeless body", feature = "timeless-body", by = ["uncanny-initiative"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["pure-power"] },
]
+++

While all monks train in both unarmed combat and with weapons, the weapon adept seeks to become one
with his weapons, transforming them into perfect extensions of his own body. Through such training,
a weapon adept seeks to attain perfection by becoming a living weapon himself. A weapon adept has
the following class features.

## Perfect Strike (Ex) {#perfect-strike}

At 1st level, a weapon adept gains [Perfect Strike](ref/feat/perfect-strike) as a bonus feat, even
if he does not meet the prerequisites. At 10th level, the monk can roll his attack roll three times
and take the higher result. If one of these rolls is a critical threat, he can choose which one of
his other two rolls to use as his confirmation roll. This ability replaces Stunning Fist.

## Way of the Weapon Master (Ex) {#way-of-the-weapon-master}

At 2nd level, a weapon adept gains [Weapon Focus](ref/feat/weapon-focus) as a bonus feat with one of
his monk weapons. At 6th level, the monk gains
[Weapon Specialization](ref/feat/weapon-specialization) with the same weapon as a bonus feat, even
if he does not meet the prerequisites. This ability replaces evasion.

## Evasion (Ex) {#evasion}

At 9th level, the monk gains [evasion](ref/ability/evasion). This ability replaces improved evasion.

## Uncanny Initiative (Ex) {#uncanny-initiative}

At 17th level, a weapon adept does not need to roll for initiative. He always treats his initiative
roll as if it resulted in any number of his choosing (from 1 to 20). This ability replaces timeless
body.

## Pure Power {#pure-power}

At 20th level, a weapon adept forsakes the ideals of the perfect self to become a bastion of the
physical and mental virtues monks hold dear. The monk gains a +2 bonus to Strength, Dexterity, and
Wisdom. This ability replaces perfect self.
