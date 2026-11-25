+++
id = "ref/arc-witch/scarred-witch-doctor"
kind = "archetype"
title = "Scarred Witch Doctor"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Scarred%20Witch%20Doctor"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scarred_witch_doctor", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "advanced-race-guide"
page = "140"

[fields]
kind = "archetype"
features = [
  { anchor = "fierce-intelligence" },
  { anchor = "hex-scar" },
  { anchor = "fetish-mask", level = 1 },
  { anchor = "scarshield", level = 1 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["fetish-mask"] },
  { replaces = "1st-level hex", feature = "hex", levels = [1], by = ["scarshield"] },
]
+++

The scarred witch doctor draws power from her ability to endure pain and suffering. She mutilates
her own flesh, inflicting horrific scars, in order to attract the attention of her patron. Rather
than call forth a familiar, she creates a repulsive fetish mask that she uses as a repository for
her power. A scarred witch doctor has the following class features.

## Fierce Intelligence {#fierce-intelligence}

A scarred witch doctor treats her Intelligence as 2 points higher when determining the highest level
of spells she can cast, the number of spells she can cast per day, her spell save DCs, her number of
spells known at 1st level, and any effects of her hexes determined by her Intelligence.

## Hex Scar {#hex-scar}

Whenever a scarred witch doctor learns a hex, she must carve or brand a symbol in her flesh to
represent this hex. She can disguise these scars with mundane or magical means, but they cannot be
permanently removed.

## Fetish Mask (Su) {#fetish-mask}

At 1st level, a scarred witch doctor forms a bond with a wooden mask. As she gains power, her
connection to this mask causes it to grow ever more hideous and grotesque as it absorbs the weight
of the self-induced pain that underlies her magic. Her spells derive from the insights her patron
grants her while she's enduring the cuts, burns, and other sorts of mutilations she inflicts upon
herself. Her fetish mask acts in all ways like a witch's familiar for the purpose of preparing and
gaining spells. Rather than communing with a familiar to prepare spells each day, a scarred witch
doctor hangs her mask on a wall, tree branch, or something similar and contemplates the agony it
represents.

When wearing her fetish mask, a scarred witch doctor gains a +2 circumstance bonus on Heal and
Intimidate checks and gains a +2 bonus on saving throws against effects that specifically cause pain
or have the pain descriptor. If the mask is destroyed, the witch doctor can create another fetish
mask (which almost immediately adopts the shocking appearance of the original) for the same price
and time it takes a witch to replace a dead familiar.

At 5th level, the scarred witch doctor gains the ability to add magical abilities to her mask as if
she had the [Craft Wondrous Item](ref/feat/craft-wondrous-item) feat.

This ability otherwise functions like and replaces the standard witch familiar.

## Scarshield (Su) {#scarshield}

At 1st level, a scarred witch doctor learns how to harden her mutilated skin, gaining an enhancement
bonus to her natural armor bonus equal to 1/2 her class level (minimum +1). She can use this ability
for a number of minutes per day equal to her class level. These minutes do not need to be
consecutive but she must spend them in 1-minute increments. This ability replaces the witch's
1st-level hex.

## Hexes {#hexes}

The following hexes complement the scarred witch doctor archetype: evil eye, misfortune (_Advanced
Player's Guide_); scar, unnerve beasts (_Ultimate Magic_).

## Major Hexes {#major-hexes}

The following major hexes complement the scarred witch doctor archetype: agony, nightmare (_Advanced
Player's Guide_); cook people, infected wounds (_Ultimate Magic_).

## Grand Hexes {#grand-hexes}

The following grand hexes complement the scarred witch doctor archetype: death curse, natural
disaster (_Advanced Player's Guide_); dire prophecy (_Ultimate Magic_).
