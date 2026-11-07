+++
id = "ref/spell/interrogation-greater"
kind = "spell"
title = "Greater Interrogation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "interrogation_greater", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "pain"]
levels = [
  { class = "Inquisitor", level = 4 },
  { class = "Psychic", level = 4 },
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
title = "Spell statistics"
School: necromancy
Level: 4: Inquisitor, Psychic
Casting time: 1 round
Components: V, S
Range: touch
Target: living creature touched
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: yes
Descriptors: evil, pain
:::

## Interrogation

**Sources:** Ultimate Magic pg 225

You question the target, backed up by the threat of magical pain. You may ask one question per two
caster levels. The target can either answer the question or take 1d4 points of damage plus your
Wisdom bonus. The target is not compelled to answer truthfully, but the threat of pain gives it a -4
penalty on Bluff checks to convince you when it is lying.

### Greater Interrogation

**Sources:** Ultimate Magic pg 225

This spell functions as interrogation, except you may ask one question per caster level and the
spell deals damage equal to 1d8 points plus your Wisdom bonus if the target doesn't answer a
question.
