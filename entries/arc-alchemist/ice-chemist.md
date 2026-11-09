+++
id = "ref/arc-alchemist/ice-chemist"
kind = "archetype"
title = "Ice Chemist"
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
replaces = ["Poison resistance", "poison immunity", "2nd-level discovery"]
alters = ["Bombs"]
+++

Reclusive alchemists who dwell in the highest mountains or on the frozen tundra devote their skills
to mastering the cold.

**Icy Bombs (Su)**

**Ability:** An ice chemist's bombs deal cold damage instead of fire damage. In place of an
alchemist discovery, she can learn to create bombs that deal fire damage like normal alchemist bombs
do, though she can't apply discoveries that modify bombs to such fire bombs that she creates. An ice
alchemist's icy bombs can still be poisonous or create thick vapors similar to smoke, but she cannot
apply the [explosive](ref/discovery/explosive-bomb) or [inferno bomb](ref/discovery/inferno-bomb)
discoveries to them.

**Alters:** Bombs

**Gained:** At 1st Level

**Cold Sweat (Su)**

**Flavor:** An ice chemist channels her affinity for cold energy into her personal space, keeping
herself and her gear cool.

**Gained:** At 2nd Level

**Passive:** She gains cold [resistance](ref/umr/resistance) equal to her alchemist level and can
survive comfortably in temperatures as low as -50&deg& Fahrenheit.

**Replaces:** Poison resistance, poison immunity

**Frost Bomb (Su)**

**Ability:** An ice chemist gains the [frost bomb](ref/discovery/frost-bomb) discovery.

**Gained:** At 2nd Level

**Replaces:** 2nd-level discovery
