+++
id = "ref/spell/sunder-breaker"
kind = "spell"
title = "Sunder Breaker"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sunder_breaker", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (d) or until discharged"
saving_throw = "Will negates (harmless) and see text"
spell_resistance = "yes (harmless) and see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Magus, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level (d) or until discharged
Saving throw: Will negates (harmless) and see text
Spell resistance: yes (harmless) and see text
Target: creature touched
Descriptors: force
:::

**Sources:** Advanced Class Guide pg 195

You place an invisible ward upon the target. The next time a creature succeeds at a sunder combat
maneuver against the target, the attacker's weapon takes 1d6 points of damage per caster level
(maximum 10d6). If the attacker used a natural weapon for the sunder, the attacker takes half this
damage. [Spell resistance](ref/rule/spell-resistance) applies to this damage. The attacker can
attempt a Fortitude save to halve this damage.

The ward on the target counts as a magical trap and can be detected and disabled as such.
