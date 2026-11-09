+++
id = "ref/carried/core-rulebook/spells/scrying/greater"
kind = "spell"
title = "Scrying, Greater"
aon = "SpellDisplay.aspx?ItemName=Scrying%2C%20Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Scrying"]
tags = ["divination", "scrying"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Scrying/Greater", path = "core_rulebook/spell/scrying_greater.json" },
]

[fields]
kind = "spell"
school = "divination"
subschools = ["scrying"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Warpriest", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "magical sensor" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: divination (scrying)
Level: 6: Bard, Skald\
7: Arcanist, Cleric, Druid, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: see text
Effect: magical sensor
Duration: 1 hour/level
Saving Throw: Will negates
Spell Resistance: yes
:::

_As scrying, but faster and longer._

This spell functions like _[scrying](ref/spell/scrying)_, except as noted above. Additionally, all
of the following spells function reliably through the sensor:
_[detect chaos](ref/spell/detect-chaos)_, _[detect evil](ref/spell/detect-evil)_,
_[detect good](ref/spell/detect-good)_, _[detect law](ref/spell/detect-law)_,
_[detect magic](ref/spell/detect-magic)_, _[message](ref/spell/message)_,
_[read magic](ref/spell/read-magic)_, and _[tongues](ref/spell/tongues)_.
