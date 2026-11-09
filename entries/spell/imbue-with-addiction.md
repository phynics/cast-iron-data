+++
id = "ref/spell/imbue-with-addiction"
kind = "spell"
title = "Imbue With Addiction"
aon = "SpellDisplay.aspx?ItemName=Imbue%20With%20Addiction"
source_ids = ["black-markets", "magical-marketplace"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_with_addiction", path = "json/spells14.json" },
]
[[sources]]
publication = "black-markets"
page = "19"
[[sources]]
publication = "magical-marketplace"
page = "24"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a dose of an addictive drug or substance)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Investigator\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a dose of an addictive drug or substance)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature
:::

The target immediately becomes addicted to the drug used as the material component during the
casting of the spell. If the target was ever addicted to the drug at any point in the past, it takes
a -4 penalty on its saving throw.
