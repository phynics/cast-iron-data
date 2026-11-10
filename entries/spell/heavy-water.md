+++
id = "ref/spell/heavy-water"
kind = "spell"
title = "Heavy Water"
aon = "SpellDisplay.aspx?ItemName=Heavy%20Water"
source_ids = ["magical-marketplace"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heavy_water", path = "json/spells5.json" },
]
[[sources]]
publication = "magical-marketplace"
page = "8"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "cylinder of water (5-ft. radius/level, 30 ft. deep)" },
]
duration = "1 minute/level (D)"
saving_throw = "none (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Druid, Hunter, Oracle, Ranger, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: none (see text)
Spell resistance: no
Area: cylinder of water (5-ft. radius/level, 30 ft. deep)
Descriptors: water
:::

You cause a volume of water to become heavier than normal. Swimming in or through such water
requires a Swim check with a DC equal to the saving throw DC of this spell; even creatures with a
swim speed must attempt this check. Success allows a creature to swim at up to half its speed as a
full-round action; a creature cannot swim as a move action while in an area of heavy water. If a
creature fails its Swim check by 4 or less, it makes no progress. If it fails by 5 or more, it goes
underwater. All Perception checks to see through the affected water take a -10 penalty. All ships
sailing through an area of heavy water move at half speed.
