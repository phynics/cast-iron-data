+++
id = "ref/spell/returning-weapon"
kind = "spell"
title = "Returning Weapon"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "returning_weapon", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one weapon that can be thrown" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Bloodrager, Hunter, Inquisitor, Magus, Occultist, Ranger\
2: Arcanist, Bard, Cleric, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one weapon that can be thrown
Subschool: Teleportation
:::

**Sources:** Ultimate Combat pg 242

For the duration of the spell, the target weapon acts as if it had the returning weapon special
ability.

This spell can be used as the prerequisite for the returning weapon special ability.

### Communal Returning Weapon

**Sources:** Ultimate Combat pg 243

This spell functions like returning weapon, except you divide the duration in 1-minute intervals
among the targeted weapons.
