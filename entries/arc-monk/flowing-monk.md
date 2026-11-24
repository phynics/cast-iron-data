+++
id = "ref/arc-monk/flowing-monk"
kind = "archetype"
title = "Flowing Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Flowing%20Monk"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flowing_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "58"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat" },
  { anchor = "redirection", level = 1 },
  { anchor = "unbalancing-counter", level = 2 },
  { anchor = "flowing-dodge", level = 3 },
  { anchor = "elusive-target", level = 5 },
  { anchor = "volley-spell", level = 15 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["redirection"] },
  { replaces = "The bonus feat gained at 2nd level", feature = "bonus-feat", levels = [2], by = ["unbalancing-counter"] },
  { replaces = "Fast movement", feature = "fast-movement", by = ["flowing-dodge"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["elusive-target"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["elusive-target"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["volley-spell"] },
]
+++

The flowing monk is the wind and the river. He knows how the world flows, and forces his enemies to
flow with it. Even the most powerful stone breaks under the graceful and persistent pressure of wind
and water.

## Bonus Feat {#bonus-feat}

A flowing monk replaces the normal monk bonus feats with the following:
[Agile Maneuvers](ref/feat/agile-maneuvers), [Combat Reflexes](ref/feat/combat-reflexes),
[Deflect Arrows](ref/feat/deflect-arrows), [Dodge](ref/feat/dodge),
[Improved Reposition](ref/feat/improved-reposition), [Improved Trip](ref/feat/improved-trip),
[Nimble Moves](ref/feat/nimble-moves), and [Weapon Finesse](ref/feat/weapon-finesse). At 6th level,
the following feats are also available: [Acrobatic Steps](ref/feat/acrobatic-steps),
[Bodyguard](ref/feat/bodyguard), [Improved Disarm](ref/feat/improved-disarm),
[Improved Feint](ref/feat/improved-feint), [Ki Throw](ref/feat/ki-throw),
[Mobility](ref/feat/mobility), [Second Chance](ref/feat/second-chance), and
[Sidestep](ref/feat/sidestep). At 10th level, the following feats are added:
[In Harm's Way](ref/feat/in-harms-way), [Repositioning Strike](ref/feat/repositioning-strike),
[Snatch Arrows](ref/feat/snatch-arrows), [Spring Attack](ref/feat/spring-attack), and
[Tripping Strike](ref/feat/tripping-strike). (Asterisks denotes feats from the _Advanced Player's
Guide._)

## Redirection (Ex) {#redirection}

At 1st level, as an immediate action, a flowing monk can attempt a [reposition](ref/rule/reposition)
or [trip](ref/rule/trip) combat maneuver against a creature that the flowing monk threatens and that
attacks him. If the combat maneuver is successful, the attacker is [sickened](ref/misc/sickened) for
1 round (Reflex DC = 10 + 1/2 the monk's level + monk's Wisdom modifier to halve the duration), plus
1 additional round at 4th level and for every four levels afterward (to a maximum of 6 rounds at
20th level). The monk gains a +2 bonus on the reposition or trip combat maneuver check and the save
DC for redirection increases by 2 if the attacker is using [Power Attack](ref/feat/power-attack) or
is [charging](ref/rule/charge) when attacking him. The benefit increases to a +4 bonus and an
increase of the saving throw by 4 if both apply.

At 4th level, a flowing monk can use redirection against an opponent that the flowing monk threatens
and that attacks an ally with a melee attack. At 8th level, a flowing monk can make both a
reposition and a trip maneuver as part of a single immediate action with this ability. At 12th
level, a flowing monk can use redirection against any opponent that attacks him in melee, even if
the flowing monk is not threatening the opponent who attacks him. A flowing monk can use this
ability once per day per monk level, but no more than once per round. This ability replaces stunning
fist.

## Unbalancing Counter (Ex) {#unbalancing-counter}

At 2nd level, a flowing monk's attacks of opportunity render a struck creature
[flat-footed](ref/rule/flat-footed) until the end of the flowing monk's next turn (Reflex DC 10 +
1/2 the monk's level + Wisdom modifier negates). This ability replaces the bonus feat gained at 2nd
level.

## Flowing Dodge (Ex) {#flowing-dodge}

At 3rd level, a flowing monk gains a +1 dodge bonus to AC for each enemy adjacent to him, up to a
maximum bonus equal to his Wisdom modifier (minimum 1). This ability replaces fast movement.

## Elusive Target (Ex) {#elusive-target}

At 5th level, as an immediate action, a flowing monk may spend 2 points from his ki pool to attempt
a Reflex save opposed by an attacker's attack roll to halve damage from that attack. At 11th level
and above, the flowing monk suffers no damage on a successful save, or half damage on a failed save.
If the attacker is [flanking](ref/rule/flanking) the monk, the flanking opponent who is not
attacking becomes the target of the attack. Use the same attack roll, and if the attack hits the new
target, that creatures takes half damage (or full damage if the attack is completely avoided). Any
associated effects from the attack (such as [bleed](ref/umr/bleed), poison, or spell effects) apply
fully even if the attack deals only half damage. This ability replaces purity of body and diamond
body.

## Volley Spell (Su) {#volley-spell}

At 15th level, when a targeted spell or [spell-like ability](ref/umr/spell-like-abilities) fails to
overcome a flowing monk's [spell resistance](ref/rule/spell-resistance), he may reflect the effect
onto its caster as [spell turning](ref/spell/spell-turning) by spending a number of points from his
ki pool equal to 1/2 the spell's level (minimum 1). This ability replaces quivering palm.
