+++
id = "ref/spell/flame-blade"
kind = "spell"
title = "Flame Blade"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flame_blade", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "0 ft."
effects = [
  { label = "Effect", value = "sword-like beam" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: 0 ft.
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Effect: sword-like beam
Descriptors: fire
:::

**Sources:** PRPG Core Rulebook pg 283

A 3-foot-long, blazing beam of red-hot fire springs forth from your hand. You wield this blade-like
beam as if it were a scimitar. Attacks with the flame blade are melee touch attacks. The blade deals
1d8 points of fire damage + 1 point per two caster levels (maximum +10). Since the blade is
immaterial, your Strength modifier does not apply to the damage. A flame blade can ignite
combustible materials such as parchment, straw, dry sticks, and cloth.

### Mythic Flame Blade

**Sources:** Mythic Adventures pg 94\
The blade's damage increases to 2d6 points of fire damage + 1 point per caster level (maximum +20).
The blade threatens a critical hit on a natural 18-20 as if it were an actual scimitar.

_Augmented (3rd):_ If you expend two uses of mythic power, the blade threatens a critical hit on a
natural 15-20, and bypasses [hardness](ref/umr/hardness), fire resistance, and fire immunity.
