+++
id = "ref/spell/thorny-entanglement"
kind = "spell"
title = "Thorny Entanglement"
source_ids = ["core-rulebook", "mythic-adventures", "villain-codex", "advanced-class-guide", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thorny_entanglement", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/entangle" },
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

### Mythic Entangle

**Sources:** Mythic Adventures pg 93

The spell functions in areas without any vegetation, causing plants to spring up out of the ground.
These plants can reach creatures that are up to 10 feet in the air. Plants affected or created by
the spell sprout thorns that deal 1d6 points of damage each round to creatures in the area.

### Thorny Entanglement

**Sources:** Advanced Class Guide pg 196

This spell functions as [entangle](ref/spell/entangle), except the plants also grow thorns and can
fling them up to 15 feet. Any creature that moves within 15 feet of the spell's area is attacked
once on its turn by the animated plants. The plants use your caster level as their base attack bonus
and add your spellcasting ability score modifier (Intelligence for witches; Wisdom for druids,
rangers, and shamans) to the attack roll. A volley of thorns counts as a thrown weapon and deals 2d6
points of piercing damage on a successful hit. A creature that enters the spell's area or ends its
turn there automatically takes 2d6 points of piercing damage.
