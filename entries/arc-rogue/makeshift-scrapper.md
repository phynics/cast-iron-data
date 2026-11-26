+++
id = "ref/arc-rogue/makeshift-scrapper"
kind = "archetype"
title = "Makeshift Scrapper"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Makeshift%20Scrapper"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "makeshift_scrapper", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "improvised-weapons", level = 1 },
  { anchor = "supernatural-improvisation", level = 3 },
  { anchor = "improvised-weapon-mastery", level = 12 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["improvised-weapons"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["supernatural-improvisation"] },
  { replaces = "Rogue talent gained at 12th level", feature = "rogue-talents", levels = [12], by = ["improvised-weapon-mastery"] },
]
+++

Some combatants specialize in the study of certain weapons, but those without formal training often
learn to survive a fight by making brilliant use of whatever is lying around.

## Weapon Proficiency {#weapon-proficiency}

The makeshift scrapper is proficient with only simple weapons.

## Improvised Weapons (Ex) {#improvised-weapons}

At 1st level, a makeshift scrapper gains [Catch Off-Guard](ref/feat/catch-off-guard) and
[Throw Anything](ref/feat/throw-anything) as bonus feats. This ability replaces trapfinding.

## Supernatural Improvisation (Su) {#supernatural-improvisation}

At 3rd level, a makeshift scrapper gains the ability to enhance an item, making it a more effective
weapon or changing the way it can be used. As a swift action, she can alter a single
[improvised weapon](ref/misc/improvised-weapons) to either grant it a +1 enhancement bonus on attack
rolls and damage rolls or use it to gain a +1 shield bonus to her AC. The makeshift scrapper can use
this ability for a number of rounds per day equal to her rogue level. These rounds need not be
consecutive, and the makeshift scrapper can change the enhancement each time she activates the
ability. The bonus increases by 1 every 4 levels thereafter, up to a maximum bonus of +5 at 19th
level. This ability replaces trap sense.

## Improvised Weapon Mastery (Ex) {#improvised-weapon-mastery}

At 12th level, the makeshift scrapper gains
[Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery) as a bonus feat. This ability
replaces the rogue talent gained at 12th level.

## Rogue Talents/Ninja Tricks {#rogue-talents-ninja-tricks}

The following rogue talents and ninja tricks complement the makeshift scrapper archetype: acrobatic
master, [expert leaper](ref/talent/expert-leaper), [fast getaway](ref/talent/fast-getaway),
[ki pool](ref/talent/ki-pool), [offensive defense](ref/talent/offensive-defense),
[peerless maneuver](ref/talent/peerless-maneuver), and
[surprise attack](ref/talent/surprise-attack).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the makeshift scrapper archetype: another day,
defensive roll, fast getaway, and opportunist.
