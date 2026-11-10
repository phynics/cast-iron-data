+++
id = "ref/arc-druid/river-druid"
kind = "archetype"
title = "River Druid"
source_ids = ["ultimate-wilderness", "people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "river_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "48"
[[sources]]
publication = "people-of-the-river"
page = "14"

[fields]
kind = "archetype"
replaces = ["Nature sense", "Woodland stride", "Trackless step", "Resist nature's lure", "Timeless body"]
alters = ["Class skills", "Wild shape"]
replaces_features = ["nature-sense", "woodland-stride", "trackless-step", "resist-nature-s-lure", "timeless-body"]
alters_features = ["wild-shape"]
+++

These druids are the guardians of rivers and the creatures that depend on them. Just as rivers pour
from mountains to seas, river druids adapt to many environments and cultures. They can be found
wherever water flows, even among underground rivers or sewer systems.

**Ferrier (Ex)**

**Alters:** Class skills

**Info:** A river druid adds [Diplomacy](ref/skill/diplomacy) (CHA) to her list of class skills and
gains a +2 bonus on Diplomacy and Knowledge (nature) skill checks.

**Replaces:** Nature sense

**Read the Currents (Ex)**

**Gained:** At 2nd Level

**Passive:** A river druid gains a bonus equal to [half](ref/misc/fractions-and-rounding) her druid
level on initiative checks and Acrobatics, Knowledge (geography), Perception, Stealth, Survival, and
Swim checks when she is in, on, or adjacent to flowing water.

**Replaces:** Woodland stride

**Countercurrent (Ex)**

**Gained:** At 3rd Level

**Passive:** A river druid takes no penalty to speed or on Acrobatics or Stealth checks in shallow
water up to 2 feet deep (1 foot deep for Small characters) such as shallow bogs, shorelines,
streams, and partially flooded areas. A river druid (and any vehicle she pilots) isn't moved by
flowing water unless she allows it. Water that has been magically manipulated to impede or boost
motion still affects her.

**Replaces:** Trackless step

**Deep Breath (Ex)**

**Ability:** A river druid can [hold her breath](ref/misc/hold-your-breath) for a number of minutes
equal to her Constitution score (after this, she must begin attempting Constitution checks to avoid
suffocation as normal).

**Gained:** At 4th Level

**Replaces:** Resist nature's lure

**Wild Shape (Su)**

**Ability:** A river druid gains _wild shape,_ except her effective druid level for the ability is
equal to her druid level - 2.

**Alters:** Wild shape

**Gained:** At 6th Level

**Tongue of the Sun and Moon (Ex)**

**Gained:** At 15th Level

**Passive:** A river druid can speak with any living creature.

**Replaces:** Timeless body
