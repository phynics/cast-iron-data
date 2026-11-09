+++
id = "ref/carried/core-rulebook/spells/restoration/greater"
kind = "spell"
title = "Restoration, Greater"
aon = "SpellDisplay.aspx?ItemName=Restoration%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Restoration"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Restoration/Greater", path = "core_rulebook/spell/restoration_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Warpriest", level = 7 },
]
casting_time = "3 rounds"
components = "V, S, M (diamond dust worth 5,000 gp)"
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
Level: 7: Cleric, Oracle, Shaman, Warpriest
Casting Time: 3 rounds
Components: V, S, M (diamond dust worth 5,000 gp)
Range: touch
Target: creature touched
Duration: instantaneous
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As restoration, plus restores all levels and ability scores._

This spell functions like _[lesser restoration](ref/spell/restoration-lesser)_, except that it
dispels all permanent and temporary negative levels afflicting the healed creature.
_[Greater restoration](ref/spell/restoration-greater)_ also dispels all magical effects penalizing
the creature's abilities, cures all temporary ability damage, and restores all points permanently
drained from all ability scores. It also eliminates fatigue and exhaustion, and removes all forms of
insanity, confusion, and similar mental effects.
