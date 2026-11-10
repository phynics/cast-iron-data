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
replaces = ["Gunslinger's dodge deed", "Gunslinger initiative", "Nimble +1"]
+++

Prepared to reload or repair her lord's firearms at a moment's notice, the gunner squire is an
indispensable aid for knights skilled in the use of pistols and rifles.

**Deeds**

**Info:** A gunner squire swaps a pair of deeds for the following.

**Spotter (Ex)**

**Gained:** At 1st Level

**Replaces:** Gunslinger's dodge deed

**Special:** The gunner squire must be adjacent to her liege and able to communicate to use this
deed, though a knight may move away from the gunner squire during his turn and still gain the
benefits of this deed.

**Standard:** A gunner squire can spend 1 grit point to pinpoint a target within her line of sight
and inform her knightly liege of the target's exact location. During the knight's next turn, if he
makes a ranged attack against the pinpointed target and would take a penalty on his attack roll due
to range, he may reduce this penalty by an amount equal to his gunner squire's Wisdom modifier (to a
minimum penalty of 0).

**Side Arm (Ex)**

**Fullround:** A gunner squire can spend 1 grit point to reload a one-handed or two-handed firearm
she is holding. If the firearm has multiple barrels, she can reload a number of barrels per round
equal to her Dexterity modifier (minimum 1). A gunner squire equipped with alchemical cartridges can
use this deed to reload multiple firearms at once, dividing the number of barrels she's able to
reload among the firearms she is carrying however she wishes, even if this would mean stowing and
retrieving multiple firearms from her equipment with one action. Abilities, deeds, and feats that
decrease reloading time (such as [Rapid Reload](ref/feat/rapid-reload)) do not improve this deed.

**Gained:** At 3rd Level

**Replaces:** Gunslinger initiative

**Safe Handling (Ex)**

**Fullround:** A gunner squire can temporarily ensure the safety of a firearm she is holding,
reducing its misfire chance by 1 (to a minimum of 0) on the next attack roll made with that firearm.
This reduction does not stack with itself. This reduction occurs after any increases are calculated
for firing with the [broken](ref/misc/broken) condition, or for any other effect that might increase
the misfire value of a firearm.

**Gained:** At 2nd Level

**Replaces:** Nimble +1
