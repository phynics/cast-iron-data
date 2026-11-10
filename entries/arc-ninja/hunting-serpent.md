+++
id = "ref/arc-ninja/hunting-serpent"
kind = "archetype"
title = "Hunting Serpent"
aon = "ArchetypeDisplay.aspx?FixedName=Ninja%20Hunting%20Serpent"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunting_serpent", path = "json/archetypes_ninja.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ninja" },
]
[[sources]]
publication = "villain-codex"
page = "104"

[fields]
kind = "archetype"
replaces = ["No trace", "Uncanny dodge", "improved uncanny dodge", "ninja tricks gained at 12th and 16th levels", "Ninja trick gained at 10th level"]
replaces_features = ["no-trace", "uncanny-dodge", "improved-uncanny-dodge"]
+++

The order dispatches specially trained killers to hunt relentlessly and fight from the shadows.

**Gained class skills:** sur

**Lost class skills:** kno

**Relentless Pursuit (Ex)**

**Gained:** At 3rd Level

**Passive:** A hunting serpent gains a bonus on Diplomacy checks to gather information and on
Survival checks to identify or follow tracks. The bonus is equal to
[one-third](ref/misc/fractions-and-rounding) of her ninja level.

**Replaces:** No trace

**Death Mark (Ex)**

**Gained:** At 4th Level

**Replaces:** Uncanny dodge, improved uncanny dodge, ninja tricks gained at 12th and 16th levels

**Special:** The effects of _death mark_ last for 24 hours, until the marked creature is slain, or
until the hunting serpent chooses to mark another creature, whichever comes first.

**Swift:** Once per day, a hunting serpent can mark an opponent damaged by her sneak attack for
death. A hunting serpent gains a +1 competence bonus on attack and damage rolls against an opponent
affected by _death mark_ as well as on Survival checks to track the marked creature.

**Certain Demise (Ex)**

**Ability:** The hunting serpent's sneak attack damage applies on the first attack she makes each
round against the target of her _death mark_ ability, even if it normally wouldn't.

**Gained:** At 10th Level

**Replaces:** Ninja trick gained at 10th level

**Special:** Other effects that trigger on a sneak attack do not apply with this ability.
