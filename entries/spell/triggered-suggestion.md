+++
id = "ref/spell/triggered-suggestion"
kind = "spell"
title = "Triggered Suggestion"
source_ids = ["core-rulebook", "mythic-adventures", "blood-of-the-beast", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "triggered_suggestion", path = "json/spells16.json" },
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

### Mythic Suggestion

**Sources:** Mythic Adventures pg 109

Mythic suggestion loses the language-dependent descriptor, and can target one or more living
creatures in a 10-foot-radius burst.

### Triggered Suggestion

**Sources:** Advanced Class Guide pg 197

This spell functions as [suggestion](ref/spell/suggestion), except you can use it only to specify a
condition that triggers a special activity, and the subject does not remember that you made the
suggestion. For example, you could use triggered suggestion on a palace guard to make him attack the
king the next time he and the king are alone, and the guard would not remember the suggestion to do
so until the trigger occurred.
