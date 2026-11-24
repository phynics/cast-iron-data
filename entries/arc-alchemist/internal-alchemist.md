+++
id = "ref/arc-alchemist/internal-alchemist"
kind = "archetype"
title = "Internal Alchemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Internal%20Alchemist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "internal_alchemist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-magic"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "breath-mastery", level = 1 },
  { anchor = "disease-resistance", level = 3 },
  { anchor = "uncanny-dodge", level = 6 },
]
trades = [
  { replaces = "Throw Anything", feature = "throw-anything", by = ["breath-mastery"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["disease-resistance"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["uncanny-dodge"] },
]
+++

An internal alchemist studies medicine, diet, and the living body to purify the self in the hope of
gaining immortality by means of alchemical concoctions and controlling vital energy. Internal
alchemists develop unusual physical abilities from heightened knowledge of how their bodies work. An
internal alchemist has the following class features.

## Breath Mastery {#breath-mastery}

At 1st level, the internal alchemist can control his breath and the flow of vital energy within his
body. Without preparation, he can [hold his breath](ref/misc/hold-your-breath) for a number of
minutes equal to his Constitution score (after this, he must begin making Constitution checks or
risk suffocation); by spending a full-round action preparing himself, he can increase this duration
to 1 hour per point of Constitution. The alchemist can survive twice as long as normal without food
or water before he starts to take penalties. He can put himself into a state of suspended animation
as a move action, and is then unconscious and appears completely dead; he awakens at a preset time
or in response to a condition set by him when he enters this state. This ability replaces Throw
Anything.

## Bonus Feats {#bonus-feats}

An internal alchemist can select [Alertness](ref/feat/alertness), Extra _Ki_,
[Great Fortitude](ref/feat/great-fortitude), [Improved Critical](ref/feat/improved-critical)
(unarmed strike), [Improved Initiative](ref/feat/improved-initiative),
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike), [Iron Will](ref/feat/iron-will),
[Lightning Reflexes](ref/feat/lightning-reflexes), [Stunning Fist](ref/feat/stunning-fist), or
[Weapon Focus](ref/feat/weapon-focus) (unarmed strike) in place of an alchemical discovery.

## Disease Resistance {#disease-resistance}

At 3rd level, an internal alchemist gains a bonus on all saving throws against disease equal to his
alchemist class bonus against poison. When he gains the poison immunity alchemist class ability, he
becomes immune to disease as well. This ability replaces swift alchemy.

## Uncanny Dodge {#uncanny-dodge}

Starting at 6th level, an internal alchemist can react to danger before his senses would normally
allow him to do so. He cannot be caught [flat-footed](ref/rule/flat-footed), nor does he lose his
Dexterity bonus to AC if the attacker is invisible. However, he still loses his Dexterity bonus to
AC if he is immobilized, or if an opponent successfully uses the feint action against him. If the
internal alchemist already has uncanny dodge from a different class, he automatically gains
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) (as a rogue) instead. This ability
replaces swift poisoning.

## Discoveries {#discoveries}

The following discoveries complement the internal alchemist archetype:
[cognatogen](ref/discovery/cognatogen), [elixir of life](ref/discovery/elixir-of-life),
[grand cognatogen](ref/discovery/grand-cognatogen),
[greater cognatogen](ref/discovery/greater-cognatogen),
[lingering spirit](ref/discovery/lingering-spirit), [mummification](ref/discovery/mummification),
and [spontaneous healing](ref/discovery/spontaneous-healing).
