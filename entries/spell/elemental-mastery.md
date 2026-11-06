+++
id = "ref/spell/elemental-mastery"
kind = "spell"
title = "Elemental Mastery"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_mastery", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation [see text]"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation \[see text\]
Level: 4: Arcanist, Bloodrager, Druid, Hunter, Magus, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Inner Sea Races pg 219

> _The following spell is available to the indicated races or ethnicities: [Ifrit](ref/race/ifrit),
> [Oread](ref/race/oread), [Suli](ref/race/suli), [Sylph](ref/race/sylph),
> [Undine](ref/race/undine)_

You gain mastery over the element matching the elemental essence in your blood (fire for ifrits,
earth for oreads, air for sylphs, and water for undines). If you are a suli, you can choose any one
of the four options as you cast this spell, but the duration is reduced to 1 round per level. Your
mastery gives you an insight bonus to your speed or a new movement mode, depending on the element
you master, and grants one additional benefit. This spell's descriptor matches the chosen element.

|Element (Race)|Movement|Benefit|
| --- | --- | --- |
|Air (suli, sylph)|Fly 30 ft. (average)|+1 circumstance bonus on attack rolls when both you and your foe are airborne.|
|Earth (oread, suli)|Burrow 15 ft.|+1 circumstance bonus on attack rolls when both you and your foe are touching the ground.|
|Fire (ifrit, suli)|+20 ft. all speeds|+1 circumstance bonus on attack rolls when your foe is on fire.|
|Water (suli, undine)|+30 ft. swim|+1 circumstance bonus on attack rolls when both you and your foe are touching water.|
