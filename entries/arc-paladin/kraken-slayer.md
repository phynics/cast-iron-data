+++
id = "ref/arc-paladin/kraken-slayer"
kind = "archetype"
title = "Kraken Slayer"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Kraken%20Slayer"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kraken_slayer", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "smite-deepest-evil", level = 1 },
  { anchor = "divine-immunity", level = 3 },
  { anchor = "divine-bond" },
  { anchor = "aura-of-elusion", level = 14 },
]
trades = [
  { replaces = "Divine health", feature = "divine-health", by = ["divine-immunity"] },
  { replaces = "Aura of faith", feature = "aura-of-faith", by = ["aura-of-elusion"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["smite-deepest-evil"] },
  { alters = "Divine bond", feature = "divine-bond", by = ["divine-bond"] },
]
+++

Triton kraken slayers oppose all underwater threats, but they especially target the tentacled
monstrosities called [krakens](ref/monster/kraken). Kraken slayers develop specialized tactics to
defeat their hated enemies as well as learn to recognize the signs of kraken activity in an area. A
kraken slayer's greatest responsibility is to destroy evil; all other commitments fall by the
wayside. Though kraken slayers uphold all promises they make, they must balance their obligations as
kraken slayers with their role as knights and defenders of the ocean.

## Smite Deepest Evil (Su) {#smite-deepest-evil}

This functions as the smite evil ability, but the kraken slayer does not get a bonus of 2 points of
damage per level on the first successful attack against any creatures other than evil creatures with
the aquatic or water subtype. She gains a bonus of 2 points of damage per level on all smite attacks
made against evil creatures with the aquatic or water subtype.

This ability alters smite evil.

## Divine Immunity (Ex) {#divine-immunity}

At 3rd level, a kraken slayer is immune to poisons and diseases, including supernatural and magical
diseases, delivered by the natural attacks of creatures with the aquatic or water subtype.

This ability replaces divine health.

## Divine Bond (Sp) {#divine-bond}

A kraken slayer who chooses a weapon as her divine bond may either increase her weapon's enhancement
bonus or add any of the following properties to her weapon: _[axiomatic](ref/magic-enh/axiomatic)_,
_[brilliant energy](ref/magic-enh/brilliant-energy)_, _[defending](ref/magic-enh/defending)_,
_[grayflame](ref/magic-enh/grayflame)_, _[holy](ref/magic-enh/holy)_, _[keen](ref/magic-enh/keen)_,
_[merciful](ref/magic-enh/merciful)_, _[seaborne](ref/magic-enh/seaborne)_, and
_[speed](ref/magic-enh/speed)_. A kraken slayer who chooses a mount must select one suitable for an
aquatic environment, such as an [elasmosaurus](ref/companion/elasmosaurus),
[giant seahorse](ref/companion/seahorse-giant), or [orca](ref/companion/orca).

This ability alters divine bond.

## Aura of Elusion (Su) {#aura-of-elusion}

At 14th level, a kraken slayer gains a sacred bonus equal to her kraken slayer level on Escape
Artist checks and combat maneuver checks to escape a grapple and to her CMD to avoid being grappled.
Each ally within 10 feet of her gains a sacred bonus equal to half her kraken slayer level on Escape
Artist checks and combat maneuver checks to escape a grapple and to CMD to avoid being grappled.
This ability functions only while the paladin is conscious, not if she is unconscious or dead.

This ability replaces aura of faith.
