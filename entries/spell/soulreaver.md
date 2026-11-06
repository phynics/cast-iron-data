+++
id = "ref/spell/soulreaver"
kind = "spell"
title = "Soulreaver"
source_ids = ["mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulreaver", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "living creatures in a 20-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Fortitude half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude half
Spell resistance: yes
Target: living creatures in a 20-ft.-radius spread
Descriptors: death
:::

**Sources:** Mythic Origins pg 15

Favored by the necromancer Geb as a tool to turn his enemies' armies against themselves, this potent
death spell deals 1d6 points of damage per caster level (maximum 20d6) to living creatures in the
area of effect.

### Mythic Soulreaver

**Sources:** Mythic Origins pg 15\
You can expend one use of mythic power to raise creatures killed by this effect as undead thralls.
You can animate a number of Hit Dice worth of undead up to double your tier as if you had animated
them with [animate dead](ref/spell/animate-dead). The undead created by this spell count toward the
total number of Hit Dice worth of undead you can control.

_Augmented (8th):_ If you expend two uses of mythic power, you can raise slain foes as undead
creatures chosen from the list of undead for create undead. By expending three uses of mythic power,
you can select from the list for create greater undead. The total number of Hit Dice worth of undead
created in this way can't exceed double your tier. Created undead are not automatically under your
control. If you are capable of commanding undead, you may attempt to command the undead creatures as
they form.
