+++
id = "ref/carried/core-rulebook/spells/dispel-magic/greater"
kind = "spell"
title = "Dispel Magic, Greater"
source_ids = ["core-rulebook"]
section = ["Spells", "Dispel Magic"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Dispel Magic/Greater", path = "core_rulebook/spell/dispel_magic_greater.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target or Area", value = "one spellcaster, creature, or object; or a 20-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
School: abjuration
Level: 5: Bard, Skald, Summoner\
6: Arcanist, Cleric, Druid, Hunter, Hunter, Inquisitor, Magus, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting Time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target or Area: one spellcaster, creature, or object; or a 20-ft.-radius burst
Duration: instantaneous
Saving Throw: none
Spell Resistance: no
:::

_As dispel magic, but with multiple targets._

This spell functions like _[dispel magic](ref/spell/dispel-magic)_, except that it can end more than
one spell on a target and it can be used to target multiple creatures.

You choose to use _[greater dispel magic](ref/spell/dispel-magic-greater)_ in one of three ways: a
targeted dispel, area dispel, or a counterspell:

_Targeted Dispel_: This functions as a targeted _[dispel magic](ref/spell/dispel-magic)_, but it can
dispel one spell for every four caster levels you possess, starting with the highest level spells
and proceeding to lower level spells.

Additionally, _[greater dispel magic](ref/spell/dispel-magic-greater)_ has a chance to dispel any
effect that _[remove curse](ref/spell/remove-curse)_ can remove, even if
_[dispel magic](ref/spell/dispel-magic)_ can't dispel that effect. The DC of this check is equal to
the curse's DC.

_Area Dispel_: When _[greater dispel magic](ref/spell/dispel-magic-greater)_ is used in this way,
the spell affects everything within a 20-foot-radius burst. Roll one dispel check and apply that
check to each creature in the area, as if targeted by _[dispel magic](ref/spell/dispel-magic)_. For
each object within the area that is the target of one or more spells, apply the dispel check as with
creatures. Magic items are not affected by an area dispel.

For each ongoing area or effect spell whose point of origin is within the area of the
_[greater dispel magic](ref/spell/dispel-magic-greater)_ spell, apply the dispel check to dispel the
spell. For each ongoing spell whose area overlaps that of the
_[greater dispel magic](ref/spell/dispel-magic-greater)_ spell, apply the dispel check to end the
effect, but only within the overlapping area.

If an object or creature that is the effect of an ongoing spell (such as a monster summoned by
_[summon monster](ref/spell/summon-monster)_) is in the area, apply the dispel check to end the
spell that conjured that object or creature (returning it whence it came) in addition to attempting
to dispel one spell targeting the creature or object.

You may choose to automatically succeed on dispel checks against any spell that you have cast.

_Counterspell_: This functions as _[dispel magic](ref/spell/dispel-magic)_, but you receive a +4
bonus on your dispel check to counter the other spellcaster's spell.
