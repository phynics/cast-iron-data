+++
id = "ref/spell/adjustable-disguise"
kind = "spell"
title = "Adjustable Disguise"
aon = "SpellDisplay.aspx?ItemName=Adjustable%20Disguise"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adjustable_disguise", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/disguise-self" },
]
[[sources]]
publication = "advanced-class-guide"
page = "172"

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
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Medium, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Glamer
Descriptors: glamer
:::

This spell functions as [disguise self](ref/spell/disguise-self), except as a swift action you can
alter the disguise (within the limitations of disguise self). For example, you could make yourself
look like a young human city guard, then an old elven wizard of the opposite gender, then a halfling
thief, and so on. You can change the disguise a number of times equal to your caster level.
