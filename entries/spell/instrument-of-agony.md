+++
id = "ref/spell/instrument-of-agony"
kind = "spell"
title = "Instrument of Agony"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instrument_of_agony", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless, object), see text"
spell_resistance = "yes (harmless, object), see text"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless, object), see text
Spell resistance: yes (harmless, object), see text
Target: weapon touched
:::

**Sources:** Ultimate Combat pg 232

You cause a weapon to exude a palpable aura of divine fury. While wielding this weapon, a creature
gains a +2 morale bonus on Intimidate checks. When an attack made using the targeted weapon hits,
the wielder can spend a free action to discharge the effect to inflict agony on the creature the
weapon hit. If that creature has [spell resistance](ref/rule/spell-resistance), it applies against
this effect. If the creature fails a Will save, it is nauseated for 1d4+1 rounds. If it succeeds at
the saving throw, the creature is instead sickened for 1 round. The sickened condition created by
the instrument is a mind-affecting effect.
