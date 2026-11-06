+++
id = "ref/spell/accept-affliction"
kind = "spell"
title = "Accept Affliction"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "accept_affliction", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["good"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (dove's heart)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Bard, Cleric, Druid, Hunter, Oracle, Paladin, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (dove's heart)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
Descriptors: good
:::

**Sources:** Champions of Purity pg 28

The caster can transfer the effects of afflictions such as curses, diseases, and poisons from the
target creature to himself. This spell can also transfer the blinded, deafened, fatigued, nauseated,
shaken, and sickened conditions. All aspects of the transferred afflictions (save DCs, remaining
duration, removal conditions, and so on) remain the same, but affect the caster instead of the
original target. After transferring the affliction or condition, the caster is free to cure it in
any way he can.
