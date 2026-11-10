+++
id = "ref/arc-magus/mindblade"
kind = "archetype"
title = "Mindblade"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindblade", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "occult-adventures"
page = "121"

[fields]
kind = "archetype"
replaces = ["Spellcasting", "Arcane pool", "Spell recall", "knowledge pool", "improved spell recall", "greater spell combat", "greater spell access", "Medium armor", "Improved spell combat", "Heavy armor"]
replaces_features = ["arcane-pool", "spell-recall", "knowledge-pool", "improved-spell-recall", "greater-spell-combat", "greater-spell-access", "medium-armor", "improved-spell-combat", "heavy-armor"]
+++

A mindblade blends psychic talent and martial skill to lethal effect. By forming weapons with her
mind, she always has the right tool for any situation.

**Spells**

**Action:** Ability

**Replaces:** Spellcasting

A mindblade casts spells from the magus spell list as psychic spells. She can cast any spell she
knows without preparing it ahead of time. To learn or cast a spell, a mindblade must have an
Intelligence score equal to at least 10 + the spell's level. The saving throw DC to resist a
mindblade's spell is equal to 10 + the spell's level + the mindblade's Intelligence modifier.

Like other spellcasters, a mindblade can cast only a certain number of spells of each spell level
per day. She knows the same number of spells and receives the same number of spells slots per day as
a [bard](ref/class/bard) of her magus level, and knows and uses 0-level knacks as a bard uses
cantrips. In addition, she receives [bonus spells per day](ref/rule/determine-bonuses) if she has a
high Intelligence score.

At 5th level and every 3 levels thereafter, a mindblade can learn a new spell in place of one she
already knows, using the same rules as a bard. In effect, the mindblade loses the old spell in
exchange for the new one. The new spell's level must be the same as that of the spell being
exchanged, and the new spell must be at least 1 level lower than the highest-level spell the
mindblade can cast.

A mindblade need not prepare her spells in advance. She can cast any magus spell she knows at any
time, assuming she has not yet used up her allotment of spells per day for the spell's level.

**Psychic Pool (Su)**

**Ability:** A mindblade gains a _psychic pool,_ similar to a normal magus's _arcane pool._

**At 1st Level:** A mindblade can expend 1 point from her _psychic pool_ as a **standard action** to
manifest a light melee weapon of her choice, formed from psychic energy. By spending 2 points, the
mindblade can manifest a one-handed melee weapon, and by spending 3 points, she can manifest a
two-handed melee weapon (but not a [double](ref/misc/double) weapon). This psychic weapon can last
indefinitely, but it vanishes if it leaves the mindblade's hand. The mindblade can dismiss a held
psychic weapon as a **free action**. When a psychic weapon vanishes, the mindblade regains the
psychic energy used to create it. She can maintain only one weapon at a time. A psychic weapon
counts as a magic weapon of whatever type the mindblade selected, with an enhancement bonus equal to
1 + [one-third](ref/misc/fractions-and-rounding) of her magus level, to a maximum of +5 at 12th
level. At 15th and 18th levels, the weapon gains an additional +1 enhancement bonus, which the
mindblade can spend only on weapon special abilities (see below).

**At 5th Level:** The mindblade can add any of the weapon special abilities listed in the _arcane
pool_ class feature in place of these bonuses, although the weapon must maintain at least a +1 bonus
to benefit from any weapon special abilities.

**Replaces:** Arcane pool

**Special:** This ability counts as _arcane pool_ for the purpose of feats, abilities, and class
features.

**Psychic Access (Su)**

**Ability:** The mindblade gains access to an expanded spell list. She adds two spells from the
psychic class spell list to her magus spell list as magus spells of the same spell level. These must
be spells of levels the mindblade is able to cast.

**Gained:** At 4th Level

**Repeat At:** She adds two more psychic class spells to her spell list, following the same
restrictions., 7, 11, 14, 19

**Replaces:** Spell recall, knowledge pool, improved spell recall, greater spell combat, greater
spell access

**Special:** When a mindblade takes the [spell blending](ref/arcana/spell-blending) arcana, she
gains spells from the psychic class spell list instead of the wizard spell list.

**Dual Weapons (Su)**

**At 12th Level:** Each of the two psychic weapons (or each end of a double weapon) instead has an
enhancement bonus 2 lower than normal. When using two-weapon fighting with two psychic weapons or a
psychic double weapon, the mindblade can use her _spell combat_ ability as though she had a hand
free.

**At 7th Level:** A mindblade can maintain two psychic weapons at a time or a psychic double weapon,
though each weapon (or each end of a double weapon) has an enhancement bonus 1 lower than normal.

**Replaces:** Medium armor

**Rapid Manifest (Su)**

**Gained:** At 8th Level

**Replaces:** Improved spell combat

**Swift:** A mindblade can manifest a psychic weapon as a swift action.

**Dual Manifest (Su)**

**Ability:** A mindblade can manifest two psychic weapons with the same action. She must pay the
cost for both weapons. Also, when wielding a weapon two-handed, she can use her _spell combat_
ability as though she had a hand free.

**Gained:** At 13th Level

**Replaces:** Heavy armor
