+++
id = "ref/rule/rc-energy-overload"
kind = "rule"
title = "Energy Overload"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rc_energy_overload", path = "json/rules_opt_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 183\
A sudden surge of energy builds up within your item, threatening to damage or destroy it.

### Tasks

**Channel into Your Body** Fortitude DC 20 + item's caster level

**Divert to Another Item** Craft (item's type) DC 20 + item's caster level

### Results

**Critical Success** Overload leveraged. -2 days, -10% cost, 1 perk.

**Success** Overload diverted. 1 quirk.

**Failure** Expensive damage. +7 days, +15% cost.

**Critical Failure** Eldritch explosion. Item destroyed. Creators take 1d6 points of damage per
caster level of the item.
