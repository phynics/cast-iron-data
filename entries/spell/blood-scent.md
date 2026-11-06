+++
id = "ref/spell/blood-scent"
kind = "spell"
title = "Blood Scent"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_scent", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature/2 levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin, Hunter, Ranger\
3: Alchemist, Arcanist, Bloodrager, Cleric, Druid, Inquisitor, Investigator, Oracle, Psychic, Red Mantis Assassin, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature/2 levels, no two of which can be more than 30 ft. apart
:::

**Sources:** Advanced Race Guide pg 143

> _[Orcs](ref/race/orc) have access to the following spell._

You greatly magnify the target's ability to smell the presence of blood. The target is considered to
have the [scent](ref/umr/scent) universal monster ability, but only for purposes of detecting and
pinpointing injured creatures (below full hit points). Creatures below half their full hit points or
suffering bleed damage are considered strong scents for this ability.

Orcs and any creature under the effects of rage gain a +2 morale bonus on attack and damage rolls
against creatures they can smell with this spell, or a +4 morale bonus if the target's blood counts
as a strong scent.
