+++
id = "ref/arc-rogue/desert-raider"
kind = "archetype"
title = "Desert Raider"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Desert%20Raider"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "desert_raider", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "76"

[fields]
kind = "archetype"
features = [
  { anchor = "desert-tracker", level = 1 },
  { anchor = "sun-at-your-back", level = 2 },
  { anchor = "light-step", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["desert-tracker"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["sun-at-your-back"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["light-step"] },
]
+++

Desert raiders constantly threaten caravans that cross vast, desolate expanses. Some desert raiders
are tribespeople who raid to supplement their hardscrabble existence, while others are career
thieves who take to the desert to avoid the noose. To survive, a desert raider must learn the
secrets of the deserts and become inured to their dangers.

Though most often associated with hot deserts, desert raiders can also operate in tundra, where
sunlight on snow can blind as easily as on sand.

## Class Skills {#class-skills}

A desert raider adds Knowledge (geography) and Survival to her list of class skills instead of
Knowledge (dungeoneering) and Swim.

This alters the rogue's class skills.

## Desert Tracker (Ex) {#desert-tracker}

A desert raider is immune to the [dazzled](ref/misc/dazzled) condition. A desert raider adds half
her level (minimum 1) as a bonus on Survival skill checks to follow or identify tracks in desert
terrain.

This replaces trapfinding.

## Sun at Your Back (Ex) {#sun-at-your-back}

At 2nd level, a desert raider can use the reflected light of the blinding sun to conceal her
presence. A desert raider in bright light can attempt Stealth checks without cover or concealment
but takes a -5 penalty on her check. The desert raider cannot use this ability to hide from
creatures immune to the [blinded](ref/misc/blinded) or dazzled conditions.

This replaces the rogue talent gained at 2nd level.

## Light Step (Ex) {#light-step}

At 3rd level, the DC of Survival checks to track the desert raider increase by 3. In addition, she
gains a +1 bonus on Perception checks to avoid being surprised by a foe. The DC increase and the
bonus on Perception checks increase by 1 every 3 rogue levels thereafter (to a maximum increase of 8
and a maximum bonus of +6 at 18th level).

This replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the desert raider archetype: fast stealth, getaway artist,
ledge walker, rogue crawl, stand up, surprise attack.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the desert raider archetype: hide in plain sight,
stealthy sniper.
