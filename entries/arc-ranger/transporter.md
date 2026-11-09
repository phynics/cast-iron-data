+++
id = "ref/arc-ranger/transporter"
kind = "archetype"
title = "Transporter"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transporter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "43"

[fields]
kind = "archetype"
replaces = ["Wild empathy", "Favored terrain", "Woodland stride"]
alters = ["Hunter's bond"]
+++

Transporters specialize in smuggling people as efficiently as possible through harsh and difficult
environments. Individuals such as escaped political exiles, refugees fleeing danger, and various
criminals all seek the transporter's services. While some transporters actively work to serve
justice or a political cause, others are wily opportunists filling a need and profiting from the
high price that desperate people are willing to pay for safe, discrete passage.

**Trailbreaker (Ex)**

**Flavor:** A transporter constantly works to obscure his trail.

**Passive:** He increases the Survival DC to track him, or a group of which he is a part, by an
amount equal to half his ranger level (minimum 1). This does not stack with similar abilities, such
as a [traceless operative's](ref/arc-inquisitor/traceless-operative) _trackless_ ability.

**Replaces:** Wild empathy

**Plot Course (Ex)**

**Ability:** A transporter can spend 1d4 hours and attempt a DC 15 Knowledge (geography) check to
plot a subtle course of travel between his current location and another destination. The
transporter's course of travel is almost never direct, as it is optimized for smuggling. Thereafter,
the transporter gains a +2 bonus on initiative, Knowledge (geography), Perception, Stealth, and
Survival checks involving traveling along his plotted course.

**Gained:** At 3rd Level

**Replaces:** Favored terrain

**Special:** A transporter can gain the benefits of only a single plotted course at any given time.
If the transporter ever strays from the course or attempts to plot a new course for any reason, he
loses the benefits of his current course immediately. A transporter can retry his Knowledge
(geography) check to plot a course as long as he spends 1d4 hours each time.

**Smuggler's Bond (Ex)**

**Alters:** Hunter's bond

**Info:** A transporter must choose his allies as his _hunter's bond,_ not an animal companion.

**Gained:** At 4th Level

**Passive:** Instead of granting the transporter's _favored enemy_ bonus to his allies as a move
action, he instead grants his _plot course_ bonus to his allies constantly.

**Hideaway (Ex)**

**Ability:** A transporter^1^ can spend 1 hour and attempt a DC 20 Survival check to create a hidden
shelter, useful for staying unseen by patrols of enemy creatures. The transporter's shelter can hold
the transporter and one additional creature for every 2 by which the transporter exceeds the DC. The
created shelter incorporates scents from the local area, preventing creatures on the inside from
being detected by the [scent](ref/umr/scent) ability of creatures outside of the shelter, and vice
versa. Additionally, its floor is either elevated or constructed of a different substance than the
nearby ground, preventing creatures outside of the shelter from using
[tremorsense](ref/umr/tremorsense) to detect creatures inside, and vice versa. Finally, the clever
structure of the hideaway causes creatures outside of the shelter to take a -10 penalty on
Perception checks to notice creatures inside, as if through a 1-foot-thick wall, while only causing
creatures inside to take a -2 penalty on Perception checks to notice creatures outside.

**Replaces:** Woodland stride

**Special:** These bonuses do not apply if the enemy creatures are intimately familiar with the area
in which the hideaway was built (such as an area right near their home).

^1^ There is no listed level at which this ability is granted. Given that it replaces a 7th-level
ability, the intention was probably that this ability would also be gained at 7th level. Consult
your GM.
