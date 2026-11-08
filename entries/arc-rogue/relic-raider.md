+++
id = "ref/arc-rogue/relic-raider"
kind = "archetype"
title = "Relic Raider"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "relic_raider", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]

[fields]
kind = "archetype"
replaces = ["Uncanny dodge", "Improved uncanny dodge"]
+++

**Sources:** Black Markets pg 27\
Relic raiders are rogues who specialize in recovering treasures from ruins and tombs, some in a
quest for knowledge, others out of a desire for riches. In addition to natural dangers and mundane
traps, these locations are often protected by ancient curses or the psychic imprints of former
occupants. Though not versed in magic, relic raiders learn to unweave these maledictions as easily
as they unlock ancient vaults.

**Curse Sense (Ex)**

**Ability:** A relic raider adds 1/2 her rogue level on Perception checks to notice haunts and on
Spellcraft checks to identify cursed items (using [detect magic](ref/spell/detect-magic) or similar
effects).

**Gained:** At 4th Level

**Passive:** In addition, the relic raider gains a bonus on saving throws against curses and haunts
and a dodge bonus to AC against attacks by haunts. These bonuses are equal to one-third of her rogue
level.

**Replaces:** Uncanny dodge

**Disable Curse (Su)**

**Ability:** A relic raider can attempt to disable a curse as she would a magical trap. This ability
acts as [remove curse](ref/spell/remove-curse), except instead of a caster level check, the relic
raider attempts a Disable Device check (DC = 15 + the DC of the curse). Disabling a curse takes 2d4
rounds, and the relic raider cannot take 10 or 20 on this check.

**Gained:** At 8th Level

**Replaces:** Improved uncanny dodge

**Usage:** 1 time/day + 1 per 4 rogue levels beyond 8th

**Advanced Rogue Talents**

**Ability:** A relic raider can select the following new advanced rogue talents. These talents are
considered Primary Sneak Attack Talents, and add effects to a rogue's sneak attack. Only one Primary
Sneak Attack Talent can be applied to an individual attack, and the decision must be made before
making the attack roll.

**Cursed Strike (Su)**

**Ability:** Once per day, when the relic raider would normally deal sneak attack damage, she can
instead forgo all bonus damage to attempt to curse her target (as per the spell
[bestow curse](ref/spell/bestow-curse)). The save is DC equal to 10 + 1/2 the relic raider's rogue
level + her Intelligence modifier.

**Prereq:** [Major magic](ref/talent/major-magic) rogue talent

**Etheric Strike (Su)**

**Ability:** With a successful sneak attack against haunts or undead, the relic raider can deal her
sneak attack damage as positive energy damage rather than physical damage. The additional damage
affects undead that are normally immune to sneak attacks because of their lack of a discernible
anatomy (such as [ghosts](ref/template/ghost)).

**Usage:** Charisma3 modifier times/day
