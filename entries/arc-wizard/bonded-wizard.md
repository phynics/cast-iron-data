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
replaces = ["Scribe Scroll", "5th- and 15th-level bonus feats", "10th-level bonus feat"]
alters = ["Arcane bond"]
+++

Many wizards form an arcane bond with an item, but for some this bond becomes a powerful mystic
union.

**Arcane Bond (Ex)**

**Alters:** Arcane bond

**Info:** A bonded wizard must select an item as her _arcane bond._ The bonded object's hit point
and [hardness](ref/umr/hardness) increase by +1 per level the bonded wizard possesses.

**Hidden Bond (Sp)**

**Ability:** A bonded wizard can change the appearance and magical aura of her bonded item at will,
as if using [disguise self](ref/spell/disguise-self) and [magic aura](ref/spell/magic-aura), but
affecting only the item; for the purpose of _[disguise self](ref/spell/disguise-self),_ the item's
item type (such as weapon or ring) is its creature type.

**Replaces:** Scribe Scroll

**Bonded Force (Su)**

**Ability:** Alternatively, the bonded wizard can expend a point from her force pool to create a
_tool of force,_ which functions as a masterwork version of a simple tool of her choice that could
be reproduced by a [traveler's any-tool](ref/magic-wondrous/travelers-any-tool). The _tool_ has the
same AC and durability as a _[spiritual weapon](ref/spell/spiritual-weapon)_ and lasts for 10
minutes. The circumstance bonus the _tool of force_ grants to appropriate skill checks starts at +2
(as masterwork tools).

**At 9th Level:** When the bonded wizard uses _bonded force_ for
_[mage armor](ref/spell/mage-armor),_ the armor bonus increases by 1; when she uses _bonded force_
for _[shield](ref/spell/shield),_ the shield bonus increases by 1; and she gains a +1 enhancement
bonus on attack and damage rolls when using _bonded force_ for
_[spiritual weapon](ref/spell/spiritual-weapon)._

The bonus for the _tool of force_ increases to +3.

**Info:** A bonded wizard wearing or wielding her bonded object can channel magical energies through
it to create tools, armor, and weapons from pure force. She gains a pool of force points equal to
half her wizard level.

**Gained:** At 5th Level

**Replaces:** 5th- and 15th-level bonus feats

**Special:** When she uses _bonded force_ for _[spiritual weapon](ref/spell/spiritual-weapon),_ the
bonded wizard can choose to reduce this enhancement bonus by 1 to double the _spiritual weapon's_
critical threat range as the [keen](ref/magic-enh/keen) weapon property, and for
_[mage armor](ref/spell/mage-armor)_ or _[shield](ref/spell/shield),_ she can choose to reduce the
armor or shield bonus by 1 to protect herself from critical hits and sneak attacks as the
[light fortification](ref/magic-enh/fortification-light) armor property. A bonded wizard can only
have one instance of _bonded force_ active at a time. If she uses this ability again, any previously
created force construct immediately ends.

**Standard:** She can expend 1 point from her force pool to create an effect that acts as
[mage armor](ref/spell/mage-armor) (lasting 1 hour), [shield](ref/spell/shield) (lasting 1 minute),
or [spiritual weapon](ref/spell/spiritual-weapon) (any simple or martial weapon, using her
Intelligence modifier to determine its attack bonus rather than Wisdom and lasting 1 round per
wizard level). These effects are visible; they take the appearance of armor, shields, or weapons as
appropriate, and they always have some visual detail reminiscent of the wizard's bonded item (such
as the pattern of a bonded ring appearing as decoration on a _[mage armor](ref/spell/mage-armor)_ or
_[shield](ref/spell/shield)_ effect).

**Reshape Bond (Sp)**

**Fullround:** A bonded wizard can repair her bonded item or turn it into another object once per
day. Transforming it functions as [polymorph any object](ref/spell/polymorph-any-object), but does
not alter the item's magical properties (including its item slot), while repairing it functions as
[make whole](ref/spell/make-whole). The wizard may also sacrifice a prepared spell in order to
repair an additional 1d6 points of damage per level of the sacrificed spell.

**Gained:** At 10th Level

**Replaces:** 10th-level bonus feat
