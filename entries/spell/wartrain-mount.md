+++
id = "ref/spell/wartrain-mount"
kind = "spell"
title = "Wartrain Mount"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wartrain_mount", path = "json/spells11.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "248"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 2 },
]
casting_time = "1 minute"
components = "V, S, M (a swatch of black cloth)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one indifferent or friendly animal" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin, Hunter, Inquisitor, Paladin, Ranger\
2: Bard, Druid, Mesmerist, Skald
Casting time: 1 minute
Components: V, S, M (a swatch of black cloth)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: none
Spell resistance: yes
Target: one indifferent or friendly animal
Subschool: Compulsion
Descriptors: mind-affecting
:::

You instill the target animal with the combat training general purpose (see the
[Handle Animal](ref/skill/handle-animal) skill). This supersedes the animal's previous trained
purpose and any tricks it knows. When the spell ends, it reverts to its previous trained purpose and
known tricks.
