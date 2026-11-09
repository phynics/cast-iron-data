+++
id = "ref/spell/shield-of-wings"
kind = "spell"
title = "Shield of Wings"
source_ids = ["paths-of-the-righteous"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_wings", path = "json/spells9.json" },
]
[[sources]]
publication = "paths-of-the-righteous"
page = "9"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (see below)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Cleric, Inquisitor, Oracle, Paladin, Ranger, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 minute/level (see below)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: fire
:::

> _The following spell is available to worshipers of [Ragathiel](ref/faith/ragathiel)._

You gain five burning wings that grant a fly speed equal to the number of wings × 10 (average
maneuverability) for an initial fly speed of 50 feet. The first time in a round where you would take
fire damage, a wing vanishes (reducing the fly speed granted) and you gain fire resistance 30 for
the remainder of the round. When you are down to one wing (and a fly speed of 10 feet), your
maneuverability drops to poor. When you lose your final wing, you become immune to fire damage for 1
additional minute, after which the effects of this spell end.
