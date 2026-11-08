+++
id = "ref/spell/compel-tongue"
kind = "spell"
title = "Compel Tongue"
source_ids = ["advanced-players-guide", "black-markets", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "compel_tongue", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/share-language" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a page from a dictionary)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Bard, Medium, Mesmerist, Psychic, Skald\
2: Arcanist, Cleric, Druid, Hunter, Occultist, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a page from a dictionary)
Range: touch
Duration: 24 hours
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

### Compel Tongue

**Sources:** Black Markets pg 24

This spell functions as [share language](ref/spell/share-language), granting a creature the ability
to read, understand, and communicate to the best of its ability in any one language you know. For
the spell's entire duration, the target can speak and write only in the language imparted, but its
ability to understand other languages is unaffected.
