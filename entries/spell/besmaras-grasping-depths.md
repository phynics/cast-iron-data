+++
id = "ref/spell/besmaras-grasping-depths"
kind = "spell"
title = "Besmara's Grasping Depths"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "besmaras_grasping_depths", path = "json/spells12.json" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "26"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "haunted", "mind-affecting"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a vial of sea water)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one 5-ft. cube/level (S)" },
]
duration = "see text"
saving_throw = "Will partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Spiritualist\
6: Cleric, Inquisitor, Oracle, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a vial of sea water)
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: Will partial; see text
Spell resistance: yes
Area: one 5-ft. cube/level (S)
Descriptors: emotion, fear, haunted, mind-affecting
:::

You call upon the restless souls of those who died at sea. This spell can be cast only on an area of
deep water. When a creature enters the area, the haunt manifests, automatically grabbing the
creature and dragging it under the water on initiative count 10. Each round, the haunt deals 1d6
points of nonlethal damage as it drags its victim down 10 feet; a successful DC 15 Swim check
reduces the descent to 5 feet and negates the nonlethal damage. Each round in the haunt's clutches
reduces the duration the victim can [hold her breath](ref/misc/hold-your-breath) by 2 rounds. A
victim can make a single move or standard action each round while in the haunt's grasp if she
succeeds at a Will save; on a failed save, she can only struggle helplessly against the haunt. A
victim cannot use her actions to swim toward the surface while the haunt is active. If the haunt
reaches the bottom of its body of water, it pounds its victim against the bottom, dealing 2d6 points
of nonlethal damage per round to the victim and reducing the duration the victim can hold her breath
by an additional round. This continues until either the haunt is neutralized (in which case the
victim must still swim to the surface) or the victim drowns.

The haunt can grab and attempt to drown multiple creatures in its area on its initiative count. The
magic holding the haunt together is unstable and deteriorates while the haunt is active. Each round
at the end of its turn, the haunt automatically loses 1d6 hit points per creature it is currently
affecting. Furthermore, the spell's haunt-like manifestation is active throughout the spell's
duration, rendering it vulnerable to effects that damage haunts. When the haunt reaches 0 hit
points, the spell ends.

#### Haunt Statistics

**Notice:** Perception DC 30 (To detect the smell of brine)

**Hit points:** 5 hp/level

**Trigger:** proximity

**Reset:** none
