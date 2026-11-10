+++
id = "ref/feat/bless-equipment"
kind = "feat"
title = "Bless Equipment"
aon = "FeatDisplay.aspx?ItemName=Bless%20Equipment"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bless_equipment", path = "json/feat02.json" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "7"

[fields]
kind = "feat"
prerequisites = "Caster level 3rd, channel energy class feature."
benefit = "As a standard action, you may expend uses of your channel energy ability to touch a single weapon, suit of armor, or shield and temporarily grant it one weapon, armor, or shield special ability. To bless a piece of equipment with a particular blessing, you must expend a number of uses of channel energy equal to the number listed in the table above, and your caster level must be equal to or greater than that listed for the selected blessing."
+++

You can bless armor and weapons with a touch to imbue them with magical properties.\
**Prerequisites:** Caster level 3rd, [channel energy](ref/ability/channel-energy) class feature.\
**Benefit:** As a standard action, you may expend uses of your channel energy ability to touch a
single weapon, suit of armor, or shield and temporarily grant it one weapon, armor, or shield
special ability. To bless a piece of equipment with a particular blessing, you must expend a number
of uses of channel energy equal to the number listed in the table above, and your caster level must
be equal to or greater than that listed for the selected blessing.

This blessing lasts for a number of rounds equal to the number of damage dice you are capable of
dealing or healing with your channel energy ability (for example, the blessing of a cleric capable
of channeling 3d6 points of damage would last for 3 rounds), during which time the item is treated
as though it possessed the selected special ability. If the piece of equipment belongs to an
unwilling creature, that creature may attempt a Will save to prevent the blessing, as if attempting
a saving throw against your channel energy ability (so bonuses from
[channel resistance](ref/rule/channel-resistance) and similar effects apply); if the creature
succeeds at its save, the channeled energy is expended to no effect.

Only magical and masterwork weapons, armor, and shields may be blessed with this feat. When you
bless a masterwork item, you must expend one additional use of your channel energy ability beyond
those normally expended to grant the selected blessing. In addition to the selected blessing, the
masterwork item gains a temporary +1 enhancement bonus for the blessing's duration.

You can grant a piece of equipment only one blessing at a time. Blessing an item that has already
been blessed by you or another character replaces the preexisting blessing with the new one and
resets the duration.

### Equipment Blessings

|Weapon Blessings|Uses of Channel Energy|Caster Level Required|
| --- | --- | --- |
|[Bane](ref/magic-enh/bane) ^[1](ref/feat/bless-equipment#footnote-n)^|2|3rd|
|[Ghost touch](ref/magic-enh/ghost-touch-weapon)|2|3rd|
|[Disruption](ref/magic-enh/disruption)|3|6th|
|[Lifesurge](ref/magic-enh/lifesurge)|3|6th|
|[Nullifying](ref/magic-enh/nullifying)|4|9th|

|Armor/Shield Blessings|Uses of Channel Energy|Caster Level Required|
| --- | --- | --- |
|[Deathless](ref/magic-enh/deathless) ^[2](ref/feat/bless-equipment#footnote-s)^|2|3rd|
|[Stanching](ref/magic-enh/stanching) ^[2](ref/feat/bless-equipment#footnote-s)^|2|3rd|
|[Ghost touch](ref/magic-enh/ghost-touch-armor)|4|9th|
|[Undead-controlling](ref/magic-enh/undead-controlling)|6|13th|

###### ^1^ {#footnote-n}

You must choose the creature type or subtype at the time of blessing.

###### ^2^ {#footnote-s}

Cannot be applied to shields.
