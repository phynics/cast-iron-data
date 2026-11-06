+++
id = "ref/spell/fog-cloud"
kind = "spell"
title = "Fog Cloud"
source_ids = ["core-rulebook", "mythic-adventures", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fog_cloud", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "fog spreads in 20-ft. radius" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Druid, Hunter, Magus, Shaman, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Effect: fog spreads in 20-ft. radius
Subschool: Creation
:::

**Sources:** PRPG Core Rulebook pg 284

A bank of fog billows out from the point you designate. The fog obscures all sight, including
[darkvision](ref/rule/darkvision), beyond 5 feet. A creature within 5 feet has concealment (attacks
have a 20% miss chance). Creatures farther away have total concealment (50% miss chance, and the
attacker can't use sight to locate the target).

A moderate wind (11+ mph) disperses the fog in 4 rounds; a strong wind (21+ mph) disperses the fog
in 1 round.

The spell does not function underwater.

### Mythic Fog Cloud

**Sources:** Mythic Adventures pg 95

The radius of the fog increases to 50 feet.

_Augmented (3rd):_ If you expend two uses of mythic power, the fog's radius changes to 500 feet, and
its height changes to 100 feet. Winds can't dissipate the fog unless the area of the wind affects
the entire area of the augmented mythic fog cloud. If you're at least 6th tier and instead expend
three uses of mythic power, the range increases to 1 mile, the fog's radius changes to 1 mile, and
its height changes to 500 feet. The cloud is as resistant to wind as the 3rd-tier augmented version.

### Poisonous Cloud

**Sources:** Potions and Poisons pg 11

Poisonous cloud creates a bank of fog like that created by fog cloud, except that the vapors are
toxic. The cloud deals 1d2 points of Constitution damage per round to living creatures that fail
their Fortitude saves. A creature that succeeds at its save but remains in the cloud must continue
to attempt a new saving throw each round on your turn.

Poisonous cloud can be made permanent with a [permanency](ref/spell/permanency) spell cast by a
caster of 13th level or higher, at a cost of 12,500 gp. A permanent poisonous cloud dispersed by
wind re-forms in 10 minutes.
