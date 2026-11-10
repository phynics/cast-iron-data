+++
id = "ref/arc-swashbuckler/inspired-blade"
kind = "archetype"
title = "Inspired Blade"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inspired_blade", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "125"

[fields]
kind = "archetype"
replaces = ["Swashbuckler finesse", "Bleeding wound", "Swashbuckler weapon training", "Swashbuckler weapon mastery"]
alters = ["Panache"]
replaces_features = ["swashbuckler-finesse", "swashbuckler-weapon-training", "swashbuckler-weapon-mastery"]
alters_features = ["panache"]
+++

An inspired blade is both a force of personality and a sage of swordplay dedicated to the perfection
of combat with the rapier. They use the science and geometry with swordplay to beautiful and deadly
effect.

**Inspired Panache (Ex)**

**Alters:** Panache

**Info:** Each day, an inspired blade gains a number of panache points equal to her Charisma
modifier (minimum 1) and Intelligence modifier (minimum 1), instead of just her Charisma modifier.

**Special:** Unlike other swashbucklers, an inspired blade gains no panache from a killing blow. She
gains panache only from scoring a critical hit with a [rapier](ref/eq-weapon/rapier).

**Inspired Finesse (Ex)**

**Ability:** An inspired blade gains the benefits of [Weapon Finesse](ref/feat/weapon-finesse) with
the rapier (this ability counts as having the Weapon Finesse feat for the purpose of meeting feat
prerequisites) and gains [Weapon Focus](ref/feat/weapon-focus) (rapier) as a bonus feat.

**Gained:** At 1st Level

**Replaces:** Swashbuckler finesse

**Deeds**

**Ability:** The inspired blade gains the following deed.

**Inspired Strike (Ex)**

**Ability:** An inspired blade can spend 1 panache point when making an attack with a rapier to gain
an insight bonus on that attack roll equal to her Intelligence modifier (minimum +1).

**Ability2:** When an inspired blade hits with an attack augmented by _inspired strike,_ she can
spend 1 additional panache point to make the hit a critical threat, though if she does so, she does
not regain panache if she confirms that critical threat. The cost of this deed cannot be reduced by
abilities such as [Signature Deed](ref/feat/signature-deed).

**Gained:** At 11th Level

**Replaces:** Bleeding wound

**Rapier Training (Ex)**

**Gained:** At 5th Level

**Passive:** An inspired blade gains a +1 bonus on attack rolls and a +2 bonus on damage rolls with
rapiers. While wielding a rapier, she gains the benefit of the
[Improved Critical](ref/feat/improved-critical) feat.

**Replaces:** Swashbuckler weapon training

**Rapier Weapon Mastery (Ex)**

**Gained:** At 20th Level

**Passive:** When an inspired blade threatens a critical hit with a rapier, that critical hit is
automatically confirmed. Furthermore, the critical threat range increases by 1 (this increase to the
critical threat range stacks with the increases from _rapier training,_ to a total threat range of
14-20), and the critical modifier of the weapon increases by 1 (&times&2 becomes &times&3, for
example).

**Replaces:** Swashbuckler weapon mastery
