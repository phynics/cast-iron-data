+++
id = "ref/spell/sun-metal"
kind = "spell"
title = "Sun Metal"
aon = "SpellDisplay.aspx?ItemName=Sun%20Metal"
source_ids = ["ultimate-combat", "faiths-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sun_metal", path = "json/spells16.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "245"
[[sources]]
publication = "faiths-of-purity"
page = "28"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one melee weapon" },
]
duration = "1 round/level (see text)"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Hunter, Oracle, Paladin, Ranger, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (see text)
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: one melee weapon
Descriptors: fire
:::

The target weapon ignites into flame that does not hurt the weapon or the wielder, but damages those
hit by the weapon. When the weapon's wielder hits with this weapon, it deals an additional 1d4
points of fire damage. This damage is not multiplied in the case of a critical hit. This effect
immediately ends if the weapon is submerged in water. This effect does not stack with the flaming or
flaming burst weapon special ability or any other effect that grants the weapon extra fire damage.
It does not function on weapons with the frost or icy burst weapon special ability or any other
effect that grants a weapon extra cold damage.
