+++
id = "ref/spell/brand"
kind = "spell"
title = "Brand"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brand", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "207"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Inquisitor", level = 0 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 day/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 0: Inquisitor
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 day/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

Brand etches an indelible rune or mark of no more than 6 characters onto a creature, inflicting 1
point of damage. The mark may be placed on any exposed portion of the creature, typically the head
or forearm. A brand can be hidden by clothing or removed by scraping it away (causing 1d6 points of
damage), though the brand returns if the damage is healed.
