+++
id = "ref/spell/instigate-psychic-duel"
kind = "spell"
title = "Instigate Psychic Duel"
aon = "SpellDisplay.aspx?ItemName=Instigate%20Psychic%20Duel"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instigate_psychic_duel", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-adventures"
page = "174"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Spiritualist", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Medium, Mesmerist, Occultist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Targets: one creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

You begin a [psychic duel](ref/rule/psychic-duels) with a creature. This psychic duel takes place on
a [binary mindscape](ref/rule/binary-mindscapes) that includes only two minds: yours and the
target's. This spell ends and both minds return to their respective bodies if one of you drops below
0 hit points or if both of you agree to end the psychic duel (a free action that you can perform
even if it isn't your turn).

Even if you cast the spell, you must succeed at a Will save to escape your own psychic duel if your
opponent doesn't want to allow you to leave. Spells like mindscape door can also free you from the
mindscape (and mindscape door is one of the few spells you can cast in a binary mindscape). A binary
mindscape is clearly illusory, and disbelieving the illusion doesn't alter how the mindscape works.
