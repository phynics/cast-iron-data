+++
id = "ref/spell/arcane-concordance"
kind = "spell"
title = "Arcane Concordance"
aon = "SpellDisplay.aspx?ItemName=Arcane%20Concordance"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_concordance", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "203"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a spent wand)"
range = "personal"
effects = [
  { label = "Area", value = "10-ft.-radius emanation centered on you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Bard, Skald
Casting time: 1 standard action
Components: V, S, M (a spent wand)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Area: 10-ft.-radius emanation centered on you
:::

A shimmering, blue and gold radiance surrounds you, enhancing arcane spells cast by your allies
within its area. Any arcane spell cast by a creature within the area gains a +1 enhancement bonus to
the DC of any saving throws against the spell, and can be cast as if one of the following metamagic
feats was applied to it (without increasing the spell level or casting time):
[Enlarge Spell](ref/feat/enlarge-spell), [Extend Spell](ref/feat/extend-spell),
[Silent Spell](ref/feat/silent-spell), or [Still Spell](ref/feat/still-spell) (you choose the
metamagic feat when you cast arcane concordance).
