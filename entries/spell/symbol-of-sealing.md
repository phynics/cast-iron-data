+++
id = "ref/spell/symbol-of-sealing"
kind = "spell"
title = "Symbol of Sealing"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_sealing", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 5,000 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Occultist\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 5,000 gp)
Range: 0 ft.; see text
Duration: permanent
Saving throw: none
Spell resistance: no
Effect: one symbol
Descriptors: force
:::

**Sources:** Ultimate Magic pg 242

This spell allows you to scribe a potent rune of power upon or above a door or other opening
measuring no more than 20 square feet/level in size. When the casting is completed, the symbol
immediately triggers, glowing visibly and sealing the door or opening with an invisible barrier of
force equivalent to a [wall of force](ref/spell/wall-of-force). Destroying the symbol ends the
effect, though destroying it once the symbol has been activated requires destroying the wall of
force first. Once triggered, the wall remains for 10 minutes per caster level.

When scribing a symbol of sealing, you can specify a password or phrase that allows a creature
speaking it to bypass the seal and pass through the opening. You can also attune any number of
creatures to the symbol of sealing, but doing this extends the casting time as described under
symbol of death. However, the force wall created by the symbol blocks attacks and line of effect
even for creatures that know the password or are attuned - the password only prevents them from
triggering the symbol, not from ignoring its effects if triggered.

A [disintegrate](ref/spell/disintegrate) spell or similar effect can destroy the wall of force
created by the symbol if the caster makes a caster level check against a DC of 11 + your caster
level. A [knock](ref/spell/knock) spell has no effect on a symbol of sealing or its force wall. A
symbol of sealing cannot be dispelled, but [mage's disjunction](ref/spell/mages-disjunction)
automatically destroys it.
