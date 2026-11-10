+++
id = "ref/arc-druid/plains-druid"
kind = "archetype"
title = "Plains Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plains_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "100"

[fields]
kind = "archetype"
replaces = ["Woodland stride", "Trackless step", "Resist nature's lure", "Venom immunity", "A thousand faces"]
alters = ["Wild shape"]
+++

Out upon the wide and rolling prairies and savannahs, plains druids stand guard over the grasslands.
These druids range far and wide, watching over nomadic tribes and wandering herds and preserving the
sometimes fragile ecosystem of the wide open spaces.

**Plains Traveler (Ex)**

**Gained:** At 2nd Level

**Passive:** A plains druid gains a bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks equal to [half](ref/misc/fractions-and-rounding) her druid
level in plains terrain, and she cannot be tracked in such an environment.

**Replaces:** Woodland stride

**Run Like the Wind (Ex)**

**Ability:** Once per hour, she may [run](ref/rule/run) or [charge](ref/rule/charge) at double the
normal speed for 1 round.

**Gained:** At 3rd Level

**Passive:** A plains druid gains +10 feet to her land speed when wearing light or no armor and
carrying a light load.

**Replaces:** Trackless step

**Special:** If riding her animal companion, it gains this ability instead.

**Savanna Ambush (Ex)**

**Immediate:** A plains druid can stand up from prone during a surprise round.

**Gained:** At 4th Level

**Passive:** A plains druid gains [concealment](ref/rule/concealment) whenever she is
[prone](ref/rule/prone) in natural surroundings, and can make Stealth checks at no penalty when
prone and not moving or at -5 when crawling.

**Replaces:** Resist nature's lure

**Wild Shape (Su)**

**Ability:** A plains druid gains _wild shape,_ except that her effective druid level for this
ability is equal to her druid level - 2.

**Alters:** Wild shape

**Gained:** At 6th Level

**Canny Charger (Ex)**

**Ability:** A plains druid can charge through allies' squares without difficulty (whether mounted
or afoot) and can turn up to 90 degrees once during a charge, provided the last 10 feet toward the
target are in a straight line.

**Gained:** At 9th Level

**Passive:** She also gains a +4 dodge bonus to AC against enemy charge attacks and a +4 bonus to
damage with a [readied action](ref/rule/ready) against a charging foe.

**Replaces:** Venom immunity

**Evasion (Ex)**

**Gained:** At 13th Level

**Passive:** A plains druid gains [evasion](ref/ability/evasion) when wearing light or no armor and
carrying a light load. This functions as the [rogue](ref/class/rogue) ability of the same name.

**Replaces:** A thousand faces
