+++
id = "ref/carried/advanced-players-guide/spells/brand/greater"
kind = "spell"
title = "Brand, Greater"
source_ids = ["advanced-players-guide"]
section = ["Spells", "Brand"]
tags = ["transmutation", "curse"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Advanced Players Guide/Spells/Brand/Greater", path = "advanced_players_guide/spell/brand_greater.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
School: transmutation \[curse\]
Level: 4: Inquisitor
Casting Time: 1 round
Components: V, S, DF
Range: touch
Target: creature touched
Duration: permanent
Saving Throw: Fortitude negates
Spell Resistance: yes
:::

_As brand, but brand glows when near your holy symbol._

This spell functions like _[brand](ref/spell/brand)_, except that it inflicts 1d6 points of damage
when applied and cannot be removed, even temporarily. In addition, a
_[greater brand](ref/spell/brand-greater)_ blazes as bright as a torch when brought within 30 feet
of a visible symbol of your faith. While the symbol is blazing, the recipient is sickened. Like the
effects of _[bestow curse](ref/spell/bestow-curse)_, a _[greater brand](ref/spell/brand-greater)_
cannot be dispelled, but it can be removed by any means that removes a
_[mark of justice](ref/spell/mark-of-justice)_.
