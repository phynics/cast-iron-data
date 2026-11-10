+++
id = "ref/arc-magus/skirnir"
kind = "archetype"
title = "Skirnir"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Skirnir"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skirnir", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-combat"
page = "56"

[fields]
kind = "archetype"
replaces = ["Spell combat", "Spell recall", "Knowledge pool", "Improved spell combat", "greater spell combat", "greater spell access", "Counterstrike"]
alters = ["Spellstrike", "Spell combat"]
replaces_features = ["spell-combat", "spell-recall", "knowledge-pool", "improved-spell-combat", "greater-spell-combat", "greater-spell-access", "counterstrike"]
alters_features = ["spellstrike", "spell-combat"]
+++

Sometimes called a shield-vassal or shieldmaiden, the skirnir has learned to infuse his power into
his shield.

**Diminished Spellcasting**

**Ability:** A skirnir casts one fewer spell of each level than normal. If this reduces the number
to 0, he may cast spells of that level only if his Intelligence allows
[bonus spells](ref/rule/determine-bonuses) of that level.

**Arcane Bond (Su)**

**Ability:** A skirnir gains a shield (except for a tower shield) as an _arcane bond_ item. This is
identical to the [wizard](ref/class/wizard) class ability, but the skirnir may only bond with a
shield, not a familiar or other item.

**Gained:** At 1st Level

**Bonded Object**

**Action:** Ability

**Flavor:** Relevant text from the wizard ability.

You begin play with a bonded object at no cost. This object is always masterwork quality. Weapons
acquired at 1st level are not made of any special material. If the object is an amulet or ring, it
must be worn to have effect, while staves, wands, and weapons must be wielded. If you attempt to
cast a spell without your bonded object in hand, you must make a
[concentration](ref/rule/concentration) check or lose the spell. The DC for this check is equal to
20 + the spell's level.

A bonded object can be used once per day to cast any one spell that you have in your spellbook and
are capable of casting, even if the spell is not prepared. This spell is treated like any other
spell cast by you, including casting time, duration, and other effects dependent on your level. This
spell cannot be modified by metamagic feats or other abilities.

You can add additional magic abilities to your bonded object as if you have the required item
creation feats and if you meet the level prerequisites of the feat. For example, a wizard with a
bonded dagger must be at least 5th level to add magic abilities to the dagger (see
[Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor)). The magic properties of a bonded
object, including any magic abilities added to the object, only function for the wizard who owns it.
If a bonded object's owner dies, or the item is replaced, the object reverts to being an ordinary
masterwork item of the appropriate type.

If a bonded object is damaged, it is restored to full hit points the next time you prepare your
spells. If the object of an arcane bond is lost or destroyed, it can be replaced after 1 week in a
special ritual that costs 200 gp per wizard level plus the cost of the masterwork item. This ritual
takes 8 hours to complete. Items replaced in this way do not possess any of the additional
enchantments of the previous bonded item. You can designate an existing magic item as your bonded
item. This functions in the same way as replacing a lost or destroyed item except that the new magic
item retains its abilities while gaining the benefits and drawbacks of becoming a bonded item.

**Arcane Pool**

**Ability:** A skirnir can use his _arcane pool_ to grant an enhancement bonus to a weapon as
normal, as well as to his shield, paying the _arcane pool_ cost separately for each.

**At 5th Level:** He can also add the following shield special abilities:
[animated](ref/magic-enh/animated), [arrow catching](ref/magic-enh/arrow-catching),
[arrow deflection](ref/magic-enh/arrow-deflection), [bashing](ref/magic-enh/bashing),
[blinding](ref/magic-enh/blinding), [fortification](ref/magic-enh/fortification) (any),
[reflecting](ref/magic-enh/reflecting), [spell resistance](ref/magic-enh/spell-resistance) (any).

**Gained:** At 1st Level

**Sorcerous Shield (Ex)**

**Ability:** Skirnirs are proficient with all types of shields, including tower shields, and do not
suffer an arcane spell failure chance when casting magus spells while using a shield. They treat
their magus levels as their fighter levels for the purpose of qualifying for shield-related feats.

**Gained:** At 1st Level

**Replaces:** Spell combat

**Spellstrike (Su)**

**Ability:** A skirnir may use this ability with a weapon or [shield bash](ref/misc/shield-bash)
attack.

**Alters:** Spellstrike

**Gained:** At 1st Level

**Shield Pool (Ex)**

**Free:** A skirnir may spend 1 point from his _arcane pool_ to add his shield bonus to AC (not
including enhancement bonuses) on a [concentration](ref/rule/concentration) check to cast
defensively. He may also use a touch attack or shield bash with his shield in conjunction with any
_pool strike_ magus arcana.

**Gained:** At 4th Level

**Replaces:** Spell recall

**Spellshield (Su)**

**Gained:** At 7th Level

**Replaces:** Knowledge pool

**Standard:** A skirnir may store a magus spell in his shield by spending 1 point from his _arcane
pool_ per level of the spell. This functions as the [spell storing](ref/magic-enh/spell-storing)
weapon special ability, but activates only on a successful shield bash by the skirnir and is not
limited to spells of 3rd level or less.

**Shielded Spell Combat (Su)**

**Ability:** A skirnir gains the _spell combat_ ability, but only when wielding his _bonded shield._
A skirnir may use his shield hand to perform somatic components for magus spells, forfeiting the
shield's bonus to AC until the beginning of his next turn; if the _bonded shield_ is a buckler, he
retains its bonus to AC.

**Alters:** Spell combat

**At 14th Level:** He gains the benefits of _improved spell combat._

**At 19th Level:** He retains his shield's bonus to AC when using any type of shield with _spell
combat._

**Gained:** At 8th Level

**Replaces:** Improved spell combat, greater spell combat, greater spell access

**Greater Spellshield (Su)**

**Immediate:** A skirnir may activate a stored spell after being struck in combat. He may choose to
have the spell affect himself or the creature that struck him.

**Gained:** At 16th Level

**Replaces:** Counterstrike

**Magus Arcana:** The following magus arcana complement the skirnir archetype:
[arcane redoubt](ref/arcana/arcane-redoubt),
[greater arcane redoubt](ref/arcana/arcane-redoubt-greater),
[enduring blade](ref/arcana/enduring-blade) (may use on weapon or shield),
[pool strike](ref/arcana/pool-strike), [pool strike (arcing)](ref/arcana/pool-strike-arcing),
[pool strike (clinging)](ref/arcana/pool-strike-clinging),
[pool strike (thunderous)](ref/arcana/pool-strike-thunderous),
[prescient defense](ref/arcana/prescient-defense), [reflection](ref/arcana/reflection).
