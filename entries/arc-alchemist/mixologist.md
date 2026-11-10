+++
id = "ref/arc-alchemist/mixologist"
kind = "archetype"
title = "Mixologist"
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
replaces = ["Mutagen", "The discovery gained at 2nd level", "Persistent mutagen"]
alters = ["Alchemy", "brew potion", "Poison resistance"]
+++

Certain alchemists focus on mastering the chemical reactions between alcohol and the physical body.
Though the powerful potions they brew can have drawbacks, they are at least pleasurable.

**Note:** This archetype makes heavy use of the alternate [drunkenness](ref/rule/drunkenness) rules.

**Alcoholic Alchemy (Su)**

**Ability:** When a mixologist brews a potion, he can spend an additional 10 gp in raw materials to
increase his caster level by 1 for the purpose of the potion's effects, but the potion counts as a
**strong alcoholic drink.** When a mixologist creates his extracts, he can spend 1 extra minute
doing so to increase his caster level by 1 for the purpose of that extract's effects, but the
extract counts as a **strong alcoholic drink.** A mixologist can prepare one alcoholic extract for
each level of extracts he can prepare.

**Alters:** Alchemy, brew potion

**Flavor:** A mixologist can infuse potions and extracts he creates with alcohol, increasing their
potency.

**Gained:** At 1st Level

**Replaces:** Mutagen

**Special:** A mixologist can't ever gain a mutagen or discoveries that alter mutagens.

**Alcoholic Bombs (Su)**

**Ability:** When the mixologist creates a bomb, he can cause the detonation to produce intoxicating
fumes. A creature that takes a direct hit from an alcoholic bomb becomes **tipsy** if it fails a
Fortitude saving throw. If the creature is already tipsy, it becomes **drunk** instead. If the
creature is already drunk, it becomes **soused** instead. A soused creature that fails its Fortitude
saving throw passes out for 1d3 hours and wakes up with a **hangover**.

**Gained:** At 1st Level

**Replaces:** The discovery gained at 2nd level

**Special:** This ability counts as a discovery that modifies bombs (Primary Bomb Discovery), so it
doesn't stack with other discoveries that modify bombs.

**Alcoholic Resistance (Ex)**

**Alters:** Poison resistance

**Gained:** At 2nd Level

**Passive:** A mixologist's bonus on saving throws against poison also applies on saving throws to
become less drunk and to avoid passing out. This doesn't allow a mixologist to become immune to
alcohol.

**Mixologist Master (Su)**

**Ability:** A mixologist can have up to two alcoholic extracts for each level of extracts he can
prepare as long as he can prepare at least two extracts of that level.

**Gained:** At 14th Level

**Replaces:** Persistent mutagen
