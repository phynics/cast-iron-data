+++
id = "ref/arc-cleric/ecclesitheurge"
kind = "archetype"
title = "Ecclesitheurge"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Ecclesitheurge"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ecclesitheurge", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "advanced-class-guide"
page = "91"

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies", "The increase to channel energy gained at 3rd level"]
alters = ["The normal domain ability"]
+++

Eschewing physical armor for protection via the strength of his faith, an ecclesitheurge focuses on
the miracles his deity bestows and the breadth of that deity's dominion.

**Weapon and Armor Proficiency**

**Info:** An ecclesitheurge is proficient with the [club](ref/eq-weapon/club),
[dagger](ref/eq-weapon/dagger), [heavy crossbow](ref/eq-weapon/heavy-crossbow),
[light crossbow](ref/eq-weapon/light-crossbow), and [quarterstaff](ref/eq-weapon/quarterstaff), but
he's not proficient with any type of armor or shield.

**Replaces:** Weapon and armor proficiencies

**Ecclesitheurge's Vow**

**At 1st Level:** An ecclesitheurge makes a vow to his deity to be protected solely by his faith,
not by armor or shields. An ecclesitheurge who wears armor or uses a shield is unable to use his
_blessing of the faithful_ ability, use cleric domain powers, or cast cleric spells.

**Blessing of the Faithful (Su)**

**Standard:** The ecclesitheurge can bless one ally within close range (25 ft. + 5 ft./2 levels). A
blessed ally gains a +2 sacred or profane bonus (depending on whether the ecclesitheurge channels
positive or negative energy) on attack rolls, skill checks, ability checks, or saving throws or to
AC until the ecclesitheurge's next turn. The ecclesitheurge can expend 1 use of _channel energy_
when activating this ability to increase the duration to a number of rounds equal to the number of
dice of his channel energy.

**Domain Mastery**

**Action:** Ability

**Alters:** The normal domain ability

**Gained:** At 1st Level

When an ecclesitheurge first chooses his cleric domains, he designates one as his primary domain and
the other as his secondary domain. An ecclesitheurge can use his non-domain spell slots to prepare
spells from his primary domain's spell list.

Each day when he prepares spells, an ecclesitheurge can select a different domain granted by his
deity to gain access to that domain's spell list instead of his secondary domain spell list. He does
not lose access to his actual secondary domain's granted powers or gain access to the other domain's
granted powers. For example, an ecclesitheurge of [Sarenrae](ref/faith/sarenrae) with Glory as his
primary domain and Good as his secondary domain can choose to gain access to the
[Healing](ref/domain/healing) domain; until the next time he prepares spells, he uses the Healing
domain spell list as his secondary domain spell list instead of the Good domain spell list, but
still keeps the granted powers of the Good domain and does not gain the granted powers of the
Healing domain.

**Bonded Holy Symbol (Su)**

**Action:** Ability

**Gained:** At 3rd Level

**Replaces:** The increase to channel energy gained at 3rd level

An ecclesitheurge forms a powerful bond with a holy symbol of his deity, which functions identically
to a [wizard's](ref/class/wizard) _bonded object_ except it can be used to cast cleric and domain
spells (instead of wizard spells) and the ecclesitheurge can grant his _bonded holy symbol_ only
magic abilities appropriate for a holy symbol or a [neck slot](ref/rule/magic-items-on-the-body)
item.

As with a wizard's _bonded item,_ an ecclesitheurge can add additional magic abilities to his
_bonded holy symbol_ as if he had the required item creation feat (typically
[Craft Wondrous Item](ref/feat/craft-wondrous-item)), provided he meets the feat's level
prerequisites. For example, an ecclesitheurge with a _bonded holy symbol_ who wants to add a
wondrous amulet ability, like [amulet of natural armor](ref/magic-wondrous/amulet-of-natural-armor),
to his _bonded holy symbol_ must be at least 3rd level to do so. The magic properties of a _bonded
holy symbol,_ including any magic abilities the ecclesitheurge added to the object, function for
only the ecclesitheurge. If a _bonded holy symbol's_ owner dies or the item is replaced, the object
loses all enhancements the ecclesitheurge added using this ability.

**Bonded Object**

**Action:** Ability

**Flavor:** Text from the wizard class

If you select a bonded object, you begin play with one at no cost. These objects are always
masterwork quality. If you attempt to cast a spell without your bonded object worn or in hand, you
must make a [concentration](ref/rule/concentration) check or lose the spell. The DC for this check
is equal to 20 + the spell's level.

A bonded object can be used once per day to cast any one spell that you have in your spellbook and
are capable of casting, even if the spell is not prepared. This spell is treated like any other
spell cast by you, including casting time, duration, and other effects dependent on your level. This
spell cannot be modified by metamagic feats or other abilities.

If a bonded object is damaged, it is restored to full hit points the next time you prepare your
spells. If the object of an arcane bond is lost or destroyed, it can be replaced after 1 week in a
special ritual that costs 200 gp per wizard level plus the cost of the masterwork item. This ritual
takes 8 hours to complete. Items replaced in this way do not possess any of the additional
enchantments of the previous bonded item. You can designate an existing magic item as your bonded
item. This functions in the same way as replacing a lost or destroyed item except that the new magic
item retains its abilities while gaining the benefits and drawbacks of becoming a bonded item.
