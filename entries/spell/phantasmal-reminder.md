+++
id = "ref/spell/phantasmal-reminder"
kind = "spell"
title = "Phantasmal Reminder"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantasmal_reminder", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round (see text)"
saving_throw = "Will disbelief, then Fortitude partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Antipaladin, Arcanist, Mesmerist, Psychic, Sorcerer, Witch, Wizard\
4: Bard, Shaman, Skald
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round (see text)
Saving throw: Will disbelief, then Fortitude partial; see text
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

**Sources:** Magic Tactics Toolbox pg 26

You create a memory loop of a successful attack made against the target, forcing its conscious mind
to recall the details of the attack in such excruciating detail that its physical body is racked by
the recollection. This spell can affect only a creature that has taken damage since the end of your
last turn. The target first can attempt a Will save to recognize the attack as unreal. If it fails
that saving throw, the target must succeed at a Fortitude save or take an amount of damage equal to
1d6 × your caster level (maximum 10d6). Because the damage is a quasi-real memory of existing
wounds, this damage can't be reduced or prevented (such as by the
[shield other](ref/spell/shield-other) spell).

If the target of a phantasmal reminder attack succeeds at the Will save to disbelieve the memory
loop and either has natural telepathy or is wearing a
[helm of telepathy](ref/magic-wondrous/helm-of-telepathy), the memory of damage automatically
rebounds to affect you. You must immediately attempt a Will save to disbelieve; if you fail, you
take half the spell's damage yourself.
