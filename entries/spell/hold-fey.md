+++
id = "ref/spell/hold-fey"
kind = "spell"
title = "Hold Fey"
source_ids = ["core-rulebook", "the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_fey", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hold-person" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a small, straight piece of iron)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin, Bard, Cleric, Inquisitor, Medium, Mesmerist, Oracle, Psychic, Shaman, Skald, Warpriest, Witch\
3: Arcanist, Bloodrager, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a small, straight piece of iron)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Target: one humanoid creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Hold Fey

**Sources:** The First World, Realm of the Fey pg 12

This spell functions as per [hold person](ref/spell/hold-person), except it affects a fey instead of
a humanoid.
