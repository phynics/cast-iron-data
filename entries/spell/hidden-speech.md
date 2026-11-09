+++
id = "ref/spell/hidden-speech"
kind = "spell"
title = "Hidden Speech"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hidden_speech", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "227"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["language-dependant"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a cipher written on a piece of parchment)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you plus one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bard, Medium, Mesmerist, Psychic, Skald, Witch\
3: Inquisitor
Casting time: 1 standard action
Components: V, S, M/DF (a cipher written on a piece of parchment)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: you plus one creature/level, no two of which can be more than 30 ft. apart
Descriptors: language-dependant
:::

You greatly enhance the ability of the subjects to communicate hidden messages to each other. Each
target gains a +10 competence bonus on Bluff checks to send secret message to other recipients.
Others using opposed Sense Motive checks to decipher these messages receive a -5 penalty. All
subjects affected by the spell must share a language to be able to pass messages.
