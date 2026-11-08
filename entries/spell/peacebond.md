+++
id = "ref/spell/peacebond"
kind = "spell"
title = "Peacebond"
source_ids = ["ultimate-combat", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "peacebond", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one sheathed or slung weapon" },
]
duration = "1 minute/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Arcanist, Inquisitor, Occultist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one sheathed or slung weapon
:::

**Sources:** Ultimate Combat pg 238

You lock a weapon in place on its owner's body, or within the weapon's sheath or holster. Anyone who
then tries to draw the weapon must spend a standard action and succeed at a Strength check (DC equal
to the saving throw DC) to do so, provoking attacks of opportunity whether the attempt succeeds or
fails.
