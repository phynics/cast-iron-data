+++
id = "ref/arc-witch/cartomancer"
kind = "archetype"
title = "Cartomancer"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Cartomancer"
source_ids = ["the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cartomancer", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "the-harrow-handbook"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "spell-deck", level = 1 },
  { anchor = "deliver-touch-spells", level = 3 },
  { anchor = "deadly-dealer", level = 2 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["spell-deck"] },
  { replaces = "2nd-level hex", feature = "hex", levels = [2], by = ["deadly-dealer"] },
]
+++

More than mere playing cards, harrow decks allow individuals to communicate with powers beyond
mortal ken. A witch who serves the spirits of the harrow in exchange for mystical power is known as
a cartomancer. Rather than connecting with a familiar, a cartomancer communes with her patron
through a consecrated harrow deck.

## Spell Deck {#spell-deck}

Each cartomancer carries a special [harrow deck](ref/eq-misc/harrow-deck) that allows her to
communicate with her patron. Its ability to hold spells functions identically to the way a witch's
spells are granted by her familiar. The cartomancer must consult her harrow deck each day to prepare
her spells and cannot prepare spells that are not stored in the deck. The spell deck cannot be used
for this purpose if any cards are missing. This ability replaces the witch's familiar. The following
familiar ability works differently for a cartomancer.

## Deliver Touch Spells (Su) {#deliver-touch-spells}

At 3rd level, when the cartomancer uses the Deadly Dealer feat with a card from her spell deck, the
card is not destroyed and gains the _[returning](ref/magic-enh/returning)_ weapon special ability.

In addition, the cartomancer can deliver a touch spell with a thrown card. This uses the Deadly
Dealer feat (see below), except the attack is resolved as a ranged touch attack and the card deals
no damage of its own. This ability can be used with any card (not just one from the cartomancer's
spell deck).

## Deadly Dealer {#deadly-dealer}

At 2nd level, a cartomancer gains the [Deadly Dealer](ref/feat/deadly-dealer) feat (see sidebar) as
a bonus feat, even if she does not meet the prerequisites. The cartomancer gains the benefits of the
[Arcane Strike](ref/feat/arcane-strike) feat, but only for the purposes of using Deadly Dealer. This
replaces the witch's 2nd-level hex.

## Hexes {#hexes}

The following witch hexes complement the cartomancer archetype: evil eye, fortune, misfortune,
soothsayer (see below).

## Major Hexes {#major-hexes}

The following major hexes complement the cartomancer archetype: harrowing curse (see below), vision.

## Grand Hexes {#grand-hexes}

The following grand hex complements the cartomancer archetype: dire prophecy.
