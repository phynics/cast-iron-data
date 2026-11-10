+++
id = "ref/spell/incorporeal-chains"
kind = "spell"
title = "Incorporeal Chains"
aon = "SpellDisplay.aspx?ItemName=Incorporeal%20Chains"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "incorporeal_chains", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-adventures"
page = "174"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Psychic", level = 6 },
  { class = "Spiritualist", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one incorporeal creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "concentration"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Spiritualist\
6: Psychic
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration
Saving throw: none
Spell resistance: yes
Target: one incorporeal creature/level, no two of which can be more than 30 ft. apart
Descriptors: force
:::

You summon ghostly chains to bind incorporeal creatures. The chains' CMB is equal to your caster
level + your Intelligence modifier. Roll only once for the entire spell effect and apply the result
to all targeted incorporeal creatures.

If the chains succeed in grappling an incorporeal creature, the creature takes an amount of damage
equal to 1d8 + your key spellcasting ability score modifier and gains the grappled condition.
Grappled opponents can't move without first breaking the grapple. The spell prohibits all other
movement unless the creature breaks the grapple first (although dimensional magic and the like still
work as normal). Each round you concentrate, the chains continue grappling their current targets
(though they don't seek out targets they aren't currently grappling). The incorporeal chains receive
a +5 bonus on grapple combat maneuver checks against opponents the chains are already grappling, but
can't move foes or pin foes. Each round the incorporeal chains succeed at a grapple combat maneuver
check, they deal an additional amount of damage equal to 1d8 + your key spellcasting ability score
modifier. The CMD of incorporeal chains, for the purposes of escaping the grapple, is equal to 10 +
its CMB. If you move out of range of any of the grappled creatures, the chains cease grappling those
creatures.
