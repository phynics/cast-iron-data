+++
id = "ref/spell/spit-venom"
kind = "spell"
title = "Spit Venom"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spit_venom", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "240"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one stream of venom" },
]
duration = "instantaneous; see text"
saving_throw = "Fortitude partial"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Witch\
4: Cleric, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous; see text
Saving throw: Fortitude partial
Spell resistance: no
Effect: one stream of venom
Descriptors: poison
:::

You spit a stream of venom at a target using a ranged touch attack. If the venom hits, it causes
blindness for 1 round. The target must also save or be poisoned by black adder venom; the DC in
successive rounds of the poison is equal to the spell's DC.
