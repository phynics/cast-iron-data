+++
id = "ref/rule/poisons"
kind = "rule"
title = "Poisons"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poisons", path = "json/rules_adv_gm01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 139

The poison track simulates the progressive effects of poison in the body. A character who is
poisoned rolls a saving throw after the listed onset at the listed frequency. On an initial exposure
to poison, regardless of whether her save succeeds, a victim takes an amount of poison damage equal
to the poison's DC - 10, divided by 2 (for example, 5 points of poison damage for a DC 20 poison).
This is hit point damage, not ability damage. If a victim is exposed to additional doses of the same
poison, a failed save progresses the poison track by one step and increases the duration by 50%, but
doesn't increase the DC.
