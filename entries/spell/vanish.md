+++
id = "ref/spell/vanish"
kind = "spell"
title = "Vanish"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vanish", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invisibility" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (up to 5 rounds) (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Magus, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (up to 5 rounds) (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Advanced Player's Guide pg 253

This spell functions like [invisibility](ref/spell/invisibility), except the effect only lasts for 1
round per caster level (maximum of 5 rounds). Like invisibility, the spell immediately ends if the
subject attacks any creature.
