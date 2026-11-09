+++
id = "ref/arc-alchemist/alchemical-sapper"
kind = "archetype"
title = "Alchemical Sapper"
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
replaces = ["Mutagen", "Poison resistance", "Swift alchemy", "The discovery gained at 6th level", "Poison immunity"]
alters = ["Extracts", "Bomb"]
+++

Alchemical sappers are trained to create explosives.

**Diminished Alchemy**

**Alters:** Extracts

**Passive:** An alchemical sapper can prepare one fewer extract of each level than normal. If this
reduces the number to 0, he can prepare extracts of that level only if his Intelligence allows bonus
extracts of that level.

**Gained class skills:** ke, stl

**Demolition Bomb (Su)**

**Ability:** An alchemical sapper can create a demolition bomb. This bomb deals double his normal
bomb damage, half of which is bludgeoning and piercing damage, the other half of which is fire
damage. This bomb ignores a number of points of [hardness](ref/umr/hardness) up to
[half](ref/misc/fractions-and-rounding) the alchemical sapper's level (minimum 1).

**Alters:** Bomb

**Gained:** At 1st Level

**Special:** This counts as an ability that modifies the alchemical sapper's bomb, so it doesn't
stack with other discoveries that modify bombs (Primary Bomb Discoveries). The alchemical sapper
can't use his demolition bomb with the [fast bombs](ref/discovery/fast-bombs) discovery.

**Usage:** An alchemical sapper can only expend one use of his bomb class feature to create a
demolition bomb once per day.

**Usage:** An alchemical sapper can only expend one use of his bomb class feature to create a
demolition bomb once per day.

At 5th level: He can create 2 demolition bombs per day.

At 9th level: He can create 3 demolition bombs per day.

At 13th level: He can create 4 demolition bombs per day.

At 17th level: He can create 5 demolition bombs per day.

**Delayed Bomb (Su)**

**Ability:** An alchemical sapper gains the [delayed bomb](ref/discovery/delayed-bomb) discovery at
1st level.

**Gained:** At 1st Level

**Replaces:** Mutagen

**Special:** He does not qualify for the [mutagen](ref/discovery/mutagen) or
[cognatogen](ref/discovery/cognatogen) discoveries until 8th level.

**Master Engineer (Ex)**

**Gained:** At 2nd Level

**Passive:** An alchemical sapper adds 1/2 his alchemist level to Knowledge (engineering) checks,
Craft (stonemasonry) checks, and Craft (traps) checks.

**Replaces:** Poison resistance

**Camouflage Bomb (Ex)**

**Fullround:** When deploying a _delayed bomb_ or _trip mine_ (see below), the alchemical sapper can
camouflage the bomb by taking an additional full-round action. Creatures searching for traps must
succeed at a Perception check (DC = 10 + the alchemical sapper's alchemist level + his Intelligence
modifier) to notice a camouflaged bomb.

**Gained:** At 3rd Level

**Replaces:** Swift alchemy

**Trip Mine (Su)**

**Ability:** An alchemical sapper can expend two uses of his bomb class feature to prepare a special
kind of trap called a _trip mine._ This special bomb remains inert until 1 round after it leaves the
alchemical sapper's possession, after which time it becomes armed. When a creature enters a square
containing an armed trip mine, it explodes, dealing normal bomb damage to all creatures in its
square (DC = 10 + 1/2 the alchemical sapper's alchemist level + his Intelligence modifier; Reflex
half) and splash damage to every creature adjacent to that square. A trip mine can be disarmed with
a successful Disable Device check (with a DC equal to the trip mine's save DC); otherwise, it lasts
until the next time the alchemical sapper refreshes his daily bombs.

**Gained:** At 6th Level

**Replaces:** The discovery gained at 6th level

**Special:** If the alchemical sapper expends four uses of his bomb class feature, his trip mine
deals damage as per a _demolition bomb;_ this does not count against his daily uses of the
demolition bomb ability. Other than _demolition bomb,_ discoveries that modify bombs cannot apply to
trip mine.

**Selective Detonation (Su)**

**Ability:** When an alchemical sapper plants a _trip mine,_ he can designate a number of allies up
to his Intelligence modifier, allowing the designated allies to pass safely through an armed trip
mine's square without causing it to detonate. If another creature triggers the trip mine while an
ally is nearby, the ally still takes damage as normal.

**Gained:** At 10th Level

**Replaces:** Poison immunity
