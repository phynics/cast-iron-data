+++
id = "ref/spell/angelic-aspect-greater"
kind = "spell"
title = "Greater Angelic Aspect"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "angelic_aspect_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/angelic-aspect-lesser" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Paladin", level = 4 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Paladin\
8: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Descriptors: good
:::

### Greater Angelic Aspect

**Sources:** Champions of Purity pg 28

This spell functions like [lesser angelic aspect](ref/spell/angelic-aspect-lesser), except you gain
[low-light vision](ref/rule/low-light-vision); [darkvision](ref/rule/darkvision) 60 feet; DR
10/evil; immunity to acid, cold, and petrification; resistance to electricity 10 and fire 10; a +4
racial bonus on saves against poison; and protective aura and truespeech as supernatural abilities
for the duration of the spell. Also, your wings give you a fly speed of 60 feet with good
maneuverability.

Protective aura provides a +4 deflection bonus to AC and a +4 resistance bonus on saving throws
against attacks made or effects created by evil creatures to anyone within 20 feet. Otherwise, it
functions as a [magic circle against evil](ref/spell/magic-circle-against-evil) and a
[lesser globe of invulnerability](ref/spell/globe-of-invulnerability-lesser), both with a radius of
20 feet.

Truespeech allows you to speak with any creature that has a language, as though using the tongues
spell.
