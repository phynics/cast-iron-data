+++
id = "ref/spell/yellow-sign"
kind = "spell"
title = "Yellow Sign"
source_ids = ["pathfinder-110-the-thrushmoor-terror"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "yellow_sign", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, M (ochre and sulfur, plus powdered gold worth a total of 15,000 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Bard, Skald\
9: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (ochre and sulfur, plus powdered gold worth a total of 15,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Effect: one symbol
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Pathfinder \#110: The Thrushmoor Terror pg 72

> _Priests of [Hastur](ref/faith/hastur) have access to the following spell._

This spell functions as per [symbol of death](ref/spell/symbol-of-death), save that creatures that
succumb to this spell become dominated (as per [dominate monster](ref/spell/dominate-monster)) by
[Hastur](ref/monster/great-old-one-hastur). This causes such creatures to seek to aid any obvious
minions or worshipers of Hastur in sight, and any true worshiper of Hastur can command the affected
creatures as if that worshiper had been the one to dominate them. In the case of conflicting
commands issued from different true worshipers of Hastur, the commanders must attempt opposed
Charisma checks, with the winner being able to command the targets for that round. If no worshipers
or agents of Hastur are in sight, an affected creature can act normally. When affected by this
spell's Yellow Sign in this way, the effects last for 1 round per level. Once triggered, the Yellow
Sign remains active for 10 minutes per caster level.

There is a 1% chance when a creature fails its saving throw against this spell that Hastur takes
note and, for reasons of his own, decides to control the target personally. In this case, the
actions taken by the dominated creature are left to the GM to determine, but the effects of this
spell's Yellow Sign persist for 1 day per level and the commands issued cannot be countermanded by
any other creature, even if they are Hastur worshipers.

Regardless of how long the effects last or whether Hastur directly controls a victim, if a creature
failed to resist this spell's effects, Hastur can target that victim for the rest of its life with
his fulvous dreams ability. Whether or not the Great Old One ever chooses to do so is left to the GM
to determine.

Yellow Sign can be made permanent with a [permanency](ref/spell/permanency) spell by a caster of
18th level or higher for the cost of 40,000 gp.
