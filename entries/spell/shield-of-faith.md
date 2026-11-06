+++
id = "ref/spell/shield-of-faith"
kind = "spell"
title = "Shield of Faith"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_faith", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (parchment with a holy text written on it)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (parchment with a holy text written on it)
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 342

This spell creates a shimmering, magical field around the target that averts and deflects attacks.
The spell grants the subject a +2 deflection bonus to AC, with an additional +1 to the bonus for
every six levels you have (maximum +5 deflection bonus at 18th level).

### Mythic Shield of Faith

**Sources:** Mythic Adventures pg 108\
Add half your tier to the spell's deflection bonus.
