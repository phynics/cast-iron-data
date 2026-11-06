+++
id = "ref/spell/feast-of-ashes"
kind = "spell"
title = "Feast of Ashes"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feast_of_ashes", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of ash)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "2 days/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Occultist, Psychic, Witch
Casting time: 1 standard action
Components: V, S, M (a pinch of ash)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 days/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

**Sources:** Advanced Player's Guide pg 220

You curse the target with a hunger no food can assuage. On a failed saving throw, the target begins
to starve. The effects of this spell cannot inflict more nonlethal damage than the target has hit
points. No amount of eating can counter the effect and, further, even attempting to eat causes the
target to become nauseated for 1 round unless they make a DC 12 Fortitude save. The target still
experiences the other normal effects of anything consumed (such as poisons or potions). Feast of
ashes can be removed with a [break enchantment](ref/spell/break-enchantment),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish) spell, but effects suffered as a
result of starvation must be healed by normal means.

### Mythic Feast of Ashes

**Sources:** Mythic Adventures pg 93\
On a failed save, the target immediately takes 1d6 points of nonlethal damage per tier. Add your
tier to the DC of any further Constitution checks the target attempts to resist the effects of
starvation as part of this spell's effects. While the curse is in effect, the target gains no
benefit from any spell, effect, or item that requires eating, such as the food from a
[heroes' feast](ref/spell/heroes-feast) spell (though the food is still used up when the target eats
it).
