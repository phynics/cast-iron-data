+++
id = "ref/spell/power-word-stun"
kind = "spell"
title = "Power Word Stun"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "power_word_stun", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature with 150 hp or less" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: none
Spell resistance: yes
Target: one creature with 150 hp or less
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 324

You utter a single word of power that instantly causes one creature of your choice to become
stunned, whether the creature can hear the word or not. The duration of the spell depends on the
target's current hit point total. Any creature that currently has 151 or more hit points is
unaffected by power word stun.

|Hit Points|Duration|
| --- | --- |
|50 or less|4d4 rounds|
|51 to 100|2d4 rounds|
|101 to 150|1d4 rounds|

### Mythic Power Word Stun

**Sources:** Mythic Adventures pg 104\
Treat the target's current hit point total as though it were lowered by 5 times your tier. For
example, a 3rd-tier archmage casting this spell would affect a creature with 60 hp as though it had
45 hp, and the spell would last an additional 2d4 rounds.

You can target a creature with more hit points than this spell could normally affect, causing it to
become dazed for 1 round.

_Augmented (6th):_ If you expend three uses of mythic power, the magic of the word lingers around
the target. Until the beginning of your next turn, if the target's hit points are reduced enough to
put it in a lower category for the spell's effects, the spell affects the creature according to its
new hit point total. For example, a creature in the 101 to 150 hp category reduced to 80 hp is
immediately stunned for an additional 1d4 rounds. The spell's effects don't diminish if the target
regains hit points.
