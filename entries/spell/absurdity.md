+++
id = "ref/spell/absurdity"
kind = "spell"
title = "Absurdity"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absurdity", path = "json/spells.json" },
]
[[sources]]
publication = "horror-adventures"
page = "108"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Spiritualist", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "up to one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Bard, Medium, Mesmerist, Psychic, Skald, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: no
Target: up to one creature/level, no two of which can be more than 30 ft. apart
Subschool: Phantasm
Descriptors: emotion, mind-affecting
:::

Your targets perceive intimidation and threats as laughably absurd. A character attempting to
intimidate your targets is instead perceived as having exaggerated facial features or babbling and
awkward speech. Effects that impose fear conditions become objects of ridicule, with the targets
making fun of the source of the object as it attempts to scare them.

Absurdity protects your targets from gaining
[lesser fear conditions](ref/rule/lesser-fear-and-greater-fear) (spooked, shaken, and scared),
granting them immunity to spooked and a 50% chance to negate shaken or scared conditions instead of
gaining them from any effect, including uses of the Intimidate skill to demoralize. Any other effect
related to a spell or ability that generates fear (such as dying from a
[phantasmal killer](ref/spell/phantasmal-killer)) affects them normally, and effects that ignore
immunity to fear also ignore absurdity.

However, target creatures also have serious difficulty noticing potential threats; they take a -10
penalty on Sense Motive checks to avoid surprise or to notice that a creature is actively
threatening or malicious and a -2 penalty on initiative checks. The spell doesn't prevent spells or
effects that provide early warning or a form of danger sense (like
[anticipate peril](ref/spell/anticipate-peril) or [find traps](ref/spell/find-traps)) from alerting
the affected character to danger.
