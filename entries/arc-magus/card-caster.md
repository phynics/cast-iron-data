+++
id = "ref/arc-magus/card-caster"
kind = "archetype"
title = "Card Caster"
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
replaces = ["Spellstrike", "Magus arcana gained at 3rd level"]
alters = ["Arcane pool"]
replaces_features = ["spellstrike"]
alters_features = ["arcane-pool"]
+++

Though it is known primarily as a tool of knowledge, the harrow is also an instrument of defense and
even war. The card caster is an ancient, martial offshoot of the traditional harrower, learning to
not only draw power from the harrow, but also to invest each card with deadly power.

**Deadly Dealer (Su)**

**Ability:** The card caster gains [Deadly Dealer](ref/feat/deadly-dealer) as a bonus feat, even if
he does not meet the prerequisites. A card caster can invest cards with enough magic to deal lethal
damage even without the [Arcane Strike](ref/feat/arcane-strike) feat so long as he has at least 1
point in his _arcane pool._

**Gained:** At 1st Level

**Arcane Pool Focus (Su)**

**Ability:** A card caster's _arcane pool_ can be used to augment only ranged weapons.

**Alters:** Arcane pool

**At 5th Level:** A card caster can use his _arcane pool_ to add the following weapon special
abilities to ranged weapons: [brilliant energy](ref/magic-enh/brilliant-energy),
[distance](ref/magic-enh/distance), [flaming](ref/magic-enh/flaming),
[flaming burst](ref/magic-enh/flaming-burst), [frost](ref/magic-enh/frost),
[icy burst](ref/magic-enh/icy-burst), [returning](ref/magic-enh/returning),
[seeking](ref/magic-enh/seeking), [shock](ref/magic-enh/shock),
[shocking burst](ref/magic-enh/shocking-burst), and [speed](ref/magic-enh/speed). He can use his
_arcane pool_ to augment an entire [harrow deck](ref/eq-misc/harrow-deck) as if it were ammunition.
All cards from a deck enhanced with a special ability, such as flaming, must share the same bonus.

**Harrowed Spellstrike (Su)**

**Ability:** A card caster can invest a single thrown weapon with a single touch or ranged spell as
part of the spell's normal casting time. The spell must target a single creature, and the spell's
range changes to match the thrown weapon's range increment. This ability otherwise functions
identically to _spellstrike,_ except it can only be applied to thrown ranged weapons instead of
melee attacks.

**Gained:** At 2nd Level

**Replaces:** Spellstrike

**Role Dealer (Su)**

**Gained:** At 3rd Level

**Passive:** Whenever the card caster randomly draws and throws a harrow card matching one axis of
his alignment, the card's critical threat range increases to 19-20. If the card caster draws and
throws a harrow card matching his alignment exactly, the attack's critical multiplier also increases
to &times&3 and the magus gains a +4 bonus on his confirmation roll.

**Replaces:** Magus arcana gained at 3rd level
