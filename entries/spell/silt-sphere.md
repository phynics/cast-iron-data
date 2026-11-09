+++
id = "ref/spell/silt-sphere"
kind = "spell"
title = "Silt Sphere"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silt_sphere", path = "json/spells9.json" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "21"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a smooth stone)"
range = "20 ft."
effects = [
  { label = "Effect", value = "20-ft.-radius centered on you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a smooth stone)
Range: 20 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Effect: 20-ft.-radius centered on you
Subschool: Glamer
Descriptors: glamer
:::

This spell generates an illusory silt cloud that drifts around you and moves with you. The cloud
provides total [concealment](ref/rule/concealment) to creatures within it (including you) when the
spell is cast. Creatures moving into the cloud after the spell is cast gain concealment (but not
total concealment) due to the illusion. Any creatures within the cloud can see each other normally
and can see out from within the cloud as though it were transparent. If a creature other than you
that has total concealment due to the cloud makes an attack against any foe, it loses total
concealment and gains concealment instead. If you make an attack against any creature, the spell
ends.

A creature that examines the cloud from the outside and succeeds at a DC 20 Knowledge (nature) check
notices the silt cloud is unnaturally compact and fast moving, and that creature can attempt an
immediate saving throw to disbelieve the illusion. Other circumstances (such as if the silt cloud
floats in the middle of otherwise clear waters) can modify the DC of the Knowledge (nature) check.

This spell can be cast only underwater.
