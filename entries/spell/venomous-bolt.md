+++
id = "ref/spell/venomous-bolt"
kind = "spell"
title = "Venomous Bolt"
aon = "SpellDisplay.aspx?ItemName=Venomous%20Bolt"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venomous_bolt", path = "json/spells11.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "254"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["poison"]
levels = [
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 swift action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Target", value = "one arrow or bolt" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Hunter, Ranger
Casting time: 1 swift action
Components: V, S
Range: 0 ft.
Duration: instantaneous
Saving throw: Fortitude negates, see text
Spell resistance: yes
Target: one arrow or bolt
Descriptors: poison
:::

You infuse a single arrow or crossbow bolt with natural venom as you fire it. In addition to its
normal damage, anyone struck by this arrow or bolt is affected as if by the poison spell. If the
arrow is not fired immediately, the spell ends with no effect.
