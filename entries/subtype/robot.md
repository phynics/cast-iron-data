+++
id = "ref/subtype/robot"
kind = "rule"
title = "Robot"
source_ids = ["bestiary-5", "inner-sea-bestiary"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "robot", path = "json/monster_subtypes.json" },
]

[fields]
kind = "none"
+++

## Subtype: Robot

**Sources:** Bestiary 5, Inner Sea Bestiary

"Robot" is a special subtype that can be applied to any [construct](ref/type/construct) without
changing its CR. Robots share some features with [clockwork](ref/subtype/clockwork) constructs, and
as with clockworks, you can simply remove the robot subtype and its traits to transform it into a
typical construct animated by magic. A construct cannot possess both the robot and the clockwork
subtypes. All robots gain the following traits, unless noted otherwise.

- **Difficult to Create (Ex):** Robots are crafted via complex methods hidden and well guarded. A
  robot does not have a construction entry.
- **Intelligent:** Robots are intelligent, and thus have skills and feats as appropriate for their
  Hit Dice. Unless otherwise indicated for a specific robot, all robots have Intelligence scores
  of 10. The following are class skills for robots: [Climb](ref/skill/climb),
  [Disable Device](ref/skill/disable-device), [Fly](ref/skill/fly),
  [Knowledge](ref/skill/knowledge-all) (all), [Linguistics](ref/skill/linguistics),
  [Perception](ref/skill/perception), and [Sense Motive](ref/skill/sense-motive).
- **Vulnerable to Critical Hits:** Whenever a robot takes extra damage from a critical hit, it must
  succeed at a DC 15 Fortitude save or be [stunned](ref/misc/stunned) for 1 round. If the robot
  succeeds at the save, it is [staggered](ref/misc/staggered) for 1 round. The robot remains immune
  to all other sources of the stunned condition.
- **Vulnerable to Electricity:** Robots take 150% as much damage as normal from electricity attacks.

The following special abilities apply to some robots, but are not universal to all types of robot.

- **Combined Arms (Ex):** When making a full attack, a robot with the combined arms special attack
  can make all its melee natural weapon attacks plus its ranged integrated weapon attacks.
- **Force Field (Ex):** A robot might have a force field that sheathes it in a thin layer of energy
  that grants a number of [temporary hit points](ref/rule/temporary-hit-points) (typically 5 × the
  robot's CR). All damage dealt to a robot with an active force field is deducted from these
  temporary hit points first. As long as the force field is active, the robot is immune to critical
  hits. A force field has [fast healing](ref/umr/fast-healing) equal to the robot's CR, but once its
  hit points are reduced to 0, the force field shuts down and doesn't reactivate for 24 hours.

  - **Format:** force field (55 hp, [fast healing](ref/umr/fast-healing) 5); **Location:** hp.
- **Integrated Weaponry (Ex):** A robot that has a technological weapon built into its body treats
  it as a natural weapon and not a manufactured weapon, and can't make iterative attacks with it. An
  integrated weapon can still be targeted by effects that target manufactured weapons (such as
  [magic weapon](ref/spell/magic-weapon) or [sunder](ref/rule/sunder) attempts), but can't be
  harvested for use outside of the robot's body once the robot is destroyed. A robot is always
  proficient with its integrated weapons. Integrated ranged weapons don't provoke attacks of
  opportunity when fired in melee combat.
- **Laser Weapons (Ex):** A laser weapon emits beams of intensely focused light waves. Laser attacks
  resolve as touch attacks and deal fire damage. A laser can pass through force fields and force
  effects like a [wall of force](ref/spell/wall-of-force) without damaging that field to strike a
  foe beyond. Objects like glass or other transparent barriers don't provide cover from lasers (but
  unlike force barriers, glass still takes damage from a laser strike passing through it). Invisible
  creatures are immune to damage caused by a laser weapon. Fog, smoke, and other clouds provide
  [cover](ref/rule/cover) in addition to [concealment](ref/rule/concealment) from laser attacks.
- **Plasma Weapons (Ex):** These weapons emit bursts of superheated, electrically charged gas known
  as plasma. A plasma weapon's attacks resolve as touch attacks. Half the damage dealt by plasma is
  fire damage, and half is electricity damage.
