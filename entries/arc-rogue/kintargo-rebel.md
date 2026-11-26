+++
id = "ref/arc-rogue/kintargo-rebel"
kind = "archetype"
title = "Kintargo Rebel"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Kintargo%20Rebel"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kintargo_rebel", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "inner-sea-combat"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "sophisticated-stealth", level = 3 },
  { anchor = "misdirection", level = 4 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["sophisticated-stealth"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["misdirection"] },
]
+++

With few natural barriers, a thriving international port, and many miles separating it from Egorian,
Kintargo is geographically suited for rebellion against the rigid laws that reign in Cheliax. This
rebellion is hardly malicious in intent; business is simply easier without the imposing bureaucracy.
Whenever the Chelish navy sails into the port, these rebels are quick to appear agreeably
subservient in order to conceal their noncompliance and avoid retribution.

## Sophisticated Stealth (Ex) {#sophisticated-stealth}

At 3rd level, a Kintargo rebel gains a +1 bonus on Knowledge (nobility) checks. In addition, she
gains a +1 bonus on Bluff checks to convey a secret message and on Sense Motive checks to discern
secret messages. These bonuses increase by 1 every 3 rogue levels thereafter. This ability replaces
trap sense.

## Misdirection (Sp) {#misdirection}

At 4th level, a Kintargo rebel gains the ability to cast _[misdirection](ref/spell/misdirection)_ on
herself once per day, though instead of choosing an object for the second target, she must choose a
creature in range. The caster level for this ability is equal to her class level, and the save DC
for this spell is 12 + the Kintargo rebel's Intelligence modifier. The save DC of this ability
increases by 1 if the secondary target is lawful or evil. This ability replaces uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the Kintargo rebel archetype: canny observer, charmer, false
friend, fast getaway, honeyed words, obfuscate story, and quick disguise.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the Kintargo rebel archetype: hard to fool, master
of disguise, skill mastery, slippery mind, and thoughtful reexamining.
