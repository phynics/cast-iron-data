+++
id = "ref/spell/grease-greater"
kind = "spell"
title = "Greater Grease"
source_ids = ["core-rulebook", "mythic-adventures", "dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grease_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/grease" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (butter)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one object/2 levels or 1 10-ft. square/2 levels; see text" },
]
duration = "1 minute/level (D)"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Bard, Magus, Skald, Sorcerer, Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (butter)
Range: medium (100 ft. + 10 ft./level)
Target: one object/2 levels or 1 10-ft. square/2 levels; see text
Duration: 1 minute/level (D)
Saving throw: see text
Spell resistance: no
Subschool: Creation
:::

### Mythic Grease

**Sources:** Mythic Adventures pg 96

If you cast mythic grease on an area, add your tier to the Acrobatics DC to move within or through
the area. If you cast it on a creature's armor or clothing, add your tier to its Escape Artist
checks and combat maneuver checks attempted to escape a grapple and to its CMD to avoid being
grappled.

_Augmented:_ You can expend two uses of mythic power to make the grease flammable. It ignites from
any fire at least the size of a candle flame. If a greased area is ignited, any creature in the area
on your turn takes 1d3 points of fire damage and might catch on fire. If a greased creature is
ignited, it takes 2d6 points of fire damage, and might catch on fire; add your tier to the save DC.

### Greater Grease

**Sources:** Dirty Tactics Toolbox pg 30

This spell functions like [grease](ref/spell/grease), except as noted here. When you use this spell
to cover a solid surface with slippery grease, the 10-foot squares must form a continuous area, each
part of which must be within the spell's range. When you use this spell to create a greasy coating
on items, no two of the targeted items can be more than 30 feet apart. You cannot target both items
and surfaces with a single casting of this spell.
