+++
id = "ref/spell/stone-fist"
kind = "spell"
title = "Stone Fist"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stone_fist", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "247"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a chip of granite)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Arcanist, Bloodrager, Druid, Hunter, Investigator, Magus, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a chip of granite)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: earth
:::

This spell transforms your hands into living stone. While this spell is in effect, your unarmed
strikes do not provoke attacks of opportunity and deal 1d6 points of lethal bludgeoning damage (1d4
if you are Small). In addition, your unarmed strikes ignore the [hardness](ref/umr/hardness) of any
object with a hardness less than 8.

[Stone to flesh](ref/spell/stone-to-flesh) immediately dispels stone fist. Should you be the target
of [transmute rock to mud](ref/spell/transmute-rock-to-mud), this spell immediately ends and you
take 4d6 points of damage.
