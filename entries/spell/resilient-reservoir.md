+++
id = "ref/spell/resilient-reservoir"
kind = "spell"
title = "Resilient Reservoir"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resilient_reservoir", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "special, see text" },
]
duration = "1 round/ level"
saving_throw = "none (see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Magus, Mesmerist, Paladin\
4: Arcanist, Psychic, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/ level
Saving throw: none (see below)
Spell resistance: yes
Area: special, see text
:::

**Sources:** Advanced Race Guide pg 49

> _[Half-elves](ref/race/half-elf) have access to the following spell._

Upon casting this spell, damage from melee attacks and touch spells gets transferred into a special
pool that you then redirect before the spell's duration expires.

Each time you are struck by a melee attack or touch spell that deals hit point damage, 1 point of
damage is negated and transferred into the reservoir created by this spell. The total number of
points in the reservoir cannot exceed your caster level (to a maximum of 20 points at 20th level).
As an immediate action, anytime before the spell's duration expires, you can expend a number of
points of energy from the reservoir, granting yourself an insight bonus on one skill check, attack
roll, damage roll, or combat maneuver check, but you must do so before the roll is made. This bonus
is equal to the number of points spent. For every five caster levels, you may call upon the
reservoir one additional time (maximum of four times at 15th level).

If you are reduced to negative hit points while you are under the effect of this spell, the spell
automatically release the remaining magic of the reservoir in a concussive blast of force. All
creatures within a 15-foot radius take 1d6 points of force damage per 2 points remaining in the
reserve (maximum of 10d6). A successful Reflex save halves this damage, and
[spell resistance](ref/rule/spell-resistance) applies to this effect.
