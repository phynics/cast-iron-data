+++
id = "ref/arc-oracle/hermit"
kind = "archetype"
title = "Hermit"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Hermit"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hermit", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "mystery" },
  { anchor = "oracle-s-curse" },
  { anchor = "recluse-s-stride", level = 1 },
  { anchor = "fade-from-memory", level = 7 },
]
trades = [
  { replaces = "The oracle's normal mystery bonus spells at these levels", feature = "mystery", levels = [4, 8, 12, 16], power = "bonus spells" },
]
+++

A hermit is a recluse who gained her oracular powers from isolation in a deep desert, on a mountain
peak, or in another secluded location. A connection to untraveled places gives the hermit powers to
evade his enemies.

## Mystery {#mystery}

A hermit must choose a mystery that adds Survival to his list of class skills, such as
[nature](ref/mystery/nature) or [stone](ref/mystery/stone).

## Oracle's Curse {#oracle-s-curse}

A hermit must choose the [reclusive](ref/oraclecurse/reclusive) curse (below) at 1st level.

## Bonus Spells {#bonus-spells}

_Blindness/deafness_ (4th), _crushing despair_ (8th), _wall of force_ (12th), _maze_ (16th).

These bonus spells replace the oracle's normal mystery bonus spells at these levels.

## Revelations {#revelations}

A hermit must take the following revelations at the listed levels.

## Recluse's Stride (Su) {#recluse-s-stride}

Your base speed increases by 10 feet. At 5th level, once per round when leaving a square, you can
treat the square as though it isn't threatened by any opponents that you can see. At 10th level, you
can teleport a distance equal to your base land speed (as per
_[dimension door](ref/spell/dimension-door)_) as a move action, provided that there are no other
creatures within 10 feet of you when you use this ability and no other creatures within 10 feet of
your destination. You can teleport a number of times per day equal to 3 + your Charisma modifier.
You must take this revelation at 1st level.

## Fade from Memory (Su) {#fade-from-memory}

At 7th level, whenever there are no creatures within 10 feet of you at the end of your turn, you
gain 20% [concealment](ref/rule/concealment) until the beginning of your next turn as a free action.
At 14th level, you instead gain 50% concealment until the beginning of your next turn. You can use
this ability a number of times per day equal to your oracle level. You must take this revelation at
7th level.

## Recommended Mysteries {#recommended-mysteries}

[Heavens](ref/mystery/heavens), [life](ref/mystery/life), nature, stone.
