+++
id = "ref/spell/power-word-kill"
kind = "spell"
title = "Power Word Kill"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "power_word_kill", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["death", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature with 100 hp or less" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one living creature with 100 hp or less
Subschool: Compulsion
Descriptors: death, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 324

You utter a single word of power that instantly kills one creature of your choice, whether the
creature can hear the word or not. Any creature that currently has 101 or more hit points is
unaffected by power word kill.

### Mythic Power Word Kill

**Sources:** Mythic Adventures pg 103\
Treat the target's current hit point total as though it were lowered by 5 times your tier. For
example, a 3rd-tier archmage casting mythic power word kill would instantly kill a creature with 85
hit points or fewer.

You can target a creature with more hit points than this spell could normally affect, causing it to
become exhausted.

_Augmented (6th):_ If you expend four uses of mythic power, the magic of the word lingers around the
target. Until the beginning of your next turn, if the target's hit point total drops to the point
that this spell would have killed it upon casting, it's instantly slain.
