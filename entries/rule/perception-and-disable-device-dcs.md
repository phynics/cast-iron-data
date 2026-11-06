+++
id = "ref/rule/perception-and-disable-device-dcs"
kind = "rule"
title = "Perception and Disable Device DCs"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "perception_and_disable_device_dcs", path = "json/rules_gm08.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 417

The builder sets the Perception and Disable Device DCs for a mechanical trap. For a magic trap, the
values depend on the highest-level spell used.

**Mechanical Trap:** The base DC for both Perception and Disable Device checks is 20. Raising or
lowering either of these DCs affects the CR ([Table 13-3](ref/rule/mechanical-trap-cost)).

**Magic Trap:** The DC for both Perception and Disable Device checks is equal to 25 + the spell
level of the highest-level spell used. Only characters with the trapfinding class feature can
attempt a Disable Device check involving a magic trap.
