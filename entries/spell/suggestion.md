+++
id = "ref/spell/suggestion"
kind = "spell"
title = "Suggestion"
aon = "SpellDisplay.aspx?ItemName=suggestion"
source_ids = ["core-rulebook", "blood-of-the-beast", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suggestion", path = "json/spells16.json" },
]
[[sources]]
publication = "core-rulebook"
page = "350"

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

You influence the actions of the target creature by suggesting a course of activity (limited to a
sentence or two). The suggestion must be worded in such a manner as to make the activity sound
reasonable. Asking the creature to do some obviously harmful act automatically negates the effect of
the spell.

The suggested course of activity can continue for the entire duration. If the suggested activity can
be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.
You can instead specify conditions that will trigger a special activity during the duration. If the
condition is not met before the spell duration expires, the activity is not performed.

A very reasonable suggestion causes the save to be made with a penalty (such as -1 or -2).
