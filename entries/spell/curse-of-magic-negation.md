+++
id = "ref/spell/curse-of-magic-negation"
kind = "spell"
title = "Curse of Magic Negation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_magic_negation", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (powdered lead and platinum worth 250 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Mesmerist\
4: Arcanist, Inquisitor, Occultist, Psychic, Sorcerer, Witch, Wizard\
5: Cleric, Oracle, Warpriest
Casting time: 1 round
Components: V, S, M (powdered lead and platinum worth 250 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: no
Target: one creature
Descriptors: curse
:::

**Sources:** Ultimate Magic pg 215

You disrupt the target creature's ability to draw upon magical energies. For the duration of the
spell, it gains the [negated spellblight](ref/rule/major-spellblights). Dispel checks to remove the
spellblight take a -5 penalty due to this spell's interference with magical energies.
