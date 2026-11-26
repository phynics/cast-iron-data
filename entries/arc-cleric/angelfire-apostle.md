+++
id = "ref/arc-cleric/angelfire-apostle"
kind = "archetype"
title = "Angelfire Apostle"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Angelfire%20Apostle"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "angelfire_apostle", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "healers-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "extra-channel", level = 1 },
  { anchor = "channel-angelfire" },
  { anchor = "versatile-healing-channel", level = 5 },
  { anchor = "cleansing-flames", level = 9 },
]
trades = [
  { alters = "The cleric's armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "The cleric's spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-angelfire"] },
]
+++

Angelfire apostles use the powers of good to avoid violence when possible and cleanse both maladies
and evil creatures with blinding flames. Angelfire apostles typically follow
[Sarenrae](ref/faith/sarenrae), but a few serve empyreal lords such as
[Ragathiel](ref/faith/ragathiel).

## Armor Proficiency {#armor-proficiency}

Angelfire apostles are not proficient with medium armor.

This ability alters the cleric's armor proficiency.

## Diminished Spellcasting {#diminished-spellcasting}

An angelfire apostle is less concerned with the traditional divine magic that many religious
adherents receive. The angelfire apostle receives one fewer spell slot at each spell level. When an
angelfire apostle gets no spells per day at a spell level, he can cast domain spells of that level
normally, but can only cast non-domain spells of that level if he gets them as
[bonus spells](ref/rule/determine-bonuses).

This ability alters the cleric's spellcasting.

## Extra Channel {#extra-channel}

At 1st level, the angelfire apostle gains [Extra Channel](ref/feat/extra-channel) as a bonus feat.

## Channel Angelfire (Su) {#channel-angelfire}

An angelfire apostle must be of good or neutral alignment and must choose to
[channel positive energy](ref/ability/channel-energy), even if his deity is neutral or if he is not
devoted to a particular deity. When an angelfire apostle channels positive energy, affected nongood
creatures are [dazzled](ref/misc/dazzled) for 1 round, with no saving throw for this effect, in
addition to experiencing the normal effects of channel energy.

This ability alters channel energy.

## Versatile Healing Channel (Sp) {#versatile-healing-channel}

At 5th level, the angelfire apostle can spend two uses of his channel energy ability to cast
_[remove blindness/deafness](ref/spell/remove-blindness-deafness)_ or
_[lesser restoration](ref/spell/restoration-lesser)_ as a
[spell-like ability](ref/umr/spell-like-abilities). At 7th level, he can choose
_[remove disease](ref/spell/remove-disease)_ or _[remove paralysis](ref/spell/remove-paralysis)_. At
9th level, he can choose _[neutralize poison](ref/spell/neutralize-poison)_. At 11th level, he can
choose _[breath of life](ref/spell/breath-of-life)_. At 13th level, he can choose
_[heal](ref/spell/heal)_. At 15th level, he can choose _[regenerate](ref/spell/regenerate)_. At 17th
level, he can choose _[restoration](ref/spell/restoration)_ but cannot affect permanent negative
levels. At 19th level, he can choose _[resurrection](ref/spell/resurrection)_ but can affect only a
target that has been dead no more than 1 round per his cleric level.

## Cleansing Flames (Su) {#cleansing-flames}

At 9th level, the angelfire apostle becomes a direct conduit for the righteous power of his deity.
Whenever the angelfire apostle casts a spell that belongs to the healing subschool that is a lower
spell level than the highest spell he can cast, he can unleash a blast of flames as a swift action
by expending one use of his channel energy ability. The flames last for 1 round and fill a
contiguous area equal to one 10-foot cube per level of the healing spell cast (at least one side of
the cube must be adjacent to the angelfire apostle's space). The flames deal 1d4 points of damage
per spell level. Half of the damage is fire damage, and half is raw divine power not subject to fire
resistance or immunity. Any creature in the area can halve the damage with a successful Reflex
saving throw against the spell's DC. The angelfire apostle can use this ability a number of times
per day equal to his Charisma modifier.
