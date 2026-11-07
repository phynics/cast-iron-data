+++
id = "ref/spell/suggestion-mass"
kind = "spell"
title = "Mass Suggestion"
source_ids = ["core-rulebook", "mythic-adventures", "blood-of-the-beast", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "suggestion_mass", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, M (a snake's tongue and a honeycomb)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level or until completed"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Occultist, Psychic, Skald\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, M (a snake's tongue and a honeycomb)
Range: medium (100 ft. + 10 ft./level)
Targets: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 hour/level or until completed
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

## Suggestion

**Sources:** PRPG Core Rulebook pg 350

You influence the actions of the target creature by suggesting a course of activity (limited to a
sentence or two). The suggestion must be worded in such a manner as to make the activity sound
reasonable. Asking the creature to do some obviously harmful act automatically negates the effect of
the spell.

The suggested course of activity can continue for the entire duration. If the suggested activity can
be completed in a shorter time, the spell ends when the subject finishes what it was asked to do.
You can instead specify conditions that will trigger a special activity during the duration. If the
condition is not met before the spell duration expires, the activity is not performed.

A very reasonable suggestion causes the save to be made with a penalty (such as -1 or -2).

### Mythic Suggestion

**Sources:** Mythic Adventures pg 109

Mythic suggestion loses the language-dependent descriptor, and can target one or more living
creatures in a 10-foot-radius burst.

### Contagious Suggestion

**Sources:** Blood of the Beast pg 14

This spell functions as per suggestion, except the target can pass on the enchantment to other
targets. The target is compelled to communicate your suggestion to another creature, forcing the new
target to attempt a saving throw as if it were the initial target. If a secondary target
successfully saves, the suggestion effect on the initial target isn't negated. If a secondary target
fails, it is placed under the same compulsion as the initial target and can further spread the
suggestion. This spell can affect a total number of Hit Dice of creatures equal to your caster
level. Creatures that save against this spell cannot be affected by that particular casting of
contagious suggestion for 24 hours.

### Mass Suggestion

**Sources:** PRPG Core Rulebook pg 350

This spell functions like suggestion, except that it can affect more creatures. The same suggestion
applies to all these creatures.

### Triggered Suggestion

**Sources:** Advanced Class Guide pg 197

This spell functions as suggestion, except you can use it only to specify a condition that triggers
a special activity, and the subject does not remember that you made the suggestion. For example, you
could use triggered suggestion on a palace guard to make him attack the king the next time he and
the king are alone, and the guard would not remember the suggestion to do so until the trigger
occurred.
