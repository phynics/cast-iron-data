+++
id = "ref/spell/evolution-surge-greater"
kind = "spell"
title = "Greater Evolution Surge"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "evolution_surge_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/evolution-surge-lesser" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a chameleon scale)"
range = "touch"
effects = [
  { label = "Target", value = "your eidolon" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, M (a chameleon scale)
Range: touch
Target: your eidolon
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
:::

## Lesser Evolution Surge

**Sources:** Advanced Player's Guide pg 220

This spell causes your eidolon to take on new characteristics. You can grant the eidolon any
evolution whose total cost does not exceed 2 evolution points. You may only grant one evolution with
this spell, even if that evolution can be taken multiple times. You can grant an evolution that
allows you to spend additional evolution points to upgrade that evolution. This spell cannot be used
to grant an upgrade to an evolution that the eidolon already possesses. The eidolon must meet any
prerequisites of the selected evolution. This spell does not allow an eidolon to exceed its maximum
number of natural attacks.

### Evolution Surge

**Sources:** Advanced Player's Guide pg 220

This spell functions as [lesser evolution surge](ref/spell/evolution-surge-lesser), except that you
can grant any evolution whose total cost does not exceed 4 evolution points.

### Greater Evolution Surge

**Sources:** Advanced Player's Guide pg 220

This spell functions as lesser evolution surge, except that you can grant any two evolutions whose
total cost does not exceed 6 evolution points.
