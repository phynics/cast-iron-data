+++
id = "ref/carried/advanced-players-guide/spells/shared-wrath"
kind = "spell"
title = "Shared Wrath"
source_ids = ["advanced-players-guide"]
section = ["Spells"]
tags = ["enchantment", "compulsion", "emotion", "mind-affecting"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Advanced Players Guide/Spells/Shared Wrath", path = "advanced_players_guide/spell/shared_wrath.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a thorny vine)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "up to one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
School: enchantment (compulsion) \[emotion, mind-affecting\]
Level: 4: Inquisitor
Casting Time: 1 standard action
Components: V, S, M (a thorny vine)
Range: close (25 ft. + 5 ft./2 levels)
Targets: up to one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_As wrath, but affects multiple creatures._

This spell functions as _[wrath](ref/spell/wrath)_, except that you grant multiple creatures the
bonuses against your designated foe. All subjects of _shared wrath_ receive their bonuses against
the same creature.
