+++
id = "ref/spell/storm-of-vengeance"
kind = "spell"
title = "Storm of Vengeance"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storm_of_vengeance", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Cleric", level = 9 },
  { class = "Druid", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Witch", level = 9 },
]
casting_time = "1 round"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "360-ft.-radius storm cloud" },
]
duration = "concentration (maximum 10 rounds) (D)"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Cleric, Druid, Oracle, Shaman, Witch
Casting time: 1 round
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: concentration (maximum 10 rounds) (D)
Saving throw: see text
Spell resistance: yes
Effect: 360-ft.-radius storm cloud
Subschool: Summoning
:::

**Sources:** PRPG Core Rulebook pg 350

You create a huge black storm cloud in the air. Each creature under the cloud must succeed on a
Fortitude save or be deafened for 1d4 × 10 minutes. Each round you continue to concentrate, the
spell generates additional effects as noted below. Each effect occurs on your turn.

_2nd Round:_ Acid rains down in the area, dealing 1d6 points of acid damage (no save).

_3rd Round:_ You call six bolts of lightning down from the cloud. You decide where the bolts strike.
No two bolts may be directed at the same target. Each bolt deals 10d6 points of electricity damage.
A creature struck can attempt a Reflex save for half damage.

_4th Round:_ Hailstones rain down in the area, dealing 5d6 points of bludgeoning damage (no save).

_5th through 10th Rounds:_ Violent rain and wind gusts reduce visibility. The rain obscures all
sight, including [darkvision](ref/rule/darkvision), beyond 5 feet. A creature 5 feet away has
concealment (attacks have a 20% miss chance). Creatures farther away have total concealment (50%
miss chance, and the attacker cannot use sight to locate the target). Speed is reduced by
three-quarters.

Ranged attacks within the area of the storm are impossible. Spells cast within the area are
disrupted unless the caster succeeds on a [concentration](ref/rule/concentration) check against a DC
equal to the storm of vengeance's save DC + the level of the spell the caster is trying to cast.
