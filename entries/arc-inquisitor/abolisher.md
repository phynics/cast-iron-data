+++
id = "ref/arc-inquisitor/abolisher"
kind = "archetype"
title = "Abolisher"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Abolisher"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abolisher", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "sworn-to-purity", level = 1 },
  { anchor = "revealing-gaze", level = 1 },
  { anchor = "expose-aberration", level = 2 },
  { anchor = "escape-corruption-s-grasp", level = 5 },
]
trades = [
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["revealing-gaze"] },
  { replaces = "Detect alignment", feature = "detect-alignment", by = ["expose-aberration"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["escape-corruption-s-grasp"] },
  { alters = "Domains", feature = "domain", by = ["sworn-to-purity"] },
  { alters = "Bane", feature = "bane", by = ["expose-aberration"] },
]
+++

Abolishers are incorruptible inquisitors who weed out creatures of alien, unnatural origins, finding
and exposing aberrations for what they are.

## Sworn to Purity (Ex) {#sworn-to-purity}

An abolisher must select one of the following domains: [Air](ref/domain/air),
[Animal](ref/domain/animal), [Earth](ref/domain/earth), [Fire](ref/domain/fire),
[Plant](ref/domain/plant), [Water](ref/domain/water), or [Weather](ref/domain/weather). If she ever
changes her deity to one that has none of the listed domains, she loses this archetype and becomes a
normal inquisitor or ex-inquisitor.

This ability alters domains.

## Revealing Gaze (Ex) {#revealing-gaze}

An abolisher receives a morale bonus on opposed Perception checks against other creatures' Disguise
and Stealth checks equal to [half](ref/misc/fractions-and-rounding) her inquisitor level (minimum
+1). She grants this bonus to all adjacent allies.

This ability replaces stern gaze.

## Expose Aberration (Sp) {#expose-aberration}

At 2nd level, an abolisher can use _[detect aberration](ref/spell/detect-aberration)_ at will. When
she hits a creature with a weapon attack, she automatically knows if the creature is an aberration
or not. At 5th level, she can activate her [bane](ref/spell/bane) ability as an immediate action
after she hits an aberration but before damage is rolled.

This ability replaces detect alignment and alters bane.

## Escape Corruption's Grasp (Sp) {#escape-corruption-s-grasp}

At 5th level, an abolisher is divinely protected against the grasping tentacles and paralyzing
secretions of aberrations. For a number of rounds per day equal to her inquisitor level, she can
ignore impediments to movement, as per _[freedom of movement](ref/spell/freedom-of-movement)_. These
rounds don't need to be consecutive. Activating this ability is an immediate action.

This ability replaces discern lies.
