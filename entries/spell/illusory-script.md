+++
id = "ref/spell/illusory-script"
kind = "spell"
title = "Illusory Script"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "illusory_script", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 minute per page"
components = "V, S, M (lead-based ink worth 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one touched object weighing no more than 10 lbs." },
]
duration = "one day/level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 minute per page
Components: V, S, M (lead-based ink worth 50 gp)
Range: touch
Duration: one day/level (D)
Saving throw: Will negates; see text
Spell resistance: yes
Target: one touched object weighing no more than 10 lbs.
Subschool: Phantasm
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 299

You write instructions or other information on parchment, paper, or any suitable writing material.
The illusory script appears to be some form of foreign or magical writing. Only the person (or
people) designated by you at the time of the casting can read the writing; it's unintelligible to
any other character.

Any unauthorized creature attempting to read the script triggers a potent illusory effect and must
make a saving throw. A successful saving throw means the creature can look away with only a mild
sense of disorientation. Failure means the creature is subject to a suggestion implanted in the
script by you at the time the illusory script spell was cast. The suggestion lasts only 30 minutes.
Typical suggestions include "Close the book and leave," "Forget the existence of this note," and so
forth. If successfully dispelled by [dispel magic](ref/spell/dispel-magic), the illusory script and
its secret message disappear. The hidden message can be read by a combination of the
[true seeing](ref/spell/true-seeing) spell with the [read magic](ref/spell/read-magic) or
[comprehend languages](ref/spell/comprehend-languages) spell.
