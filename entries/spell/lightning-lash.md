+++
id = "ref/spell/lightning-lash"
kind = "spell"
title = "Lightning Lash"
source_ids = ["pathfinder-74-sword-of-valor"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lightning_lash", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "20-foot-radius spread" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Hunter, Ranger\
3: Cleric, Inquisitor, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes
Area: 20-foot-radius spread
Descriptors: electricity
:::

**Sources:** Pathfinder \#74: Sword of Valor pg 74

You create a crackling lash of unholy lightning that flickers and flashes in your hand like a whip,
shifting color in response to your mood and will. Once per round, you can make a melee touch attack
with the lightning lash against a target within 15 feet. If the attack is successful, it deals 1d6
points of electricity damage and 1d6 points of damage from divine power (similar to flame strike),
and allows you to attempt a trip combat maneuver check as a free action against your target (using
your caster level as your CMB).
