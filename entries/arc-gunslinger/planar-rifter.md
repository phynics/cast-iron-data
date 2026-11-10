+++
id = "ref/arc-gunslinger/planar-rifter"
kind = "archetype"
title = "Planar Rifter"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Planar%20Rifter"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_rifter", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "6"

[fields]
kind = "archetype"
replaces = ["Deadeye deed", "Dead shot deed", "Menacing shot deed", "Death's shot deed", "Nimble", "Gun training"]
alters = ["Grit"]
+++

Followers of the daemonic harbinger [Cixyron](ref/faith/cixyron) invented a method of harvesting
pieces from Abaddon, absorbing some of the energy into themselves and condensing other portions of
it into bullets they could fire from their guns. While these methods originated among Cixyron's
followers, they have spread among a few other seasoned planar travelers. Not all planar rifters are
evil, as the same methods that proved effective in slaying the celestial host are just as useful
against other planar forces.

**Infused Grit (Su)**

**Ability:** Each day when a planar rifter recovers grit, he can attune his grit pool to one of the
following subtypes: air, chaotic, earth, evil, fire, good, lawful, or water.

**Alters:** Grit

**Free:** After reducing an outsider to 0 hit points or below, he can switch his attunement to match
one of that outsider's subtypes.

**Special:** He regains grit as normal from critical hits, but killing blows replenish his grit pool
only if the target is an outsider.

**Standard:** Whenever he is on a plane that has an alignment or elemental trait, he can switch his
attunement to match one of that plane's traits.

**Deeds**

**Info:** A planar rifter gains the following deeds.

**Infused Bullet (Su)**

**Action:** Ability

**Gained:** At 1st Level

**Replaces:** Deadeye deed

A planar rifter's bullets carry the essence of a plane to which his grit pool is attuned, striking
true against creatures that shrink from that plane's nature. As long as he has at least 1 point in
his grit pool, he gains the following benefits.

- If he infuses his bullets with an alignment, his bullet's damage counts as that alignment for the
  purposes of overcoming DR
- If he infuses his bullets with an element, half of his bullet's damage changes to an energy type
  determined by the element infused: acid (earth), cold (water), electricity (air), or fire (fire)

**Planar Surge (Su)**

**Gained:** At 7th Level

**Replaces:** Dead shot deed

**Swift:** A planar rifter can spend 1 grit point to change the attunement of his grit pool to any
alignment or element. This new attunement remains for 1 minute, after which time the grit pool
becomes unattuned.

**Breaching Shot (Su)**

**Flavor:** A planar rifter can fire bullets with such precision that he tears temporary rifts
between planes.

**Gained:** At 15th Level

**Replaces:** Menacing shot deed

**Standard:** He can spend 3 grit points to shoot at a location within his firearm's first range
increment and tear a 10-foot-radius portal to a plane of his choice. The rift leads to a random
location on the plane that is between 5 and 500 miles from his intended destination, as
[plane shift](ref/spell/plane-shift). The rift remains open for 1 minute, during which time any
number of willing creatures can pass through. It is a one-way rift, and it is insufficiently stable
to reveal details about the environment on the other side.

**Banishing Shot (Su)**

**Ability:** Whenever a planar rifter confirms a critical hit against an extraplanar target, he can
spend 1 grit to deal normal damage, and the target must succeed at a Will saving throw with a DC
equal to 20 + the planar rifter's Wisdom modifier. On a failed saving throw, the target is returned
to its original plane as per the [banishment](ref/spell/banishment) spell.

**Gained:** At 19th Level

**Replaces:** Death's shot deed

**Planar Resistance (Su)**

**Gained:** At 2nd Level

**Passive:** When a planar rifter infuses his grit with the essence of a plane, he gains protection
against that plane's dangers. If he attunes his grit pool to chaos, good, evil, or law, he gains
resistance to magical effects that deal damage based on the chosen alignment, such as
[holy smite](ref/spell/holy-smite), [order's wrath](ref/spell/orders-wrath), a
[paladin's](ref/class/paladin) _smite evil_ attack, or an [unholy](ref/magic-enh/unholy) weapon. If
he attunes his grit pool to air, earth, fire, or water, he gains protection against the energy type
associated with that element (see _infused bullet_). He reduces the amount of damage taken from
attacks of the chosen type by 2 points per gunslinger level.

**Replaces:** Nimble

**Planar Strike (Su)**

**At 13th Level:** This damage increases to 2d6.

**Gained:** At 5th Level

**Passive:** As long as he has at least 1 point in his grit pool, a planar rifter's weapon attacks
deal an extra 1d6 points of damage of the same damage type reduced by his planar resistance. Aligned
damage harms only creatures of an opposed alignment.

**Replaces:** Gun training
