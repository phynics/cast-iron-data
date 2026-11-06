+++
id = "ref/carried/ultimate-magic/spells/false-life/greater"
kind = "spell"
title = "False Life, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "False Life"]
tags = ["necromancy"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/False Life/Greater", path = "ultimate_magic/spell/false_life_greater.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of blood)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level or until discharged; see text"
+++

::: statblock
School: necromancy
Level: 4: Alchemist, Arcanist, Bloodrager, Investigator, Shaman, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S, M (a drop of blood)
Range: personal
Target: you
Duration: 1 hour/level or until discharged; see text
:::

_Gain 2d10 temporary hp + 1/level._

This spell functions as _[false life](ref/spell/false-life)_, except you gain temporary hit points
equal to 2d10 + 1 point per caster level (maximum +20). The effects of this spell do not stack with
those of _[false life](ref/spell/false-life)_.
