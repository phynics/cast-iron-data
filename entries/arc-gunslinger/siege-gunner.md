+++
id = "ref/arc-gunslinger/siege-gunner"
kind = "archetype"
title = "Siege Gunner"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Siege%20Gunner"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "siege_gunner", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "inner-sea-combat"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "grit" },
  { anchor = "engineer-training" },
  { anchor = "deeds" },
  { anchor = "targeted-blast", level = 1 },
  { anchor = "scattershot", level = 3 },
]
trades = [
  { replaces = "Nimble", feature = "nimble", by = ["engineer-training"] },
  { replaces = "Deadeye", feature = "deeds", power = "deadeye", by = ["targeted-blast"] },
  { replaces = "Gunslinger initiative", feature = "deeds", power = "gunslinger initiative", by = ["scattershot"] },
  { replaces = "The gunslinger's normal bonus feats", feature = "bonus-feats" },
]
+++

The Grand Duchy of Alkenstar has spawned all manner of firearm specialists, wielding small and large
firearms alike. Siege gunners specialize in the very largest-[cannons](ref/eq-siegeengine/cannon),
[bombards](ref/eq-siegeengine/bombard-standard), and [firedrakes](ref/eq-siegeengine/firedrake).
These specialists are rarely seen outside of Alkenstar, however, in part because the duchy keeps
close tabs on its most powerful guns and few are found elsewhere in the Inner Sea. A few siege
gunners outside of Alkenstar make a living renting out their services and the use of their personal
collection of siege weaponry to causes in which they believe or to the highest bidder.

## Grit (Ex) {#grit}

A siege gunner relies less on luck and intuition and more on cold calculation and wit. The number of
grit points a siege gunner gains each day and her maximum grit are based on the siege gunner's
Intelligence modifier rather than her Wisdom modifier.

## Engineer Training (Ex) {#engineer-training}

A siege gunner is trained in all aspects of siegecraft, including the workings of siege engines and
knowledge of the structures that are often the target of their assaults. Starting at 2nd level, a
siege gunner gains a bonus on Knowledge (engineering) checks equal to 1/2 her gunslinger level. This
ability replaces nimble.

## Deeds {#deeds}

A siege gunner swaps a pair of deeds of her choosing for the following.

## Targeted Blast (Ex) {#targeted-blast}

At 1st level, when using a firearm or siege engine that targets an area rather than a specific
creature, the siege gunner can spend 1 grit point to focus the brunt of the blast on a single
creature within the target area. The target creature takes 1 additional point of damage for each
level the siege gunner possesses. This is precision damage and is not multiplied on a critical hit.
At 5th level and for every 5 levels the siege gunner possesses beyond that, she can select an
additional creature to target with this bonus damage. Targets must be selected before any attack
rolls or saving throws are made. This ability replaces deadeye.

## Scattershot (Ex) {#scattershot}

At 3rd level, if the siege gunner has at least 1 grit point, she can increase the effectiveness of
[scattering shots](ref/misc/scatter) from hand-held firearms and
[blast shots](ref/eq-siegeengine/blast-shot) from siege engines. The cone radius of scattering shots
or blast shots increases by 5 feet for every three levels the siege gunner possesses (to a maximum
of 30 feet at 18th level). This ability replaces gunslinger initiative.

## Bonus Feats {#bonus-feats}

At 4th level, a siege gunner gains [Siege Engineer](ref/feat/siege-engineer) as a bonus feat. At 8th
level, she gains [Master Siege Engineer](ref/feat/master-siege-engineer) as a bonus feat. She does
not need to meet the prerequisites for these feats. At 12th level and for every 4 levels thereafter,
the siege gunner gains a bonus feat in addition to those gained by normal advancement. These
additional bonus feats must be combat or grit feats, and she must meet the prerequisites as normal.
This replaces the gunslinger's normal bonus feats.
