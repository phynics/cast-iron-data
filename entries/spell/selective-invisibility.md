+++
id = "ref/spell/selective-invisibility"
kind = "spell"
title = "Selective Invisibility"
aon = "SpellDisplay.aspx?ItemName=Selective%20Invisibility"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "selective_invisibility", path = "json/spells15.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "31"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (three translucent pebbles)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you and one other creature" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Magus, Skald, Sorcerer, Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (three translucent pebbles)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Target: you and one other creature
Subschool: Glamer
Descriptors: glamer
:::

Upon casting this spell, you turn invisible, as per the [invisibility](ref/spell/invisibility)
spell, and you choose a second target. That creature can still see you as though you were not
invisible, and you can attack that creature without ending the invisibility effect on you. However,
if you attack any other creature, this spell ends. If you cast this spell multiple times, you can
attack any of the affected creatures without ending the spell.
