+++
id = "ref/spell/toxic-gift"
kind = "spell"
title = "Toxic Gift"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxic_gift", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "243"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous; see text"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin\
3: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous; see text
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Target: living creature touched
Descriptors: poison
:::

You can cast this spell only if you are currently poisoned. You draw upon the poison in your body
and duplicate its effects in the target, which is affected by the same poison you are, except it
uses this spell's DC instead of the poison's normal DC. If you are affected by more than one poison,
you must choose one to afflict upon the target.
