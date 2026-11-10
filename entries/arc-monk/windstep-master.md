+++
id = "ref/arc-monk/windstep-master"
kind = "archetype"
title = "Windstep Master"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "windstep_master", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "17"

[fields]
kind = "archetype"
replaces = ["Stunning fist", "Slow fall", "The ability to spend ki to increase his base speed"]
alters = ["Ki pool"]
replaces_features = ["stunning-fist", "slow-fall"]
alters_features = ["ki-pool"]
+++

Most monks are agile and fleet of foot, but few can rival a windstep master's lightness of step.
Windstep masters train in mountaintop monasteries and other holy houses dedicated to the wind, such
as the Monastery of Unfolding Wind in Niswan.

**Hurricane Punch (Ex)**

**At 1st Level:** A windstep master gains [Hurricane Punch](ref/feat/hurricane-punch) as a bonus
feat, even if he does not meet the prerequisites. While using this feat, he doesn't provoke an
attack of opportunity, even if he doesn't have the [Improved Bull Rush](ref/feat/improved-bull-rush)
feat.

**At 12th Level:** The windstep master's Hurricane Punch target can be up to three size categories
larger.

**At 16th Level:** He can now push the target of his Hurricane Punch bull rush back an additional 10
feet.

**At 20th Level:** The Hurricane Punch target can be of any size category.

**At 4th Level:** While using the Hurricane Punch feat, the windstep master can
[bull rush](ref/rule/bull-rush) a target up to two size categories larger.

**At 8th Level:** When the windstep master uses the Hurricane Punch feat to successfully bull rush a
creature, he can push the creature back an additional 5 feet.

**Replaces:** Stunning fist

**Wind Step (Su)**

**Flavor:** The windstep master's steps become supernaturally light.

**Gained:** At 4th Level

**Move:** He can use [air walk](ref/spell/air-walk) (as per the spell) up to a distance equal to his
fast movement bonus. He must reach a solid, level surface able to support his weight by the end of
his turn or he falls.

**Replaces:** Slow fall

**Swift Ki (Su)**

**Ability:** He can also spend 1 point from his _ki pool_ as a **swift action** to increase his wind
step distance by 20 feet for 1 round.

**Alters:** Ki pool

**Gained:** At 4th Level

**Replaces:** The ability to spend ki to increase his base speed

**Swift:** The windstep master can spend 1 point from his _ki pool_ to sustain his _wind step_ for 1
minute. During this time, the windstep master can remain airborne even if he doesn't reach a solid
surface.
