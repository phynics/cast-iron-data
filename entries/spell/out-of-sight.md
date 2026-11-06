+++
id = "ref/spell/out-of-sight"
kind = "spell"
title = "Out of Sight"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "out_of_sight", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a strip of black cloth)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (d); see text"
saving_throw = "Will negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Medium, Mesmerist\
4: Psychic
Casting time: 1 standard action
Components: V, S, M (a strip of black cloth)
Range: personal
Duration: 1 minute/level (d); see text
Saving throw: Will negates, see text
Spell resistance: yes
Target: you
Descriptors: mind-affecting
:::

**Sources:** Occult Origins pg 31

The spell inhibits the memories of creatures that perceive you. While creatures can perceive you
normally, when a creature stops observing you, it must attempt a Will save
([spell resistance](ref/rule/spell-resistance) applies). If it fails, it loses all memory of its
awareness of you and your actions while you were under the effects of this spell. The spell's
duration listed above measures how long the out of sight effect lasts on you, but the memory
alteration is instantaneous and can be reversed only by magic such as
[modify memory](ref/spell/modify-memory).

The creature is still aware of any other changes to itself or its environment. For instance, a guard
will remember running, and may notice a newly unlocked door, but will not remember that he was
chasing after you.
