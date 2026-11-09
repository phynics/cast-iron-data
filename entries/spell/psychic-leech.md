+++
id = "ref/spell/psychic-leech"
kind = "spell"
title = "Psychic Leech"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_leech", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-origins"
page = "29"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Mesmerist, Psychic, Spiritualist, Witch\
3: Arcanist, Bloodrager, Magus, Medium, Sorcerer, Wizard
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will partial
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

The target experiences feelings of ennui and lethargy, becoming fatigued for the spell's duration.
While the target is fatigued and is within the spell's range, you gain a +2 enhancement bonus to
Strength and Dexterity. On a successful save, the target is fatigued for only 1d4 rounds and you
receive no bonus. This spell has no effect if it targets a creature that is already fatigued.
