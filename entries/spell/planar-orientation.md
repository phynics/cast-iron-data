+++
id = "ref/spell/planar-orientation"
kind = "spell"
title = "Planar Orientation"
source_ids = ["the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_orientation", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/know-direction" },
]
[[sources]]
publication = "the-first-world-realm-of-the-fey"
page = "13"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Oracle, Psychic, Ranger, Shaman, Skald, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

This spell helps creatures accustomed to the concrete reality of the Material Plane to navigate
within the confusing realities of other planes. When cast, it functions as
[know direction](ref/spell/know-direction), save that instead of revealing true north, it reveals
the direction of the palace or demesnes most associated with that plane or demiplane's ruling god or
demigod, as well as a brief and generic vision of that entity's appearance or holy symbol. The spell
functions only within whatever plane or demiplane you are located in at the time; for instance, if
cast within a specific demon lord's Abyssal realm or on a given layer of Hell, it would point to the
seat of power for that demon lord or archdevil, not Lamashtu or Asmodeus. If a plane or demiplane
has multiple gods or rulers, such as the [Eldest](ref/rule/the-eldest) of the First World or
Heaven's various Empyreal Lords and deities, it reveals the directions of the closest three,
allowing for triangulation.

This spell reveals the location of the god or demigod's official seat of power only, not the entity
itself, and if such a location is deliberately hidden via magic of any sort, the spell automatically
fails. It does not function on the Material Plane.
