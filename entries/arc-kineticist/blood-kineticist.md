+++
id = "ref/arc-kineticist/blood-kineticist"
kind = "archetype"
title = "Blood Kineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Blood%20Kineticist"
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
features = [
  { anchor = "blood-focus" },
  { anchor = "wrack", level = 1 },
  { anchor = "bleeding-infusion", level = 5 },
  { anchor = "blood-tell", level = 6 },
  { anchor = "blood-blast", level = 7 },
  { anchor = "blood-throw", level = 8 },
  { anchor = "gut-wrenching-infusion", level = 9 },
  { anchor = "vampiric-infusion", level = 11 },
  { anchor = "blood-mastery", level = 20 },
]
trades = [
  { replaces = "The 1st-level infusion", feature = "infusion", levels = [1], by = ["wrack"] },
  { replaces = "The 5th-level infusion", feature = "infusion", levels = [5], by = ["bleeding-infusion"] },
  { replaces = "The 6th-level utility wild talent", feature = "wild-talents", levels = [6], by = ["blood-tell"] },
  { replaces = "The 8th-level utility wild talent", feature = "wild-talents", levels = [8], by = ["blood-throw"] },
  { replaces = "The 9th-level infusion", feature = "infusion", levels = [9], by = ["gut-wrenching-infusion"] },
  { replaces = "The 11th-level infusion", feature = "infusion", levels = [11], by = ["vampiric-infusion"] },
  { replaces = "Omnikinesis", feature = "omnikinesis", by = ["blood-mastery"] },
  { alters = "Expanded element", feature = "expanded-element", by = ["blood-blast"] },
]
+++

To a blood kineticist, the water in a creature's blood is just like any other sort, and she uses
that knowledge to brutal ends.

## Blood Focus (Ex) {#blood-focus}

A blood kineticist must choose water as her primary [element](ref/ability/elements) and must choose
[water blast](ref/kinetic/water-blast) as her first simple blast. All of her infusions granted by
this archetype work only on targets with blood and automatically fail if the target is immune to
[bleed](ref/rule/bleed) damage.

## Wrack (Su) {#wrack}

At 1st level, a blood kineticist can use her abilities to wrack a target within 30 feet, harming the
target by manipulating its blood from the inside. The target takes half the normal damage of the
blood kineticist's blast, and can attempt a Fortitude save to reduce that amount to 1/4 normal
damage, but the damage is untyped and ignores [damage reduction](ref/rule/damage-reduction). This is
a 1st-level form infusion that costs 0 points of burn and can be used with water and blood blasts.
This ability replaces the 1st-level infusion.

## Bleeding Infusion (Su) {#bleeding-infusion}

At 5th level, a blood kineticist can infuse her blasts with a vicious power that causes internal or
external bleeding. On a failed Fortitude save, the target takes 1 point of bleed damage for every
die of the blast's damage. A target that fails its saving throw against the wrack form infusion does
not receive a saving throw to avoid the bleed damage from bleeding infusion on the same blast. This
is a 2nd-level substance infusion that costs 2 points of burn and can be used with water and blood
blasts. This ability replaces the 5th-level infusion.

## Blood Tell (Sp) {#blood-tell}

At 6th level, a blood kineticist's connection to blood allows her to learn much from the blood of
another. This works as _[blood biography](ref/spell/blood-biography)_, except the blood kineticist
suddenly knows the information, rather than having it appear on a parchment. This is a 3rd-level
utility wild talent and costs 0 points of burn. She can accept 1 point of burn to reduce the casting
time to a standard action instead of 1 minute. This ability replaces the 6th-level utility wild
talent.

## Blood Blast (Su) {#blood-blast}

The first time a blood kineticist selects water with expanded element, she doesn't gain the
[cold simple blast](ref/kinetic/cold-blast) or the [ice composite blast](ref/kinetic/ice-blast);
instead, she gains the blood composite blast, which costs 2 points of burn. A blood blast is a
physical blast that deals bludgeoning damage. It is associated with the same infusions as the water
blast. If the blood kineticist selects water with expanded element a second time, she gains the cold
simple blast and ice composite blast as normal. This ability alters expanded element.

## Blood Throw (Su) {#blood-throw}

At 8th level, a blood kineticist gains the [foe throw](ref/kinetic/foe-throw) infusion as a bonus
infusion, and can use it with the water element on water and blood blasts, in addition to its normal
associated element and blast. This ability replaces the 8th-level utility wild talent.

## Gut-Wrenching Infusion (Su) {#gut-wrenching-infusion}

At 9th level, a blood kineticist can infuse her blasts with the ability to manipulate her opponent's
insides to the point of impairing their function. On a failed Fortitude save, the target is
[sickened](ref/misc/sickened) for 1 minute. A target that fails its saving throw against the wrack
form infusion does not receive a saving throw to avoid the sickened condition from gut-wrenching
infusion on the same blast. This is a 4th-level substance infusion that costs 3 points of burn and
can be used with water and blood blasts. This ability replaces the 9th-level infusion.

## Vampiric Infusion (Su) {#vampiric-infusion}

At 11th level, a blood kineticist can drain the vitality from her enemy's blood to restore her own.
If her blast hits (or the enemy fails its saving throw against a blast without an attack roll) the
blood kineticist can activate the [kinetic healer](ref/kinetic/kinetic-healer) utility wild talent
on herself by accepting its burn cost; she doesn't need to take an action to do so. If she doesn't
possess the kinetic healer utility wild talent, she can still use this ability, but it heals only
half as much. This is a 5th-level substance infusion that costs 3 points of burn and can be used
with water and blood blasts. This ability replaces the 11th-level infusion.

## Blood Mastery (Su) {#blood-mastery}

At 20th level, a blood kineticist no longer ages and can't be magically aged. She doesn't take
penalties to her ability scores for [aging](ref/rule/age) and removes any such penalties she already
possesses. She still accrues age bonuses as normal, but she doesn't die of old age when her time
would be up. Because of her utter control over her own blood, she is immune to bleed, injected
poisons, injury diseases, and the sickened and [nauseated](ref/misc/nauseated) conditions unless she
chooses to be affected. This ability replaces omnikinesis.
