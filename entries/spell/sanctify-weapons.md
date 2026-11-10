+++
id = "ref/spell/sanctify-weapons"
kind = "spell"
title = "Sanctify Weapons"
aon = "SpellDisplay.aspx?ItemName=Sanctify%20Weapons"
source_ids = ["chronicle-of-the-righteous"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanctify_weapons", path = "json/spells8.json" },
]
[[sources]]
publication = "chronicle-of-the-righteous"
page = "50"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius spread" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Paladin\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Area: 20-ft.-radius spread
:::

This spell originated among the armies of Heaven. Choose a specific subtype of evil outsider when
you cast this spell, such as daemon, demon, devil, or div. All manufactured weapons in the area of
effect bypass the DR of that type of outsider. The weapons do not become aligned or change
composition.
