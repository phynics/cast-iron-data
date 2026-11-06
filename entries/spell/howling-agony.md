+++
id = "ref/spell/howling-agony"
kind = "spell"
title = "Howling Agony"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "howling_agony", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "pain"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a needle and a dried eyeball)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Inquisitor, Mesmerist, Psychic\
3: Arcanist, Bloodrager, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a needle and a dried eyeball)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature/level, no two of which can be more than 30 ft. apart
Descriptors: death, pain
:::

**Sources:** Ultimate Magic pg 223

You send wracking pains through the targets' bodies. Because of the pain, affected creatures take a
-2 penalty to AC, attacks, melee damage rolls, and Reflex saving throws, and must succeed at a
[concentration](ref/rule/concentration) check (DC equal to the DC of this spell) to cast spells.
However, if an affected creature spends a move action screaming as loudly as possible, it can act
without any other penalties for the remainder of its turn. "Screaming," for the purposes of this
spell, includes any vocalization of pain or its telepathic equivalent; creatures that cannot scream
(such as creatures without the natural ability to communicate or vocalize) suffer the full effect of
the spell.
