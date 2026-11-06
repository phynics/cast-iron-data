+++
id = "ref/spell/circle-of-clarity"
kind = "spell"
title = "Circle of Clarity"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "circle_of_clarity", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 8 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a crystal lens worth 100 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "20-ft.-radius emanation centered on a creature, object or point in space" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 7: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Wizard\
8: Shaman
Casting time: 1 standard action
Components: V, S, F (a crystal lens worth 100 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Effect: 20-ft.-radius emanation centered on a creature, object or point in space
:::

**Sources:** Ultimate Magic pg 211

You create a magical emanation that interferes with all figments and glamers within it, giving
creatures a +4 bonus on saving throws to recognize them as illusions. The emanation negates
[concealment](ref/rule/concealment) less than total concealment within the area. Perception checks
to notice creatures or objects within the area gain a bonus equal to half your caster level (maximum
+10). The spell is stationary if cast on a point in space. It is mobile if centered on a creature or
object, though creatures or attended objects can negate the spell with a saving throw or
[spell resistance](ref/rule/spell-resistance).
