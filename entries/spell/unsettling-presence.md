+++
id = "ref/spell/unsettling-presence"
kind = "spell"
title = "Unsettling Presence"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unsettling_presence", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "haunted", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one 5-ft. cube/level (S)" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Medium\
2: Arcanist, Bard, Mesmerist, Occultist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: one 5-ft. cube/level (S)
Descriptors: emotion, fear, haunted, mind-affecting
:::

**Sources:** Haunted Heroes Handbook pg 29

Those in this spell's area who fail their Will saving throws harbor a faint sense of paranoia and
evoke the same feeling in others for the duration of the spell. Domesticated animals (not including
familiars and animal companions) don't willingly approach affected creatures unless the animal's
master succeeds at a DC 25 Handle Animal, Ride, or [wild empathy](ref/ability/wild-empathy) check.
Affected creatures take a -4 penalty on Handle Animal, Ride, and wild empathy checks against
familiars, animal companions, animal cohorts, and other permanent companions provided by class
abilities for the spell's duration. Anyone an affected creature interacts with must succeed at a
Will save or have its initial attitude automatically worsened by one step for the spell's duration.
Every time an affected creature attempts a Sense Motive check to get a hunch or detect a Bluff from
another creature (or vice versa), it must succeed at a Will save or automatically assume the other
party is lying or otherwise harbors ill will against it. Each time this spell causes an affected
creature (or someone interacting with the affected creature) to attempt a Will saving throw, the
spell's haunt-like manifestation occurs.

#### Haunt Statistics

**Notice:** Perception DC 20 (to feel a sudden sense of dread, or to hear victims' names whispered
behind their backs)

**Hit points:** 2 hp/level

**Trigger:** proximity

**Reset:** none
