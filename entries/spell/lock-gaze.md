+++
id = "ref/spell/lock-gaze"
kind = "spell"
title = "Lock Gaze"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lock_gaze", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
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
School: enchantment
Level: 1: Arcanist, Bard, Inquisitor, Magus, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Ultimate Combat pg 236

You compel the target to look at you and only you for the spell's duration or until the spell is
discharged. While staring at you, the target is considered to be averting its eyes from every
creature but you, granting creatures other than you [concealment](ref/rule/concealment) against the
target's attacks. If the target willingly leaves your line of sight, it is blinded for 1 round and
the spell ends. If you willingly leave the target's line of sight or become unconscious or dead, the
spell ends but the target suffers no ill effects. Blind creatures and creatures immune to gaze
attacks are immune to this spell.
