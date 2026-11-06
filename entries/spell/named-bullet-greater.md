+++
id = "ref/spell/named-bullet-greater"
kind = "spell"
title = "Greater Named Bullet"
source_ids = ["ultimate-combat", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "named_bullet_greater", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
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
Level: 3: Hunter, Ranger\
4: Arcanist, Inquisitor, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (an item from the selected creature or creature type)
Range: touch
Duration: 10 minutes/level or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one piece of ammunition or one thrown weapon
:::

## Named Bullet

**Sources:** Ultimate Combat pg 238

You imbue the target with deadly accuracy against a selected creature type (and subtype for
humanoids or outsiders) or a specific creature you know and can name. When used against the selected
creature, the ammunition never misfires and is unaffected by [concealment](ref/rule/concealment)
(but not total concealment), and at a range of 30 feet or less, the attack targets the selected
creature's touch AC. When the target hits the selected creature, you must overcome that creature's
[spell resistance](ref/rule/spell-resistance), or this spell has no effect. A normal hit scored
using the target against the selected creature is considered to be a critical threat and deals 1
extra point of damage per caster level (maximum 20), which is not multiplied on a critical hit. A
natural critical hit deals the same extra damage, but that damage is multiplied due to the critical.

Once the target is used to attack the selected creature, successfully or not, this spell is
discharged.

### Mythic Named Bullet

**Sources:** Mythic Adventures pg 102

Increase the critical multiplier of the target weapon by 1 (maximum ×4).

_Augmented (2nd):_ If you expend two uses of mythic power, the target ammunition or weapon returns
to the creature that shot or threw it just before that creature's next turn (similar to a returning
weapon). The spell isn't discharged until the target is used to attempt a second attack against the
named creature. Ammunition that hits is destroyed and doesn't return.

### Greater Named Bullet

**Sources:** Ultimate Combat pg 238

This spell functions like named bullet, except it deals 2 extra points of damage per caster level
(maximum 40).
