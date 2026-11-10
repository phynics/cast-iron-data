+++
id = "ref/arc-kineticist/blood-kineticist"
kind = "archetype"
title = "Blood Kineticist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_kineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "occult-adventures"
page = "88"

[fields]
kind = "archetype"
replaces = ["The 1st-level infusion", "The 5th-level infusion", "The 6th-level utility wild talent", "The 8th-level utility wild talent", "The 9th-level infusion", "The 11th-level infusion", "Omnikinesis"]
alters = ["Expanded element"]
replaces_features = ["omnikinesis"]
alters_features = ["expanded-element"]
+++

To a blood kineticist, the water in a creature's blood is just like any other sort, and she uses
that knowledge to brutal ends.

**Blood Focus (Ex)**

**Info:** A blood kineticist must choose water as her primary [element](ref/ability/elements) and
must choose [water blast](ref/kinetic/water-blast) as her first simple blast. All of her infusions
granted by this archetype work only on targets with blood and automatically fail if the target is
immune to [bleed](ref/rule/bleed) damage.

**Wrack (Su)**

**Ability:** A blood kineticist can use her abilities to wrack a target within 30 feet, harming the
target by manipulating its blood from the inside. The target takes half the normal damage of the
blood kineticist's blast, and can attempt a Fortitude save to reduce that amount to 1/4 normal
damage, but the damage is untyped and ignores [damage reduction](ref/rule/damage-reduction).

**Gained:** At 1st Level

**Replaces:** The 1st-level infusion

**Special:** This is a 1st-level form infusion that costs 0 points of burn and can be used with
water and blood blasts.

**Bleeding Infusion (Su)**

**Ability:** A blood kineticist can infuse her blasts with a vicious power that causes internal or
external bleeding. On a failed Fortitude save, the target takes 1 point of bleed damage for every
die of the blast's damage. A target that fails its saving throw against the wrack form infusion does
not receive a saving throw to avoid the bleed damage from bleeding infusion on the same blast.

**Gained:** At 5th Level

**Replaces:** The 5th-level infusion

**Special:** This is a 2nd-level substance infusion that costs 2 points of burn and can be used with
water and blood blasts.

**Blood Tell (Sp)**

**Ability:** A blood kineticist's connection to blood allows her to learn much from the blood of
another. This works as [blood biography](ref/spell/blood-biography), except the blood kineticist
suddenly knows the information, rather than having it appear on a parchment.

**Gained:** At 6th Level

**Replaces:** The 6th-level utility wild talent

**Special:** This is a 3rd-level utility wild talent and costs 0 points of burn. She can accept 1
point of burn to reduce the casting time to a **standard action** instead of 1 minute.

**Blood Blast (Su)**

**Alters:** Expanded element

**Info:** The first time a blood kineticist selects water with _expanded element,_ she doesn't gain
the [cold simple blast](ref/kinetic/cold-blast) or the [ice composite blast](ref/kinetic/ice-blast);
instead, she gains the _blood composite blast,_ which costs 2 points of burn. A _blood blast_ is a
physical blast that deals bludgeoning damage. It is associated with the same infusions as the _water
blast._ If the blood kineticist selects water with _expanded element_ a second time, she gains the
_cold blast_ and _ice blast_ as normal.

**Blood Throw (Su)**

**Ability:** A blood kineticist gains the [foe throw](ref/kinetic/foe-throw) infusion as a bonus
infusion, and can use it with the water element on water and blood blasts, in addition to its normal
associated element and blast.

**Gained:** At 8th Level

**Replaces:** The 8th-level utility wild talent

**Gut-Wrenching Infusion (Su)**

**Ability:** A blood kineticist can infuse her blasts with the ability to manipulate her opponent's
insides to the point of impairing their function. On a failed Fortitude save, the target is
[sickened](ref/misc/sickened) for 1 minute. A target that fails its saving throw against the wrack
form infusion does not receive a saving throw to avoid the sickened condition from _gut-wrenching
infusion_ on the same blast.

**Gained:** At 9th Level

**Replaces:** The 9th-level infusion

**Special:** This is a 4th-level substance infusion that costs 3 points of burn and can be used with
water and blood blasts.

**Vampiric Infusion (Su)**

**Ability:** A blood kineticist can drain the vitality from her enemy's blood to restore her own. If
her blast hits (or the enemy fails its saving throw against a blast without an attack roll) the
blood kineticist can activate the [kinetic healer](ref/kinetic/kinetic-healer) utility wild talent
on herself by accepting its burn cost; she doesn't need to take an action to do so. If she doesn't
possess the _kinetic healer_ utility wild talent, she can still use this ability, but it heals only
half as much.

**Gained:** At 11th Level

**Replaces:** The 11th-level infusion

**Special:** This is a 5th-level substance infusion that costs 3 points of burn and can be used with
water and blood blasts.

**Blood Mastery (Su)**

**Gained:** At 20th Level

**Passive:** A blood kineticist no longer ages and can't be magically aged. She doesn't take
penalties to her ability scores for [aging](ref/rule/age) and removes any such penalties she already
possesses. She still accrues age bonuses as normal, but she doesn't die of old age when her time
would be up. Because of her utter control over her own blood, she is immune to bleed, injected
poisons, injury diseases, and the sickened and [nauseated](ref/misc/nauseated) conditions unless she
chooses to be affected.

**Replaces:** Omnikinesis
