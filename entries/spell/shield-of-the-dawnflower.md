+++
id = "ref/spell/shield-of-the-dawnflower"
kind = "spell"
title = "Shield of the Dawnflower"
source_ids = ["inner-sea-world-guide", "gods-and-magic", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_the_dawnflower", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "good", "light"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Bard, Cleric, Hunter, Magus, Oracle, Paladin, Ranger, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level
Saving throw: see text
Spell resistance: no
Target: you
Descriptors: fire, good, light
:::

**Sources:** Inner Sea World Guide pg 296, Gods and Magic pg 35

You create a disk of sunlight on one arm. Any creature that strikes you with a melee attack deals
normal damage, but also takes 1d6 points of fire damage + 1 point per caster level (maximum +15).
Creatures with reach weapons are not subject to this damage if they attack you. The shield provides
illumination as if it were a [continual flame](ref/spell/continual-flame) spell. You can only have
one instance of this spell in effect at a time. It does not stack with similar damaging aura spells
such as fire shield.
