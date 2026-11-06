+++
id = "ref/spell/magic-boulder"
kind = "spell"
title = "Magic Boulder"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_boulder", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["earth"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "up to three boulders touched" },
]
duration = "30 minutes or until discharged"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 30 minutes or until discharged
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Targets: up to three boulders touched
Descriptors: earth
:::

**Sources:** Monster Codex pg 69

This spell works like [magic stone](ref/spell/magic-stone), except you transmute as many as three
boulders (rocks up to two size categories smaller than yourself) to use with the
[rock throwing](ref/umr/rock-throwing) ability or as siege engine ammunition. The boulder's damage
increases by one step, and the boulder gains a +1 enhancement bonus on attack and damage rolls.
