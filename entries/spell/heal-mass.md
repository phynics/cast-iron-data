+++
id = "ref/spell/heal-mass"
kind = "spell"
title = "Mass Heal"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heal_mass", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Shaman", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Cleric, Oracle, Shaman
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Targets: one or more creatures, no two of which can be more than 30 ft. apart
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Healing
:::

## Heal

**Sources:** PRPG Core Rulebook pg 294

Heal enables you to channel positive energy into a creature to wipe away injury and afflictions. It
immediately ends any and all of the following adverse conditions affecting the target: ability
damage, blinded, confused, dazed, dazzled, deafened, diseased, exhausted, fatigued, feebleminded,
insanity, nauseated, poisoned, sickened, and stunned. It also cures 10 hit points of damage per
level of the caster, to a maximum of 150 points at 15th level.

Heal does not remove negative levels or restore permanently drained ability score points.

If used against an undead creature, heal instead acts like [harm](ref/spell/harm).

### Mythic Heal

**Sources:** Mythic Adventures pg 97

The damage cured increases to 15 points of damage per caster level (maximum 225 points).

_Augmented:_ If you expend two uses of mythic power, the spell also acts as
[restoration](ref/spell/restoration).

### Mass Heal

**Sources:** PRPG Core Rulebook pg 294

This spell functions like heal, except as noted above. The maximum number of hit points restored to
each creature is 250.
