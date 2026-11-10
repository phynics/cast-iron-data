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
replaces = ["Stunning fist", "The bonus feat gained at 2nd level", "Fast movement", "Purity of body", "diamond body", "Quivering palm"]
+++

The flowing monk is the wind and the river. He knows how the world flows, and forces his enemies to
flow with it. Even the most powerful stone breaks under the graceful and persistent pressure of wind
and water.

**Bonus Feat**

**At 1st Level:** A flowing monk replaces the normal monk bonus feats with the following:
[Agile Maneuvers](ref/feat/agile-maneuvers), [Combat Reflexes](ref/feat/combat-reflexes),
[Deflect Arrows](ref/feat/deflect-arrows), [Dodge](ref/feat/dodge),
[Improved Reposition](ref/feat/improved-reposition), [Improved Trip](ref/feat/improved-trip),
[Nimble Moves](ref/feat/nimble-moves), and [Weapon Finesse](ref/feat/weapon-finesse).

**At 10th Level:** The following feats are added: [In Harm's Way](ref/feat/in-harms-way),
[Repositioning Strike](ref/feat/repositioning-strike), [Snatch Arrows](ref/feat/snatch-arrows),
[Spring Attack](ref/feat/spring-attack), and [Tripping Strike](ref/feat/tripping-strike).

**At 6th Level:** The following feats are also available:
[Acrobatic Steps](ref/feat/acrobatic-steps), [Bodyguard](ref/feat/bodyguard),
[Improved Disarm](ref/feat/improved-disarm), [Improved Feint](ref/feat/improved-feint),
[Ki Throw](ref/feat/ki-throw), [Mobility](ref/feat/mobility),
[Second Chance](ref/feat/second-chance), and [Sidestep](ref/feat/sidestep).

**Redirection (Ex)**

**Immediate:** A flowing monk can attempt a [reposition](ref/rule/reposition) or
[trip](ref/rule/trip) combat maneuver against a creature that the flowing monk threatens and that
attacks him. If the combat maneuver is successful, the attacker is [sickened](ref/misc/sickened) for
a number of rounds equal to 1 + [one-fourth](ref/misc/fractions-and-rounding) of her monk level
(Reflex DC = 10 + 1/2 the monk's level + monk's Wisdom modifier to halve the duration). The monk
gains a +2 bonus on the reposition or trip combat maneuver check and the save DC for redirection
increases by 2 if the attacker is using [Power Attack](ref/feat/power-attack) or is
[charging](ref/rule/charge) when attacking him. The benefit increases to a +4 bonus and an increase
of the saving throw by 4 if both apply.

**At 12th Level:** A flowing monk can use redirection against any opponent that attacks him in
melee, even if the flowing monk is not threatening the opponent who attacks him.

**At 4th Level:** A flowing monk can use redirection against an opponent that the flowing monk
threatens and that attacks an ally with a melee attack.

**At 8th Level:** A flowing monk can make both a reposition and a trip maneuver as part of a single
immediate action with this ability.

**Gained:** At 1st Level

**Replaces:** Stunning fist

**Special:** A flowing monk can use this ability once per day per monk level, but no more than once
per round.

**Unbalancing Counter (Ex)**

**Ability:** A flowing monk's attacks of opportunity render a struck creature
[flat-footed](ref/rule/flat-footed) until the end of the flowing monk's next turn (Reflex DC 10 +
1/2 the monk's level + Wisdom modifier negates).

**Gained:** At 2nd Level

**Replaces:** The bonus feat gained at 2nd level

**Flowing Dodge (Ex)**

**Gained:** At 3rd Level

**Passive:** A flowing monk gains a +1 dodge bonus to AC for each enemy adjacent to him, up to a
maximum bonus equal to his Wisdom modifier (minimum 1).

**Replaces:** Fast movement

**Elusive Target (Ex)**

**Immediate:** A flowing monk may spend 2 points from his _ki pool_ to attempt a Reflex save opposed
by an attacker's attack roll to halve damage from that attack.

**At 11th Level:** The flowing monk suffers no damage on a successful save, or half damage on a
failed save. If the attacker is [flanking](ref/rule/flanking) the monk, the flanking opponent who is
not attacking becomes the target of the attack. Use the same attack roll, and if the attack hits the
new target, that creatures takes half damage (or full damage if the attack is completely avoided).
Any associated effects from the attack (such as [bleed](ref/umr/bleed), poison, or spell effects)
apply fully even if the attack deals only half damage.

**Gained:** At 5th Level

**Replaces:** Purity of body, diamond body

**Volley Spell (Su)**

**Ability:** When a targeted spell or [spell-like ability](ref/umr/spell-like-abilities) fails to
overcome a flowing monk's [spell resistance](ref/rule/spell-resistance), he may reflect the effect
onto its caster as [spell turning](ref/spell/spell-turning) by spending a number of points from his
_ki pool_ equal to 1/2 the spell's level (minimum 1).

**Gained:** At 15th Level

**Replaces:** Quivering palm
