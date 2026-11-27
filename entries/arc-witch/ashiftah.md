+++
id = "ref/arc-witch/ashiftah"
kind = "archetype"
title = "Ashiftah"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Ashiftah"
source_ids = ["qadira-jewel-of-the-east"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ashiftah", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "qadira-jewel-of-the-east"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "protecting-veil", level = 1 },
  { anchor = "ghostwalk", level = 2 },
  { anchor = "deliver-touch-spells", level = 3 },
  { anchor = "fog-of-war", level = 6 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["protecting-veil"] },
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["ghostwalk"] },
  { replaces = "Hex gained at 6th level", feature = "hex", levels = [6], by = ["fog-of-war"] },
]
+++

Qadira's armies strike terror into foes, but tales of something even more terrible than desert
dervishes or charging cavalry haunt foot soldiers serving Qadira's neighbors. Known in Taldane as a
"battle witch," an ashiftah drifts like a phantom among the enemy armies, calling down disaster upon
their heads and weakening their resolve. Qadiran ashiftahs usually go veiled, and even their cohorts
in the Imperial Forces superstitiously believe that seeing their faces brings misfortune.

## Protecting Veil {#protecting-veil}

An ashiftah's veil is not merely a uniform, but a magical vestment imbued with power. Its ability to
hold spells functions identically to a witch's familiar. An ashiftah must veil herself and commune
with her patron each day to prepare her spells and cannot prepare spells not stored in the veil.

This ability replaces familiar.

## Ghostwalk (Su) {#ghostwalk}

Starting at 2nd level, as a move action after using a hex, an ashiftah can become invisible as per
_[vanish](ref/spell/vanish)_ and can then take a 5-foot step. Using ghostwalk doesn't provoke
attacks of opportunity.

This ability replaces the hex gained at 2nd level.

## Deliver Touch Spells (Su) {#deliver-touch-spells}

Starting at 3rd level, an ashiftah can use her veil to deliver touch spells. After casting a touch
spell, as a full-round action, she can tear a strip from her veil and whisper to it, designating a
target. She then releases the scrap of fabric, which drifts on the wind to the target and delivers
the spell as a ranged touch attack. The target must be within 20 feet of the witch. The veil mends
itself after the spell is delivered.

## Fog of War (Sp) {#fog-of-war}

At 6th level, as a standard action, an ashiftah can blanket a 20-foot-radius area of the battlefield
in a clammy mist that functions as per _[barrow haze](ref/spell/barrow-haze)_, allowing her to treat
any area within the mist as within 30 feet for purposes of her hexes, as long as some part of that
area is within 30 feet of her.

This replaces the hex gained at 6th level.
