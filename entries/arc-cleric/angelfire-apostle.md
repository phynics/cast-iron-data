+++
id = "ref/arc-cleric/angelfire-apostle"
kind = "archetype"
title = "Angelfire Apostle"
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
alters = ["The cleric's armor proficiency", "The cleric's spellcasting", "Channel energy"]
alters_features = ["channel-energy"]
+++

Angelfire apostles use the powers of good to avoid violence when possible and cleanse both maladies
and evil creatures with blinding flames. Angelfire apostles typically follow
[Sarenrae](ref/faith/sarenrae), but a few serve empyreal lords such as
[Ragathiel](ref/faith/ragathiel).

**Prerequisites:** An angelfire apostle must be of good or neutral alignment.

**Armor Proficiency**

**Alters:** The cleric's armor proficiency

**Info:** Angelfire apostles are not proficient with medium armor.

**Diminished Spellcasting**

**Alters:** The cleric's spellcasting

**Flavor:** An angelfire apostle is less concerned with the traditional divine magic that many
religious adherents receive.

**Info:** The angelfire apostle receives one fewer spell slot at each spell level. When an angelfire
apostle gets no spells per day at a spell level, he can cast domain spells of that level normally,
but can only cast non-domain spells of that level if he gets them as
[bonus spells](ref/rule/determine-bonuses).

**Extra Channel**

**Ability:** The angelfire apostle gains [Extra Channel](ref/feat/extra-channel) as a bonus feat.

**Gained:** At 1st Level

**Channel Angelfire (Su)**

**Alters:** Channel energy

**Info:** An angelfire apostle must choose to [channel positive energy](ref/ability/channel-energy),
even if his deity is neutral or if he is not devoted to a particular deity.

**Passive:** When an angelfire apostle channels positive energy, affected nongood creatures are
[dazzled](ref/misc/dazzled) for 1 round, with no saving throw for this effect, in addition to
experiencing the normal effects of channel energy.

**Versatile Healing Channel (Sp)**

**At 11th Level:** He can choose [breath of life](ref/spell/breath-of-life).

**At 13th Level:** He can choose [heal](ref/spell/heal).

**At 15th Level:** He can choose [regenerate](ref/spell/regenerate).

**At 17th Level:** He can choose [restoration](ref/spell/restoration) but cannot affect permanent
negative levels.

**At 19th Level:** He can choose [resurrection](ref/spell/resurrection) but can affect only a target
that has been dead no more than 1 round per his cleric level.

**At 5th Level:** The angelfire apostle can spend two uses of his channel energy ability to cast
[remove blindness/deafness](ref/spell/remove-blindness-deafness) or
[lesser restoration](ref/spell/restoration-lesser) as a
[spell-like ability](ref/umr/spell-like-abilities).

**At 7th Level:** He can choose [remove disease](ref/spell/remove-disease) or
[remove paralysis](ref/spell/remove-paralysis).

**At 9th Level:** He can choose [neutralize poison](ref/spell/neutralize-poison).

**Cleansing Flames (Su)**

**Flavor:** The angelfire apostle becomes a direct conduit for the righteous power of his deity.

**Gained:** At 9th Level

**Swift:** Whenever the angelfire apostle casts a spell that belongs to the healing subschool that
is a lower spell level than the highest spell he can cast, he can unleash a blast of flames by
expending one use of his channel energy ability. The flames last for 1 round and fill a contiguous
area equal to one 10-foot cube per level of the healing spell cast (at least one side of the cube
must be adjacent to the angelfire apostle's space). The flames deal 1d4 points of damage per spell
level. Half of the damage is fire damage, and half is raw divine power not subject to fire
resistance or immunity. Any creature in the area can halve the damage with a successful Reflex
saving throw against the spell's DC.

**Usage:** Cha modifier times/day
