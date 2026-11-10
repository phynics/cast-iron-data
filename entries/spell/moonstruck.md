+++
id = "ref/spell/moonstruck"
kind = "spell"
title = "Moonstruck"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "moonstruck", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "232"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of powdered moonstone)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bloodrager, Druid, Hunter, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of powdered moonstone)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You invoke the mystical power of the moon to drive the target into a mad, bestial frenzy. If the
target fails its save, it is dazed for 1 round, dropping held items as its nails and teeth elongate
and sharpen. The target gains a bite attack and two claw attacks that deal damage appropriate for
the creature's size, and for the remainder of the spell's duration the target behaves as if under
simultaneous rage and confusion spells, attacking with its natural weapons in preference to other
actions. During the final round of the spell's duration, the target is again dazed as it returns to
its normal state.
