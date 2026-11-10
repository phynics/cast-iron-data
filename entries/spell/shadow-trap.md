+++
id = "ref/spell/shadow-trap"
kind = "spell"
title = "Shadow Trap"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_trap", path = "json/spells15.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "31"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Antipaladin, Arcanist, Bloodrager, Bard, Cleric, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Shadow
:::

You pin the target's shadow to its current location, causing the target to become entangled and
preventing it from moving farther than 5 feet from its original position, as if its shadow were
anchored to the terrain. Each round on its turn, the target can attempt a new saving throw to end
the effect as a full-round action. A flying creature can only hover in place or fall while entangled
in this manner. This spell automatically fails when cast on a creature that doesn't throw a shadow,
and it ends if the creature is entirely in an area with no illumination.
