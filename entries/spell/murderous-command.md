+++
id = "ref/spell/murderous-command"
kind = "spell"
title = "Murderous Command"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "murderous_command", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Antipaladin, Cleric, Medium, Mesmerist, Occultist, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Ultimate Magic pg 230

You give the target a mental urge to kill its nearest ally, which it obeys to the best of its
ability. The target attacks its nearest ally on its next turn with a melee weapon or natural weapon.
If necessary, it moves to or charges to the nearest ally in order to make this attack. If it is
unable to reach its closest ally on its next turn, the target uses its turn to get as close as
possible to the ally.
