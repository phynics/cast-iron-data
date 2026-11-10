+++
id = "ref/spell/interrogation-greater"
kind = "spell"
title = "Greater Interrogation"
aon = "SpellDisplay.aspx?ItemName=Interrogation%2C%20Greater"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "interrogation_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/interrogation" },
]
[[sources]]
publication = "ultimate-magic"
page = "225"

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

### Greater Interrogation

This spell functions as [interrogation](ref/spell/interrogation), except you may ask one question
per caster level and the spell deals damage equal to 1d8 points plus your Wisdom bonus if the target
doesn't answer a question.
