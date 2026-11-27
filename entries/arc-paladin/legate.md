+++
id = "ref/arc-paladin/legate"
kind = "archetype"
title = "Legate"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Legate"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "legate", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "celestial-armor", level = 3 },
]
trades = [
  { replaces = "Mercy", feature = "mercy", by = ["celestial-armor"] },
]
+++

The first legates in the Inner Sea region were ambassadors from Holomog, a celestial-worshiping
confederation in southern Garund. Though they hold to the same strict paladin code, legates present
themselves not as armed crusaders, but as peaceful envoys and advisors, bringing wisdom garnered
from the long, stable history of their nation. They often serve as diplomats (and sometimes spies)
for good organizations. Yet woe to those who believe them defenseless, for a legate can call upon
her divine patron to provide her with armor and weapons.

## Celestial Armor (Sp) {#celestial-armor}

At 3rd level, a legate can conjure armor as a standard action. This ability acts as the spell
_[instant armor](ref/spell/instant-armor)_, using her paladin level as her caster level, except as
follows. At 6th level and every 3 paladin levels thereafter, the armor gains an additional +1
enhancement bonus. These bonuses can be used to add any of the following armor special abilities:
_[champion](ref/magic-enh/champion)_, _[fortification](ref/magic-enh/fortification)_ (heavy, light,
or medium), _[invulnerability](ref/magic-enh/invulnerability)_, or
_[spell resistance](ref/magic-enh/spell-resistance)_ (13, 15, 17, or 19). In addition, the legate
can grant her armor the _[energy resistance](ref/magic-enh/energy-resistance)_ special ability at
the cost of a +3 bonus, the _[improved energy resistance](ref/magic-enh/energy-resistance-improved)_
special ability at the cost of a +5 bonus, or the _[righteous](ref/magic-enh/righteous)_ special
ability at a cost of a +4 bonus. The armor must have least a +1 enhancement bonus before any special
abilities can be added. The bonus and special abilities granted are determined when this ability is
used and cannot be changed until this ability is used again. If the legate has a steed bond and is
riding her steed, she can include her steed when summoning celestial armor, granting the steed
barding with the same bonuses and special abilities as her own. The legate can use this ability a
number of times per day equal to her Wisdom bonus plus [half](ref/misc/fractions-and-rounding) her
paladin level.

This ability replaces mercy.
