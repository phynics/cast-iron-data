+++
id = "ref/arc-monk/black-asp"
kind = "archetype"
title = "Black Asp"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "black_asp", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "67"

[fields]
kind = "archetype"
replaces = ["Stunning fist", "still mind"]
replaces_features = ["stunning-fist", "still-mind"]
+++

The black asps are a sinister order of monks who train as assassins and infiltrators with no need
for weapons to achieve their goals. Through meditation and study, they learn how to use poison, hide
any magics they choose to employ, and even empty their minds of thought to protect themselves from
divinations.

**Black Asp's Path (Ex)**

**Ability:** A black asp is trained in the use of poison and cannot accidentally poison himself when
applying poison to a weapon or when rolling a natural 1 on an attack roll with a poisoned weapon.

**At 3rd Level:** The black asp's ability to use poison improves. He gains
[Adder Strike](ref/feat/adder-strike) as a bonus feat even if he does not meet the prerequisites.

**Replaces:** Stunning fist, still mind

**Forbidden Powers (Su)**

**Ability:** A black asp can select a _forbidden ki power_ in place of any of the following monk
class abilities: _slow fall_ (4th), _high jump_ (5th), _wholeness of body_ (7th), _diamond body_
(11th), _abundant step_ (12th), _diamond soul_ (13th), _quivering palm_ (15th), _tongue of the sun
and moon_ (17th), and _empty body_ (19th). If he chooses to do so, he replaces the monk class
ability the black asp gives up for the chosen _forbidden ki power._ The black asp can select any of
the following _forbidden ki powers._

**Black Asp Venom (Su)**

**Prereq:** 12th-level monk

**Swift:** A black asp with this ki power can poison his unarmed strike or a weapon in his hand. The
poison lasts for 1 minute or until expended. A creature damaged by the poisoned weapon is affected
as per the [poison](ref/spell/poison) spell. The save DC is equal to 10 + 1/2 the black asp's monk
level + his Wisdom modifier. Each use of this ability costs 2 ki points.

**Hidden Magic (Sp)**

**Immediate:** The black asp can spend 1 ki point to hide the auras of all magic items he is
carrying (as if they were all under [magic aura](ref/spell/magic-aura)) for 1 hour per monk level.

**Greater Hidden Magic (Sp)**

**Immediate:** He can spend 2 ki points to cause himself and any magic items he is carrying to
appear to be nonmagical (as if he had cast [greater magic aura](ref/spell/magic-aura-greater)) for 1
hour per monk level.

**Passive:** As long as he has at least 1 point in his _ki pool,_ all of the black asp's items are
constantly under the effects of _[magic aura](ref/spell/magic-aura)._

**Prereq:** 8th-level monk, _hidden magic_ ki power

**Empty Mind (Sp)**

**Ability:** A black asp with this ki power can choose to lower the number of ki points in his _ki
pool_ by 3 when he recovers his ki points for the day. If he does so, he gains the benefits of
[mind blank](ref/spell/mind-blank) for 24 hours.

**Prereq:** 16th-level monk, _greater hidden magic_ ki power

**Shifting Form (Su)**

**Immediate:** A black asp can spend 1 ki point to make his outline shift and waver for 1 round.
This ability otherwise functions as per the spell [blur](ref/spell/blur).
