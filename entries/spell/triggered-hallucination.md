+++
id = "ref/spell/triggered-hallucination"
kind = "spell"
title = "Triggered Hallucination"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "triggered_hallucination", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/audiovisual-hallucination" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "227"

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

### Triggered Hallucination

This spell functions as [audiovisual hallucination](ref/spell/audiovisual-hallucination), except
that this spell's phantasm has no apparent effect until a specific condition occurs. You must
overcome the target's [spell resistance](ref/rule/spell-resistance) to plant the triggered
hallucination, but the target doesn't attempt a Will save to disbelieve the illusion until the
condition occurs (at which point it receives an automatic Will save, as with audiovisual
hallucination). The phantasm can include auditory, olfactory, visual, tactile, and thermal elements,
including intelligible speech.

You set the triggering condition (such as hearing a certain word or seeing a type of creature) when
casting the spell. The event that triggers the illusion can be as general or detailed as desired but
must be based on an audible, tactile, olfactory, or visual trigger. The trigger can't be based on
any quality not normally obvious to the senses, such as alignment. Triggered hallucination uses the
target's senses to notice triggers.
