+++
id = "ref/magic-artifact/staff-of-eldritch-sovereignty"
kind = "item"
title = "Staff of Eldritch Sovereignty"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "staff_of_eldritch_sovereignty", path = "json/magic_artifact.json" },
]

[fields]
kind = "item"
category = "Artifacts"
price = "-"
weight = "5 lbs."
slot = "none"
aura = "strong varied"
caster_level = "20th"
+++

**Sources:** Mythic Adventures pg 161\
**Aura** strong varied; **CL** 20th\
**Slot** none; **Price** -; **Weight** 5 lbs.

Similar to the [staff of the magi](ref/magic-artifact/staff-of-the-magi), this long ivory staff is
inlaid with platinum sigils and burns with eldritch fire when its powers are called upon. Unlike a
normal staff, a staff of eldritch sovereignty holds 50 charges and can't be recharged normally. Some
of its powers use charges, and others don't. A staff of eldritch sovereignty doesn't lose its powers
if it runs out of charges. The following powers don't use charges:

- [Arcane lock](ref/spell/arcane-lock)
- [Arcane sight](ref/spell/arcane-sight)
- [Daylight](ref/spell/daylight)
- [Knock](ref/spell/knock)
- [Mage armor](ref/spell/mage-armor)
- [Mage hand](ref/spell/mage-hand)
- [Touch of idiocy](ref/spell/touch-of-idiocy)

The following powers drain 1 charge per use:

- [Black tentacles](ref/spell/black-tentacles)
- [Cone of cold](ref/spell/cone-of-cold) (15d6 damage, Reflex DC 20 half)
- [Fireball](ref/spell/fireball) (10d6 damage, Reflex DC 18 half)
- [Greater dispel magic](ref/spell/dispel-magic-greater)
- [Greater invisibility](ref/spell/invisibility-greater)
- [Greater teleport](ref/spell/teleport-greater)
- [Lightning arc](ref/spell/lightning-arc) (15d6 damage, Reflex DC 20 half)
- [Major image](ref/spell/major-image) (Will DC 18 disbelief)
- [Suggestion](ref/spell/suggestion) (Will DC 18 negates)

These powers drain 2 charges per use:

- [Summon monster IX](ref/spell/summon-monster-9) (the summoned creatures receive the benefits of
  the [Augment Summoning](ref/feat/augment-summoning) feat)
- [Plane shift](ref/spell/plane-shift) (Will DC 22 negates, arrive 2 to 200 miles from the intended
  destination)
- [Prismatic sphere](ref/spell/prismatic-sphere) (DC 24)
- [Prismatic spray](ref/spell/prismatic-spray) (DC 22)

For 5 charges, the staff of arcane sovereignty creates a [gate](ref/spell/gate).

The staff of eldritch sovereignty has higher DCs than normal for a staff. The wielder still uses her
own save DCs if they exceed those of the staff.

The wielder can use any of her metamagic feats on spells cast with the staff of eldritch sovereignty
by expending 1 charge per increase in spell level, with a minimum of 1 charge spent. The adjusted
level of the spell can't be increased above 9th level. For example, a user with
[Quicken Spell](ref/feat/quicken-spell) can spend 5 charges to cast a quickened
_[cone of cold](ref/spell/cone-of-cold)_ with the staff, but couldn't use it to cast quickened
_[greater teleport](ref/spell/teleport-greater)._

The wielder can expend one use of mythic power to gain the benefit of a number of charges equal to
her mythic tier. Any excess charges are lost. For example, a 5th-tier wielder with
[Empower Spell](ref/feat/empower-spell) could expend one use of mythic power to cast an empowered
_[fireball](ref/spell/fireball)_ without consuming any charges from the staff. A wielder who knows
the mythic version of one of the staff's spells can cast such spells from the staff by expending one
use of mythic power. This can be combined with using mythic power to provide charges. Finally, the
wielder can expend one use of mythic power to add 1 charge to the staff, with no risk of explosion
if the staff is already fully charged.

A staff of eldritch sovereignty gives the wielder [spell resistance](ref/rule/spell-resistance)
equal to 23 plus her tier. If this is willingly lowered, however, the staff can be used to absorb
arcane energy directed at its wielder, as a [rod of absorption](ref/magic-rod/rod-of-absorption)
does. Unlike the rod, this staff converts spell levels into charges rather than retaining them as
spell energy usable by a spellcaster. If the staff absorbs enough energy to exceed its limit of 50
charges, it explodes as if the wielder had performed a retributive strike (see Destruction). The
wielder has no idea how many spell levels are cast at her - the staff doesn't communicate this
knowledge as a rod of absorption does. Thus, absorbing spells can be risky.

### Destruction

A staff of eldritch sovereignty can be broken for a retributive strike. Such an act must be
purposeful and declared by the wielder. All charges in the staff are released in a 30-foot-radius
[spread](ref/misc/spread). Quadruple the wielder's tier and add this amount to the number of charges
remaining in the staff. All creatures within 10 feet of the staff take an amount of damage equal to
10 times this number. A successful Reflex save with a DC equal to 23 plus the wielder's tier halves
the damage. Unlike with the staff of the magi, breaking a staff of arcane sovereignty invariably
destroys the wielder (no saving throw).
