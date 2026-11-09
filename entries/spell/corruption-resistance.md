+++
id = "ref/spell/corruption-resistance"
kind = "spell"
title = "Corruption Resistance"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "corruption_resistance", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "212"

[fields]
kind = "spell"
school = "abjuration [chaotic, evil, good, or lawful]"
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Paladin", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration \[chaotic, evil, good, or lawful\]
Level: 2: Antipaladin, Inquisitor, Paladin
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You grant the touched creature limited protection from magical effects that inflict damage based on
the target creature's alignment, such as holy smite, order's wrath, a paladin's smite evil attack,
or an unholy weapon. Choose one alignment type: chaos, evil, good, or law. The subject takes 5 less
points of damage from effects that specifically harm creatures of that alignment. The value of the
protection increases to 10 points at 7th level and 15 points at 11th level. The spell protects the
recipient's equipment as well.

Corruption resistance protects against spells, [spell-like abilities](ref/umr/spell-like-abilities),
and special abilities, not physical attacks. Corruption resistance only protects against damage. The
subject can still suffer side effects from such attacks. When you use this spell to protect an
alignment, it gains the descriptor of that alignment.
