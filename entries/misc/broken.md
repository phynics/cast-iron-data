+++
id = "ref/misc/broken"
kind = "rule"
title = "Broken"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "broken", path = "json/misc.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "149"

[fields]
kind = "none"
+++

Some weapons have special features in addition to those noted in their descriptions.

**Broken:** Items that have taken damage in excess of half their total hit points gain the
[broken condition](ref/rule/broken-and-fragile), meaning they are less effective at their designated
task. Attacks made with a broken weapon suffer a -2 penalty on attack and damage rolls. Such weapons
only score a critical hit on a natural 20 and only deal ×2 damage on a confirmed critical hit. Both
firearms and [fragile](ref/misc/fragile) weapons include effects that grant a weapon the broken
condition without the weapon explicitly taking damage.

If a weapon gains the broken condition from an effect, that weapon is considered to have taken
damage equal to half its hit points +1. This damage is repaired either by something that addresses
the effect that granted the weapon the broken condition (like quick clear in the case of firearm
misfires or the [Field Repair](ref/feat/field-repair) feat in the case of weapons with the fragile
quality) or by the normal method for recovering item hit points (detailed in the broken condition
description). When an effect that grants the broken condition is removed, the weapon regains the hit
points it lost when the broken condition was applied.

Damage done by an attack against a weapon cannot be repaired by an effect that removes the broken
condition.
