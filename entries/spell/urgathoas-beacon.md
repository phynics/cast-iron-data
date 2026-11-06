+++
id = "ref/spell/urgathoas-beacon"
kind = "spell"
title = "Urgathoa's Beacon"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urgathoas_beacon", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "haunted", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one 5-ft cube/level (S)" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: one 5-ft cube/level (S)
Descriptors: emotion, fear, haunted, mind-affecting
:::

**Sources:** Haunted Heroes Handbook pg 29

You shroud an area in Urgathoa's unclean influence, rendering those who pass through it and fail
their Will saving throws more enticing to ravenous undead. When an affected creature comes within 60
feet of an undead creature, the spell immediately draws the undead creature's attention, granting it
a +4 bonus on Perception checks to notice the affected creature and on saving throws to resist
spells that hide or disguise the affected creature (such as
[hide from undead](ref/spell/hide-from-undead)). Once the undead creature notices the affected
creature, it feels compelled to kill and devour the affected creature, and gains a +1 profane bonus
on attack rolls made against the affected creature and a +1 profane bonus on saving throws against
the affected creature's spells and special abilities. The undead also ignores any
[concealment](ref/rule/concealment) less than total concealment that an affected creature has. Each
time the spell draws an undead creature's attention to an affected creature, the spell's haunt-like
manifestation occurs during that round.

#### Haunt Statistics

**Notice:** Perception DC 20 (to see a pale light briefly in the area)

**Hit points:** 2 hp/level

**Trigger:** proximity

**Reset:** none
