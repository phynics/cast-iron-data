+++
id = "ref/carried/ultimate-magic/spells/interrogation/greater"
kind = "spell"
title = "Interrogation, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "Interrogation"]
tags = ["necromancy", "evil", "pain"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Interrogation/Greater", path = "ultimate_magic/spell/interrogation_greater.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "pain"]
levels = [
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
School: necromancy \[evil, pain\]
Level: 4: Inquisitor
Casting Time: 1 round
Components: V, S
Range: touch
Target: living creature touched
Duration: 1 minute/level
Saving Throw: Fortitude negates
Spell Resistance: yes
:::

This spell functions as _[interrogation](ref/spell/interrogation)_, except you may ask one question
per caster level and the spell deals damage equal to 1d8 points plus your Wisdom bonus if the target
doesn't answer a question.
