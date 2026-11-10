+++
id = "ref/arc-alchemist/crypt-breaker"
kind = "archetype"
title = "Crypt Breaker"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crypt_breaker", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "inner-sea-magic"
page = "33"

[fields]
kind = "archetype"
replaces = ["Bombs", "Mutagen", "Brew potion", "Persistent mutagen"]
replaces_features = ["mutagen", "brew-potion", "persistent-mutagen"]
+++

Crypt breakers are most common in Osirion, where they use their powers of perception and alchemical
adaptation to safely investigate the mysteries of that lands' past. They are often involved in
expeditions into dangerous tombs and catacombs, where their ability to create alchemical devices
designed to neutralize constructs and undead are often crucial to survival. A crypt breaker has the
following class features.

**Alkahest Bombs (Su)**

**Ability:** Against constructs and corporeal undead, alkahest bombs deal 1d8 points of damage, plus
1d8 points of damage for every odd-numbered level instead of 1d6. Against all other creatures,
alkahest bombs deal 1d4 points of damage, plus 1d4 points of force damage for every odd-numbered
level. This otherwise works like the standard bombs class feature.

**Info:** A crypt breaker's bombs are specially designed to work best against constructs and
corporeal undead - two foes commonly encountered in ancient tombs. Known as alkahest bombs, these
bombs deal acid damage instead of fire damage. Alkahest is an alchemical fluid that eats away
unliving flesh and animated constructs, but it doesn't work as well against other targets.

**Gained:** At 1st Level

**Replaces:** Bombs

**Crypt Breaker's Draught (Su)**

**Ability:** Rather than develop mutagens that increase their natural armor and physical abilities
at the expense of their minds, crypt breakers focus on the creation of special draughts that can
enhance their senses. When a crypt breaker drinks one of these draughts, he gains a +4 bonus on all
Perception checks and gains one of the following special senses: [darkvision](ref/rule/darkvision)
60 feet, [low-light vision](ref/rule/low-light-vision), or [scent](ref/umr/scent). While under the
effects of a crypt breaker's draught, the alchemist also gains
[light blindness](ref/umr/light-blindness).

**Gained:** At 1st Level

**Replaces:** Mutagen

**Special:** A crypt breaker cannot create mutagens unless he selects the
[mutagen](ref/discovery/mutagen) discovery.

**Trapfinding**

**Gained:** At 1st Level

**Passive:** A crypt breaker adds [half](ref/misc/fractions-and-rounding) his level on Perception
checks made to locate traps and to Disable Device checks (minimum +1). A crypt breaker can use
Disable Device to disarm magic traps. When determining the ability of a crypt breaker to
[deal with locks or traps](ref/ability/trapfinding), treat his alchemist levels as rogue levels.

**Replaces:** Brew potion

**Discoveries**

**Gained:** At 1st Level

**Passive:** A crypt breaker may take the following rogue talents as discoveries:
[quick disable](ref/talent/quick-disable), _trap sense_ (see below), and
[trap spotter](ref/talent/trap-spotter). Treat the crypt breaker's alchemist level as his rogue
level for these talents.

> _Per errata, Trap Sense refers to the rogue [class ability](ref/ability/trap-sense). The crypt
> breaker can take it as a discovery, and it improves as the crypt breaker levels up._

**Enhanced Alkahest (Su)**

**Gained:** At 14th Level

**Passive:** Against constructs and corporeal undead, the crypt breaker's alkahest bombs deal +1
points of damage per die, and the bomb threatens a critical hit on a 19-20. This does not stack with
other effects that improve critical hit threat ranges.

**Replaces:** Persistent mutagen
