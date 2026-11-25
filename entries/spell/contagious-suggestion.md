+++
id = "ref/spell/contagious-suggestion"
kind = "spell"
title = "Contagious Suggestion"
aon = "SpellDisplay.aspx?ItemName=Contagious%20Suggestion"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagious_suggestion", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/suggestion" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "14"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 hour/level or until completed (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Medium, Mesmerist, Skald\
5: Arcanist, Occultist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level or until completed (D)
Saving throw: none
Spell resistance: no
Target: one living creature
Subschool: compulsion
Descriptors: language-dependant, mind-affecting
:::

### Contagious Suggestion

This spell functions as per [suggestion](ref/spell/suggestion), except the target can pass on the
enchantment to other targets. The target is compelled to communicate your suggestion to another
creature, forcing the new target to attempt a saving throw as if it were the initial target. If a
secondary target successfully saves, the suggestion effect on the initial target isn't negated. If a
secondary target fails, it is placed under the same compulsion as the initial target and can further
spread the suggestion. This spell can affect a total number of Hit Dice of creatures equal to your
caster level. Creatures that save against this spell cannot be affected by that particular casting
of contagious suggestion for 24 hours.
