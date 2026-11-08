+++
id = "ref/spell/inflict-critical-wounds"
kind = "spell"
title = "Inflict Critical Wounds"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_critical_wounds", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
5: Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 300

This spell functions like [inflict light wounds](ref/spell/inflict-light-wounds), except that you
deal 4d8 points of damage + 1 point per caster level (maximum +20).

### Mythic Inflict Critical Wounds

**Sources:** Mythic Adventures pg 98

The damage dealt increases to 8d8 points of damage + 2 points per caster level (maximum +40). A
living target is sickened for 1 round per caster level (maximum 20 rounds) if it fails its saving
throw.
