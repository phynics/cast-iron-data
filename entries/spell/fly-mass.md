+++
id = "ref/spell/fly-mass"
kind = "spell"
title = "Mass Fly"
source_ids = ["core-rulebook", "mythic-adventures", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fly_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fly" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Elementalist Wizard", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a wing feather)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Elementalist Wizard, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a wing feather)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Mythic Fly

**Sources:** Mythic Adventures pg 95

The fly speed changes to 120 feet (or 80 feet if the target is wearing medium or heavy armor, or
carrying a medium or heavy load) with perfect maneuverability. When the duration expires, the target
is protected by feather fall for a number of rounds equal to your caster level.

_Augmented (3rd):_ If you expend two uses of mythic power, the target adds your tier on Reflex saves
and as a dodge bonus to AC. It gains these bonuses only while flying.

### Mass Fly

**Sources:** Advanced Player's Guide pg 223

This spell functions as [fly](ref/spell/fly), save that it can target numerous creatures and lasts
longer.
