+++
id = "ref/spell/holy-aura"
kind = "spell"
title = "Holy Aura"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_aura", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "297"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (a tiny reliquary worth 500 gp)"
range = "20 ft."
effects = [
  { label = "Targets", value = "one creature/level in a 20-ft.-radius burst centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, F (a tiny reliquary worth 500 gp)
Range: 20 ft.
Duration: 1 round/level (D)
Saving throw: see text
Spell resistance: yes
Targets: one creature/level in a 20-ft.-radius burst centered on you
Descriptors: good
:::

A brilliant divine radiance surrounds the subjects, protecting them from attacks, granting them
resistance to spells cast by evil creatures, and causing evil creatures to become blinded when they
strike the subjects. This abjuration has four effects.

First, each warded creature gains a +4 deflection bonus to AC and a +4 resistance bonus on saves.
Unlike [protection from evil](ref/spell/protection-from-evil), this benefit applies against all
attacks, not just against attacks by evil creatures.

Second, each warded creature gains [spell resistance](ref/rule/spell-resistance) 25 against evil
spells and spells cast by evil creatures.

Third, the abjuration protects the recipient from possession and mental influence, just as
protection from evil does.

Finally, if an evil creature succeeds on a melee attack against a creature warded by a holy aura,
the offending attacker is blinded (Fortitude save negates, as blindness/deafness, but against holy
aura's save DC).
