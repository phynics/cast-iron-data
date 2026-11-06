+++
id = "ref/spell/minor-dream"
kind = "spell"
title = "Minor Dream"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "minor_dream", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 minute"
components = "V, S"
range = "unlimited"
effects = [
  { label = "Target", value = "you or one gnome touched" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Alchemist, Investigator, Medium, Witch\
3: Arcanist, Bard, Mesmerist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S
Range: unlimited
Duration: see text
Saving throw: none
Spell resistance: no
Target: you or one gnome touched
Subschool: Figment
Descriptors: mind-affecting
:::

**Sources:** Advanced Race Guide pg 39

> _[Gnomes](ref/race/gnome) have access to the following spell._

This spell functions as the [dream](ref/spell/dream) spell, except as follows. The messenger must be
yourself or a gnome touched. The message can be no longer than 20 words. If the recipient of the
message is not asleep when the spell is cast, the spell automatically fails.
