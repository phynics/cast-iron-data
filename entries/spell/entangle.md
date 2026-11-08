+++
id = "ref/spell/entangle"
kind = "spell"
title = "Entangle"
source_ids = ["core-rulebook", "mythic-adventures", "villain-codex", "advanced-class-guide", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entangle", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "plants in a 40-ft.-radius spread" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex partial; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level (D)
Saving throw: Reflex partial; see text
Spell resistance: no
Area: plants in a 40-ft.-radius spread
:::

**Sources:** PRPG Core Rulebook pg 278

This spell causes tall grass, weeds, and other plants to wrap around creatures in the area of effect
or those that enter the area. Creatures that fail their save gain the entangled condition. Creatures
that make their save can move as normal, but those that remain in the area must save again at the
end of your turn. Creatures that move into the area must save immediately. Those that fail must end
their movement and gain the entangled condition. Entangled creatures can attempt to break free as a
move action, making a Strength or Escape Artist check. The DC for this check is equal to the DC of
the spell. The entire area of effect is considered difficult terrain while the effect lasts.

If the plants in the area are covered in thorns, those in the area take 1 point of damage each time
they fail a save against the entangle or fail a check made to break free. Other effects, depending
on the local plants, might be possible at GM discretion.

### Mythic Entangle

**Sources:** Mythic Adventures pg 93

The spell functions in areas without any vegetation, causing plants to spring up out of the ground.
These plants can reach creatures that are up to 10 feet in the air. Plants affected or created by
the spell sprout thorns that deal 1d6 points of damage each round to creatures in the area.
