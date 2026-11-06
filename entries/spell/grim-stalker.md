+++
id = "ref/spell/grim-stalker"
kind = "spell"
title = "Grim Stalker"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grim_stalker", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "haunted", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 minute"
components = "V, S, M/DF (a hound's fang)"
range = "touch"
effects = [
  { label = "Target", value = "one object touched" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates (object); see text"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Magus, Summoner, Unchained Summoner\
7: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S, M/DF (a hound's fang)
Range: touch
Duration: 1 day/level (D)
Saving throw: Will negates (object); see text
Spell resistance: yes (object)
Target: one object touched
Descriptors: emotion, fear, haunted, mind-affecting
:::

**Sources:** Haunted Heroes Handbook pg 27

You bind spirits of ill fate to an object, focusing their wrath onto the next creature that touches
the object. When a creature touches the target object, it can attempt a Will save to negate the
spell's effect. Although a successful save prevents the creature from becoming haunted, the haunt
still resides within the object, and targets either the next creature to touch the object or the
same creature again if it still holds the object after 24 hours. The haunt remains within the object
until a creature fails its save or the spell's duration ends.

Once a creature is affected by the haunt, it begins noticing a large, black mastiff with ominous
green eyes watching and following it from a distance, always just beyond the range of focus or
interaction. The grim stalker terrorizes the creature's sleep, affecting it as per nightmare every
night during the spell's duration (Will negates for one night). Each time the creature takes hit
point damage, the grim stalker lunges closer, causing the creature to become shaken for 1 round
(Will negates). Each time the creature is reduced to less than one-tenth of its maximum hit points,
the grim stalker lunges at the creature as an immediate action, affecting it as per phantasmal
killer.

Each time the grim stalker lunges at the affected creature, the spell's haunt-like manifestation
occurs during that round. Alternatively, a haunted creature can attempt to force the grim stalker to
manifest using a simple ritual that requires a successful Knowledge (arcana), Knowledge (religion),
or Spellcraft check; occult reagents costing 450 gp (which are consumed as part of the ritual); and
a full-round action. The DC for this check equals the spell's save DC. Successfully performing the
ritual causes the grim stalker to manifest as a Nessian warhound in an available square 20 feet away
from the victim, save that its only subtype is extraplanar, its alignment is neutral, its bite and
breath weapon deal negative energy damage instead of fire damage, and it has negative energy
affinity instead of fire immunity and vulnerability to cold. The grim stalker immediately attacks
the affected creature, persisting until either it or the creature is slain, at which point the spell
effect (and the warhound) disappears.

#### Haunt Statistics

**Notice:** Perception DC 30 (to see a black dog darting toward the target out of the corner of the
eye)

**Hit points:** 4 hp/level

**Trigger:** touch (object)

**Reset:** none
