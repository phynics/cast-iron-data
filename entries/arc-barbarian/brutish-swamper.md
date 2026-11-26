+++
id = "ref/arc-barbarian/brutish-swamper"
kind = "archetype"
title = "Brutish Swamper"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Brutish%20Swamper"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brutish_swamper", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "marsh-march", level = 1 },
  { anchor = "home", level = 2 },
  { anchor = "stubborn", level = 3 },
  { anchor = "wrastlin", level = 6 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["marsh-march"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["home"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["home"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["stubborn"] },
  { replaces = "Rage power normally gained at 6th level", feature = "rage-powers", levels = [6], by = ["wrastlin"] },
]
+++

The hardy and insular denizens of the swamp produce warriors of narrow focus and great strength. The
prejudice and misunderstanding with which civilized folk often regard barbarians is often even more
pronounced in the case of these belligerent outcasts from society, in large part due to the fact
that brutish swampers deliberately mock and antagonize the so-called "city folk." To a brutish
swamper, an urban lifestyle is one that breeds weakness and lassitude in the body. The brutish
swamper has little interest or patience in maintaining alliances or friendship with those who live
such soft lifestyles, and this aggression only further encourages feelings of prejudice on both
sides of the cultural divide. When a brutish swamper joins an adventuring party, they usually come
to value the skills and talents of their more urbanized companions, but never fully understand the
desire to live lives surrounded by creature comforts.

## Swamp Skills {#swamp-skills}

A brutish swamper adds Knowledge (geography) and Knowledge (local) to her list of class skills.

This alters the barbarian's skills.

## Marsh March (Ex) {#marsh-march}

A brutish swamper can move through the underbrush and muddy terrain of bogs and swamps at her normal
speed without taking damage or suffering other impairments. Briars, mud, thorns, and overgrown areas
that have been magically manipulated to impede motion, however, still affect her.

This replaces fast movement.

## Home (Ex) {#home}

At 2nd level, a brutish swamper gains a +2 bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks when in swamps. This bonus increases by +1 at 5th level and
again every 3 levels after 5th (up to a maximum bonus of +8 at 20th level).

This replaces uncanny dodge and improved uncanny dodge.

## Stubborn (Ex) {#stubborn}

At 3rd level, a brutish swamper resists any attempts to change her attitude or compel her to action.
Diplomacy and Intimidate checks against her take a -2 penalty, and no result can shift her attitude
more than one step in a 24-hour period. These penalties increase by 2 for every 3 levels the brutish
swamper has beyond 3rd.

This replaces trap sense.

## Wrastlin' (Ex) {#wrastlin}

At 6th level, while raging, a brutish swamper gains a +2 bonus to her CMD against
[grapple](ref/rule/grapple) combat maneuvers and a +2 bonus on damage rolls made as part of
successful grapple combat maneuver checks.

This replaces the rage power normally gained at 6th level.

## Rage Powers {#rage-powers}

The following rage powers complement the brutish swamper archetype:
[brawler](ref/ragepower/brawler), [greater brawler](ref/ragepower/greater-brawler),
[greater tyrant totem](ref/ragepower/greater-tyrant-totem),
[lesser tyrant totem](ref/ragepower/lesser-tyrant-totem),
[lizard stride](ref/ragepower/lizard-stride), [low-light vision](ref/ragepower/low-light-vision),
[superstition](ref/ragepower/superstition), and [tyrant totem](ref/ragepower/tyrant-totem).
