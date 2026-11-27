+++
id = "ref/arc-alchemist/mixologist"
kind = "archetype"
title = "Mixologist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Mixologist"
source_ids = ["inner-sea-taverns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mixologist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "inner-sea-taverns"
page = "57"

[fields]
kind = "archetype"
features = [
  { anchor = "alcoholic-alchemy", level = 1 },
  { anchor = "alcoholic-bombs", level = 2 },
  { anchor = "alcoholic-resistance", level = 2 },
  { anchor = "mixologist-master", level = 14 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["alcoholic-alchemy"] },
  { replaces = "The discovery gained at 2nd level", feature = "discovery", levels = [2], by = ["alcoholic-bombs"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["mixologist-master"] },
  { alters = "Alchemy", feature = "alchemy", by = ["alcoholic-alchemy"] },
  { alters = "brew potion", feature = "brew-potion", by = ["alcoholic-alchemy"] },
  { alters = "Poison resistance", feature = "poison-resistance", by = ["alcoholic-resistance"] },
]
+++

Certain alchemists focus on mastering the chemical reactions between alcohol and the physical body.
Though the powerful potions they brew can have drawbacks, they are at least pleasurable.

## Alcoholic Alchemy (Su) {#alcoholic-alchemy}

A mixologist can infuse potions and extracts he creates with alcohol, increasing their potency. When
a mixologist brews a potion, he can spend an additional 10 gp in raw materials to increase his
caster level by 1 for the purpose of the potion's effects, but the potion counts as a strong
alcoholic drink (see the sidebar on page 55). When a mixologist creates his extracts, he can spend 1
extra minute doing so to increase his caster level by 1 for the purpose of that extract's effects,
but the extract counts as a strong alcoholic drink. A mixologist can prepare one alcoholic extract
for each level of extracts he can prepare. A mixologist can't ever gain a mutagen or discoveries
that alter mutagens.

This alters alchemy and brew potion and replaces mutagen.

## Alcoholic Bombs (Su) {#alcoholic-bombs}

When the mixologist creates a bomb, he can cause the detonation to produce intoxicating fumes. A
creature that takes a direct hit from an alcoholic bomb becomes tipsy (see page 54) if it fails a
Fortitude saving throw. If the creature is already tipsy, it becomes drunk instead. If the creature
is already drunk, it becomes soused instead. A soused creature that fails its Fortitude saving throw
passes out for 1d3 hours and wakes up with a hangover. This ability counts as a discovery that
modifies bombs, so it doesn't stack with other discoveries that modify bombs.

This replaces the discovery gained at 2nd level.

## Alcoholic Resistance (Ex) {#alcoholic-resistance}

At 2nd level, a mixologist's bonus on saving throws against poison also applies on saving throws to
become less drunk and to avoid passing out. This doesn't allow a mixologist to become immune to
alcohol.

This alters poison resistance.

## Mixologist Master (Su) {#mixologist-master}

At 14th level, a mixologist can have up to two alcoholic extracts for each level of extracts he can
prepare as long as he can prepare at least two extracts of that level.

This replaces persistent mutagen.
