+++
id = "ref/spell/dispel-magic-greater"
kind = "spell"
title = "Greater Dispel Magic"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dispel_magic_greater", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dispel-magic" },
]
[[sources]]
publication = "core-rulebook"
page = "272"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
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
title = "Spell statistics"
School: abjuration
Level: 5: Bard, Occultist, Skald, Summoner, Unchained Summoner\
6: Arcanist, Cleric, Druid, Hunter, Inquisitor, Magus, Oracle, Psychic, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target or Area: one spellcaster, creature, or object; or a 20-ft.-radius burst
Duration: instantaneous
Saving throw: none
Spell resistance: no
:::

### Greater Dispel Magic

This spell functions like [dispel magic](ref/spell/dispel-magic), except that it can end more than
one spell on a target and it can be used to target multiple creatures.

You choose to use greater dispel magic in one of three ways: a targeted dispel, area dispel, or a
counterspell:

_Targeted Dispel:_ This functions as a targeted dispel magic, but it can dispel one spell for every
four caster levels you possess, starting with the highest level spells and proceeding to lower level
spells.

Additionally, greater dispel magic has a chance to dispel any effect that remove curse can remove,
even if dispel magic can't dispel that effect. The DC of this check is equal to the curse's DC.

_Area Dispel:_ When greater dispel magic is used in this way, the spell affects everything within a
20-foot-radius burst. Roll one dispel check and apply that check to each creature in the area, as if
targeted by dispel magic. For each object within the area that is the target of one or more spells,
apply the dispel check as with creatures. Magic items are not affected by an area dispel.

For each ongoing area or effect spell whose point of origin is within the area of the greater dispel
magic spell, apply the dispel check to dispel the spell. For each ongoing spell whose area overlaps
that of the greater dispel magic spell, apply the dispel check to end the effect, but only within
the overlapping area.

If an object or creature that is the effect of an ongoing spell (such as a monster summoned by
summon monster) is in the area, apply the dispel check to end the spell that conjured that object or
creature (returning it whence it came) in addition to attempting to dispel one spell targeting the
creature or object.

You may choose to automatically succeed on dispel checks against any spell that you have cast.

_Counterspell:_ This functions as dispel magic, but you receive a +4 bonus on your dispel check to
counter the other spellcaster's spell.
