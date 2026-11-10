+++
id = "ref/arc-kineticist/blighted-defiler"
kind = "archetype"
title = "Blighted Defiler"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blighted_defiler", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "62"

[fields]
kind = "archetype"
replaces = ["Internal buffer", "Elemental defense", "Omnikinesis"]
alters = ["Alignment", "Gather power", "The key ability score of wild talents", "elemental overflow"]
replaces_features = ["internal-buffer", "elemental-defense", "omnikinesis"]
alters_features = ["gather-power", "elemental-overflow"]
+++

A few kineticists have developed the ability to steal the life force from the surrounding land in
order to infuse themselves with unnatural strength beyond their bodies' normal capabilities.

**Alignment**

**Alters:** Alignment

**Info:** Blighted defilers must be evil in order to use _[steal power](ref/spell/steal-power),_
since defiling the land and reaping the vulnerable for power is a particularly vile act. Nonevil
blighted defilers can continue to gain kineticist levels and use their other abilities.

**Steal Power (Su)**

**Action:** Ability

**Alters:** Gather power

**Usage:** Strength modifier times/day

A blighted defiler can draw energy from the surrounding land to _gather power,_ gaining one of the
three following benefits.

1. She can increase the burn reduction from _gather power_ by 1 for a blast wild talent.
1. Alternatively, she can use _gather power_ to reduce the cost of a defense, infusion, or utility
  wild talent by 1, regardless of whether she _gathers power_ for longer or has abilities that
  increase the burn reduction from _gather power._
1. Finally, she can siphon the energy into healing herself, recovering 2 hit points per kineticist
  level.

When a blighted defiler uses _[steal power](ref/spell/steal-power),_ she afflicts the area within a
radius of 250 feet per kineticist level (maximum 5,000 feet at 20th level) by stunting plants as the
stunt growth option from [diminish plants](ref/spell/diminish-plants), weakening and killing minor
wildlife (creatures too small or insignificant to themselves have statistics), and reducing the rate
of live birth among the other surviving creatures in the area. If a blighted defiler uses
_[steal power](ref/spell/steal-power)_ in an area that overlaps a previous use of her
_[steal power](ref/spell/steal-power)_ within the same month, she expends a daily use and the
remaining area is still blighted as above, but she doesn't gain any benefits.
_[Steal power](ref/spell/steal-power)_ doesn't work in barren landscapes, the void of space, or
other places without enough life to steal.

**Elemental Might (Ex)**

**Action:** Info

**Alters:** The key ability score of wild talents, elemental overflow

A blighted defiler uses her Strength modifier instead of her Constitution modifier to determine her
damage with wild talents, the DCs of Constitution-based wild talents, the durations of wild talents
with Constitution-based durations, her bonus on [concentration](ref/rule/concentration) checks for
wild talents, and other Constitution-based effects of her wild talents. She can't use abilities to
substitute her Strength modifier for another ability score when determining damage from wild
talents.

A blighted defiler gains attack and damage bonuses from _elemental overflow_ based on her current
burn total + the number of times she successfully used _[steal power](ref/spell/steal-power)_ that
day. For instance, a 9th-level blighted defiler who used _[steal power](ref/spell/steal-power)_
twice and had 1 point of burn would add a +3 bonus on attack rolls and a +6 bonus on damage rolls. A
blighted defiler does not gain size bonuses to physical ability scores or a chance to ignore
critical hits and sneak attacks from _elemental overflow._

**Life Buffer (Su)**

**Ability:** A blighted defiler gains a _buffer_ she can use to store life potential from healthy
areas in order to use it later. She must use _[steal power](ref/spell/steal-power)_ on a healthy
area and take none of the three usual benefits, and this doesn't count as a use of
_[steal power](ref/spell/steal-power)_ for elemental might or stolen strength. This grants her
_buffer_ 1 life point. When using _[steal power](ref/spell/steal-power),_ she can spend 1 life point
to gain the benefits even in an area she already blighted that month. Life points remain in the
_buffer_ until she spends them.

**At 11th Level:** It can now hold 2 life points.

**At 16th Level:** It can now hold 3 life points.

**At 6th Level:** The _buffer_ can hold a maximum of 1 life point.

**Gained:** At 6th Level

**Replaces:** Internal buffer

**Stolen Strength (Su)**

**Ability:** A blighted defiler gains the ability to collect unused portions of the life she's
stolen throughout the day to bolster herself. After the third time she successfully uses
_[steal power](ref/spell/steal-power)_ in a given day, she gains a +2 size bonus to Strength and to
either Dexterity or Constitution until she recovers uses of _[steal power](ref/spell/steal-power)._

**At 11th Level:** After the fifth time the blighted defender successfully uses
_[steal power](ref/spell/steal-power)_ in a day, she instead gains a +4 size bonus to Strength and a
+2 size bonus to Dexterity and Constitution, and she can use the life energy to increase her size
category by one (to a maximum of Large).

**At 16th Level:** After the seventh time the blighted defender successfully uses
_[steal power](ref/spell/steal-power)_ in a day, her size bonuses increase to +6 to Strength, +4 to
either Dexterity or Constitution, and +2 to the remaining ability score, and she can also grow to
Huge.

**At 20th Level:** After the 9th time she successfully uses _[steal power](ref/spell/steal-power)_
in a day, she can also grow to Gargantuan.

**Gained:** At 6th Level

**Replaces:** Elemental defense

**Special:** All of these size increases function as [kinetic form](ref/kinetic/kinetic-form),
meaning they don't change her ability scores in any way. A blighted defiler can never gain an
elemental defense, even from _expanded defense._

**Steal Life (Su)**

**Ability:** A blighted defiler who successfully uses _[steal power](ref/spell/steal-power)_ when
_gathering power_ as a move action can use a **standard action** on the same turn and choose a
living creature within 30 feet. The creature must succeed at a Fortitude save (DC = 20 + the
blighted defiler's Strength modifier) or die; this is a death effect. If the creature dies and was
CR 10 or higher, on the blighted defiler's next turn, she counts as if she had used a full round to
_gather power_ with _[steal power](ref/spell/steal-power)._ If the target survives or was lower than
CR 10, she loses all benefits from both her _gather power_ and
_[steal power](ref/spell/steal-power),_ as normal at the end of her turn.

**Gained:** At 20th Level

**Replaces:** Omnikinesis
