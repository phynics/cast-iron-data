+++
id = "ref/spell/adoration"
kind = "spell"
title = "Adoration"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adoration", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Mesmerist, Skald\
2: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one creature
Descriptors: emotion, mind-affecting
:::

**Sources:** Ultimate Combat pg 222

The target of this spell is the subject of adoration by those whom it tries to affect with Diplomacy
or during performance combat. If the target is out of combat, it receives a +2 morale bonus on all
Diplomacy checks it makes to influence creatures. If the creature is engaged in
[performance combat](ref/rule/performance-combat), the target gains a +2 morale bonus on all
performance combat checks.
