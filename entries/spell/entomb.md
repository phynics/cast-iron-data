+++
id = "ref/spell/entomb"
kind = "spell"
title = "Entomb"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entomb", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 minute"
components = "V, S, M (a pristine geode worth at least 1,000 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "up to three 10-ft. cubes/level (S)" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Arcanist, Druid, Shaman, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M (a pristine geode worth at least 1,000 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: permanent
Saving throw: none
Spell resistance: no
Effect: up to three 10-ft. cubes/level (S)
Descriptors: earth
:::

**Sources:** Heroes of the Darklands pg 20

You designate an aboveground area and send it deep within the earth. During the casting of this
spell, the chosen area is rocked by minor tremors that alert nearby creatures to the impending
danger. Once the spell is complete, the chosen area is drawn into the earth and buried in a
self-contained vault, with the uppermost point at a depth of up to 10 feet per caster level below
the surface. The surrounding atmosphere and all creatures within the selected area at the end of the
spell's casting time are entombed in this vault.

The magic of the vault maintains the natural light, temperature, and air quality of the area as it
originally existed aboveground, but any magical effects that affected these qualities do not have
their duration extended. For example, a sunny field would remain brightly lit indefinitely, despite
being buried underground, while a [daylight](ref/spell/daylight) spell would expire at the end of
that spell's duration.

When creating the vault, you can leave a tunnel to the surface world (up to 20 feet wide), or you
can completely isolate the vault from the outside world. Casting this spell does not destroy or
damage anything that may have existed in the ground where you choose to place this vault, but
instead pushes it farther down into the earth. Should your vault be dispelled, the entombed area
returns to the surface, and anything that may have been displaced by the vault returns to its
original place. If there is something already on the surface that blocks the vault's path, the vault
pushes it harmlessly aside when returning.
