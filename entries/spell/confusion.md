+++
id = "ref/spell/confusion"
kind = "spell"
title = "Confusion"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "confusion", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (three nutshells)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "all creatures in a 15-ft.-radius burst" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Skald\
4: Arcanist, Bloodrager, Occultist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (three nutshells)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: all creatures in a 15-ft.-radius burst
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 258

This spell causes confusion in the targets, making them unable to determine their actions. Roll on
the following table at the start of each subject's turn each round to see what it does in that
round.

|d%|Behavior|
| --- | --- |
|01-25|Act normally|
|26-50|Do nothing but babble incoherently|
|51-75|Deal 1d8 points of damage + Str modifier to self with item in hand|
|76-100|Attack nearest creature (for this purpose, a familiar counts as part of the subject's self)|

A confused character who can't carry out the indicated action does nothing but babble incoherently.
Attackers are not at any special advantage when attacking a confused character. Any confused
character who is attacked automatically attacks its attackers on its next turn, as long as it is
still confused when its turn comes. Note that a confused character will not make attacks of
opportunity against any creature that it is not already devoted to attacking (either because of its
most recent action or because it has just been attacked).
