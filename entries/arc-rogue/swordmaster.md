+++
id = "ref/arc-rogue/swordmaster"
kind = "archetype"
title = "Swordmaster"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Swordmaster"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swordmaster", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-race-guide"
page = "164"

[fields]
kind = "archetype"
features = [
  { anchor = "trance", level = 3 },
]
trades = [
  { replaces = "All increments of trap sense", feature = "trap-sense", by = ["trance"] },
]
+++

A swordmaster meditates to strengthen her spiritual connection to her blade. She strives to perfect
her skills by mastering six deadly trances. A swordmaster has the following class features.

## Class Skills {#class-skills}

The swordmaster adds Knowledge (nature) and Survival to her list of class skills and removes
Disguise and Knowledge (dungeoneering) from her list of class skills.

## Trance (Ex) {#trance}

At 3rd level, a swordmaster learns to focus her martial prowess using an intense meditative trance.
Under the influence of a trance, the swordmaster can perform fantastic martial feats. Entering a
trance is a full-round action that provokes attacks of opportunity. The swordmaster can maintain the
trance for a number of rounds per day equal to 4 + her Wisdom modifier. At each level beyond 3rd,
she can remain in the trance for 1 additional round. She can end her trance as a free action.
Following a trance, the swordmaster is [fatigued](ref/misc/fatigued) for a number of rounds equal to
2 × the number of rounds she spent in the trance. A swordmaster cannot enter a new trance while
fatigued but can otherwise enter a trance multiple times during a single encounter or combat. If a
swordmaster falls unconscious, her trance immediately ends.

At 3rd level, the swordmaster chooses one trance from the list below. She chooses another trance at
6th, 9th, 12th, 15th, and 18th level. She can only use one type of trance at a time.

### Crane Trance (Ex) {#crane-trance}

The swordmaster's blade rises and falls with the graceful sweeping arcs of the mountain crane. When
in this trance, a swordmaster gains the benefits of the [Crane Style](ref/feat/crane-style) feat.

### Dragon Trance (Ex) {#dragon-trance}

Like the dragon, the swordmaster has honed the steadiness of her mind and body. When in this trance,
a swordmaster gains the benefits of the [Dragon Style](ref/feat/dragon-style) feat.

### Leopard Trance (Ex) {#leopard-trance}

Using the swiftness of the leopard, a swordmaster's evasive footwork confuses her opponents. When in
this trance, a swordmaster gains the benefits of the [Mobility](ref/feat/mobility) feat.

### Monkey Trance (Ex) {#monkey-trance}

As the monkey springs, the swordmaster leaps from the reach of her enemies. While in this trance, a
swordmaster can make an Acrobatics check opposed by an opponent's CMD. If she succeeds, she may move
5 feet as a swift action within the opponent's threatened area; this movement does not provoke
attacks of opportunity and does not count as a 5-foot step.

### Serpent Trance (Ex) {#serpent-trance}

Like the serpent, the swordmaster's quick movements allow her to catch her opponent unawares. While
in this trance, a swordmaster receives a +4 bonus on Bluff checks made to feint during combat.

### Tiger Trance (Ex) {#tiger-trance}

The swordmaster pounces upon her opponents, striking with the ferocity and brute force of a wild
tiger. While in this trance, a swordmaster can make a combat maneuver check against an opponent
within [charge](ref/rule/charge) range. If she succeeds, she may charge that opponent and make a
full attack against that opponent.

This ability replaces all increments of trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the swordmaster archetype: combat trick, stand up, surprise
attack, weapon training (_Core Rulebook_); befuddling strike, positioning strike (_Advanced Player's
Guide_).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the swordmaster archetype: crippling strike,
defensive roll (_Core Rulebook_); hunter's surprise, redirect attack (_Advanced Player's Guide_);
confounding blade (_Ultimate Combat_).
