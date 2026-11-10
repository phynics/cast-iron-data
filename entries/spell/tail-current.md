+++
id = "ref/spell/tail-current"
kind = "spell"
title = "Tail Current"
aon = "SpellDisplay.aspx?ItemName=Tail%20Current"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tail_current", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/tailwind" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "236"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "120 ft."
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 120 feet apart" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Occultist, Ranger, Shaman, Spiritualist\
4: Arcanist, Bloodrager, Cleric, Magus, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: 120 ft.
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: one or more creatures, no two of which can be more than 120 feet apart
Descriptors: air
:::

### Tail Current

This spell functions as [tailwind](ref/spell/tailwind) except it creates a helpful current in water
instead of in the air. It grants free movement while swimming rather than while flying and functions
only underwater.
