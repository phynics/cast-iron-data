+++
id = "ref/arc-fighter/taldor-rondelero-duelist"
kind = "archetype"
title = "Taldor: Rondelero Duelist"
source_ids = ["inner-sea-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "taldor_rondelero_duelist", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "inner-sea-primer"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "buckler-bash", level = 2 },
  { anchor = "buckler-catch", level = 3 },
  { anchor = "strong-swing", level = 5 },
  { anchor = "armor-training", level = 7 },
  { anchor = "chopping-blow", level = 11 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["buckler-bash"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["buckler-catch"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["strong-swing"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["armor-training"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["chopping-blow"] },
]
+++

Taldor's warriors have perfected the art of fighting with the [falcata](ref/eq-weapon/falcata) and
[buckler](ref/eq-armor/buckler) in an art they call rondelero. They use their bucklers both to
defend themselves and to launch unexpected strikes while chopping and hewing at their foes'
unprotected bodies and heads with their falcatas. Rondeleros wear any type of armor, but favor
bucklers, and are comfortable using both hands for offense and defense.

## Suggested Feats {#suggested-feats}

[Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency) (falcata),
[Improved Shield Bash](ref/feat/improved-shield-bash),
[Improved Two-Weapon Fighting](ref/feat/improved-two-weapon-fighting),
[Power Attack](ref/feat/power-attack), [Shield Slam](ref/feat/shield-slam),
[Shield Master](ref/feat/shield-master), [Taldan Duelist](ref/feat/taldan-duelist) (see _World
Guide: The Inner Sea_), [Two-Weapon Fighting](ref/feat/two-weapon-fighting),
[Weapon Focus](ref/feat/weapon-focus) (falcata),
[Weapon Specialization](ref/feat/weapon-specialization) (falcata).

## Buckler Bash (Ex) {#buckler-bash}

At 2nd level, a rondelero can perform a [shield bash](ref/misc/shield-bash) with a buckler (use the
same damage and critical modifier as for a light shield). This ability replaces bravery.

## Buckler Catch (Ex) {#buckler-catch}

At 3rd level, a rondelero can catch his opponent's weapon between his buckler and his forearm,
effectively wedging the hafts of polearms and hammers or the flats of blades. This functions as a
[disarm](ref/rule/disarm) combat maneuver, and the rondelero gains a +4 bonus on the roll. If the
rondelero's attack fails by 10 or more, he suffers a -2 penalty to his AC until the start of his
next turn. This ability replaces armor training 1.

## Strong Swing (Ex) {#strong-swing}

At 5th level, a rondelero gains a +1 bonus on attack and damage rolls when wielding a falcata and
buckler that applies to attacks made by either hand. These bonuses increase by +1 for every four
levels beyond 5th. With a [full-attack](ref/rule/full-attack) action, a rondelero may alternate
between using his falcata or his buckler for each attack. This does not grant additional attacks or
incur penalties as two-weapon fighting does. This ability replaces weapon training 1.

## Armor Training (Ex) {#armor-training}

At 7th level, a rondelero gains armor training 1, and can move at his normal speed in medium armor.
At 15th level, the rondelero gains armor training 2, and can move at his normal speed in heavy
armor. This ability replaces armor training 2.

## Chopping Blow (Ex) {#chopping-blow}

At 11th level, as a standard action, a rondelero can make a single melee attack with a falcata. If
the attack hits, he may make a [sunder](ref/rule/sunder) combat maneuver against the target of his
attack as a free action that does not provoke an attack of opportunity. This ability replaces armor
training 3.
