+++
id = "ref/spell/power-word-blind"
kind = "spell"
title = "Power Word Blind"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "power_word_blind", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature with 200 hp or less" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Mesmerist\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text
Saving throw: none
Spell resistance: yes
Target: one creature with 200 hp or less
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 324

You utter a single word of power that causes a creature to become blinded, whether the creature can
hear the word or not. The duration of the spell depends on the target's current hit point total. Any
creature that currently has 201 or more hit points is unaffected.

|Hit Points|Duration|
| --- | --- |
|50 or less|Permanent|
|51 to 100|1d4+1 minutes|
|101 to 200|1d4+1 rounds|

### Mythic Power Word Blind

**Sources:** Mythic Adventures pg 103\
Treat the target's current hit point total as though it were lowered by 5 times your tier. For
example, a 3rd-tier archmage casting mythic power word blind would affect a creature with 60 hp as
though it had 45 hp, and the spell would permanently blind the target.

You can target a creature with more hit points than this spell could normally affect, causing it to
treat all opponents as though they had concealment (20% miss chance) for 1d4 rounds.

_Augmented (3rd):_ If you expend two uses of mythic power, the magic of the word lingers around the
target. Until the beginning of your next turn, if the target's hit points are reduced enough to put
it in a lower category for the spell's effects, the spell affects the creature according to its new
hit point total. For example, a creature in the 101 to 200 hp category reduced to 80 hp immediately
becomes blinded for 1d4+1 minutes instead of 1d4+1 rounds. The spell's effects don't diminish if the
target regains hit points.
