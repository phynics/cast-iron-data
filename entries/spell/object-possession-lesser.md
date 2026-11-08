+++
id = "ref/spell/object-possession-lesser"
kind = "spell"
title = "Lesser Object Possession"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "object_possession_lesser", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/possession" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "unattended Tiny or Small object" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium, Occultist\
3: Mesmerist, Psychic, Spiritualist\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Target: unattended Tiny or Small object
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
:::

**Sources:** Occult Adventures pg 179

This spell functions as [possession](ref/spell/possession), except you possess an object instead of
a creature.

A possessed object becomes capable of animation, gaining the statistics of an
[animated object](ref/monster/animated-object) of its size (including 1 CP worth of abilities). You
can't use any spells or other abilities while possessing an object.

A spiritual tether connects your body to the possessed object, in a manner similar to a
[silver cord](ref/rule/astral-plane-oa). If the possessed object and your body are ever farther than
close range (25 ft. + 5 ft./2 levels) from one another, this tether breaks, returning your
consciousness to your body.

### Object Possession

**Sources:** Occult Adventures pg 179

This spell functions as lesser object possession, except as noted above. The possessed animated
object has a number of Construction Points appropriate for its size (up to 3 CP for Large objects).

You can return your consciousness to your body as a standard action. On your next turn, you can
attempt to possess a different object as a standard action instead of ending the spell.

### Greater Object Possession

**Sources:** Occult Adventures pg 179

This spell functions as object possession, except as noted above. The possessed animated object has
a number of Construction Points appropriate for its size (up to 5 CP for Gargantuan objects). Your
silver cord extends to medium range (100 ft. + 10 ft./level).

You can attempt to possess a construct instead of an unattended object as your first possession with
this spell. If you do, this spell acts as control construct, except as noted above.
