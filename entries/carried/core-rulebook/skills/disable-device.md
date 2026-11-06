+++
id = "ref/carried/core-rulebook/skills/disable-device"
kind = "skill"
title = "Disable Device"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Disable Device", path = "core_rulebook/skill/disable_device.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Dex
Trained Only: Yes
Armor Check Penalty: Yes
:::

_You are skilled at disarming traps and opening locks. In addition, this skill lets you sabotage
simple mechanical devices, such as catapults, wagon wheels, and doors._

## Check {#check}

When disarming a trap or other device, the Disable Device check is made secretly, so that you don't
necessarily know whether you've succeeded.

The DC depends on how tricky the device is. If the check succeeds, you disable the device. If it
fails by 4 or less, you have failed but can try again. If you fail by 5 or more, something goes
wrong. If the device is a trap, you trigger it. If you're attempting some sort of sabotage, you
think the device is disabled, but it still works normally.

You also can rig simple devices such as saddles or wagon wheels to work normally for a while and
then fail or fall off some time later (usually after 1d4 rounds or minutes of use).

::: table
head = [
  [
    { text = "Device", header = true },
    { text = "Time", header = true },
    { text = "Disable Device DC\\*", header = true },
    { text = "Example", header = true },
  ],
]
body = [
  [
    { text = "Simple" },
    { text = "1 round" },
    { text = "10" },
    { text = "Jam a lock" },
  ],
  [
    { text = "Tricky" },
    { text = "1d4 rounds" },
    { text = "15" },
    { text = "Sabotage a wagon wheel" },
  ],
  [
    { text = "Difficult" },
    { text = "2d4 rounds" },
    { text = "20" },
    { text = "Disarm a trap, reset a trap" },
  ],
  [
    { text = "Extreme" },
    { text = "2d4 rounds" },
    { text = "25" },
    { text = "Disarm a complex trap, cleverly sabotage a clockwork device" },
  ],
]
foot = [
  [
    { text = "\\* If you attempt to leave behind no trace of your tampering, add 5 to the DC.", colspan = 4 },
  ],
]
:::

|Lock Quality|Disable Device DC|
| --- | --- |
|Simple|20|
|Average|25|
|Good|30|
|Superior|40|

### Open Locks {#open-locks}

The DC for opening a lock depends on its quality. If you do not have a set of thieves' tools, these
DCs increase by 10.

## Action {#action}

The amount of time needed to make a Disable Device check depends on the task, as noted above.
Disabling a simple device takes 1 round and is a full-round action. A tricky or difficult device
requires 1d4 or 2d4 rounds. Attempting to open a lock is a full-round action.

## Try Again {#try-again}

Varies. You can retry checks made to disable traps if you miss the check by 4 or less. You can retry
checks made to open locks.

## Special {#special}

If you have the Deft Hands feat, you get a bonus on Disable Device checks (see Feats).

A rogue who beats a trap's DC by 10 or more can study the trap, figure out how it works, and bypass
it without disarming it. A rogue can rig a trap so her allies can bypass it as well.

## Restriction {#restriction}

Characters with the trapfinding ability (like rogues) can disarm magic traps. A magic trap generally
has a DC of 25 + the level of the spell used to create it.

The spells _[fire trap](ref/spell/fire-trap)_, _[glyph of warding](ref/spell/glyph-of-warding)_,
_symbol_, and _[teleportation circle](ref/spell/teleportation-circle)_ also create traps that a
rogue can disarm with a successful Disable Device check. _[Spike growth](ref/spell/spike-growth)_
and _[spike stones](ref/spell/spike-stones)_, however, create magic hazards against which Disable
Device checks do not succeed. See the individual spell descriptions for details.
