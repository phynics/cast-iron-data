+++
id = "ref/spell/forceful-strike"
kind = "spell"
title = "Forceful Strike"
aon = "SpellDisplay.aspx?ItemName=Forceful%20Strike"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forceful_strike", path = "json/spells13.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "55"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 swift action"
components = "V, S"
range = "touch or reach of melee weapon"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Inquisitor, Magus, Oracle, Paladin, Warpriest
Casting time: 1 swift action
Components: V, S
Range: touch or reach of melee weapon
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: 1 creature
Descriptors: force
:::

You cast this spell as you strike a creature with a melee weapon, unarmed strike, or natural attack
to unleash a concussive blast of force. You deal normal weapon damage from the blow, but also deal
an additional amount of force damage equal to 1d4 points per caster level (maximum of 10d4). The
force of the blow may be enough to knock the target backward as well. To determine if the target is
pushed back, make a combat maneuver check with a bonus equal to your caster level to resolve a bull
rush attempt against the creature struck. You do not move as a result of this free bull rush, but it
can push the target back if it defeats the target's CMD. A successful Fortitude save halves the
force damage and negates the bull rush effect.
