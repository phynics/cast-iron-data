+++
id = "ref/spell/storm-of-blades"
kind = "spell"
title = "Storm of Blades"
source_ids = ["people-of-the-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storm_of_blades", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a sword)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Magus, Sorcerer, Wizard\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (a sword)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one creature
Subschool: Creation
:::

**Sources:** People of the Sands pg 11

You create floating swords of the type used as the material component for this spell (such as a
rapier or scimitar) and magically propel them at your target. You can create one sword for every 2
caster levels that you possess, up to a maximum of five swords at 10th level. You must have line of
effect between you and the target, and the target must be within the spell's range. You make a
ranged attack roll for each sword (with no penalties for range increments or using melee weapons as
ranged weapons); each attack has the same threat range and critical modifier and deals the same
damage as a standard sword of the type expended. Swords created by this spell disappear after
striking (or missing) their targets.
