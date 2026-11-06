+++
id = "ref/spell/miasmatic-form"
kind = "spell"
title = "Miasmatic Form"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "miasmatic_form", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air", "poison"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S, M (contact or inhaled poison worth 100 gp)"
range = "touch"
effects = [
  { label = "Target", value = "willing corporeal creature touched" },
]
duration = "1 minute/level"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Investigator, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, M (contact or inhaled poison worth 100 gp)
Range: touch
Duration: 1 minute/level
Saving throw: none, see text
Spell resistance: no
Target: willing corporeal creature touched
Descriptors: air, poison
:::

**Sources:** Advanced Race Guide pg 160

> _[Sylphs](ref/race/sylph) have access to the following spell._

This spell functions like gaseous form, except the target's vaporous body is dangerous to creatures
that touch it. A creature can make a Fortitude save (DC 14 + your Intelligence modifier) on its turn
to resist the vapors. When you cast this spell, you select one of the following options.

_Stinking cloud:_ The target's body nauseates creatures that fail their saving throws, as stinking
cloud (Fortitude negates, see text). This form of the spell does not require a material component.

_Poisonous cloud:_ The target's body is deadly poison, dealing 1d2 points of Constitution damage to
creatures that fail their saves (Fortitude halves). This form of the spell requires a material
component.
