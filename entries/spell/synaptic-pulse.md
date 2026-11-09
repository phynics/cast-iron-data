+++
id = "ref/spell/synaptic-pulse"
kind = "spell"
title = "Synaptic Pulse"
aon = "SpellDisplay.aspx?ItemName=Synaptic%20Pulse"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synaptic_pulse", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "187"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius spread centered on you" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Mesmerist, Psychic
Casting time: 1 standard action
Components: V
Range: 30 ft.
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Area: 30-ft.-radius spread centered on you
Subschool: Compulsion
Descriptors: mind-affecting
:::

You emit a pulsating mental blast that stuns all creatures in range of your psychic shriek for 1
round.
