+++
id = "ref/spell/peerless-integrity"
kind = "spell"
title = "Peerless Integrity"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "peerless_integrity", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Area", value = "10-ft.-radius emanation centered on you" },
]
duration = "10 minutes/level"
saving_throw = "none or Will negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Antipaladin, Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 10 minutes/level
Saving throw: none or Will negates, see text
Spell resistance: no
Area: 10-ft.-radius emanation centered on you
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Black Markets pg 31

Peerless integrity conceals the alignment of creatures from divination magic. All creatures within
the spell's area, including you, appear to have lawful good auras for the purposes of divination
spells and effects that reveal alignments (such as [detect law](ref/spell/detect-law) and
[see alignment](ref/spell/see-alignment)), instead of their actual alignments. If the caster of such
divination magic succeeds at a Will save, the caster recognizes whether the readings are true or
false. Any creature under the effects of this spell gains a +2 circumstance modifier on Bluff and
Diplomacy checks.

This spell does not affect other types of divination magic (such as detect thoughts or discern lies)
and does not protect against spells or effects that cause harm based on targeted creatures'
alignments.
