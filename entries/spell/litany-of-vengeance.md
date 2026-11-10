+++
id = "ref/spell/litany-of-vengeance"
kind = "spell"
title = "Litany of Vengeance"
aon = "SpellDisplay.aspx?ItemName=Litany%20of%20Vengeance"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_vengeance", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "235"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["language-dependant"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Inquisitor", level = 5 },
  { class = "Paladin", level = 4 },
]
casting_time = "1 swift action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Antipaladin, Paladin\
5: Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: none
Spell resistance: yes
Target: one creature
Descriptors: language-dependant
:::

This litany causes your enemy to feel the pain of blows more sharply. Anyone who hits the target
with an attack gains a +5 sacred or profane bonus (depending on the alignment of the caster) to that
attack's damage.

While subject to this spell, the target cannot be the target of another spell that has the word
"litany" in the title.
