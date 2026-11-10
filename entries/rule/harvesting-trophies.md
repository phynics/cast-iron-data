+++
id = "ref/rule/harvesting-trophies"
kind = "rule"
title = "Harvesting Trophies"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harvesting_trophies", path = "json/rules_adv_gm04.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "162"

[fields]
kind = "none"
+++

When a monster is defeated in combat, the process of identifying what portions of the creature can
serve as a trophy and harvesting the trophy are somewhat abstracted; there's no need to track the
values for each part of every monster in the game once they're gathered as trophies.

In order to harvest and preserve a trophy from a kill, a character must attempt three checks: one to
determine what parts of the creature are worth harvesting for a trophy, one to determine if she
successfully harvests the trophy components without damaging or ruining them, and one to turn the
components into a permanent trophy.

**Identifying Trophies:** To identify what portions of a creature have value as trophies, a
character must succeed at a Knowledge check determined by the creature type, as normal. The DC for
this check is equal to 15 + the creature's CR. This examination takes 1 minute to perform.

**Harvesting Trophy Components:** Once a character identifies potential trophies, she must attempt a
skill check to harvest the relevant components. This is typically either a Survival check (for
external features, such as hide, horns, teeth, or the like) or a Heal check (for internal features,
such as blood, internal organs, or sweat). The DC for this check is equal to 15 + the creature's CR.
Harvesting trophy components generally takes 10 minutes of work (at the GM's discretion, this could
be as much as 1 hour of work for creatures whose bodies are particularly difficult to work with).

**Creating Trophies:** Once trophy components are harvested, they generally remain viable for 24
hours before decay or spoilage ruins them. Application of [gentle repose](ref/spell/gentle-repose),
[unguent of timelessness](ref/magic-wondrous/unguent-of-timelessness), or similar magic can extend
this period of decay. In order to turn components harvested from a creature into a long-lasting
trophy, a character must attempt a check with an appropriate Craft skill (the exact skill varies
according to the nature of the trophy the character is creating, but it is usually one from the
following list: alchemy, jewelry, leather, or taxidermy) to preserve the components and turn them
into a trophy. The DC of this check is equal to 15 + the creature's CR.

### Feats for Crafting Trophies

Although any character can take trophies from fallen creatures for cosmetic or roleplaying purposes,
the following feats allow characters to derive functionality from items they salvage from monstrous
corpses. These feats work similarly to item creation feats, except trophies are created using a
single Craft or Heal check, they are nonmagical, and the benefits they provide are typically
temporary. The DC of such a check is equal to 15 + the creature's CR, and creating a trophy takes a
number of minutes equal to the creature's CR.

- [Harvest Parts](ref/feat/harvest-parts)

  - [Grisly Ornament](ref/feat/grisly-ornament)

    - [Monstrous Crafter](ref/feat/monstrous-crafter)
