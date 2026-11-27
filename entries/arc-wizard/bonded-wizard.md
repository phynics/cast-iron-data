+++
id = "ref/arc-wizard/bonded-wizard"
kind = "archetype"
title = "Bonded Wizard"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Bonded%20Wizard"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bonded_wizard", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-bond", level = 1 },
  { anchor = "hidden-bond", level = 1 },
  { anchor = "bonded-force", level = 5 },
  { anchor = "reshape-bond", level = 10 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["hidden-bond"] },
  { replaces = "A wizard's bonus feats normally gained at 5th and 15th level", feature = "bonus-feats", levels = [5, 15], by = ["bonded-force"] },
  { replaces = "The wizard's bonus feat normally gained at 10th level", feature = "bonus-feats", levels = [10], by = ["reshape-bond"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["arcane-bond"] },
]
+++

Many wizards form an arcane bond with an item, but for some this bond becomes a powerful mystic
union.

## Arcane Bond (Ex) {#arcane-bond}

A bonded wizard must select an item as her arcane bond. The bonded object's hit point and
[hardness](ref/umr/hardness) increase by +1 per level the bonded wizard possesses.

## Hidden Bond (Sp) {#hidden-bond}

A bonded wizard can change the appearance and magical aura of her bonded item at will, as if using
_[disguise self](ref/spell/disguise-self)_ and _[magic aura](ref/spell/magic-aura)_, but affecting
only the item; for the purpose of _[disguise self](ref/spell/disguise-self)_, the item's item type
(such as weapon or ring) is its creature type. This ability replaces Scribe Scroll.

## Bonded Force (Su) {#bonded-force}

At 5th level, a bonded wizard wearing or wielding her bonded object can channel magical energies
through it to create tools, armor, and weapons from pure force. She gains a pool of force points
equal to half his wizard level. She can expend 1 point from his force pool as a standard action to
create an effect that acts as _[mage armor](ref/spell/mage-armor)_ (lasting 1 hour),
_[shield](ref/spell/shield)_ (lasting 1 minute), or _[spiritual weapon](ref/spell/spiritual-weapon)_
(any simple or martial weapon, using her Intelligence modifier to determine its attack bonus rather
than Wisdom and lasting 1 round per wizard level). These effects are visible; they take the
appearance of armor, shields, or weapons as appropriate, and they always have some visual detail
reminiscent of the wizard's bonded item (such as the pattern of a bonded ring appearing as
decoration on a _[mage armor](ref/spell/mage-armor)_ or _[shield](ref/spell/shield)_ effect).

At 9th level, when the bonded wizard uses bonded force for _[mage armor](ref/spell/mage-armor)_, the
armor bonus increases by 1; when she uses bonded force for _[shield](ref/spell/shield)_, the shield
bonus increases by 1; and she gains a +1 enhancement bonus on attack and damage rolls when using
bonded force for _[spiritual weapon](ref/spell/spiritual-weapon)_. The increases for
_[mage armor](ref/spell/mage-armor)_ and _shield_ and the enhancement bonus for
_[spiritual weapon](ref/spell/spiritual-weapon)_ improve by an additional 1 at 13th level and again
at 17th level. When she uses bonded force for _[spiritual weapon](ref/spell/spiritual-weapon)_, the
bonded wizard can choose to reduce this enhancement bonus by 1 to double the _spiritual weapon's_
critical threat range as the _[keen](ref/magic-enh/keen)_ weapon property, and for _mage armor_ or
_shield_, she can choose to reduce the armor or shield bonus by 1 to protect herself from critical
hits and sneak attacks as the _[light fortification](ref/magic-enh/fortification-light)_ armor
property.

Alternatively, the bonded wizard can expend a point from her force pool to create a tool of force,
which functions as a masterwork version of a simple tool of her choice that could be reproduced by a
_[traveler's any-tool](ref/magic-wondrous/travelers-any-tool)_. The tool has the same AC and
durability as a _spiritual weapon_ and lasts for 10 minutes. The circumstance bonus the tool of
force grants to appropriate skill checks starts at +2 (as masterwork tools) and increases to +3 at
9th level, and by an additional +1 every 4 levels thereafter, to a maximum of +5 at 17th level.

A bonded wizard can only have one instance of bonded force active at a time. If she uses this
ability again, any previously created force construct immediately ends.

This ability replaces a wizard's bonus feats normally gained at 5th and 15th level.

## Reshape Bond (Sp) {#reshape-bond}

At 10th level, a bonded wizard can repair her bonded item or turn it into another object once per
day as a full-round action. Transforming it functions as
_[polymorph any object](ref/spell/polymorph-any-object)_, but does not alter the item's magical
properties (including its item slot), while repairing it functions as
_[make whole](ref/spell/make-whole)_. The wizard may also sacrifice a prepared spell in order to
repair an additional 1d6 points of damage per level of the sacrificed spell. This replaces the
wizard's bonus feat normally gained at 10th level.
