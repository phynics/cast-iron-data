+++
id = "ref/carried/core-rulebook/spells/restoration/lesser"
kind = "spell"
title = "Restoration, Lesser"
source_ids = ["core-rulebook"]
section = ["Spells", "Restoration"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Restoration/Lesser", path = "core_rulebook/spell/restoration_lesser.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "3 rounds"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: conjuration (healing)
Level: 1: Paladin\
2: Alchemist, Cleric, Druid, Hunter, Hunter, Inquisitor, Oracle, Shaman, Warpriest
Casting Time: 3 rounds
Components: V, S
Range: touch
Target: creature touched
Duration: instantaneous
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_Dispels magical ability penalty or repairs 1d4 ability damage._

_[Lesser restoration](ref/spell/restoration-lesser)_ dispels any magical effects reducing one of the
subject's ability scores or cures 1d4 points of temporary ability damage to one of the subject's
ability scores. It also eliminates any fatigue suffered by the character, and improves an exhausted
condition to fatigued. It does not restore permanent ability drain.
