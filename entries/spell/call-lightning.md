+++
id = "ref/spell/call-lightning"
kind = "spell"
title = "Call Lightning"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "call_lightning", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Shaman", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one or more 30-ft.-long vertical lines of lightning" },
]
duration = "1 minute/level"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Druid, Hunter, Occultist, Shaman
Casting time: 1 round
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Reflex half
Spell resistance: yes
Effect: one or more 30-ft.-long vertical lines of lightning
Descriptors: electricity
:::

**Sources:** PRPG Core Rulebook pg 251

Immediately upon completion of the spell, and once per round thereafter, you may call down a
5-foot-wide, 30-foot-long, vertical bolt of lightning that deals 3d6 points of electricity damage.
The bolt of lightning flashes down in a vertical stroke at whatever target point you choose within
the spell's range (measured from your position at the time). Any creature in the target square or in
the path of the bolt is affected.

You need not call a bolt of lightning immediately; other actions, even spellcasting, can be
performed first. Each round after the first you may use a standard action (concentrating on the
spell) to call a bolt. You may call a total number of bolts equal to your caster level (maximum 10
bolts).

If you are outdoors and in a stormy area - a rain shower, clouds and wind, hot and cloudy
conditions, or even a tornado (including a whirlwind formed by a djinni or an air elemental of at
least Large size)-each bolt deals 3d10 points of electricity damage instead of 3d6.

This spell functions indoors or underground but not underwater.

### Mythic Call Lightning

**Sources:** Mythic Adventures pg 87

Each lightning bolt's damage increases to 3d10 points of damage (or 5d10 points outdoors in stormy
weather). Half of this damage is electricity damage, and the other half is sonic. Creatures that
succeed at their saving throws are dazzled and deafened for 1 round. Those that fail at their saving
throws are dazzled and deafened for 1 minute.

### Call Lightning Storm

**Sources:** PRPG Core Rulebook pg 252

This spell functions like call lightning, except that each bolt deals 5d6 points of electricity
damage (or 5d10 if created outdoors in a stormy area), and you may call a maximum of 15 bolts.
