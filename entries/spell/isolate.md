+++
id = "ref/spell/isolate"
kind = "spell"
title = "Isolate"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "isolate", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Antipaladin, Arcanist, Bard, Inquisitor, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: Will partial
Spell resistance: yes
Target: creature touched
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Monster Codex pg 21

You cause the target to become invisible and silent, but only to his allies. Any creature with an
attitude of indifferent or worse toward the target, and any creature that wishes the target harm,
can see the target normally. The target can see and hear himself, can cast spells with verbal
components, and can use command words normally, but any effect that requires allies to see or hear
the target does not function. An ally that can see invisible creatures can both see and hear the
target of isolate.

If the target succeeds at its save, the duration of the spell is reduced to 1 round.
