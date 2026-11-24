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
descriptors = ["mind-affecting"]
levels = [
  { class = "Inquisitor", level = 4 },
]
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to one creature/level, no two of which can be more than 30 ft. apart" },
]
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Inquisitor
Range: close (25 ft. + 5 ft./2 levels)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: up to one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

### Shared Wrath

This spell functions as [wrath](ref/spell/wrath), except that you grant multiple creatures the
bonuses against your designated foe. All subjects of shared wrath receive their bonuses against the
same creature.
