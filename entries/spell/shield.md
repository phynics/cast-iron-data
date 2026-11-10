+++
id = "ref/spell/shield"
kind = "spell"
title = "Shield"
aon = "SpellDisplay.aspx?ItemName=Shield"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "342"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Occultist, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: force
:::

Shield creates an invisible shield of force that hovers in front of you. It negates
[magic missile](ref/spell/magic-missile) attacks directed at you. The disk also provides a +4 shield
bonus to AC. This bonus applies against incorporeal touch attacks, since it is a force effect. The
shield has no armor check penalty or arcane spell failure chance.
