+++
id = "ref/spell/thought-echo"
kind = "spell"
title = "Thought Echo"
aon = "SpellDisplay.aspx?ItemName=Thought%20Echo"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_echo", path = "json/spells10.json" },
]
[[sources]]
publication = "occult-adventures"
page = "189"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
]
casting_time = "1 round"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Mesmerist, Psychic
Casting time: 1 round
Components: V
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Glamer
Descriptors: glamer
:::

When you cast this spell, you establish a mental echo of up to 25 words. Any attempt to read the
surface thoughts of the target creature reads only this mental echo unless the caster succeeds at a
caster level check (DC = 11 + your caster level). If you cast thought echo on yourself, the DC is
instead equal to 15 + your caster level. In addition, when casting this spell upon yourself, you can
change the echoed thoughts by taking a standard action and concentrating.

Each time you change the words echoed by the spell in this way, you reduce the spell's remaining
duration by 1 minute. Thought echo does not interfere with telepathy or mind reading effects that
are capable of reaching thoughts deeper than surface thoughts.
