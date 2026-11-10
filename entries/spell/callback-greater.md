+++
id = "ref/spell/callback-greater"
kind = "spell"
title = "Greater Callback"
aon = "SpellDisplay.aspx?ItemName=Callback%2C%20Greater"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "callback_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/callback" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "228"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a crushed grasshopper)"
range = "1 mile/level"
effects = [
  { label = "Target", value = "your familiar or spirit animal" },
]
duration = "1 hour/level or until expended"
saving_throw = "Fortitude negates"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a crushed grasshopper)
Range: 1 mile/level
Target: your familiar or spirit animal
Duration: 1 hour/level or until expended
Saving throw: Fortitude negates
Spell resistance: yes (harmless)
Subschool: Teleportation
:::

### Greater Callback

This spell functions as [callback](ref/spell/callback), except as noted above.
