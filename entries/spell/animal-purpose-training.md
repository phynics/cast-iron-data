+++
id = "ref/spell/animal-purpose-training"
kind = "spell"
title = "Animal Purpose Training"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_purpose_training", path = "json/spells.json" },
]

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
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Witch", level = 1 },
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
Level: 1: Antipaladin, Hunter, Inquisitor, Paladin, Psychic, Ranger, Witch\
2: Bard, Druid, Shaman, Skald
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

**Sources:** Advanced Class Guide pg 173

You instill the target animal with a general purpose (see the
[Handle Animal](ref/skill/handle-animal) skill), which can be any purpose except combat training:
fighting, guarding, heavy labor, hunting, performance, or
riding.^[1](ref/spell/animal-purpose-training#footnote-1)^ This purpose supersedes the animal's
previous trained purpose and any tricks it knows. When the spell ends, the animal reverts to its
previous trained purpose and known tricks.

###### ^1^ {#footnote-1}

Other purposes have been added by other sourcebooks. Consult your GM if you wish to use one of the
purposes not listed in the spell.
