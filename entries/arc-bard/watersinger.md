+++
id = "ref/arc-bard/watersinger"
kind = "archetype"
title = "Watersinger"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Watersinger"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "watersinger", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-race-guide"
page = "176"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "watersong", level = 1 },
  { anchor = "waterstrike", level = 3 },
  { anchor = "lifewater", level = 5 },
  { anchor = "watersinger-spells" },
]
trades = [
  { replaces = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["watersong"] },
  { replaces = "suggestion", feature = "bardic-performance", power = "suggestion", by = ["watersong"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["watersong"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["waterstrike"] },
  { replaces = "The use of lore master gained at 5th level", feature = "lore-master", levels = [5], by = ["lifewater"] },
]
+++

The watersinger's song reaches from the depths of his soul into the elemental waters from which life
first sprang. His voice commands water, bending and shaping it to his desire.

## Bardic Performance {#bardic-performance}

A watersinger has some unique bardic performances, which replace some of the standard bardic
performances as listed in each entry. These bardic performances follow all the general rules and
restrictions of a bard's bardic performances.

## Watersong (Su) {#watersong}

At 1st level, a watersinger can use bardic performance to manipulate and control the shape of water
within 30 feet. A successful Perform check allows the bard to animate and control a 5-foot-cube of
water. The watersinger can command the water to take various forms, bend, rise, fall, or sustain a
shape, and can make it support weight as if it were solid ice. For example, the watersinger could
create a pillar of water (to provide cover), ladder, channel, bridge, stairs, slide, and so on. The
manipulated water is as slippery as normal ice. This ability cannot create forms more fragile or
complex than what could be carved in normal ice. While under the bard's control, the water has
[hardness](ref/umr/hardness) 0 and 3 hit points per inch of thickness. At level 3, the manipulated
water gains [hardness](ref/umr/hardness) 1, and this increases by +1 for every 3 bard levels beyond
that. At 5th, 10th, 15th, and 20th level, the volume affected increases by an additional 5-foot cube
(these cubes must be adjacent to each other). The manipulated water retains its shape for 1 round
after the bard stops spending bardic performance rounds to maintain it. This ability replaces
fascinate, suggestion, and mass suggestion.

## Waterstrike (Su) {#waterstrike}

At 3rd level, the watersinger can spend 1 round of bardic performance to command any water he is
currently manipulating with his watersong performance to lash out and strike an opponent with a slam
attack. The watersinger uses his base attack bonus and Charisma bonus to make this attack, and deals
1d6 points of bludgeoning damage plus his Charisma bonus. The attack can originate from any square
of water the bard is manipulating, and the water can get a flanking bonus or help a combatant get
one, but cannot make attacks of opportunity. The water can make multiple attacks per round if your
base attack bonus allows you to do so. At 10th level, the water's slam damage increases to 1d8
points and the water gains a reach of 10 feet. At 15th level, the water's slam damage increases to
2d6 points. At 20th level, the water's slam damage increases to 2d8 points. This performance
replaces inspire competence.

## Lifewater (Su) {#lifewater}

At 5th level, the watersinger can spend 1 round of bardic performance as a standard action to
manipulate the water, blood, and other fluids within a creature's body, causing the target to become
[sickened](ref/misc/sickened) for 1d4 rounds. Alternatively, he may use this ability to attempt a
[reposition](ref/rule/reposition) combat maneuver (_Advanced Player's Guide_), using his base attack
bonus and his Charisma modifier as his CMB. This ability has a range of 30 feet, only works on
creatures whose bodies contain fluid, and does not affect creatures that are immune to critical
hits. This performance replaces the use of lore master gained at 5th level (though a watersinger
still gains the use of lore master once per day at 11th level and twice per day at 17th).

## Watersinger Spells {#watersinger-spells}

A watersinger adds certain water-themed spells to his spell list. He adds these abilities to his
spell list as soon as his bard level allows him to cast spells of that spell level. 0—_create
water_; 1st—_hydraulic push_ (_Advanced Player's Guide_), _slipstream_ (_Advanced Player's Guide_);
2nd—_aqueous orb_ (_Advanced Player's Guide_), _hydraulic torrent_ (_Advanced Player's Guide_),
_water walk_; 3rd—_fluid form_ (_Advanced Player's Guide_), _ride the waves_ (_Ultimate Magic_);
4th—_control water_, _communal water walk_ (_Ultimate Combat_); 5th—_vortex_ (_Advanced Player's
Guide_); 6th—_seamantle_ (_Advanced Player's Guide_).
