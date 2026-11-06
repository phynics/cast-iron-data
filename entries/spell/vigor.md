+++
id = "ref/spell/vigor"
kind = "spell"
title = "Vigor"
source_ids = ["orcs-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vigor", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Adept", level = 0 },
  { class = "Cleric", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Warpriest", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 0: Adept, Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched
:::

**Sources:** Orcs of Golarion pg 28

This spell infuses the subject with a small surge of strength. The creature gets a +1 competence
bonus on a single melee damage roll. It must choose to use the bonus before making the roll to which
it applies. Ranged or spell attacks are unaffected by this spell.
