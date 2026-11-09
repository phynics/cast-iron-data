+++
id = "ref/spell/arcane-disruption"
kind = "spell"
title = "Arcane Disruption"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_disruption", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-class-origins"
page = "30"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of pepper)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bloodrager, Bard, Magus, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of pepper)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse, mind-affecting
:::

This spell makes it difficult for the subject to cast arcane spells, use
[spell-like abilities](ref/umr/spell-like-abilities), and use some abilities granted by arcane
spellcasting classes. The subject must succeed at a [concentration](ref/rule/concentration) check
(DC = 10 + 1/2 its caster level) in order to cast an arcane spell, use any spell-like ability (even
those that come from a divine source), use arcane spell completion or spell trigger magic items, or
use any of the following class features that come from an arcane spellcasting class: arcane school
powers, arcanist exploits, bardic performances, magus arcana, or witch hexes. Spells, spell-like
abilities, or class features that take a free, swift, or immediate action aren't affected by this
spell, nor are mythic spells or mythic powers.

While under the effect of this spell, if the subject must attempt a concentration check to cast an
arcane spell or use an arcane [spell-like ability](ref/umr/spell-like-abilities) for any reason
other than the effect of this spell (such as casting defensively, being injured while casting, and
so on), it takes a penalty on that check equal to 1/2 its caster level.
