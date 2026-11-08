+++
id = "ref/spell/contagious-suggestion"
kind = "spell"
title = "Contagious Suggestion"
source_ids = ["core-rulebook", "blood-of-the-beast", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagious_suggestion", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/suggestion" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, M (a snake's tongue and a honeycomb)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 hour/level or until completed"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Medium, Mesmerist, Psychic, Skald\
3: Arcanist, Occultist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, M (a snake's tongue and a honeycomb)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level or until completed
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

### Contagious Suggestion

**Sources:** Blood of the Beast pg 14

This spell functions as per [suggestion](ref/spell/suggestion), except the target can pass on the
enchantment to other targets. The target is compelled to communicate your suggestion to another
creature, forcing the new target to attempt a saving throw as if it were the initial target. If a
secondary target successfully saves, the suggestion effect on the initial target isn't negated. If a
secondary target fails, it is placed under the same compulsion as the initial target and can further
spread the suggestion. This spell can affect a total number of Hit Dice of creatures equal to your
caster level. Creatures that save against this spell cannot be affected by that particular casting
of contagious suggestion for 24 hours.
