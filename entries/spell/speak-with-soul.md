+++
id = "ref/spell/speak-with-soul"
kind = "spell"
title = "Speak with Soul"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_with_soul", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 6 },
  { class = "Medium", level = 4 },
  { class = "Oracle", level = 6 },
  { class = "Paladin", level = 4 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 minute"
components = "V, S, M (a drop of candle wax)"
range = "10 ft."
effects = [
  { label = "Target", value = "see text" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Medium, Paladin\
6: Cleric, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 minute
Components: V, S, M (a drop of candle wax)
Range: 10 ft.
Duration: 1 minute/level (D)
Saving throw: Will negates; see text
Spell resistance: no
Target: see text
:::

**Sources:** Planar Adventures pg 45

You commune with the soul of a dead creature. To cast this spell, you must be at the soul's place of
death or be in the soul's presence, whether it is contained in a receptacle, powers an intelligent
magic item, or other possibilities. The soul can attempt a Will save to resist the spell as if it
were alive.

A soul contacted this way can speak normally in any language it knows. Unlike
[speak with dead](ref/spell/speak-with-dead) and similar spells, you are not limited to asking
questions and can engage in normal conversation with the soul (and vice versa). The soul isn't an
undead creature and isn't compelled to speak or be truthful. Generally, the soul only knows what it
knew in life, although souls that persisted with awareness of their surroundings after death may
have more to offer.
