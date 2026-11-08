+++
id = "ref/spell/curse-major"
kind = "spell"
title = "Major Curse"
source_ids = ["core-rulebook", "pathfinder-82-secrets-of-the-sphinx", "ultimate-intrigue", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_major", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bestow-curse" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Adept, Antipaladin, Cleric, Mesmerist, Occultist, Oracle, Shaman, Spiritualist, Warpriest, Witch\
4: Arcanist, Bloodrager, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

### Major Curse

**Sources:** Ultimate Magic pg 215

This spell functions as [bestow curse](ref/spell/bestow-curse), except the DC to remove the curse is
equal to the save DC + 5.
