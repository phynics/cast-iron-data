+++
id = "ref/arc-druid/urushiol"
kind = "archetype"
title = "Urushiol"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Urushiol"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urushiol", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "toxic-secretions", level = 1 },
  { anchor = "venom-immunity" },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["toxic-secretions"] },
  { replaces = "resist nature's lure", feature = "resist-nature-s-lure", by = ["toxic-secretions"] },
  { alters = "Venom immunity", feature = "venom-immunity", by = ["venom-immunity"] },
]
+++

When an urushiol druid forms a bond with nature, it takes a vastly different form than for most
druids. His body becomes increasingly toxic, allowing him to secrete a deadly poison through his
pores.

## Toxic Secretions (Su) {#toxic-secretions}

At 1st level, an urushiol's body becomes capable of producing a single dose of poison per day. At
3rd level and every 2 druid levels thereafter, the number of daily doses increases by 1, to a
maximum of 10 doses at 19th level. The urushiol's daily doses are replenished when he regains his
spells, but any of his weapons that are still poisoned with urushiol venom count against his daily
limit. The urushiol is immune to his own poison and cannot accidentally poison himself when applying
his own poison or attacking with a weapon coated with it. Regardless of the delivery method he
chooses, his poison has the following base statistics.

### Urushiol Venom {#urushiol-venom}

_type_ poison (varies); _save_ Fortitude negates; _frequency_ 1/round for 2 rounds; _effect_ 1d3
Strength damage; _cure_ 1 save. The save DC is equal to 10 + 1/2 the urushiol's level + his Wisdom
modifier.

At 1st level, an urushiol can secrete this poison as a numbing injury poison on a natural weapon,
unarmed strike, or manufactured weapon by spending 1 of his daily doses as a standard action. He
must choose a natural weapon, unarmed strike, or manufactured weapon in his hand that deals piercing
or slashing damage and that is not already poisoned or poisonous. The weapon remains poisoned until
the urushiol scores a hit with it, the weapon leaves his possession for more than 1 round, or the
poison is wiped away.

At 4th level, an urushiol's body becomes so saturated with poison that even his flesh is poisonous.

Whenever a creature damages the urushiol with a bite or [swallow whole](ref/umr/swallow-whole)
attack, the urushiol can release ingested poison into the creature by spending 1 of his daily doses
as an immediate action.

At 7th level, an urushiol can spend 2 daily doses of his poison as a standard action to secrete a
contact poison and coat one of his limbs with the secreted poison. The urushiol can deliver the
poison by making a successful touch attack as a standard action, which can be part of the same
standard action he used to secrete the poison. If the attack misses, the poison persists upon his
limb throughout the subsequent rounds until he hits a target or touches something else with his
poisoned limb.

At 11th level, an urushiol can spend 3 daily doses of his poison as a standard action to release a
20-foot-radius cloud of inhaled poison centered around him that lasts for 1 round.

At 14th level, an urushiol's venom changes in frequency to 1/round for 4 rounds. In addition, when
using his urushiol venom, an urushiol can spend an extra dose of his poison to change the damage
type of the poison to Dexterity damage or Constitution damage. He can use this alteration in
combination with any of the other abilities. For example, he could spend a total of 3 doses to
create a cloud of inhaled poison that deals Constitution damage.

This ability replaces nature bond and resist nature's lure.

## Venom Immunity (Ex) {#venom-immunity}

An urushiol gains venom immunity at 4th level instead of 9th level.

This ability alters venom immunity.
