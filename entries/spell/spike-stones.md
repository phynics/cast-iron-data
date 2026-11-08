+++
id = "ref/spell/spike-stones"
kind = "spell"
title = "Spike Stones"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spike_stones", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Shaman", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one 20-ft. square/level" },
]
duration = "1 hour/level (D)"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level (D)
Saving throw: Reflex partial
Spell resistance: yes
Area: one 20-ft. square/level
Descriptors: earth
:::

**Sources:** PRPG Core Rulebook pg 348

Rocky ground, stone floors, and similar surfaces shape themselves into long, sharp points that blend
into the background.

Spike stones impede progress through an area and deal damage. Any creature moving on foot into or
through the spell's area moves at half speed. In addition, each creature moving through the area
takes 1d8 points of piercing damage for each 5 feet of movement through the spiked area.

Any creature that takes damage from this spell must also succeed on a Reflex save to avoid injuries
to its feet and legs. A failed save causes the creature's speed to be reduced to half normal for 24
hours or until the injured creature receives a cure spell (which also restores lost hit points).
Another character can remove the penalty by taking 10 minutes to dress the injuries and succeeding
on a Heal check against the spell's save DC.

Magic traps such as spike stones are hard to detect. A rogue (only) can use the Perception skill to
find spike stones. The DC is 25 + spell level, or DC 29 for spike stones. Spike stones is a magic
trap that can't be disabled with the Disable Device skill.
