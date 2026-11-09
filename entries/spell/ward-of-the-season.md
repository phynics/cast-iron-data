+++
id = "ref/spell/ward-of-the-season"
kind = "spell"
title = "Ward of the Season"
aon = "SpellDisplay.aspx?ItemName=Ward%20of%20the%20Season"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ward_of_the_season", path = "json/spells11.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Druid, Hunter, Ranger, Shaman, Witch\
4: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: one creature
:::

> _Most know of elven magic for its power, but those who delve deeper discover its elegance and ties
> to the natural world. The following spell is just one that the [elves](ref/race/elf) are known
> for._

This spell harnesses the power of the seasons to protect the target and grant a number of bonuses.
This spell has one of four different effects. The caster of the spell can select any one of the
following four effects, but can change the effect as a standard action that reduces the total
remaining duration by 1 hour.

_Spring:_ The target is wrapped in light vines, culminating in a crown of bright, beautiful flowers.
While the spell remains in effect, the target is immune to bleed effects and regains 1 hit point per
round whenever below 0 hit points, as long as the target is still alive. This stabilizes the target.
For each hit point restored in this way, the spell's total remaining duration is reduced by 1 hour.

_Summer:_ The target is surrounded by tiny motes of light. While the spell remains in effect, the
target's base speed increases 10 feet. The target may instead increase its base speed by 30 feet for
1 round by reducing the spell's total remaining duration by 1 hour.

_Fall:_ A cloak of autumn leaves appears on the target. While the spell remains in effect, the
target gains a +2 morale bonus on Fortitude saves. The target can decide to roll twice on any saving
throw against disease or poison and take the higher result by reducing the spell's total remaining
duration by 1 hour.

_Winter:_ A flutter of snow and crisp air surrounds the target. While this spell remains in effect,
the target automatically succeeds at Acrobatics skill checks made to avoid falling while moving
across slick or narrow surfaces. The target can move freely through difficult terrain for 1 round by
reducing the spell's remaining duration by 1 hour. Difficult terrain created by magic affects the
target normally.
