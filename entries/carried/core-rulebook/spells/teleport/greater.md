+++
id = "ref/carried/core-rulebook/spells/teleport/greater"
kind = "spell"
title = "Teleport, Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Teleport"]
tags = ["conjuration", "teleportation"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Teleport/Greater", path = "core_rulebook/spell/teleport_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "personal and touch"
effects = [
  { label = "Target", value = "you and touched objects or other touched willing creatures" },
]
duration = "instantaneous"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
School: conjuration (teleportation)
Level: 5: Summoner\
7: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V
Range: personal and touch
Target: you and touched objects or other touched willing creatures
Duration: instantaneous
Saving Throw: none and Will negates (object)
Spell Resistance: no and yes (object)
:::

_As teleport, but no range limit and no off-target arrival._

This spell functions like _[teleport](ref/spell/teleport)_, except that there is no range limit and
there is no chance you arrive off target. In addition, you need not have seen the destination, but
in that case you must have at least a reliable description of the place to which you are
teleporting. If you attempt to teleport with insufficient information (or with misleading
information), you disappear and simply reappear in your original location. Interplanar travel is not
possible.
