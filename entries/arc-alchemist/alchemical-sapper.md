+++
id = "ref/arc-alchemist/alchemical-sapper"
kind = "archetype"
title = "Alchemical Sapper"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Alchemical%20Sapper"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alchemical_sapper", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-alchemy" },
  { anchor = "class-skills" },
  { anchor = "demolition-bomb", level = 1 },
  { anchor = "delayed-bomb", level = 1 },
  { anchor = "master-engineer", level = 2 },
  { anchor = "camouflage-bomb", level = 3 },
  { anchor = "trip-mine", level = 6 },
  { anchor = "selective-detonation", level = 10 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["delayed-bomb"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["master-engineer"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["camouflage-bomb"] },
  { replaces = "The discovery gained at 6th level", feature = "discovery", levels = [6], by = ["trip-mine"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["selective-detonation"] },
  { alters = "Extracts", feature = "extracts", by = ["diminished-alchemy"] },
  { alters = "Bomb", feature = "bomb", by = ["demolition-bomb"] },
]
+++

Alchemical sappers are trained to create explosives.

## Diminished Alchemy {#diminished-alchemy}

An alchemical sapper can prepare one fewer extract of each level than normal. If this reduces the
number to 0, he can prepare extracts of that level only if his Intelligence allows bonus extracts of
that level.

## Class Skills {#class-skills}

An alchemical sapper adds Knowledge (engineering) and Stealth to his list of class skills.

This alters the alchemist's class skills.

## Demolition Bomb (Su) {#demolition-bomb}

At 1st level, an alchemical sapper can create a demolition bomb. This bomb deals double his normal
bomb damage, [half](ref/misc/fractions-and-rounding) of which is bludgeoning and piercing damage,
the other half of which is fire damage. This bomb ignores a number of points of
[hardness](ref/umr/hardness) up to 1/2 the alchemical sapper's level (minimum 1). This counts as an
ability that modifies the alchemical sapper's bomb, so it doesn't stack with other discoveries that
modify bombs. The alchemical sapper can't use his demolition bomb with the
[fast bombs](ref/discovery/fast-bombs) discovery. An alchemical sapper can only expend one use of
his bomb class feature to create a demolition bomb once per day. He can create one additional
demolition bomb per day at 5th level and every 4 alchemist levels thereafter.

This ability modifies bomb.

## Delayed Bomb (Su) {#delayed-bomb}

An alchemical sapper gains the [delayed bomb](ref/discovery/delayed-bomb) discovery at 1st level. He
does not qualify for the [mutagen](ref/discovery/mutagen) or [cognatogen](ref/discovery/cognatogen)
discoveries until 8th level.

This ability replaces mutagen.

## Master Engineer (Ex) {#master-engineer}

At 2nd level, an alchemical sapper adds 1/2 his alchemist level to Knowledge (engineering) checks,
Craft (stonemasonry) checks, and Craft (traps) checks.

This ability replaces poison resistance.

## Camouflage Bomb (Ex) {#camouflage-bomb}

At 3rd level, an alchemical sapper becomes skilled at hiding his bombs. When deploying a delayed
bomb or trip mine (see below), the alchemical sapper can camouflage the bomb by taking an additional
full-round action. Creatures searching for traps must succeed at a Perception check (DC = 10 + the
alchemical sapper's alchemist level + his Intelligence modifier) to notice a camouflaged bomb.

This ability replaces swift alchemy.

## Trip Mine (Su) {#trip-mine}

At 6th level, an alchemical sapper can expend two uses of his bomb class feature to prepare a
special kind of trap called a trip mine. This special bomb remains inert until 1 round after it
leaves the alchemical sapper's possession, after which time it becomes armed. When a creature enters
a square containing an armed trip mine, it explodes, dealing normal bomb damage to all creatures in
its square (DC = 10 + 1/2 the alchemical sapper's alchemist level + his Intelligence modifier;
Reflex half) and splash damage to every creature adjacent to that square. A trip mine can be
disarmed with a successful Disable Device check (with a DC equal to the trip mine's save DC);
otherwise, it lasts until the next time the alchemical sapper refreshes his daily bombs.

If the alchemical sapper expends four uses of his bomb class feature, his trip mine deals damage as
per a demolition bomb; this does not count against his daily uses of the demolition bomb ability.
Other than demolition bomb, discoveries that modify bombs cannot apply to trip mine.

This ability replaces the discovery gained at 6th level.

## Selective Detonation (Su) {#selective-detonation}

At 10th level, when an alchemical sapper plants a trip mine, he can designate a number of allies up
to his Intelligence modifier, allowing the designated allies to pass safely through an armed trip
mine's square without causing it to detonate. If another creature triggers the trip mine while an
ally is nearby, the ally still takes damage as normal.

This ability replaces poison immunity.
