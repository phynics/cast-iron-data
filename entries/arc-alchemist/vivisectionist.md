+++
id = "ref/arc-alchemist/vivisectionist"
kind = "archetype"
title = "Vivisectionist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Vivisectionist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vivisectionist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "sneak-attack", level = 1 },
  { anchor = "torturer-s-eye", level = 2 },
  { anchor = "cruel-anatomist", level = 3 },
  { anchor = "torturous-transformation", level = 7 },
  { anchor = "bleeding-attack" },
  { anchor = "crippling-strike", level = 10 },
]
trades = [
  { replaces = "Bomb", feature = "bomb", by = ["sneak-attack"] },
]
+++

A vivisectionist studies bodies to better understand how they function and how their parts interact.
Unlike a [chirurgeon](ref/arc-alchemist/chirurgeon), a vivisectionist's goals are not related to
healing, but rather to experimentation and knowledge that most people would consider evil. A
vivisectionist has the following class features.

## Sneak Attack {#sneak-attack}

At 1st level, a vivisectionist gains the [sneak attack](ref/ability/sneak-attack) ability as a rogue
of the same level. If a character already has sneak attack from another class, the levels from the
classes that grant sneak attack stack to determine the effective rogue level for the sneak attack's
extra damage dice (so an alchemist 1/rogue 1 has a +1d6 sneak attack like a 2nd-level rogue, an
alchemist 2/rogue 1 has a +2d6 sneak attack like a 3rd-level rogue, and so on). This ability
replaces bomb.

## Torturer's Eye {#torturer-s-eye}

At 2nd level, a vivisectionist adds _[deathwatch](ref/spell/deathwatch)_ to his formula book as a
1st-level extract.

## Cruel Anatomist {#cruel-anatomist}

At 3rd level, a vivisectionist may use his Knowledge (nature) skill bonus in place of his Heal skill
bonus.

## Torturous Transformation {#torturous-transformation}

At 7th level, a vivisectionist adds _[anthropomorphic animal](ref/spell/anthropomorphic-animal)_ to
his formula book as a 2nd-level extract. When he uses this extract, he injects it into an animal as
part of a 2-hour surgical procedure. By using multiple doses of this extract as part of the surgery,
he multiplies the duration by the number of extracts used.

At 9th level, a vivisectionist adds _[awaken](ref/spell/awaken)_ and
_[baleful polymorph](ref/spell/baleful-polymorph)_ to his formula book as 3rd-level extracts. When
he uses the _[awaken](ref/spell/awaken)_ or _[baleful polymorph](ref/spell/baleful-polymorph)_
extract, he injects it into the target (not a plant) as part of a 24-hour surgical procedure. He can
make _[anthropomorphic animal](ref/spell/anthropomorphic-animal)_ [permanent](ref/spell/permanency)
on a creature by spending 7,500 gp.

At 15th level, a vivisectionist adds _[regenerate](ref/spell/regenerate)_ to his formula book as a
5th-level extract.

## Bleeding Attack {#bleeding-attack}

A vivisectionist may select the [bleeding attack](ref/talent/bleeding-attack) rogue talent in place
of a discovery.

## Crippling Strike {#crippling-strike}

At 10th level or later, a vivisectionist may select the
[crippling strike](ref/talent/crippling-strike) rogue talent in place of a discovery.

## Discoveries {#discoveries}

The following discoveries complement the vivisectionist archetype:
[alchemical simulacrum](ref/discovery/alchemical-simulacrum),
[concentrate poison](ref/discovery/concentrate-poison),
[doppelganger simulacrum](ref/discovery/doppelganger-simulacrum),
[feral mutagen](ref/discovery/feral-mutagen), [parasitic twin](ref/discovery/parasitic-twin),
[preserve organs](ref/discovery/preserve-organs), [tentacle](ref/discovery/tentacle),
[tumor familiar](ref/discovery/tumor-familiar), [vestigial arm](ref/discovery/vestigial-arm), and
[wings](ref/discovery/wings).
