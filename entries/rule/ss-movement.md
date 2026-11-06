+++
id = "ref/rule/ss-movement"
kind = "rule"
title = "Movement"
source_ids = ["skull-and-shackles-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ss_movement", path = "json/rules_campaign_types10.json" },
]

[fields]
kind = "none"
+++

**Sources:** Skull and Shackles Player's Guide pg 12\
At the start of a pilot's turn, she can take any of the following sailing actions (except the
"uncontrolled" action) by making a sailing check to control the ship. The pilot must take whatever
action is required before doing anything else that turn. Just as in normal combat, a pilot can
perform a standard action and a move action each round. Once the pilot has selected an action, or
takes some other action forcing the ship to become uncontrolled, the ship moves. If a ship has less
than half its crew or has no pilot, or if the pilot takes no action, takes some other action instead
of piloting the ship, or delays or readies an action, the ship takes the "uncontrolled" action.

**Full Ahead (standard action):** With a successful [sailing check](ref/rule/sailing-check), the
ship's current speed increases by its acceleration (usually 30 feet), but no higher than its maximum
speed. The ship can move forward or forward diagonally. In other words, each time a ship enters a
new 30-foot square, it can choose any of its forward-facing squares - the one directly in front or
either of the squares directly forward and diagonal. This allows the ship to swerve. A pilot who
fails her sailing check does not accelerate and can only move into a square directly in front of the
ship's forward facing.

**Hard to Port or Hard to Starboard (standard action):** The pilot can turn the ship while it moves
forward at its current speed. With a successful sailing check, the pilot can change the ship's
forward facing either left (port) or right (starboard) by 90 degrees at any point during the ship's
movement. Do this by pivoting the ship so that the rear square of the ship takes the place of the
ship's former forward facing square. If a ship's current speed is twice its acceleration, the pilot
takes a -5 penalty on the sailing check. If a ship's current speed is three times its acceleration,
the pilot takes a -10 penalty on the sailing check. If its current speed is four or more times its
acceleration, the pilot takes a -20 penalty. On a failed check, the ship does not turn, but can be
moved forward diagonally during its movement. Note: A wind-propelled ship that turns into the wind
(its forward facing is pointed in the opposite direction from the wind) is said to be "in irons" and
takes the uncontrolled action until its pilot turns it to face another direction.

**Heave To (standard action):** With a successful sailing check, the ship's current speed decreases
by 30 feet. On a failed check, the ship does not decelerate. Either way, the ship can move forward
on its current facing and can move forward diagonally. If deceleration reduces a ship's speed to 0,
some amount of inertia will continue to move the ship forward. The ship moves forward (either
directly forward or forward diagonally) 1d4×30 feet before coming to a complete stop. Having the
[Expert Driver](ref/feat/expert-driver) feat reduces this distance by 30 feet (minimum 0 feet).

**Make Way (standard action):** With a successful sailing check, a pilot can make a tricky or
difficult maneuver that forces an enemy pilot to react. The result of this sailing check then
becomes the DC of the enemy pilot's next sailing check. On a failed check, the ship's speed remains
constant, but the ship cannot move forward diagonally, and the enemy pilot makes his next sailing
check at the normal DC.

**Stay the Course (move action):** With a successful sailing check, the pilot can move the ship
forward on its current facing at its current speed, and it can move directly forward or forward
diagonally. Failing the check keeps the speed constant, but the ship can only move directly forward,
not forward diagonally.

**Full Astern (full-round action):** With a successful sailing check, the pilot can move the ship
backward at a speed of 30 feet, moving either directly backward (the reverse of its forward facing)
or backward diagonally. On a failed check, it does not move backward. A ship may only be moved in
reverse if its current speed is 0.

**Uncontrolled (no action):** When the pilot does nothing, if there is no pilot, or if the ship has
less than half its crew, the ship is uncontrolled. An uncontrolled ship does nothing except take the
uncontrolled action until it stops or someone becomes its new pilot. An uncontrolled ship moves
forward only (it cannot move forward diagonally) and automatically decelerates by 30 feet. Even if a
ship does nothing, it can still perform ramming maneuvers (see [Ramming](ref/rule/ramming)).
