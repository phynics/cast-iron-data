+++
id = "ref/spell/scripted-hallucination"
kind = "spell"
title = "Scripted Hallucination"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scripted_hallucination", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/audiovisual-hallucination" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "224"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "concentration"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Magus, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: S
Range: long (400 ft. + 40 ft./level)
Duration: concentration
Saving throw: Will disbelief
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Phantasm
Descriptors: mind-affecting
:::

### Scripted Hallucination

This spell functions as [audiovisual hallucination](ref/spell/audiovisual-hallucination), except
that the phantasm includes visual, auditory, olfactory, tactile, and thermal components, and the
phantasm follows a complex script. The phantasm follows that script without your concentration and
can react to stimuli the targets perceive.
