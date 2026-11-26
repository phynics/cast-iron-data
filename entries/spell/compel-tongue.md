+++
id = "ref/spell/compel-tongue"
kind = "spell"
title = "Compel Tongue"
aon = "SpellDisplay.aspx?ItemName=Compel%20Tongue"
source_ids = ["advanced-players-guide", "black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "compel_tongue", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/share-language" },
]
[[sources]]
publication = "black-markets"
page = "24"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a wooden block carved with a letter)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Skald\
2: Arcanist, Cleric, Druid, Hunter, Medium, Mesmerist, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a wooden block carved with a letter)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: compulsion
Descriptors: mind-affecting
:::

### Compel Tongue

This spell functions as [share language](ref/spell/share-language), granting a creature the ability
to read, understand, and communicate to the best of its ability in any one language you know. For
the spell's entire duration, the target can speak and write only in the language imparted, but its
ability to understand other languages is unaffected.
