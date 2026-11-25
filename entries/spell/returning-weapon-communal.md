+++
id = "ref/spell/returning-weapon-communal"
kind = "spell"
title = "Communal Returning Weapon"
aon = "SpellDisplay.aspx?ItemName=Returning%20Weapon%2C%20Communal"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "returning_weapon_communal", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/returning-weapon" },
]
[[sources]]
publication = "ultimate-combat"
page = "243"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["teleportation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "weapons that can be thrown" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Hunter, Inquisitor, Magus, Occultist, Ranger\
3: Arcanist, Bard, Cleric, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Targets: weapons that can be thrown
Subschool: teleportation
:::

### Communal Returning Weapon

This spell functions like [returning weapon](ref/spell/returning-weapon), except you divide the
duration in 1-minute intervals among the targeted weapons.
