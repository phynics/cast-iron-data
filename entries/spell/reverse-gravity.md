+++
id = "ref/spell/reverse-gravity"
kind = "spell"
title = "Reverse Gravity"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reverse_gravity", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 8 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (lodestone and iron fillings)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "up to one 10-ft. cube/level (S)" },
]
duration = "1 round/level (D)"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Psychic, Sorcerer, Wizard\
8: Druid
Casting time: 1 standard action
Components: V, S, M/DF (lodestone and iron fillings)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none, see text
Spell resistance: no
Area: up to one 10-ft. cube/level (S)
:::

**Sources:** PRPG Core Rulebook pg 335

This spell reverses gravity in an area, causing unattached objects and creatures in the area to fall
upward and reach the top of the area in 1 round. If a solid object (such as a ceiling) is
encountered in this fall, [falling objects](ref/rule/falling-objects) and creatures strike it in the
same manner as they would during a normal downward fall. If an object or creature reaches the top of
the area without striking anything, it remains there, oscillating slightly, until the spell ends. At
the end of the spell duration, affected objects and creatures fall downward.

Provided it has something to hold onto, a creature caught in the area can attempt a Reflex save to
secure itself when the spell strikes. Creatures who can fly or levitate can keep themselves from
falling.

### Mythic Reverse Gravity

**Sources:** Mythic Adventures pg 105\
Creatures in the area or that enter the area must succeed at a Fortitude save or be nauseated.

_Augmented (8th):_ If you expend three uses of mythic power, once per round as a move action you may
select one secured creature (one that succeeded at its Reflex save) or attached object (such as a
tree or cottage) and force it to attempt a Fortitude save against the spell. The selected creature
or object can weigh no more than 100 pounds per caster level. If it fails the save, it's pulled free
and falls upward.
