+++
id = "ref/spell/imbue-with-elemental-might"
kind = "spell"
title = "Imbue with Elemental Might"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_with_elemental_might", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/imbue-with-spell-ability" },
]
[[sources]]
publication = "advanced-race-guide"
page = "203"

[fields]
kind = "spell"
school = "evocation [see text]"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "10 minutes"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched; see text" },
]
duration = "24 hours or until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation \[see text\]
Level: 2: Arcanist, Bloodrager, Cleric, Magus, Oracle, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S
Range: touch
Duration: 24 hours or until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched; see text
:::

This spell functions like [imbue with spell ability](ref/spell/imbue-with-spell-ability), except you
transfer the use of your elemental assault ability to the target. The target must have an
Intelligence score of at least 5 to use the ability. The imbued elemental assault functions exactly
like yours, except the ability's duration is based on the target's level or Hit Dice. Once you cast
this spell, you cannot use your elemental assault ability until the duration of the spell is over.
