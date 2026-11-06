+++
id = "ref/rule/buoyancy"
kind = "rule"
title = "Buoyancy"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "buoyancy", path = "json/rules_campaign_types01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Aquatic Adventures\
When a creature fails its Swim check by 5 or more, or when it doesn't spend any actions to swim
(whether voluntarily or due to paralysis or similar conditions), it either sinks or rises based on
its buoyancy. There are three normal states of buoyancy: sinking, rising, and neutral. If a
creature's buoyancy is sinking, it naturally sinks; if its buoyancy is rising, it naturally rises to
the surface; and if its buoyancy is neutral, it hangs in place unless it expends effort.

Land-dwelling creatures generally have a sinking buoyancy unless they are carrying a substantial
amount of low-density gear (like wooden items, at least until they become waterlogged) and little or
no high-density gear (such as items made from metal or stone).
[Air tanks](ref/eq-misc/air-tank-pressurized) in particular make it much easier to change your
buoyancy to rising. It's also possible to adjust an air tank to hold just enough air to achieve a
neutral buoyancy - but once a creature has done so, if it picks up other objects or uses the tank to
breathe underwater, it loses its neutral buoyancy until it readjusts (which may require returning to
the surface to refill the air tank).

In addition to these three normal states of buoyancy, there are two extreme states: swiftly sinking
and swiftly rising. If a creature is swiftly sinking, it and its gear are so dense that it can walk
on the bottom of the body of water, but it also needs to succeed at a DC 20 Swim check to swim
towards the surface or to stay off the bottom. A creature carrying plenty of dense stone or metal
items gains this buoyancy state. If a creature is swiftly rising, it needs to succeed at a DC 20
Swim check to submerge itself and stay submerged; a sizable air tank or other flotation device, or
the help of magic, is needed to achieve this state.

**Aquatic and Water Creatures:** Most naturally aquatic creatures (those with the aquatic subtype)
have some form of air bladder or other organ that allows them to adjust their buoyancy on the fly,
enabling them to maintain neutral buoyancy as a free action on their turn (unless they are carrying
something large with particularly high or low density), and creatures with the water subtype
naturally have the same buoyancy as water.

**Buoyancy Speed:** A creature begins to sink or rise at the end of its turn the first time it badly
fails (or does not attempt) a Swim check, moving up or down as appropriate at a speed of 10 feet;
this speed increases by 10 feet each subsequent round unless the creature is stopped, to a maximum
speed of 30 feet after 3 rounds. This movement provokes attacks of opportunity as normal. While
sinking or rising because of its buoyancy, creatures are considered
[off-balance](ref/rule/off-balance-and-prone-underwater).

Once per round, a creature sinking or rising because of its buoyancy can stop its momentum by
succeeding at a Swim check as a move action. A creature that chooses to continue moving in the
direction of its buoyancy under its own power, rather than through uncontrolled rising or sinking,
can do so with a successful Swim check without needing to stop first.

If a creature's buoyancy changes instantly while sinking or rising from buoyancy (such as via
jettisoning something it's holding or using magic), its buoyancy speed adjusts by 10 feet in the new
direction each round. A creature that fails the DC 20 Swim check to move against its buoyancy while
swiftly sinking or swiftly rising moves 30 feet in the appropriate direction immediately.

**Moving Against Buoyancy:** Much like flying upwards uses up twice as much of a flying creature's
movement, each square of movement swimming in the opposite direction of a creature's buoyancy costs
twice as much movement as normal (see
[Thinking in Three Dimensions](ref/rule/thinking-in-three-dimensions) for more details). Creatures
with a neutral buoyancy ignore this hindrance.

**Drag:** Sometimes, because a PC might want to alter her buoyancy (or simply because she wants to
drag a particularly large piece of treasure back home), she might swim with an item that has
significant surface area, like a giant treasure chest. In these cases, her speed is reduced by half
(or more, at the GM's discretion). If the object is narrower in one dimension, like a pole, she can
avoid drag by turning it so the narrow side faces the direction she wants to move; however, this
adjustment requires a move action, so it slows her down if she needs to turn often.
