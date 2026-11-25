+++
id = "ref/spell/complex-hallucination"
kind = "spell"
title = "Complex Hallucination"
aon = "SpellDisplay.aspx?ItemName=Complex%20Hallucination"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "complex_hallucination", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/audiovisual-hallucination" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "206"

[fields]
kind = "spell"
school = "illusion"
subschools = ["phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "concentration+ 3 rounds"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium\
4: Arcanist, Bard, Magus, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: long (400 ft. + 40 ft./level)
Duration: concentration+ 3 rounds
Saving throw: Will disbelief
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: phantasm
Descriptors: mind-affecting
:::

### Complex Hallucination

This spell functions as [audiovisual hallucination](ref/spell/audiovisual-hallucination), except
that the phantasm you create can also include olfactory, tactile, and thermal effects.
