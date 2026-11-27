+++
id = "ref/arc-magus/card-caster"
kind = "archetype"
title = "Card Caster"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Card%20Caster"
source_ids = ["the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "card_caster", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "the-harrow-handbook"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "deadly-dealer", level = 1 },
  { anchor = "arcane-pool-focus", level = 1 },
  { anchor = "harrowed-spellstrike", level = 2 },
  { anchor = "role-dealer", level = 3 },
]
trades = [
  { replaces = "Spellstrike", feature = "spellstrike", by = ["harrowed-spellstrike"] },
  { replaces = "Magus arcana gained at 3rd level", feature = "magus-arcana", levels = [3], by = ["role-dealer"] },
  { alters = "Arcane pool", feature = "arcane-pool", by = ["arcane-pool-focus"] },
]
+++

Though it is known primarily as a tool of knowledge, the harrow is also an instrument of defense and
even war. The card caster is an ancient, martial offshoot of the traditional harrower, learning to
not only draw power from the harrow, but also to invest each card with deadly power.

## Deadly Dealer (Su) {#deadly-dealer}

At 1st level, the card caster gains [Deadly Dealer](ref/feat/deadly-dealer) (see page 15) as a bonus
feat, even if he does not meet the prerequisites. A card caster can invest cards with enough magic
to deal lethal damage even without the [Arcane Strike](ref/feat/arcane-strike) feat so long as he
has at least 1 point in his arcane pool.

## Arcane Pool Focus (Su) {#arcane-pool-focus}

A card caster's arcane pool can be used to augment only ranged weapons. At 5th level, a card caster
can use his arcane pool to add the following weapon special abilities to ranged weapons:
_[brilliant energy](ref/magic-enh/brilliant-energy)_, _[distance](ref/magic-enh/distance)_,
_[flaming](ref/magic-enh/flaming)_, _[flaming burst](ref/magic-enh/flaming-burst)_,
_[frost](ref/magic-enh/frost)_, _[icy burst](ref/magic-enh/icy-burst)_,
_[returning](ref/magic-enh/returning)_, _[seeking](ref/magic-enh/seeking)_,
_[shock](ref/magic-enh/shock)_, _[shocking burst](ref/magic-enh/shocking-burst)_, and
_[speed](ref/magic-enh/speed)_. He can use his arcane pool to augment an entire
[harrow deck](ref/eq-misc/harrow-deck) as if it were ammunition. All cards from a deck enhanced with
a special ability, such as _flaming_, must share the same bonus. This ability modifies arcane pool.

## Harrowed Spellstrike (Su) {#harrowed-spellstrike}

Beginning at 2nd level, a card caster can invest a single thrown weapon with a single touch or
ranged spell as part of the spell's normal casting time. The spell must target a single creature,
and the spell's range changes to match the thrown weapon's range increment. This ability otherwise
functions identically to spellstrike, except it can only be applied to thrown ranged weapons instead
of melee attacks. This ability replaces and modifies spellstrike.

## Role Dealer (Su) {#role-dealer}

Beginning at 3rd level, whenever the card caster randomly draws and throws a harrow card matching
one axis of his alignment, the card's critical threat range increases to 19-20. If the card caster
draws and throws a harrow card matching his alignment exactly, the attack's critical multiplier also
increases to ×3 and the magus gains a +4 bonus on his confirmation roll. This ability replaces the
magus arcana gained at 3rd level.
