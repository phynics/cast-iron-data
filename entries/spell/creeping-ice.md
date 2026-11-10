+++
id = "ref/spell/creeping-ice"
kind = "spell"
title = "Creeping Ice"
aon = "SpellDisplay.aspx?ItemName=Creeping%20Ice"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "creeping_ice", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "178"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "anchored plane of ice, up to one 10-ft. square/level" },
]
duration = "10 minutes/level"
saving_throw = "Reflex negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Summoner\
4: Arcanist, Druid, Hunter, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level
Saving throw: Reflex negates (see text)
Spell resistance: yes
Effect: anchored plane of ice, up to one 10-ft. square/level
Descriptors: cold
:::

This spell covers the floor, the ground, or some other calm horizontal surface (such as a placid
lake or a gentle river) with a sheet of slowly growing ice. The initial sheet of ice cannot form in
an area occupied by physical objects or creatures. Its surface must be smooth and unbroken when
created. The ice is hard, strong, and opaque, and is 1 inch thick per caster level. The ice is
strong enough to support the weight of a typical horse, making it possible for creatures to cross a
body of water.

Each 10-foot square of ice has 3 hit points per inch of thickness. Creatures can hit the ice
automatically. A section of ice whose hit points drop to 0 is destroyed, leaving an area of ice
chunks, slush, and snow that counts as difficult terrain. If a creature tries to break through the
ice with a single attack, the DC for the Strength check is 15 + your caster level.

Each round on your turn, the sheet of ice grows 1 foot in all directions except toward you. This
growth is slow enough that any creature in the area has time to move out of the way or step onto the
ice. If the growing ice completely covers a creature's square, the creature must choose whether it
moves onto the sheet of ice, is knocked prone on the sheet of ice, or is bull rushed into an
adjacent square.
