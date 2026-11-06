+++
id = "ref/spell/hostile-levitation"
kind = "spell"
title = "Hostile Levitation"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hostile_levitation", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a leather loop studded with lodestones)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Medium\
3: Arcanist, Bloodrager, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a leather loop studded with lodestones)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
:::

**Sources:** Ultimate Combat pg 231

You levitate the target a few inches off the ground, removing solid footing and halving the target's
speed. The target also takes a -4 penalty to CMD against bull rush, drag, and reposition attempts. A
targeted creature that attacks with a melee or ranged weapon finds itself increasingly unstable; the
first attack has a -1 penalty on attack rolls, the second -2, and so on, to a maximum penalty of -5.
A full-round action spent stabilizing allows the creature to begin again at -1.

This spell fails if cast on a flying creature.
