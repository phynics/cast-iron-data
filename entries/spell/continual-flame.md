+++
id = "ref/spell/continual-flame"
kind = "spell"
title = "Continual Flame"
aon = "SpellDisplay.aspx?ItemName=Continual%20Flame"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "continual_flame", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "260"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (ruby dust worth 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
  { label = "Effect", value = "magical, heatless flame" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Occultist, Sorcerer, Wizard\
3: Adept, Cleric, Inquisitor, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S, M (ruby dust worth 50 gp)
Range: touch
Duration: permanent
Saving throw: none
Spell resistance: no
Target: object touched
Effect: magical, heatless flame
Descriptors: light
:::

A flame, equivalent in brightness to a torch, springs forth from an object that you touch. The
effect looks like a regular flame, but it creates no heat and doesn't use oxygen. A
[continual flame](ref/spell/continual-flame) can be covered and hidden but not smothered or
quenched.

Light spells counter and dispel darkness spells of an equal or lower level.
