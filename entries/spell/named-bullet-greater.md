+++
id = "ref/spell/named-bullet-greater"
kind = "spell"
title = "Greater Named Bullet"
source_ids = ["ultimate-combat", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "named_bullet_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/named-bullet" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (an item from the selected creature or creature type)"
range = "touch"
effects = [
  { label = "Target", value = "one piece of ammunition or one thrown weapon" },
]
duration = "10 minutes/level or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Hunter, Ranger\
6: Arcanist, Inquisitor, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (an item from the selected creature or creature type)
Range: touch
Target: one piece of ammunition or one thrown weapon
Duration: 10 minutes/level or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
:::

### Mythic Named Bullet

**Sources:** Mythic Adventures pg 102

Increase the critical multiplier of the target weapon by 1 (maximum ×4).

_Augmented (2nd):_ If you expend two uses of mythic power, the target ammunition or weapon returns
to the creature that shot or threw it just before that creature's next turn (similar to a returning
weapon). The spell isn't discharged until the target is used to attempt a second attack against the
named creature. Ammunition that hits is destroyed and doesn't return.

### Greater Named Bullet

**Sources:** Ultimate Combat pg 238

This spell functions like [named bullet](ref/spell/named-bullet), except it deals 2 extra points of
damage per caster level (maximum 40).
