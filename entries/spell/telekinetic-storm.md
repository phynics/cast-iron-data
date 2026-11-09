+++
id = "ref/spell/telekinetic-storm"
kind = "spell"
title = "Telekinetic Storm"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telekinetic_storm", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "188"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Psychic", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "40-ft.-radius burst centered on you" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Psychic
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Area: 40-ft.-radius burst centered on you
Descriptors: force
:::

You generate a storm of telekinetic energy that emanates from you, ripping through the spell's area
of effect with devastating force. Any creature caught in the spell's radius takes 1d6 points of
damage per caster level (maximum 20d6) and is dazed and stunned for 1 round. A successful Fortitude
save reduces the damage by half and negates the dazed and stunned effects.

The telekinetic storm damages objects in the area. If the damage caused to an interposing barrier
shatters or breaks through it, the telekinetic storm continues beyond the barrier if the spell's
area permits; otherwise, it stops at the barrier just as any other spell effect does.

You can designate any number of creatures to be immune to the spell's effect, though you must be
capable of targeting those creatures.
