+++
id = "ref/spell/audiovisual-hallucination"
kind = "spell"
title = "Audiovisual Hallucination"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "audiovisual_hallucination", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/auditory-hallucination" },
]

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

### Audiovisual Hallucination

**Sources:** Ultimate Intrigue pg 204

This spell functions as [auditory hallucination](ref/spell/auditory-hallucination), except that you
can include the image of any object, creature, or force you imagine or identify for the targets to
imagine. You can move the image while you concentrate. After you cease concentration, you can define
simple movements or changes for the phantasm to perform that can be explained in 25 words or fewer.

The image disappears when struck by an opponent unless you cause the illusion to react appropriately
or instruct it to do so. Its AC is equal to 10 + the level of this spell.
