+++
id = "ref/spell/abundant-ammunition"
kind = "spell"
title = "Abundant Ammunition"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abundant_ammunition", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a single piece of ammunition)"
range = "touch"
effects = [
  { label = "Target", value = "one container touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bard, Cleric, Hunter, Oracle, Psychic, Ranger, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a single piece of ammunition)
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: one container touched
Subschool: Summoning
:::

**Sources:** Ultimate Combat pg 222

When cast on a container such as a quiver or a pouch that contains nonmagical ammunition or shuriken
(including masterwork ammunition or shuriken, but not special materials, achemical attributes, or
nonmagical treatments on the ammunition), at the start of each round this spell replaces any
ammunition taken from the container the round before. The ammunition taken from the container the
round before vanishes. If, after casting this spell, you cast a spell that enhances projectiles,
such as align weapon or greater magic weapon, on the same container, all projectiles this spell
conjures are affected by that spell.
