+++
id = "ref/spell/inflict-moderate-wounds"
kind = "spell"
title = "Inflict Moderate Wounds"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inflict_moderate_wounds", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
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
Level: 2: Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest, Witch\
3: Antipaladin
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
deal 2d8 points of damage + 1 point per caster level (maximum +10).

### Mythic Inflict Moderate Wounds

**Sources:** Mythic Adventures pg 99

The damage dealt increases to 4d8 points of damage + 2 points per caster level (maximum +20). A
living target is sickened for 1 round per caster level (maximum 10 rounds) if it fails its saving
throw.

### Mass Inflict Moderate Wounds

**Sources:** PRPG Core Rulebook pg 300

This spell functions like [mass inflict light wounds](ref/spell/inflict-light-wounds-mass), except
that it deals 2d8 points of damage + 1 point per caster level (maximum +30).
