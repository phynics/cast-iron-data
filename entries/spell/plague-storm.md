+++
id = "ref/spell/plague-storm"
kind = "spell"
title = "Plague Storm"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plague_storm", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "231"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 minute/level and instantaneous (see text)"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Cleric, Druid, Hunter, Oracle, Warpriest, Witch\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level and instantaneous (see text)
Saving throw: Fortitude negates
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Descriptors: disease, evil
:::

You create a hideous gray cloud, similar to fog cloud, that occasionally crackles with foul-smelling
bolts of sickly green lightning. Creatures in the area must save or contract one of the following
diseases: blinding sickness, bubonic plague, cackle fever, demon fever, devil chills, filth fever,
leprosy, mindfire, red ache, shakes, or slimy doom (the disease is chosen by you when you cast the
spell and applies to all creatures that fail the save). The disease is contracted immediately (the
onset period does not apply) and is an instantaneous effect. Use the disease's listed frequency to
determine further effects, but the disease's save DC increases by +2. For more information see the
diseases section.

Unlike a fog cloud, the plague storm moves away from you at 10 feet per round, rolling along the
surface of the ground.

Figure out the cloud's new spread each round based on its new point of origin, which is 10 feet
farther away from the point of origin where you cast the spell.

Because the vapors are heavier than air, they sink to the lowest level of the terrain, even pouring
down den or sinkhole openings. The cloud cannot penetrate liquids, nor can it be cast underwater.
