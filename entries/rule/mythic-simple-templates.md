+++
id = "ref/rule/mythic-simple-templates"
kind = "rule"
title = "Mythic Simple Templates"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mythic_simple_templates", path = "json/rules_campaign_types06.json" },
]
[[sources]]
publication = "mythic-adventures"
page = "224"

[fields]
kind = "none"
+++

The following simple templates can be used to turn any monster into a mythic creature. A creature
given one of these templates counts as a mythic creature for the purposes of spells, abilities, and
magic items even though it doesn't have the [mythic subtype](ref/rule/mythic-subtype). Note that
because it doesn't have the mythic subtype, it doesn't gain the many benefits of having the mythic
subtype - the creature only gains the benefits described in the simple template.

### Mythic Bonus Hit Points

A creature with one of the mythic templates listed below gains additional hit points according to
its Hit Die type. A creature with d6 Hit Dice gains 6 hit points per mythic rank, a creature with d8
Hit Dice gains 8 hit points per rank, and a creature with d10 or d12 Hit Dice gains 10 hit points
per rank.

### Agile (MR 1, CR +1)

Creatures with the agile template are quick and deadly, moving faster than their normal counterparts
and striking with incredible speed and agility. An agile creature's quick and rebuild rules are the
same.

**Rebuild Rules:** Init +20 bonus; AC +2 dodge bonus; hp mythic bonus hit points; Defensive
Abilities evasion (as the [rogue](ref/class/rogue) class feature); Speed +30 feet for all movement
types (up to double the creature's base movement speed); Special Attacks
[dual initiative](ref/umr/dual-initiative).

### Arcane (MR 1 or 2, CR +1)

Creatures with the arcane template are infused with arcane power, capable of casting a limited
number of arcane spells. If the creature has 11 or more Hit Dice, this simple template grants a
mythic rank of 2 instead of 1. An arcane creature's quick and rebuild rules are the same.

**Rebuild Rules:** AC +2 deflection bonus; hp mythic bonus hit points; SR gains SR equal to its new
CR + 11; Special Attacks [mythic magic, simple arcane casting](ref/umr/simple-arcane-spellcasting).

### Divine (MR 1 or 2, CR +1)

Creatures with the divine template can call upon the power of the gods, allowing them to cast a
limited number of divine spells. If the creature has 11 or more Hit Dice, this simple template
grants a mythic rank of 2 instead of 1. A divine creature's quick and rebuild rules are the same.

**Rebuild Rules:** Aura aura of grace (creature and all allies within 10 feet receive a +2 sacred
bonus on saving throws - or a profane bonus if the templated creature is evil); AC +2 deflection
bonus; hp mythic bonus hit points; Special Attacks
[mythic magic, simple divine spellcasting](ref/umr/simple-divine-spellcasting).

### Invincible (MR 1 or 2, CR +1)

Creatures with the invincible template are incredibly difficult to harm. They can withstand immense
punishment and continue to fight. If the creature has 11 or more Hit Dice, this simple template
grants a mythic rank of 2 instead of 1. An invincible creature's quick and rebuild rules are the
same.

**Rebuild Rules:** AC increase natural armor bonus by 2 (or 4 if the creature has 11 or more Hit
Dice); hp mythic bonus hit points; Defensive Abilities gains DR and resistance to all types of
energy as per Table 6-3, as well as [block attacks](ref/umr/block-attacks) and
[second save](ref/umr/second-save).

#### Table 6-3: Invincible Template Defenses

|Hit Dice|Energy Resistance|DR|
| --- | --- | --- |
|1-4|5|-|
|5-10|10|5/Epic|
|11+|15|10/Epic|

### Savage (MR 1 or 2, CR +1)

Creatures with the savage template are untamed, primordial versions of their non-mythic cousins.
Their claws are sharper, their fangs larger, and their hides thicker. If the creature has 11 or more
Hit Dice, this simple template grants a mythic rank of 2 instead of 1. A savage creature's quick and
rebuild rules are the same.

**Rebuild Rules:** AC increase natural armor bonus by 2; hp mythic bonus hit points; Defensive
Abilities gains DR and resistance to all types of energy as per Table 6-4; Special Attacks all
attacks gain bleed 1 (this stacks with itself),
[feral savagery (full attack)](ref/umr/feral-savagery).

#### Table 6-4: Savage Template Defenses

|Hit Dice|Energy Resistance|DR|
| --- | --- | --- |
|1-4|5|-|
|5-10|10|5/Epic|
|11+|15|10/Epic|
