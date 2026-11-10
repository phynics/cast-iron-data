+++
id = "ref/spell/litany-of-weakness"
kind = "spell"
title = "Litany of Weakness"
aon = "SpellDisplay.aspx?ItemName=Litany%20of%20Weakness"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_weakness", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "236"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["language-dependant"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Inquisitor", level = 1 },
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
School: necromancy
Level: 1: Antipaladin, Inquisitor
Casting time: 1 swift action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: none
Spell resistance: yes
Target: one creature
Descriptors: language-dependant
:::

Your litany proclaims your target weak, sapping its strength. The target is fatigued for 1 round.

While subject to this spell, the target cannot be the target of another spell that has the word
"litany" in the title.
