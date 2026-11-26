+++
id = "ref/arc-skald/totem-channeler"
kind = "archetype"
title = "Totem Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Totem%20Channeler"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "totem_channeler", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "disciples-doctrine"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "totemic-versatility", level = 1 },
  { anchor = "tandem-totems", level = 5 },
  { anchor = "totem-s-guidance", level = 9 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["totemic-versatility"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["tandem-totems"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["totem-s-guidance"] },
  { alters = "Rage powers", feature = "rage-powers", by = ["totemic-versatility"] },
]
+++

Some Shoanti skalds discover deeper truths in their tribes' totems. These skalds, known as totem
channelers, learn how to share the totems' gifts with their allies in the heat of battle.

## Totemic Versatility (Ex) {#totemic-versatility}

When a totem channeler learns a new rage power, he can select from more than one group of totem rage
powers, even though he normally could not do so. Totem rage powers grant benefits related to a
theme, are organized in groups of three, and usually have the word "totem" in their name. (Rules for
totem rage powers begin on page 74 of _Pathfinder RPG Advanced Player's Guide_.) When the totem
channeler starts an inspired rage raging song, he can add totem rage powers from only one group at a
time. He can change the group of added totem rage powers by ending the current inspired rage and
starting a new one.

This replaces bardic knowledge and alters rage powers.

## Tandem Totems (Ex) {#tandem-totems}

At 5th level, when a totem channeler starts an inspired rage raging song and adds a totem rage
power, he can add totem rage powers from a different group. Adding or maintaining totem rage powers
from the additional group requires spending 1 additional round of raging song each round. He can
activate up to two additional totem groups at 11th level and up to three additional totem groups at
17th level. He must spend 1 additional round of raging song each round for each additional totem
group. If the totem channeler does not have enough rounds of raging song remaining to maintain his
inspired rage, the song ends.

This replaces spell kenning.

## Totem's Guidance (Su) {#totem-s-guidance}

At 9th level, the totem channeler can draw strength and protection from his totem powers when he
wades into battle with song on his lips. When he adds a totem rage power to his inspired rage, he
and his allies gain a +1 insight bonus to AC and on saving throws for the duration of the totem
channeler's raging song. At 14th level, this bonus increases to +2. This bonus applies only to the
first totem rage power he applies to his inspired rage.

This replaces [damage reduction](ref/rule/damage-reduction).
