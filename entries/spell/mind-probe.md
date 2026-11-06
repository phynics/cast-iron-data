+++
id = "ref/spell/mind-probe"
kind = "spell"
title = "Mind Probe"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_probe", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 minute"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Mesmerist, Occultist, Psychic\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

**Sources:** Occult Adventures pg 176

You gain access to the subject's memories and knowledge. You can attempt to learn the answer to one
question per round. A successful Will save ends the spell. Otherwise, the creature can attempt a
Bluff check with a DC equal to 11 + your Sense Motive modifier. If it fails its Bluff check, you
gain the answer you desire. If it succeeds at its check, you gain no information. If it succeeds by
5 or more, it answers whatever it chooses, and you believe that wrong answer to be true. Your
questions are purely telepathic inquiries, and the answers to those questions are imparted directly
to your mind. You and the target don't need to speak the same language, though less intelligent
creatures may yield up only appropriate sensory images in answer to your questions.
