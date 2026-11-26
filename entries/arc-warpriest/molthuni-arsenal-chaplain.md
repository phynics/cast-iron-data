+++
id = "ref/arc-warpriest/molthuni-arsenal-chaplain"
kind = "archetype"
title = "Molthuni Arsenal Chaplain"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Molthuni%20Arsenal%20Chaplain"
source_ids = ["weapon-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "molthuni_arsenal_chaplain", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "weapon-masters-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "war-blessing", level = 1 },
  { anchor = "sacred-weapon", level = 1 },
  { anchor = "weapon-training", level = 5 },
]
trades = [
  { replaces = "Sacred armor", feature = "sacred-armor", by = ["war-blessing"] },
  { replaces = "Channel energy", feature = "channel-energy", by = ["weapon-training"] },
  { alters = "Blessing", feature = "blessings", by = ["war-blessing"] },
  { alters = "Sacred weapon", feature = "sacred-weapon", by = ["sacred-weapon"] },
]
+++

Molthuni arsenal chaplains are warpriests trained in the Arsenal District in Korholm. They bolster
their nation's military by focusing on the militant aspects of their gods.

## War Blessing (Su) {#war-blessing}

A Molthuni arsenal chaplain must choose [War](ref/blessing/war) as his blessing, and can do so even
if it is a domain not normally granted by his deity. He does not receive a second blessing.

At 7th level, a Molthuni arsenal chaplain gains [Quicken Blessing](ref/feat/quicken-blessing) (War)
as a bonus feat even if he does not meet the prerequisites, but cannot grant a War blessing to
himself as a swift action with Quicken Blessing until he is at least 10th level.

At 13th level, a Molthuni arsenal chaplain can use the War blessing on an ally at a range of up to
30 feet by spending an additional use of the blessing ability.

At 16th level, a Molthuni arsenal chaplain can use the War blessing on a second target with a single
use of the blessing ability.

At 19th level, a Molthuni arsenal chaplain can use the War blessing on any number of targets at once
with a single use of the blessing ability.

This ability alters blessing and replaces sacred armor.

## Sacred Weapon (Su) {#sacred-weapon}

The base damage of a Molthuni arsenal chaplain's sacred weapon does not increase above 1d6. This
alters sacred weapon.

## Weapon Training (Ex) {#weapon-training}

At 5th level, a Molthuni arsenal chaplain gains weapon training as per the
[fighter](ref/class/fighter) class feature, but the benefits of this weapon training apply only to
the his sacred weapons (weapons with which the warpriest has taken
[Weapon Focus](ref/feat/weapon-focus)). This ability replaces channel energy.
