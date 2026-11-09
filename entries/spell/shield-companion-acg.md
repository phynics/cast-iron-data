+++
id = "ref/spell/shield-companion-acg"
kind = "spell"
title = "Shield Companion (ACG)"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_companion_acg", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "191"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "your companion creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Hunter, Paladin, Ranger, Shaman\
3: Arcanist, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: your companion creature
:::

This spell creates a special mystical connection between you and your companion creature - animal
companion, bonded mount, eidolon, or familiar - which allows you to transfer its wounds to you. The
creature gains a +1 deflection bonus to AC and a +1 resistance bonus on saves. As an immediate
action when your companion takes damage, you can take that damage yourself to prevent your companion
from being harmed (similar to [shield other](ref/spell/shield-other), except the damage is not split
between you and the target). Forms of harm that do not involve the loss of hit points, such as charm
effects, temporary ability damage, level drain, and death effects, are not affected. If the creature
suffers a reduction of hit points from a lowered Constitution score, you cannot take that damage on
behalf of your companion creature because it is not hit point damage. When the spell ends, damage
directed to you by the spell is not reassigned to the subject.

If you and your companion move out of range of each other, the spell ends.
