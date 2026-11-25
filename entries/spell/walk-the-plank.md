+++
id = "ref/spell/walk-the-plank"
kind = "spell"
title = "Walk the Plank"
aon = "SpellDisplay.aspx?ItemName=Walk%20the%20Plank"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "walk_the_plank", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/create-pit" },
]
[[sources]]
publication = "villain-codex"
page = "188"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a shark tooth and a splinter of a ship's hull)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "20-ft.-by-20-ft. hole, 10 ft. deep/4 levels" },
]
duration = "1 round plus 1 round/level"
saving_throw = "Reflex negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a shark tooth and a splinter of a ship's hull)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round plus 1 round/level
Saving throw: Reflex negates (see text)
Spell resistance: no
Effect: 20-ft.-by-20-ft. hole, 10 ft. deep/4 levels
Subschool: creation
:::

### Walk the Plank

This spell functions as per [create pit](ref/spell/create-pit), except as noted here. All but the
top 10 feet of the hole is filled with saltwater, reducing the fall damage for anyone falling into
the pit to 1d3 points of nonlethal damage and allowing Huge or larger creatures at the water's
surface to simply pull themselves out of the pit as part of a normal move action, without a Climb
check. Additionally, the pit contains a single advanced shark for every 4 caster levels you have
(maximum four advanced sharks). If desired, when you cast the spell, you can substitute two of the
summoned sharks for one great white shark. These sharks immediately attack any creature that falls
into the pit, even you. If multiple creatures fall in the pit, the sharks attack randomly. When the
spell ends, creatures inside the hole rise up with the bottom of the pit, as normal for create pit,
but the conjured water and sharks vanish.
