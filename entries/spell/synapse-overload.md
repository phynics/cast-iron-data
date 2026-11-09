+++
id = "ref/spell/synapse-overload"
kind = "spell"
title = "Synapse Overload"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synapse_overload", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "187"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Mesmerist\
5: Psychic
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: living creature touched
Descriptors: mind-affecting
:::

You cause the target's mind to unleash a vast overflowing torrent of information throughout the
target's body, causing the target's synapses to violently trigger. The target takes 1d6 points of
electrical damage per caster level (maximum 15d6) and is staggered for 1 minute. A successful
Fortitude saving throw doesn't reduce the damage, but it negates the staggered effect.
