+++
id = "ref/spell/inflict-light-wounds-mass"
kind = "spell"
title = "Mass Inflict Light Wounds"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_light_wounds_mass", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/inflict-light-wounds" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Cleric, Inquisitor, Occultist, Oracle, Shaman, Warpriest\
6: Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
:::

## Inflict Light Wounds

**Sources:** PRPG Core Rulebook pg 300

When laying your hand upon a creature, you channel negative energy that deals 1d8 points of damage +
1 point per caster level (maximum +5).

Since undead are powered by negative energy, this spell cures such a creature of a like amount of
damage, rather than harming it.

### Mythic Inflict Light Wounds

**Sources:** Mythic Adventures pg 99

The damage dealt increases to 2d8 points of damage + 2 points per caster level (maximum +10). A
living target is sickened for 1 round per caster level (maximum 5 rounds) if it fails its saving
throw.

### Mass Inflict Light Wounds

**Sources:** PRPG Core Rulebook pg 300

Negative energy spreads out in all directions from the point of origin, dealing 1d8 points of
damage + 1 point per caster level (maximum +25) to nearby living enemies.

Like other inflict spells, mass inflict light wounds cures undead in its area rather than damaging
them. A cleric capable of spontaneously casting inflict spells can also spontaneously cast mass
inflict spells.
