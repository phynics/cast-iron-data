+++
id = "ref/spell/shared-wrath"
kind = "spell"
title = "Shared Wrath"
aon = "SpellDisplay.aspx?ItemName=Shared%20Wrath"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shared_wrath", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/wrath" },
]
[[sources]]
publication = "advanced-players-guide"
page = "243"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a thorny vine)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Inquisitor
Casting time: 1 standard action
Components: V, S, M (a thorny vine)
Range: personal
Duration: 1 minute
Saving throw: none
Spell resistance: no
Target: you
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

### Shared Wrath

This spell functions as [wrath](ref/spell/wrath), except that you grant multiple creatures the
bonuses against your designated foe. All subjects of shared wrath receive their bonuses against the
same creature.
