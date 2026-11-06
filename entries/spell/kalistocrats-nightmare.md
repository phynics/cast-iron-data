+++
id = "ref/spell/kalistocrats-nightmare"
kind = "spell"
title = "Kalistocrat's Nightmare"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kalistocrats_nightmare", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a copper piece)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level (see text)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Bard, Inquisitor, Investigator, Magus, Occultist, Skald, Witch\
3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a copper piece)
Range: touch
Duration: 1 hour/level (see text)
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** Magic Tactics Toolbox pg 22

You temporarily curse a creature so its touch lessens the value of coins it touches. While under the
effects of this curse, whenever the target touches a coin of higher value than copper piece, that
coin changes into a copper piece. The change takes place over the course of the following minute,
allowing the target to interact with multiple coins before the effect of the curse becomes apparent.
The affected coins are permanently transmuted from their previous material (typically gold or
silver) into copper coins, though [remove curse](ref/spell/remove-curse) (which can affect up to 50
coins with a single casting) or a similar spell can restore them to their previous material.
