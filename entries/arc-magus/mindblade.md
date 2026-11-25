+++
id = "ref/arc-magus/mindblade"
kind = "archetype"
title = "Mindblade"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Mindblade"
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
features = [
  { anchor = "spells" },
  { anchor = "psychic-pool", level = 1 },
  { anchor = "psychic-access", level = 4 },
  { anchor = "dual-weapons", level = 7 },
  { anchor = "rapid-manifest", level = 8 },
  { anchor = "dual-manifest", level = 13 },
]
trades = [
  { replaces = "Spellcasting", feature = "spells", by = ["spells"] },
  { replaces = "Arcane pool", feature = "arcane-pool", by = ["psychic-pool"] },
  { replaces = "Spell recall", feature = "spell-recall", by = ["psychic-access"] },
  { replaces = "knowledge pool", feature = "knowledge-pool", by = ["psychic-access"] },
  { replaces = "improved spell recall", feature = "improved-spell-recall", by = ["psychic-access"] },
  { replaces = "greater spell combat", feature = "greater-spell-combat", by = ["psychic-access"] },
  { replaces = "greater spell access", feature = "greater-spell-access", by = ["psychic-access"] },
  { replaces = "Medium armor", feature = "medium-armor", by = ["dual-weapons"] },
  { replaces = "Improved spell combat", feature = "improved-spell-combat", by = ["rapid-manifest"] },
  { replaces = "Heavy armor", feature = "heavy-armor", by = ["dual-manifest"] },
]
+++

A mindblade blends psychic talent and martial skill to lethal effect. By forming weapons with her
mind, she always has the right tool for any situation.

## Spells {#spells}

A mindblade casts spells from the magus spell list as psychic spells. She can cast any spell she
knows without preparing it ahead of time. To learn or cast a spell, a mindblade must have an
Intelligence score equal to at least 10 + the spell's level. The saving throw DC to resist a
mindblade's spell is equal to 10 + the spell's level + the mindblade's Intelligence modifier.

Like other spellcasters, a mindblade can cast only a certain number of spells of each spell level
per day. She knows the same number of spells and receives the same number of spells slots per day as
a [bard](ref/class/bard) of her magus level, and knows and uses 0-level knacks as a bard uses
cantrips. In addition, she receives [bonus spells per day](ref/rule/determine-bonuses) if she has a
high Intelligence score (see Table 1–3 on page 17 of the _Core Rulebook_).

At 5th level and every 3 levels thereafter, a mindblade can learn a new spell in place of one she
already knows, using the same rules as a bard. In effect, the mindblade loses the old spell in
exchange for the new one. The new spell's level must be the same as that of the spell being
exchanged, and the new spell must be at least 1 level lower than the highest-level spell the
mindblade can cast.

A mindblade need not prepare her spells in advance. She can cast any magus spell she knows at any
time, assuming she has not yet used up her allotment of spells per day for the spell's level.

This ability replaces the magus's spellcasting.

## Psychic Pool (Su) {#psychic-pool}

A mindblade gains a psychic pool, similar to a normal magus's arcane pool. At 1st level, a mindblade
can expend 1 point from her psychic pool as a standard action to manifest a light melee weapon of
her choice, formed from psychic energy. By spending 2 points, the mindblade can manifest a
one-handed melee weapon, and by spending 3 points, she can manifest a two-handed melee weapon (but
not a [double](ref/misc/double) weapon). This psychic weapon can last indefinitely, but it vanishes
if it leaves the mindblade's hand. The mindblade can dismiss a held psychic weapon as a free action.
When a psychic weapon vanishes, the mindblade regains the psychic energy used to create it. She can
maintain only one weapon at a time.

At 1st level, a psychic weapon counts as a magic weapon of whatever type the mindblade selected,
with a +1 enhancement bonus. At 3rd level and every 3 levels thereafter, the weapon's enhancement
bonus increases by 1, up to maximum of +5 at 12th level. Starting at 5th level, the mindblade can
add any of the weapon special abilities listed in the arcane pool class feature in place of these
bonuses, although the weapon must maintain at least a +1 bonus to benefit from any weapon special
abilities. At 15th and 18th levels, the weapon gains an additional +1 enhancement bonus, which the
mindblade can spend only on weapon special abilities.

This ability replaces arcane pool, and counts as arcane pool for the purpose of feats, abilities,
and class features.

## Psychic Access (Su) {#psychic-access}

At 4th level, the mindblade gains access to an expanded spell list. She adds two spells from the
psychic class spell list to her magus spell list as magus spells of the same spell level. These must
be spells of levels the mindblade is able to cast. At 7th, 11th, 14th, and 19th levels, she adds two
more psychic class spells to her spell list, following the same restrictions. When a mindblade takes
the [spell blending](ref/arcana/spell-blending) arcana, she gains spells from the psychic class
spell list instead of the wizard spell list.

This ability replaces spell recall, knowledge pool, improved spell recall, greater spell combat, and
greater spell access.

## Dual Weapons (Su) {#dual-weapons}

At 7th level, a mindblade can maintain two psychic weapons at a time or a psychic double weapon,
though each weapon (or each end of a double weapon) has an enhancement bonus 1 lower than normal.
Starting at 12th level, each of the two psychic weapons (or each end of a double weapon) instead has
an enhancement bonus 2 lower than normal. When using two-weapon fighting with two psychic weapons or
a psychic double weapon, the mindblade can use her spell combat ability as though she had a hand
free. This ability replaces medium armor.

## Rapid Manifest (Su) {#rapid-manifest}

At 8th level, a mindblade can manifest a psychic weapon as a swift action. This ability replaces
improved spell combat.

## Dual Manifest (Su) {#dual-manifest}

At 13th level, a mindblade can manifest two psychic weapons with the same action. She must pay the
cost for both weapons. Also, when wielding a weapon two-handed, she can use her spell combat ability
as though she had a hand free. This ability replaces heavy armor.
