+++
id = "ref/spell/sign-of-the-dawnflower"
kind = "spell"
title = "Sign of the Dawnflower"
source_ids = ["taldor-echoes-of-glory", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sign_of_the_dawnflower", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/message" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Warpriest", level = 0 },
]
casting_time = "1 standard action"
components = "S, F (your holy symbol, or a depiction of either Sarenrae's holy symbol or the goddess herself)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 0: Cleric, Druid, Hunter, Oracle, Warpriest\
1: Paladin, Ranger
Casting time: 1 standard action
Components: S, F (your holy symbol, or a depiction of either Sarenrae's holy symbol or the goddess herself)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: one creature/level
:::

**Sources:** Taldor, Echoes of Glory pg 25

As [message](ref/spell/message), except the only information you can transmit is that you are a
worshiper of Sarenrae. Once notified, the target can reply that he understands your sign. The spell
transmits meaning, not sound, and transcends language barriers.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
