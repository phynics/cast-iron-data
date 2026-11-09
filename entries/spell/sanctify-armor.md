+++
id = "ref/spell/sanctify-armor"
kind = "spell"
title = "Sanctify Armor"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanctify_armor", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "240"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Inquisitor", level = 4 },
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "armor touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Paladin\
4: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: armor touched
Descriptors: good
:::

You imbue your armor with a righteous aura. It gains a +1 enhancement bonus per four caster levels
(maximum +5 at 20th level). When using your judgment or smite ability, you gain DR 5/evil.

An outfit of regular clothing counts as armor that grants no AC bonus for the purpose of this spell.
