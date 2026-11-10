+++
id = "ref/spell/body-double"
kind = "spell"
title = "Body Double"
aon = "SpellDisplay.aspx?ItemName=Body%20Double"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "body_double", path = "json/spells2.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (two glass beads)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "two creatures; see text" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Bloodrager, Bard, Magus, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (two glass beads)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: two creatures; see text
Subschool: Glamer
Descriptors: glamer
:::

Upon casting this spell, choose a primary target and a secondary target, both of which must be
within range. If the primary target fails or forfeits its saving throw, its appearance, scent,
sounds, and mannerisms change to match those of the secondary target.

As long as the two targets are of the same size category, they are indistinguishable. As a
consequence, if the targets are adjacent and a creature takes an action that would affect one of the
targets (such as an attack, a targeted spell, or an area effect), that action has a 50% chance of
affecting the other target instead.

Any action that would affect both of the creatures affects them both normally.

This spell does not deceive creatures that have true seeing. Likewise, a creature that can't
perceive one of the targets is not fooled by this spell (even if the spell fooled that creature
earlier), and its attacks, targeted spells, and other actions affect targets as normal.
