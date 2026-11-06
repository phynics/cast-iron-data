+++
id = "ref/spell/see-alignment"
kind = "spell"
title = "See Alignment"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "see_alignment", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (eye of newt)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1/round per level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Bard, Investigator, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (eye of newt)
Range: personal
Duration: 1/round per level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Combat pg 243

When you cast this spell, select a single alignment (such as lawful good or chaotic evil). Creatures
of that alignment glow with a ghostly radiance while they are within your vision. Though you can see
this radiance, other creatures cannot.

Spells and effects that obscure alignment, like undetectable alignment, also obscure the effects of
this spell.
