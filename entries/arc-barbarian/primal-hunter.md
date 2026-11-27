+++
id = "ref/arc-barbarian/primal-hunter"
kind = "archetype"
title = "Primal Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Primal%20Hunter"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primal_hunter", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "exceptional-pull", level = 1 },
  { anchor = "focused-rage", level = 1 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["exceptional-pull"] },
  { alters = "Rage", feature = "rage", by = ["focused-rage"] },
]
+++

Rather than exploding with anger, primal hunters focus their rage to strike distant targets. Though
able to hold their own in melee, primal hunters specialize in using some of the oldest of ranged
weapons: bows, slings, and spears.

## Exceptional Pull {#exceptional-pull}

At 1st level, a primal hunter gains [Exceptional Pull](ref/feat/exceptional-pull) (see previous
page) as a bonus feat, even if she doesn't meet the requirements. At 11th and 20th levels, the
strength rating of weapons she wields increases by 1 (weapons without a strength rating are not
affected). This ability replaces fast movement.

## Focused Rage (Ex) {#focused-rage}

While raging, a primal hunter gains a +2 bonus on attack rolls with ranged weapons. This bonus
increases to +3 at 11th level and to +4 at 20th level. While raging, a primal hunter can attempt
Stealth checks but doesn't gain a morale bonus on Will saves. This ability alters rage.

## Rage Powers {#rage-powers}

The following rage powers complement the primal hunter archetype:
[deadly accuracy](ref/ragepower/deadly-accuracy), [lethal accuracy](ref/ragepower/lethal-accuracy),
[reflexive dodge](ref/ragepower/reflexive-dodge), [rolling dodge](ref/ragepower/rolling-dodge),
[sharpened accuracy](ref/ragepower/sharpened-accuracy),
[surprise accuracy](ref/ragepower/surprise-accuracy).
