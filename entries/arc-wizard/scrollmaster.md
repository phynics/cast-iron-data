+++
id = "ref/arc-wizard/scrollmaster"
kind = "archetype"
title = "Scrollmaster"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Scrollmaster"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scrollmaster", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "ultimate-magic"
page = "89"

[fields]
kind = "archetype"
features = [
  { anchor = "scroll-blade", level = 1 },
  { anchor = "scroll-shield" },
  { anchor = "improved-scroll-casting", level = 10 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["scroll-blade"] },
  { replaces = "10th-level bonus feat", feature = "bonus-feats", levels = [10], by = ["improved-scroll-casting"] },
]
+++

To some wizards, a scroll is not just a written form of a spell, it is a physical weapon meant to be
used in combat like a sword or a shield. These strange wizards enter battle armed with scrolls,
often one in each in each hand, practicing combat techniques resembling some monk martial arts.

## Scroll Blade (Su) {#scroll-blade}

A scrollmaster can wield any paper, parchment, or cloth scroll as if it were a melee weapon. In the
hands of the wizard, the scroll acts as a [short sword](ref/eq-weapon/short-sword) with an
enhancement bonus equal to 1/2 the level of the highest-level wizard spell on the scroll; a scroll
with only a cantrip or 1st-level spell on it counts as a [masterwork](ref/rule/masterwork-weapons)
short sword. The scrollmaster is proficient in this weapon, and feats and abilities that affect
short swords (such as [Weapon Focus](ref/feat/weapon-focus)) apply to this weapon. A scrollmaster
cannot wield two scrollblades at the same time.

Activating this ability is a free action. A scroll blade only retains its abilities in the hands of
the scrollmaster. The scroll blade has [hardness](ref/umr/hardness) 0 and hit points equal to the
highest-level wizard spell on the scroll. Each successful hit by the scroll blade reduces its hit
points by 1; this damage cannot be repaired, but does not affect casting from the scroll. When its
hit points [reach](ref/misc/reach) 0, the scroll is destroyed.

If a scroll contains a spell with a metamagic feat, this ability uses the original spell level of
the spell (a _scroll of empowered fireball_ counts as a 3rd-level spell).

At 3rd level, when using a 4th-level or higher wizard scroll as a scroll blade, the scrollmaster can
choose to reduce its enhancement bonus by 1 (minimum +1 enhancement bonus) to treat it as a reach
weapon. For example, he could use a _scroll of charm monster_ (a 4th-level wizard spell) as either a
_+2 short sword_ or a _+1 short sword_ with reach.

At 5th level, when using a 4th-level or higher wizard scroll as a scroll blade, the scrollmaster can
choose to reduce its enhancement bonus (to a minimum of a +1 enhancement bonus) to give any of the
following weapon properties: _[defending](ref/magic-enh/defending)_, _[frost](ref/magic-enh/frost)_,
_[icy burst](ref/magic-enh/icy-burst)_, _[keen](ref/magic-enh/keen)_,
_[ki focus](ref/magic-enh/ki-focus)_, _[shock](ref/magic-enh/shock)_,
_[shocking burst](ref/magic-enh/shocking-burst)_, _[speed](ref/magic-enh/speed)_. Adding any of
these properties consumes an amount of enhancement bonus equal to the property's cost (see Table
15–9: Melee Weapon Special Abilities in the _Core Rulebook_). The scrollmaster must know the
prerequisite spell or spells to craft the weapon property in question (for example, he must know
_[haste](ref/spell/haste)_ to be able to give his scroll blade the _speed_ property). This ability
replaces the wizard's arcane bond.

## Scroll Shield (Su) {#scroll-shield}

A scrollmaster can wield any paper, parchment, or cloth scroll as if it were a
[light wooden shield](ref/eq-armor/light-wooden-shield). In the hands of the wizard, the scroll
grants a +1 shield bonus with an enhancement bonus equal to 1/2 the level of the highest-level
wizard spell on the scroll; a scroll with only a cantrip or 1st-level spell counts as a
[masterwork](ref/rule/masterwork-armor) light shield. The scroll shield has no armor check penalty,
arcane spell failure chance, or maximum Dexterity bonus. The scrollmaster is considered proficient
in this shield. A scrollmaster can use a scrollblade in one hand and a scroll shield in the other
hand.

Activating this ability is a free action. A scroll shield only retains its abilities in the hands of
the scrollmaster. The scroll shield has [hardness](ref/umr/hardness) 0 and hit points equal to the
highest-level wizard spell on the scroll. Each successful attack roll against the wizard reduces the
scroll shield's hit points by 1; this damage cannot be repaired, but does not affect casting from
the scroll. When its hit points reach 0, the scroll is destroyed.

At 5th level, when using a 3rd-level or higher wizard scroll as a scroll shield, the scrollmaster
can choose to reduce its enhancement bonus (to a minimum of a +1 enhancement bonus) to give it any
of the following shield properties: _[ghost touch](ref/magic-enh/ghost-touch-armor)_,
_[light fortification](ref/magic-enh/fortification-light)_,
_[moderate fortification](ref/magic-enh/fortification-moderate)_. Adding any of these properties
consumes an amount of bonus equal to the property's cost (see Table 15–5: Shield Special Abilities
in the _Core Rulebook_). The scrollmaster must know the prerequisite spell or spells to craft the
shield property in question (for example, he must know _[limited wish](ref/spell/limited-wish)_ to
be able to give his scroll shield the _fortification_ property).

If a scroll contains a spell with a metamagic feat, this ability uses the original spell level of
the spell (a _scroll of empowered fireball_ counts as a 3rd-level spell).

## Improved Scroll Casting (Su) {#improved-scroll-casting}

At 10th level, the scrollmaster can cast a wizard spell from a scroll and use his own Intelligence
score and relevant feats to set the DC for the spell, and can use his own caster level if it is
higher than that of the scroll (similar to a caster using a [staff](ref/rule/staves)). The
scrollmaster must have already deciphered the writing on the scroll to use this ability. This
ability replaces the 10th-level wizard bonus feat.
