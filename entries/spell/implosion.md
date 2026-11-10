+++
id = "ref/spell/implosion"
kind = "spell"
title = "Implosion"
aon = "SpellDisplay.aspx?ItemName=Implosion"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "implosion", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "299"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one corporeal creature/round" },
]
duration = "concentration (up to 1 round per 2 levels)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Cleric, Oracle, Psychic
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration (up to 1 round per 2 levels)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one corporeal creature/round
:::

This spell causes a destructive resonance in a corporeal creature's body. Each round you concentrate
(including the first), you can cause one creature to collapse in on itself, inflicting 10 points of
damage per caster level. If you break concentration, the spell immediately ends, though any
implosions that have already happened remain in effect. You can target a particular creature only
once with each casting of the spell. Implosion has no effect on creatures in gaseous form or on
incorporeal creatures.
