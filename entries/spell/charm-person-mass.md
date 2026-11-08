+++
id = "ref/spell/charm-person-mass"
kind = "spell"
title = "Mass Charm Person"
source_ids = ["core-rulebook", "the-first-world-realm-of-the-fey", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charm_person_mass", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/charm-person" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one or more humanoid creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Mesmerist, Occultist, Skald\
5: Arcanist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one or more humanoid creatures, no two of which can be more than 30 ft. apart
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Subschool: Charm
Descriptors: mind-affecting
:::

### Mass Charm Person

**Sources:** Ultimate Intrigue pg 206

This spell functions like [charm person](ref/spell/charm-person), except that mass charm person
affects a number of humanoid creatures whose combined Hit Dice don't exceed twice your level. If
there are more potential targets than you can affect, you choose them one at a time until you reach
the limit of HD you can affect. If you cast mass charm person on only one creature, you ignore the
spell's HD limit.
