+++
id = "ref/spell/agonizing-rebuke"
kind = "spell"
title = "Agonizing Rebuke"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "agonizing_rebuke", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "mind-affecting", "pain"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Antipaladin\
3: Cleric, Inquisitor, Mesmerist, Oracle, Psychic, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: emotion, mind-affecting, pain
:::

**Sources:** Advanced Race Guide pg 126

> _[Hobgoblins](ref/race/hobgoblin) have access to the following spell._

With a word and a gesture, you instill such apprehension about attacking you in your target that
doing so causes it mental distress and pain. Each time the target makes an attack against you,
targets you with a harmful spell, or otherwise takes and action that would harm you, it takes 2d6
points of nonlethal damage.
