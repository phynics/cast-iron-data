+++
id = "ref/spell/second-wind"
kind = "spell"
title = "Second Wind"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "second_wind", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["air"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 swift action or 1 immediate action; see text"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Antipaladin, Cleric, Hunter, Inquisitor, Oracle, Paladin, Ranger, Warpriest
Casting time: 1 swift action or 1 immediate action; see text
Components: V
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
Descriptors: air
:::

**Sources:** Elemental Master's Handbook pg 18

You can cast this spell only when you have fewer than one-quarter of your total hit points. With a
gasping utterance, you summon invigorating air to fill your lungs. You heal 2d8 points of damage + 1
point per caster level (maximum +10). You can cast this spell either as a swift action on your turn
or as an immediate action when you are brought to below 0 hit points. If you do not breathe, you
can't benefit from this spell.
