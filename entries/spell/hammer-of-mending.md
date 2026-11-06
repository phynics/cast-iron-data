+++
id = "ref/spell/hammer-of-mending"
kind = "spell"
title = "Hammer of Mending"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hammer_of_mending", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF, F (a small mithral hammer worth 300 gp)"
range = "personal"
effects = [
  { label = "Area", value = "30-ft.-radius burst centered on you" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard\
6: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF, F (a small mithral hammer worth 300 gp)
Range: personal
Duration: instantaneous
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Area: 30-ft.-radius burst centered on you
:::

**Sources:** Inner Sea Gods pg 235

Upon striking a piece of solid ground with the spell's focus or a holy symbol, you let out a wave of
energy that repairs items within its burst. All objects or constructs within the burst are repaired
of 1d6 points of damage per level. When this spell affects constructs, the spell bypasses any
immunity to magic as if the spell did not allow [spell resistance](ref/rule/spell-resistance).

Hammer of mending can fix destroyed magic items (items with 0 hit points or fewer), and restores the
magic properties of the item if your caster level is at least twice that of the item. Items with
charges (such as wands) and single-use items (such as potions and scrolls) cannot be repaired in
this way.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
