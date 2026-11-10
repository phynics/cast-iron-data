+++
id = "ref/spell/venomous-promise"
kind = "spell"
title = "Venomous Promise"
aon = "SpellDisplay.aspx?ItemName=Venomous%20Promise"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venomous_promise", path = "json/spells11.json" },
]
[[sources]]
publication = "black-markets"
page = "25"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["language-dependant", "poison"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "S, M (a vial of poison)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent or until triggered"
saving_throw = "yes"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Antipaladin, Bard, Shaman, Skald, Witch
Casting time: 1 standard action
Components: S, M (a vial of poison)
Range: touch
Duration: permanent or until triggered
Saving throw: yes
Spell resistance: yes
Target: one creature
Descriptors: language-dependant, poison
:::

You guard your words and person with poisonous power. You can impart a short amount of information -
up to 25 words - as you cast this spell, entwining your words with the poison provided as a material
component. If your target reveals the information you impart (verbally, in writing, with gestures,
or by having its mind read with spells like detect thoughts), the target is immediately exposed to
the poison (and is allowed any saving throw the poison allows).

Your target instinctively knows that revealing this information will endanger it, but doesn't
automatically understand why or how. Neutralize poison removes the effect of this spell; the
spellcaster must succeed at a caster level check against the spell's save DC rather than the
poison's.
