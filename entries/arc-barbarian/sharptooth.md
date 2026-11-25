+++
id = "ref/arc-barbarian/sharptooth"
kind = "archetype"
title = "Sharptooth"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Sharptooth"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sharptooth", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "swim-like-a-fish", level = 1 },
  { anchor = "scent-of-blood", level = 2 },
  { anchor = "ocean-breath", level = 3 },
  { anchor = "blood-in-the-water", level = 6 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["swim-like-a-fish"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["scent-of-blood"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["scent-of-blood"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["ocean-breath"] },
  { replaces = "Rage powers normally gained at 6th and 12th levels", feature = "rage-powers", levels = [6, 12], by = ["blood-in-the-water"] },
]
+++

Coastal hunters and agents of the ocean's rage, sharptooth barbarians emulate the greatest predators
of the sea. Sharks, in particular, are respected and admired by many such tribes, if not as
manifestations of divine power, then merely as scions of the power and fury of the natural world.

## Swim Like a Fish (Ex) {#swim-like-a-fish}

A sharptooth gains a swim speed of 10 feet. At 5th level and every 5 levels thereafter, her swim
speed increases by 5 feet.

This replaces fast movement.

## Scent of Blood (Ex) {#scent-of-blood}

At 2nd level, a sharptooth gains [scent](ref/umr/scent) as per the universal monster rule. At 5th
level, she also gains [keen scent](ref/umr/keen-scent) as per universal monster rule.

This replaces both uncanny dodge and improved uncanny dodge.

## Ocean Breath (Ex) {#ocean-breath}

At 3rd level, a sharptooth counts her Constitution score as 1 higher for the purposes of
[holding her breath](ref/misc/hold-your-breath). She also gains a +1 bonus on Constitution checks to
continue holding her breath. This bonus and the addition to her effective Constitution score both
increase by 1 at 6th level and every 3 levels thereafter, to a maximum bonus of +6 at 18th level.

This replaces trap sense.

## Blood in the Water (Ex) {#blood-in-the-water}

At 6th level, a sharptooth can tear the flesh from living creatures. Her attacks add 3 points of
[bleed](ref/rule/bleed) damage while she is raging. At 12th level, this bleed damage increases to
equal her Constitution modifier if it's higher.

This replaces the rage powers normally gained at 6th and 12th levels.

## Rage Powers {#rage-powers}

The following rage powers complement the sharptooth archetype:
[animal fury](ref/ragepower/animal-fury), [bleeding blow](ref/ragepower/bleeding-blow),
[contagious rage](ref/ragepower/contagious-rage), [pack rage](ref/ragepower/pack-rage),
[powerful blow](ref/ragepower/powerful-blow), [primal scent](ref/ragepower/primal-scent),
[raging swimmer](ref/ragepower/raging-swimmer), and [scent](ref/ragepower/scent).
