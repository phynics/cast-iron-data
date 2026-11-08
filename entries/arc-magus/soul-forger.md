+++
id = "ref/arc-magus/soul-forger"
kind = "archetype"
title = "Soul Forger"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_forger", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]

[fields]
kind = "archetype"
replaces = ["Knowledge pool", "Spell recall", "Improved spell recall", "Counterstrike", "Greater spell access"]
alters = ["Spell combat", "Spellstrike"]
+++

**Sources:** Ultimate Combat pg 57\
The soul forger has learned the skill of infusing the raw magical essence of his soul into armaments
of surpassing power, combining the mystic arts with the arts of war in a unity of steely perfection.

**Diminished Spellcasting**

**Ability:** A soul forger casts one fewer spell of each level than normal. If this reduces the
number to 0, he may cast spells of that level only if his Intelligence allows
[bonus spells](ref/rule/determine-bonuses) of that level.

**Arcane Bond (Su)**

**Ability:** A soul forger gains a weapon as an _arcane bond_ item. This is identical to the
[wizard](ref/class/wizard) class ability, but the soul forger must select a weapon.

**Gained:** At 1st Level

**Bonded Object**

**Action:** Ability

**Flavor:** Relevant text from the wizard ability.

You begin play with a bonded object at no cost. This object is always masterwork quality. Weapons
acquired at 1st level are not made of any special material. Weapons must be wielded to have an
effect. If you attempt to cast a spell without your bonded object in hand, you must make a
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

**Spell Combat (Su)**

**Ability:** A soul forger may use this ability only when wielding his _bonded weapon._

**Alters:** Spell combat

**Spellstrike (Su)**

**Ability:** A soul forger may use this ability only when wielding his _bonded weapon._

**Alters:** Spellstrike

**Master Smith (Ex)**

**At 7th Level:** A soul forger uses the 1/10 gp value of armor, shields, and weapons to determine
how much time it takes to craft mundane items, and he requires only half the normal amount of time
to enchant magical arms and armor.

**Passive:** A soul forger adds his magus class level on [Craft](ref/skill/craft-any) checks to
manufacture armor, shields, and weapons. This bonus applies on skill checks required when using
[Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor).

**Replaces:** Knowledge pool

**Fortify Bond (Su)**

**Ability:** A soul forger may spend 1 point from his _arcane pool_ to increase the
[hardness](ref/umr/hardness) and hit points of his _bonded item_ by an amount equal to his magus
level. These hit points last until expended or until the soul forger next prepares spells. Multiple
uses of this ability overlap and do not stack.

**Gained:** At 4th Level

**Replaces:** Spell recall

**Reforge (Su)**

**Gained:** At 11th Level

**Replaces:** Improved spell recall

**Special:** Restoring the enchantments of a destroyed magical item requires additional points from
the soul forger's _arcane pool_ equal to the item's caster level. The soul forger gains one
temporary [negative level](ref/rule/energy-drain-and-negative-levels) if the item's caster level is
lower than his own, two negative levels if equal or greater (or none if the item is his _bonded
weapon_); the save DC to remove these negative levels is equal to 10 + the item's caster level.

**Standard:** A soul forger can restore a number of hit points equal to his magus level to a damaged
object by touching it and spending 1 point from his _arcane pool._ Repairing a destroyed object
takes 1 minute and materials equal to 1/4 the item's sale value, and restores the object to 1 hit
point.

**Destructive Counterstrike (Su)**

**Gained:** At 16th Level

**Passive:** An opponent who activates a magical item while threatened by a soul forger provokes an
attack of opportunity, either against the target or to [sunder](ref/rule/sunder) the item. If the
item is destroyed, its effects are negated.

**Replaces:** Counterstrike

**Instantaneous Reconstruction (Su)**

**Gained:** At 19th Level

**Provokes attack of opportunity:** No

**Replaces:** Greater spell access

**Standard:** A soul forger can reforge a destroyed item with a touch.

**Magus Arcana:** The following magus arcana complement the soul forger archetype:
[arcane accuracy](ref/arcana/arcane-accuracy), [bane blade](ref/arcana/bane-blade),
[devoted blade](ref/arcana/devoted-blade), [dispelling strike](ref/arcana/dispelling-strike),
[enduring blade](ref/arcana/enduring-blade), and [ghost blade](ref/arcana/ghost-blade).
