+++
id = "ref/spell/alaznists-jinx"
kind = "spell"
title = "Alaznist's Jinx"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alaznists_jinx", path = "json/spells.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "21"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Antipaladin, Bard, Skald\
5: Inquisitor, Occultist, Shaman, Witch\
6: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

You inflict a curse similar to the spell burn spellblight on a creature. Each time a spellcaster who
is afflicted with this curse casts a spell or uses a
[spell-like ability](ref/umr/spell-like-abilities), her skin seems to burn as though she were on
fire. With a successful [concentration](ref/rule/concentration) check (DC = 15 + double the spell
level of the spell cast or spell-like ability used), the spellcaster can ignore the pain of the
effect, but if she fails, she loses the spell or spell slot and is staggered for a round.

Unlike with the spell burn spellblight, the burning sensation is a tangible effect, visible during
the act of spellcasting as an incorporeal, violet flame surrounding the caster.
