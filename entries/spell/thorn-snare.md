+++
id = "ref/spell/thorn-snare"
kind = "spell"
title = "Thorn Snare"
source_ids = ["conquest-of-bloodsworn-vale"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thorn_snare", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/snare" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "3 rounds"
components = "V, S, M, DF"
range = "touch"
effects = [
  { label = "Target", value = "touched nonmagical circle of vine, rope, or thong with a 2 ft. diameter + 2 ft./level" },
]
duration = "until triggered or broken"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Hunter, Ranger\
4: Druid
Casting time: 3 rounds
Components: V, S, M, DF
Range: touch
Duration: until triggered or broken
Saving throw: none
Spell resistance: no
Target: touched nonmagical circle of vine, rope, or thong with a 2 ft. diameter + 2 ft./level
:::

**Sources:** Conquest of Bloodsworn Vale pg 29

This spell functions just like the spell [snare](ref/spell/snare) but those caught in it take 1
point of damage per round, as the thorn-covered vine slowly cuts into them. In addition, any attempt
to escape or destroy the snare deals 1d6 points of damage to the trapped creature.

A thorn snare can only be found with a DC 24 Perception check. A trapped creature can escape by
making a DC 24 Escape Artist check or a DC 24 Strength check as a full-round action.

_Material Component:_ A length of blood-thorn rose vine.
