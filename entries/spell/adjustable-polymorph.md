+++
id = "ref/spell/adjustable-polymorph"
kind = "spell"
title = "Adjustable Polymorph"
aon = "SpellDisplay.aspx?ItemName=Adjustable%20Polymorph"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adjustable_polymorph", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/alter-self" },
]
[[sources]]
publication = "advanced-class-guide"
page = "172"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a small piece of doppelganger flesh)"
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
School: transmutation
Level: 4: Alchemist, Arcanist, Bard, Investigator, Magus, Medium, Psychic, Red Mantis Assassin, Shaman, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a small piece of doppelganger flesh)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

This spell functions as [alter self](ref/spell/alter-self), except you can as a swift action alter
the disguise (within the limitations of alter self). For example, you could transform yourself into
a halfling, then a lizardfolk, then an elf, and so on. You can change your form a number of times
equal to your caster level.
