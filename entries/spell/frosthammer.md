+++
id = "ref/spell/frosthammer"
kind = "spell"
title = "Frosthammer"
aon = "SpellDisplay.aspx?ItemName=Frosthammer"
source_ids = ["pathfinder-69-maiden-mother-crone"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frosthammer", path = "json/spells13.json" },
]
[[sources]]
publication = "pathfinder-69-maiden-mother-crone"
page = "66"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Antipaladin, Cleric, Hunter, Inquisitor, Oracle, Ranger, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one creature
Descriptors: cold
:::

> _Priests of [Kostchtchie](ref/faith/kostchtchie) have access to the following spell._

You create a warhammer of magically hardened ice and send it hurling toward the target. You must
succeed at a ranged touch attack to strike the target. If hit, the target takes 1d8 points of damage
per 2 caster levels you possess (maximum 5d8); half this damage is bludgeoning damage, half is cold
damage. The frosthammer counts as having a +1 enhancement bonus for the purpose of bypassing DR. If
the target takes any bludgeoning damage from the hammer, you may attempt a trip combat maneuver
check against that target, except you may use your caster level instead of your BAB and your
spellcasting ability modifier (Wisdom for clerics, and so on) instead of your Strength modifier.
