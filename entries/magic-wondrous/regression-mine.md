+++
id = "ref/magic-wondrous/regression-mine"
kind = "item"
title = "Regression Mine"
source_ids = ["pathfinder-122-into-the-shattered-continent"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "regression_mine", path = "json/magic_wondrous_slotless05.json" },
]

[fields]
kind = "item"
category = "Wondrous Items"
price = "1,500 gp"
weight = "2 lbs."
slot = "none"
aura = "moderate enchantment"
caster_level = "10th"
+++

**Sources:** Pathfinder \#122: Into the Shattered Continent pg 75\
**Aura** moderate enchantment; **CL** 10th\
**Slot** none; **Price** 1,500 gp; **Weight** 2 lbs.

A regression mine is a nondescript plate of metal that can be armed to deliver a terrible,
mind-affecting curse. Arming the mine requires a move action, and deploying it in an adjacent square
requires a standard action. An armed regression mine must be deployed within 3 rounds; otherwise, it
must be rearmed before it can be deployed.

Once it has been deployed, a regression mine triggers when any creature enters its space. The
triggered mine emits an invisible magical field in a 20-foot-radius [burst](ref/misc/burst) centered
on itself, which lasts for 1 minute before dissipating. Creatures in this field when the mine
activates or that enter it while it remains active are [confused](ref/misc/confused) and take a -4
penalty to their Intelligence scores as long as they remain in the field and for 1 minute
thereafter. When a creature with the confused condition from this effect determines its action, it
must reroll any result that isn't "attack nearest creature" and take the second result.

A creature in the field of a regression mine can avoid its effects with a successful DC 15 saving
throw, but it must continue attempting saving throws at the same DC each round it remains within the
regression mine's field.

A regression mine is a single-use item; once triggered, the mine is inert and nonmagical. An armed
regression mine in the area of another regression mine's active field automatically triggers;
therefore, a string of carefully placed mines can be activated in quick succession when only one of
them is triggered. An armed or active regression mine can be disabled with a successful DC 30
Disable Device check. Failing the check to disable an armed regression mine by more than 5
immediately triggers it. If an active mine is disabled, its magical field immediately collapses. A
regression mine is inherently unstable; a creature that takes damage while carrying an armed
regression mine must succeed at a DC 15 Reflex saving throw, or the mine immediately activates.

### Construction

**Requirements** [Craft Wondrous Item](ref/feat/craft-wondrous-item),
[confusion](ref/spell/confusion); **Cost** 750 gp
