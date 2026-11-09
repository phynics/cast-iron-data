+++
id = "ref/spell/dimensional-bounce"
kind = "spell"
title = "Dimensional Bounce"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimensional_bounce", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "179"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "you and touched objects or other touched willing creatures" },
]
duration = "1 round/level or until discharged"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Summoner, Unchained Summoner\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until discharged
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Targets: you and touched objects or other touched willing creatures
Subschool: Teleportation
:::

You designate two locations within range and create a dimensional link between them; you must have
line of effect to both locations when casting this spell. As a swift action, you can teleport from
your current location to either of the designated locations as if you had cast dimension door. The
spell is discharged once you have used it to teleport a number of times equal to one-fourth your
caster level (maximum 5 times).
