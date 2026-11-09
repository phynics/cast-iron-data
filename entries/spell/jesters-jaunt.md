+++
id = "ref/spell/jesters-jaunt"
kind = "spell"
title = "Jester's Jaunt"
aon = "SpellDisplay.aspx?ItemName=Jester%27s%20Jaunt"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jesters_jaunt", path = "json/spells6.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "230"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Bard, Mesmerist, Skald
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Teleportation
:::

You teleport the target to a space you can see within 30 feet of the target. The destination must be
on solid ground, and the teleportation cannot end in a space that is by nature hazardous to the
creature you are teleporting.
