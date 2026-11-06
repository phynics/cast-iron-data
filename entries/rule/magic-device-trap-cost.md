+++
id = "ref/rule/magic-device-trap-cost"
kind = "rule"
title = "Spell and Magic Device Trap CR and Cost"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_device_trap_cost", path = "json/rules_gm08.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 423

To determine the CR of magic traps, decide what elements you want and then determine the CR of the
resulting trap (see Table 13-4). If a player character wants to design and construct a magic trap,
he, or an ally, must have the [Craft Wondrous Item](ref/feat/craft-wondrous-item) feat. In addition,
he must be able to cast the spell or spells that the trap requires - or he must be able to hire an
NPC to cast the spells for him.

### Table 13-4: CR Modifiers for Magic Traps

|Feature|CR Modifier|
| --- | --- |
|Highest-level spell effect|+Spell level|
|Damaging spell effect|+1 per 10 points of average damage|

### Spell Trap Cost

A spell trap has a cost only if the builder must [hire an NPC spellcaster](ref/eq-misc/spellcasting)
to cast it.

### Magic Device Trap Cost

Building a magic device trap involves the expenditure of gp and requires the services of a
spellcaster. Table 13-5 summarizes the cost information for magic device traps. If the trap uses
more than one spell (for instance, a sound or visual trigger spell in addition to the main spell
effect), the builder must pay for them all (except [alarm](ref/spell/alarm), which is free unless it
must be cast by an NPC).

The costs derived from Table 13-5 assume that the builder is casting the necessary spells himself
(or perhaps some other PC is providing the spells for free). If an NPC spellcaster must be hired to
cast them, those costs must be factored in as well.

A magic device trap takes 1 day to construct per 500 gp of its cost.

### Table 13-5: Cost Modifiers for Magic Device Traps

|Feature|Cost Modifier|
| --- | --- |
|Alarm spell used in trigger|-|
|One-Shot Trap: Each spell used|+50 gp × caster level × spell level|
|One-Shot Trap: Material components|+ material component costs|
|Automatic Reset Trap: Each spell used|+500 gp × caster level × spell level|
|Automatic Reset Trap: Material components|+material component costs × 100|
