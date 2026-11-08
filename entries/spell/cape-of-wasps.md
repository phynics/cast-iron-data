+++
id = "ref/spell/cape-of-wasps"
kind = "spell"
title = "Cape of Wasps"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cape_of_wasps", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Summoning
:::

**Sources:** Ultimate Magic pg 210

You summon a wasp swarm, which fills your space (up to 5 feet by 5 feet) but does not attack you.
The dense cloud of vermin gives you partial [concealment](ref/rule/concealment) against ranged
attacks. Any creature that makes a successful melee attack against you takes 2d6 points of swarm
damage and poison from the wasp swarm, but is not affected by the swarm's distraction ability. As a
free action on your turn, you may have the swarm cling to you tightly, giving you a fly speed of 20
feet (poor maneuverability); when using the swarm to fly, it does not provide concealment or harm
creatures that strike you. You can return the swarm to its protective shape as a free action on your
turn.
