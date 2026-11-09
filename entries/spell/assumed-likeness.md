+++
id = "ref/spell/assumed-likeness"
kind = "spell"
title = "Assumed Likeness"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "assumed_likeness", path = "json/spells.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "58"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will disbelief"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Bard, Medium, Mesmerist, Skald\
2: Arcanist, Magus, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: Will disbelief
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Phantasm
Descriptors: emotion, mind-affecting
:::

You draw upon the memories of the targets to create a visual disguise for yourself that only they
can see. When you cast the spell, you choose an emotion from the table below. Each target perceives
you as a creature it feels that way toward. If it doesn't feel that way toward anyone, it instead
perceives you as a stranger with features likely to evoke that emotion (e.g., if you choose respect,
a guard who was taught to respect her elders but who currently knows no elders might see you as an
elderly version of yourself). Since you don't know how you will appear to each target, you must
match your actions and statements to fit with the illusion as best you can. While the spell grants a
+10 bonus on Disguise checks like disguise self does, you also take a -5 penalty on Disguise checks
until you can get a sense of who the target thinks you are. Each target who fails to disbelieve the
phantasm and is fooled by your Disguise check takes a -2 penalty on Sense Motive checks to notice
your lies, and each emotion choice grants you an additional benefit against such targets, as listed
in the table below.

|Emotion|Effect|
| --- | --- |
|Fear|+4 bonus on Intimidate checks|
|Hate|+2 bonus on attack rolls, -2 penalty to AC|
|Lust|+4 bonus on Sleight of Hands checks|
|Respect|+4 bonus on Diplomacy checks|
|Trust|+4 bonus on Bluff checks|
