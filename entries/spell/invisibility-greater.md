+++
id = "ref/spell/invisibility-greater"
kind = "spell"
title = "Greater Invisibility"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_greater", path = "json/spells14.json" },
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
  { class = "Alchemist", level = 4 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal or touch"
effects = [
  { label = "Target", value = "you or creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium, Summoner\
4: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Magus, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal or touch
Target: you or creature touched
Duration: 1 round/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Glamer
Descriptors: glamer
:::

### Greater Invisibility

**Sources:** PRPG Core Rulebook pg 302

This spell functions like [invisibility](ref/spell/invisibility), except that it doesn't end if the
subject attacks.
