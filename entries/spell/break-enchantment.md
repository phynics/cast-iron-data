+++
id = "ref/spell/break-enchantment"
kind = "spell"
title = "Break Enchantment"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "break_enchantment", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 minute"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to one creature per level, all within 30 ft. of each other" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Bard, Medium, Mesmerist, Occultist, Paladin, Psychic, Skald\
5: Adept, Arcanist, Cleric, Inquisitor, Oracle, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 minute
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: see text
Spell resistance: no
Targets: up to one creature per level, all within 30 ft. of each other
:::

**Sources:** PRPG Core Rulebook pg 251

This spell frees victims from enchantments, transmutations, and curses. Break enchantment can
reverse even an instantaneous effect. For each such effect, you make a caster level check (1d20 +
caster level, maximum +15) against a DC of 11 + caster level of the effect. Success means that the
creature is free of the spell, curse, or effect. For a cursed magic item, the DC is equal to the DC
of the curse.

If the spell is one that cannot be dispelled by [dispel magic](ref/spell/dispel-magic) or
[stone to flesh](ref/spell/stone-to-flesh), break enchantment works only if that spell is 5th level
or lower.

If the effect comes from a permanent magic item, break enchantment does not remove the curse from
the item, but it does free the victim from the item's effects.
