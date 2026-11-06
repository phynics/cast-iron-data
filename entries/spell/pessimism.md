+++
id = "ref/spell/pessimism"
kind = "spell"
title = "Pessimism"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pessimism", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a shard of a broken mirror)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Bard, Medium, Mesmerist, Skald\
5: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a shard of a broken mirror)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

**Sources:** Horror Adventures pg 123

You erode the target's confidence and instill a sense of despair. This fear of failure manifests as
a -2 penalty on attack rolls, saving throws, ability checks, skill checks, and weapon damage rolls.
Additionally, the target can't gain morale bonuses of any kind while the spell remains in effect. No
amount of achievement counters the spell's effects - the target simply explains away positive events
with a self-critical perspective.

Certain events can solidify the character's belief that it is doomed. Whenever the target rolls a
natural 1 on an attack roll or saving throw, fails an ability or skill check by more than 5, or
takes additional damage as a result of a foe's confirmed critical hit, the penalty to roll imposed
by pessimism becomes -3 for 1 round. This increased penalty doesn't stack, even if multiple
catastrophes occur on the same round.
