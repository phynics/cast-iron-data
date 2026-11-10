+++
id = "ref/subtype/mythic"
kind = "rule"
title = "Mythic"
source_ids = ["bestiary-5", "bestiary-4", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mythic", path = "json/monster_subtypes.json" },
]
[[sources]]
publication = "bestiary-5"
[[sources]]
publication = "bestiary-4"
[[sources]]
publication = "mythic-adventures"

[fields]
kind = "none"
+++

## Subtype: Mythic

A creature with this subtype is infused with mythic power and is capable of terrible and
awe-inspiring feats. Some mythic creatures are powerful versions of existing monsters (such as
minotaurs and medusas), others are completely new creatures that do not have a non-mythic equivalent
(such as the [devastator](ref/monster/devastator-mythic) and
[plague swarms](ref/family/plague-swarm)). For more information on mythic creatures, see the
[Mythic Rules](ref/rule/mythic-rules). Creatures with the mythic subtype have the following traits.

- Mythic rank, a number from 1 to 10, representing its overall mythic power.
- Natural armor increase equal to its mythic rank.
- Additional hit points per mythic rank, based on the type of Hit Dice it has (d6, d8, and so on).
- DR 5/epic if the creature has at least 5 Hit Dice. If the creature already had DR, it adds epic to
  the qualities needed to bypass that reduction.
- [Spell resistance](ref/rule/spell-resistance) increase (if it has spell resistance) equal to its
  mythic rank.
- Ability score increases, depending on its mythic rank.
- Mythic feats, which generally are improved versions of standard feats.
- **Mythic Power (Su):** The creature has the [mythic power](ref/umr/mythic-power) universal monster
  ability. The effect of these abilities depend on its mythic rank.
