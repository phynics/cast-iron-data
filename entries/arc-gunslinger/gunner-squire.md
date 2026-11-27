+++
id = "ref/arc-gunslinger/gunner-squire"
kind = "archetype"
title = "Gunner Squire"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Gunner%20Squire"
source_ids = ["knights-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gunner_squire", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "knights-of-the-inner-sea"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "spotter", level = 1 },
  { anchor = "side-arm", level = 3 },
  { anchor = "safe-handling", level = 2 },
]
trades = [
  { replaces = "Gunslinger's dodge deed", feature = "deeds", power = "gunslinger's dodge", by = ["spotter"] },
  { replaces = "Gunslinger initiative", feature = "deeds", power = "gunslinger initiative", by = ["side-arm"] },
  { replaces = "Nimble +1", feature = "nimble", levels = [2], by = ["safe-handling"] },
]
+++

Prepared to reload or repair her lord's firearms at a moment's notice, the gunner squire is an
indispensable aid for knights skilled in the use of pistols and rifles.

## Deeds {#deeds}

A gunner squire swaps a pair of deeds for the following two deeds. The new deed descriptions include
information on which deeds from the gunslinger class feature these new deeds replace.

## Spotter (Ex) {#spotter}

At 1st level, as a standard action, a gunner squire can spend 1 grit point to pinpoint a target
within her line of sight and inform her knightly liege of the target's exact location. During the
knight's next turn, if he makes a ranged attack against the pinpointed target and would take a
penalty on his attack roll due to range, he may reduce this penalty by an amount equal to his gunner
squire's Wisdom modifier (to a minimum penalty of 0). The gunner squire must be adjacent to her
liege and able to communicate to use this deed, though a knight may move away from the gunner squire
during his turn and still gain the benefits of this deed. This deed replaces the gunslinger's dodge
deed.

## Side Arm (Ex) {#side-arm}

At 3rd level, as a full-round action, a gunner squire can spend 1 grit point to reload a one-handed
or two-handed firearm she is holding. If the firearm has multiple barrels, she can reload a number
of barrels per round equal to her Dexterity modifier (minimum 1). A gunner squire equipped with
alchemical cartridges (see _Ultimate Equipment_) can use this deed to reload multiple firearms at
once, dividing the number of barrels she's able to reload among the firearms she is carrying however
she wishes, even if this would mean stowing and retrieving multiple firearms from her equipment with
one action. Abilities, deeds, and feats that decrease reloading time (such as
[Rapid Reload](ref/feat/rapid-reload)) do not improve this deed. This deed replaces gunslinger
initiative.

## Safe Handling (Ex) {#safe-handling}

At 2nd level, as a full-round action, a gunner squire can temporarily ensure the safety of a firearm
she is holding, reducing its misfire chance by 1 (to a minimum of 0) on the next attack roll made
with that firearm. This reduction does not stack with itself. This reduction occurs after any
increases are calculated for firing with the [broken](ref/misc/broken) condition, or for any other
effect that might increase the misfire value of a firearm. This ability replaces nimble +1.
