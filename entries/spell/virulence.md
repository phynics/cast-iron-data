+++
id = "ref/spell/virulence"
kind = "spell"
title = "Virulence"
source_ids = ["pathfinder-81-shifting-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "virulence", path = "json/spells11.json" },
]
[[sources]]
publication = "pathfinder-81-shifting-sands"
page = "73"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "40 ft."
effects = [
  { label = "Area", value = "all living creatures within a 40-ft.-radius burst centered on you" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: 40 ft.
Duration: instantaneous
Saving throw: see text
Spell resistance: yes
Area: all living creatures within a 40-ft.-radius burst centered on you
Descriptors: evil
:::

All living creatures within the area of effect, including yourself, must immediately attempt a
saving throw with a -2 penalty against any and all diseases they have contracted, even if the onset
time has not yet elapsed. On a failed saving throw, the affliction has its usual effect. A
successful save does not count toward curing the affliction.
