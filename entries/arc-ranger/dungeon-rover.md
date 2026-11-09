+++
id = "ref/arc-ranger/dungeon-rover"
kind = "archetype"
title = "Dungeon Rover"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dungeon_rover", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "22"

[fields]
kind = "archetype"
replaces = ["Track", "Wild empathy", "Woodland stride", "Swift tracker"]
alters = ["Hunter's bond"]
+++

These rangers specialize in surviving hostile subterranean environs. They are well equipped to avoid
traps, spot secret passages, and deal with inimical dungeon tenants.

**Gained class skills:** dd, ke

**Lost class skills:** ride

**Stone Scouting (Ex)**

**Passive:** A dungeon rover gains a +2 bonus on Perception checks to notice underground
environmental hazards, including traps, potential cave-ins, and dangerous flora. A dungeon rover
receives a check to notice these hazards whenever he passes within 10 feet of them, whether or not
he is actively looking.

**Replaces:** Track

**Vermin Affinity (Ex)**

**Ability:** A dungeon rover gains the ability to improve the attitude of mindless subterranean
creatures. This ability functions as the [wild empathy](ref/ability/wild-empathy) class feature,
except a dungeon rover can influence any vermin (even those without Intelligence scores) instead of
animals. Additionally, a dungeon rover can influence oozes with a -4 penalty on his vermin affinity
check.

**Replaces:** Wild empathy

**Dungeon Ally (Ex)**

**Ability:** A dungeon rover may select a [giant slug](ref/companion/slug-giant), a
[giant centipede](ref/companion/centipede-giant), a [goblin dog](ref/companion/goblin-dog), a
[giant scorpion](ref/companion/scorpion-giant), or any poisonous snake
([reef snake](ref/companion/reef-snake), [riding python](ref/companion/riding-python),
[spitting cobra](ref/companion/spitting-cobra), or [viper](ref/companion/snake-viper)) as his
[animal companion](ref/sidekick/animal-companion), in addition to the usual animal companion options
available to rangers with the _hunter's bond_ class feature.

**Alters:** Hunter's bond

**Gained:** At 4th Level

**Subterranean Stride (Ex)**

**Gained:** At 7th Level

**Passive:** A dungeon rover is never slowed by [difficult terrain](ref/rule/terrain-and-obstacles)
while underground. However, areas that are enchanted or magically manipulated to impede motion still
affect him.

**Replaces:** Woodland stride

**Improved Stone Scouting (Ex)**

**Gained:** At 8th Level

**Passive:** A dungeon rover's bonus on Perception checks to notice underground environmental
hazards increases to +4. Additionally, the rover receives a check to notice these irregularities
whenever he passes within 15 feet of them.

**Replaces:** Swift tracker
