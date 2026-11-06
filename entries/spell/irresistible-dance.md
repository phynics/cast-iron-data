+++
id = "ref/spell/irresistible-dance"
kind = "spell"
title = "Irresistible Dance"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "irresistible_dance", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1d4+1 rounds"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Mesmerist, Skald\
8: Arcanist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: 1d4+1 rounds
Saving throw: Will partial
Spell resistance: yes
Target: living creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 303

The subject feels an undeniable urge to dance and begins doing so, complete with foot shuffling and
tapping. The spell effect makes it impossible for the subject to do anything other than caper and
prance in place. The effect imposes a -4 penalty to Armor Class and a -10 penalty on Reflex saves,
and it negates any AC bonus granted by a shield the target holds. The dancing subject provokes
attacks of opportunity each round on its turn. A successful Will save reduces the duration of this
effect to 1 round.

### Mythic Irresistible Dance

**Sources:** Mythic Adventures pg 99\
When casting the spell, you can choose to make the dance either an unending dance or a dance of
death.

A target affected by unending dance receives a new saving throw at the end of each round of dancing,
even if its initial save was successful. If the save fails, the duration of the spell increases by 1
round.

A target affected by the dance of death suffers excruciating pain that inflicts a -4 penalty on
attack rolls, saving throws, and skill checks, and it takes 1d4 points of Constitution damage each
round it spends dancing.

With either form, you can direct the creature like a marionette as a move action, causing it to take
a single move action at half its speed along the path you specify. You must have line of sight to
the target and be within Medium range (100 feet + 10 feet per caster level) to command its movement.
This movement provokes attacks of opportunity as normal, and doesn't count against the target's
movement on its turn. You can't move a target that succeeded at its initial save against the spell.
