+++
id = "ref/spell/nixies-lure"
kind = "spell"
title = "Nixie's Lure"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nixies_lure", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "179"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting", "sonic"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "300 ft."
effects = [
  { label = "Target", value = "all creatures within a 300-ft.-radius burst centered on you" },
]
duration = "concentration+ 1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Psychic, Skald\
4: Arcanist, Druid, Hunter, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 300 ft.
Duration: concentration+ 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: all creatures within a 300-ft.-radius burst centered on you
Subschool: Charm
Descriptors: mind-affecting, sonic
:::

> _[Undines](ref/race/undine) have access to the following spell._

This spell creates an unearthly and infectious song that seductively summons all who hear it.
Nixie's lure affects a maximum of 24 Hit Dice of creatures. Creatures in the area who fail their
saves are lured by the song and move toward you using the most direct means available. If the path
leads them into a dangerous area such as through fire or off a cliff, the creatures each receive a
second saving throw to end the effect before moving into peril. Creatures lured by the spell's song
can take no actions other than to defend themselves. A victim within 5 feet of you simply stands
still and for the duration of the spell remains fascinated.
