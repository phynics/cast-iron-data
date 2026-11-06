+++
id = "ref/spell/mythic-severance"
kind = "spell"
title = "Mythic Severance"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mythic_severance", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Inquisitor, Mesmerist\
4: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

**Sources:** Mythic Adventures pg 114

You restrict the target's access to its mythic power. Each time the target attempts to cast a mythic
spell, expend mythic power to activate a path ability, or use any other effect that requires
expending uses of mythic power, it must attempt a Will saving throw against the DC of this spell. If
it fails this saving throw, the creature loses its action and the ability it was attempting to use
has no effect.

This spell has no effect on mythic abilities that don't require the target to expend mythic power.
