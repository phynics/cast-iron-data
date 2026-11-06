+++
id = "ref/spell/chaos-hammer"
kind = "spell"
title = "Chaos Hammer"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chaos_hammer", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["chaotic"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius burst" },
]
duration = "instantaneous (1d6 rounds); see text"
saving_throw = "Will partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous (1d6 rounds); see text
Saving throw: Will partial; see text
Spell resistance: yes
Area: 20-ft.-radius burst
Descriptors: chaotic
:::

**Sources:** PRPG Core Rulebook pg 254

You unleash chaotic power to smite your enemies. The power takes the form of a multicolored
explosion of leaping, ricocheting energy. Only lawful and neutral (not chaotic) creatures are harmed
by the spell.

The spell deals 1d8 points of damage per two caster levels (maximum 5d8) to lawful creatures (or 1d6
points of damage per caster level, maximum 10d6, to lawful outsiders) and slows them for 1d6 rounds
(see the [slow](ref/spell/slow) spell). A successful Will save reduces the damage by half and
negates the slow effect.

The spell deals only half damage against creatures who are neither lawful nor chaotic, and they are
not slowed. Such a creature can reduce the damage by half again (down to one-quarter) with a
successful Will save.

### Mythic Chaos Hammer

**Sources:** Mythic Adventures pg 88\
The damage dealt to lawful outsiders increases to 1d10 points of damage per caster level (maximum
10d10), and the damage dealt to other lawful creatures increases to 1d12 points of damage per 2
caster levels (maximum 5d12). The duration of slow increases to 2d6 rounds. Lawful creatures that
succeed at their saves are slowed for 1 round.
