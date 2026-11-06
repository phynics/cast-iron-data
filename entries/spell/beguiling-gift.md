+++
id = "ref/spell/beguiling-gift"
kind = "spell"
title = "Beguiling Gift"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beguiling_gift", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (the object to be offered)"
range = "5 ft."
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Mesmerist, Psychic, Skald, Witch
Casting time: 1 standard action
Components: V, S, F (the object to be offered)
Range: 5 ft.
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 205

You offer an object to an adjacent creature, and entice it into using or consuming the proffered
item. If the target fails its Will save, it immediately takes the offered object, dropping an
already held object if necessary. On its next turn, it consumes or dons the object, as appropriate
for the item in question. For example, an apple would be eaten, a potion consumed, a ring put on a
finger, and a sword wielded in a free hand. If the target is physically unable to accept the object,
the spell fails. The subject is under no obligation to continue consuming or using the item once the
spell's duration has expired, although it may find a cursed item difficult to be rid of.
