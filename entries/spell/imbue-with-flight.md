+++
id = "ref/spell/imbue-with-flight"
kind = "spell"
title = "Imbue with Flight"
source_ids = ["mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_with_flight", path = "json/spells14.json" },
]
[[sources]]
publication = "mythic-origins"
page = "15"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, M (handful of down)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, M (handful of down)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: object touched
:::

You grant a touched Large or smaller object the ability to fly at a speed of 40 feet with average
maneuverability. It can ascend at half speed and descend at double speed. The targeted object flies
as you direct it, using your Fly skill for any difficult maneuvers. You must be within close range
(25 ft. + 5 ft./2 levels) of the object to direct it, and moving it requires a move action. If not
directed, the object hovers in place (no Fly check required). The maximum weight of the object and
anything carried by it is 500 pounds per caster level (maximum 10,000 pounds).
