+++
id = "ref/arc-druid/plains-druid"
kind = "archetype"
title = "Plains Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Plains%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plains_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "100"

[fields]
kind = "archetype"
features = [
  { anchor = "plains-traveler", level = 2 },
  { anchor = "run-like-the-wind", level = 3 },
  { anchor = "savanna-ambush", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "canny-charger", level = 9 },
  { anchor = "evasion", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["plains-traveler"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["run-like-the-wind"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["savanna-ambush"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["canny-charger"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["evasion"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

Out upon the wide and rolling prairies and savannahs, plains druids stand guard over the grasslands.
These druids range far and wide, watching over nomadic tribes and wandering herds and preserving the
sometimes fragile ecosystem of the wide open spaces.

## Plains Traveler (Ex) {#plains-traveler}

At 2nd level, a plains druid gains a bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks equal to 1/2 her druid level in plains terrain, and she
cannot be tracked in such an environment. This ability replaces woodland stride.

## Run Like the Wind (Ex) {#run-like-the-wind}

At 3rd level, a plains druid gains +10 feet to her land speed when wearing light or no armor and
carrying a light load, and once per hour, she may [run](ref/rule/run) or [charge](ref/rule/charge)
at double the normal speed for 1 round. If riding her animal companion, it gains this ability
instead. This ability replaces trackless step.

## Savanna Ambush (Ex) {#savanna-ambush}

At 4th level, a plains druid gains [concealment](ref/rule/concealment) whenever she is
[prone](ref/rule/prone) in natural surroundings, and can make Stealth checks at no penalty when
prone and not moving or at -5 when crawling. A plains druid can stand up from prone as an immediate
action during a surprise round. This ability replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

A plains druid gains this ability at 6th level, except that her effective druid level for the
ability is equal to her druid level - 2.

## Canny Charger (Ex) {#canny-charger}

At 9th level, a plains druid can charge through allies' squares without difficulty (whether mounted
or afoot) and can turn up to 90 degrees once during a charge, provided the last 10 feet toward the
target are in a straight line. She also gains a +4 dodge bonus to AC against enemy charge attacks
and a +4 bonus to damage with a [readied action](ref/rule/ready) against a charging foe. This
ability replaces venom immunity.

## Evasion (Ex) {#evasion}

At 13th level, a plains druid gains [evasion](ref/ability/evasion) when wearing light or no armor
and carrying a light load. This functions as the [rogue](ref/class/rogue) ability of the same name.
This ability replaces a thousand faces.
