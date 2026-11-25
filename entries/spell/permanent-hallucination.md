+++
id = "ref/spell/permanent-hallucination"
kind = "spell"
title = "Permanent Hallucination"
aon = "SpellDisplay.aspx?ItemName=Permanent%20Hallucination"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "permanent_hallucination", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/audiovisual-hallucination" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "221"

[fields]
kind = "spell"
school = "illusion"
subschools = ["phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent (D)"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: S
Range: long (400 ft. + 40 ft./level)
Duration: permanent (D)
Saving throw: Will disbelief
Spell resistance: yes
Target: one creature
Subschool: phantasm
Descriptors: mind-affecting
:::

### Permanent Hallucination

This spell functions as [audiovisual hallucination](ref/spell/audiovisual-hallucination), except
that the phantasm you create includes visual, auditory, olfactory, tactile, and thermal components,
and the phantasm follows a complex script. The phantasm follows that script without your having to
concentrate on it and can react to stimuli the target perceives, as appropriate for the script.
Unlike most illusions with a save to disbelieve, if the target disbelieves a permanent
hallucination, she can choose to end the effect entirely at any time.
