+++
id = "ref/spell/unholy-blight"
kind = "spell"
title = "Unholy Blight"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unholy_blight", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil"]
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
  { label = "Area", value = "20-ft.-radius spread" },
]
duration = "instantaneous (1d4 rounds); see text"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous (1d4 rounds); see text
Saving throw: Will partial
Spell resistance: yes
Area: 20-ft.-radius spread
Descriptors: evil
:::

**Sources:** PRPG Core Rulebook pg 364

You call up unholy power to smite your enemies. The power takes the form of a cold, cloying miasma
of greasy darkness. Only good and neutral (not evil) creatures are harmed by the spell.

The spell deals 1d8 points of damage per two caster levels (maximum 5d8) to a good creature (or 1d6
per caster level, maximum 10d6, to a good outsider) and causes it to be sickened for 1d4 rounds. A
successful Will save reduces damage to half and negates the sickened effect. The effects cannot be
negated by [remove disease](ref/spell/remove-disease) or [heal](ref/spell/heal), but
[remove curse](ref/spell/remove-curse) is effective.

The spell deals only half damage to creatures who are neither evil nor good, and they are not
sickened. Such a creature can reduce the damage by half again (down to one-quarter) with a
successful Will save.
