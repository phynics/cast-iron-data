+++
id = "ref/spell/make-whole"
kind = "spell"
title = "Make Whole"
source_ids = ["core-rulebook", "technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "make_whole", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one object up to 10 cu. ft./level or one construct creature of any size" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Cleric, Occultist, Oracle, Psychic, Red Mantis Assassin, Sorcerer, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one object up to 10 cu. ft./level or one construct creature of any size
:::

**Sources:** PRPG Core Rulebook pg 311

This spell functions as [mending](ref/spell/mending), except that it repairs 1d6 points of damage
per level when cast on a construct creature (maximum 5d6).

Make whole can fix destroyed magic items (at 0 hit points or less), and restores the magic
properties of the item if your caster level is at least twice that of the item. Items with charges
(such as wands) and single-use items (such as potions and scrolls) cannot be repaired in this way.
When make whole is used on a construct creature, the spell bypasses any immunity to magic as if the
spell did not allow [spell resistance](ref/rule/spell-resistance).
