+++
id = "ref/arc-alchemist/ice-chemist"
kind = "archetype"
title = "Ice Chemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Ice%20Chemist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ice_chemist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "35"

[fields]
kind = "archetype"
features = [
  { anchor = "icy-bombs" },
  { anchor = "cold-sweat", level = 2 },
  { anchor = "frost-bomb", level = 2 },
]
trades = [
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["cold-sweat"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [10], by = ["cold-sweat"] },
  { replaces = "Discovery that the alchemist normally gains at 2nd level", feature = "discovery", levels = [2], by = ["frost-bomb"] },
  { alters = "Bombs", feature = "bomb", by = ["icy-bombs"] },
]
+++

Reclusive alchemists who dwell in the highest mountains or on the frozen tundra devote their skills
to mastering the cold.

## Icy Bombs (Su) {#icy-bombs}

An ice chemist's bombs deal cold damage instead of fire damage.

In place of an alchemist discovery, she can learn to create bombs that deal fire damage like normal
alchemist bombs do, though she can't apply discoveries that modify bombs to such fire bombs that she
creates. An ice alchemist's icy bombs can still be poisonous or create thick vapors similar to
smoke, but she cannot apply the [explosive](ref/discovery/explosive-bomb) or
[inferno bomb](ref/discovery/inferno-bomb) discoveries to them.

This alters the bomb class feature.

## Cold Sweat (Su) {#cold-sweat}

At 2nd level, an ice chemist channels her affinity for cold energy into her personal space, keeping
herself and her gear cool. She gains cold [resistance](ref/umr/resistance) equal to her alchemist
level and can survive comfortably in temperatures as low as -50º Fahrenheit.

This replaces poison resistance and poison immunity.

## Frost Bomb (Su) {#frost-bomb}

At 2nd level, an ice chemist gains the [frost bomb](ref/discovery/frost-bomb) discovery.

This replaces the discovery that the alchemist normally gains at 2nd level.
