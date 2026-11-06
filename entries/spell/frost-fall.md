+++
id = "ref/spell/frost-fall"
kind = "spell"
title = "Frost Fall"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frost_fall", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "5-foot radius burst" },
]
duration = "1 round/2 levels"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Druid, Hunter, Occultist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/2 levels
Saving throw: Fortitude partial
Spell resistance: yes
Area: 5-foot radius burst
Descriptors: cold
:::

**Sources:** Ultimate Combat pg 230

The area of this spell is covered in chilling frost, dealing 2d6 points of cold damage to all
creatures within it. Creatures that the spell initially damages must succeed at a Fortitude save or
become staggered for 1 round. The area remains chilled for the spell's duration. Any creature that
starts your turn within the spell's area takes 1d6 points of cold damage (Fortitude saving throw for
half) but does not become staggered even on a failed saving throw.
