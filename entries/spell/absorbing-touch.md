+++
id = "ref/spell/absorbing-touch"
kind = "spell"
title = "Absorbing Touch"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absorbing_touch", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "200"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Investigator", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 day/level (D)"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Investigator
Casting time: 1 standard action
Components: S
Range: touch
Duration: 1 day/level (D)
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: object touched
:::

You absorb the next object your hand touches into your body. If you are already holding an object,
you can attempt to absorb it; otherwise, you may touch an object as a standard action separate from
casting the spell. You can absorb any nonmagical, nonliving object weighing no more than 1 pound per
caster level. A container and its contents count as a single object. Objects in the possession of
another creature receive a Fortitude saving throw to prevent absorption. You may continue to attempt
to absorb objects until one is absorbed.

An absorbed object melds with your hand and cannot be targeted, but the object's weight still counts
against your carrying capacity. If you dismiss the spell, the item appears in the hand that absorbed
it, or falls to the ground if that hand is full. Multiple castings let you absorb additional items,
but you can only store a single item per hand.
