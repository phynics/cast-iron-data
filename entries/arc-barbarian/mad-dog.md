+++
id = "ref/arc-barbarian/mad-dog"
kind = "archetype"
title = "Mad Dog"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Mad%20Dog"
source_ids = ["animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mad_dog", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "animal-archive"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "war-beast", level = 1 },
  { anchor = "pack-tactics", level = 2 },
  { anchor = "rage", level = 4 },
  { anchor = "ferocious-fetch", level = 5 },
  { anchor = "damage-reduction", level = 10 },
  { anchor = "throat-cutter", level = 14 },
]
trades = [
  { replaces = "Rage powers gained at 2nd, 6th, 10th, 14th, and 18th level", feature = "rage-powers", levels = [2, 6, 10, 14, 18], by = ["war-beast"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["pack-tactics"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["ferocious-fetch"] },
  { replaces = "Indomitable will", feature = "indomitable-will", by = ["throat-cutter"] },
  { alters = "Rage", feature = "rage", by = ["rage"] },
]
+++

Though named for the wild savages who fight alongside rabid dogs, mad dogs employ all manner of
beasts as their battle brethren.

## War Beast (Ex) {#war-beast}

At 1st level, a mad dog gains the service of an animal companion, using the barbarian's level as her
effective druid level. This ability replaces the rage powers gained at 2nd, 6th, 10th, 14th, and
18th level.

## Pack Tactics (Ex) {#pack-tactics}

At 2nd level, a mad dog and her war beast gain a +4 bonus on attack rolls while flanking the same
opponent (instead of the normal +2 bonus). This ability replaces uncanny dodge.

## Rage (Ex) {#rage}

A mad dog gains this ability at 4th level, except that her effective barbarian level for the ability
is equal to her barbarian level - 3.

## Ferocious Fetch (Ex) {#ferocious-fetch}

At 5th level, a mad dog's war beast gains [Improved Drag](ref/feat/improved-drag) as a bonus feat.
As a swift action, a mad dog can command her war beast to move toward an opponent within 30 feet and
attempt a [drag](ref/rule/drag) combat maneuver to pull the target back toward the mad dog. The war
beast can move before and after performing the maneuver, but this movement counts toward the war
beast's total movement during its turn. This ability replaces improved uncanny dodge.

## Damage Reduction (Ex) {#damage-reduction}

At 10th level, a mad dog gains [damage reduction](ref/rule/damage-reduction). At 13th level and
every 3 barbarian levels thereafter, this [damage reduction](ref/rule/damage-reduction) rises by 1,
to a maximum of DR 4/- at 19th level. A mad dog's war beast gains the same damage reduction as the
mad dog.

## Throat Cutter (Ex) {#throat-cutter}

At 14th level, whenever her war beast succeeds at a bull rush, drag, grapple, overrun, or trip
combat maneuver against an opponent threatened by the mad dog, a mad dog can take an attack of
opportunity against that opponent. This ability replaces indomitable will.

## Rage Powers {#rage-powers}

The following rage powers complement the mad dog archetype:
[animal fury](ref/ragepower/animal-fury), [beast totem](ref/ragepower/beast-totem),
[bestial leaper](ref/ragepower/bestial-leaper), [primal scent](ref/ragepower/primal-scent),
[raging leaper](ref/ragepower/raging-leaper), [reckless abandon](ref/ragepower/reckless-abandon),
[scent](ref/ragepower/scent), [sprint](ref/ragepower/sprint),
[swift foot](ref/ragepower/swift-foot), and [terrifying howl](ref/ragepower/terrifying-howl). The
following new rage powers also complement this archetype:

### Ferocious Beast (Ex) {#ferocious-beast}

While the barbarian is raging, her animal companion also gains the benefits of rage (including
greater rage, mighty rage, and tireless rage), though the barbarian must spend 1 additional round of
rage per round if her companion begins or ends its turn adjacent to her, and 2 additional rounds of
rage per round if not.

### Ferocious Beast, Greater (Ex) {#ferocious-beast-greater}

While the barbarian is raging, her animal companion shares the benefits of the barbarian's rage
powers that are constant in effect. It gains no benefit from rage powers that require actions to
activate, even if they are free actions. A barbarian must have the
[ferocious beast](ref/ragepower/ferocious-beast) rage power and be at least 8th level to select this
rage power.
