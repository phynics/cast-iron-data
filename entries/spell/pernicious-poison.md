+++
id = "ref/spell/pernicious-poison"
kind = "spell"
title = "Pernicious Poison"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pernicious_poison", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "231"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Arcanist, Druid, Hunter, Occultist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: yes
Target: creature touched
Descriptors: poison
:::

You weaken the target's defenses against poison. The target gains a -4 penalty on saves against
poison, and poisons affecting the target continue for another 2 frequency increments (for example,
black adder venom lasts 8 rounds instead of 6, and arsenic lasts for 6 minutes instead of 4).
Attempts to cure the poisoned target with skill or magic take a -4 penalty.
