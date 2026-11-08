+++
id = "ref/spell/synaptic-pulse-greater"
kind = "spell"
title = "Greater Synaptic Pulse"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synaptic_pulse_greater", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/synaptic-pulse" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius spread centered on you" },
]
duration = "1d4 rounds; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Mesmerist\
5: Psychic
Casting time: 1 standard action
Components: V
Range: 30 ft.
Area: 30-ft.-radius spread centered on you
Duration: 1d4 rounds; see text
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

## Synaptic Pulse

**Sources:** Occult Adventures pg 187

You emit a pulsating mental blast that stuns all creatures in range of your psychic shriek for 1
round.

### Greater Synaptic Pulse

**Sources:** Occult Adventures pg 187

You emit a pulsating mental blast that stuns all creatures in range of your psychic shriek for 1d4
rounds. On a successful save, a creature is instead sickened for 1 round.
