+++
id = "ref/monster/robot-director-robot"
kind = "creature"
title = "Director Robot"
source_ids = ["pathfinder-90-the-divinity-drive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "robot_director_robot", path = "json/monsters20.json" },
]

[fields]
kind = "creature"
cr = "10"
creature_type = "construct"
subtypes = ["robot"]
size = "large"
alignment = "neutral"
ac = "23/13/19"
hp = "121~14d10+44"
fortitude = "+7"
reflex = "+10"
will = "+9"
melee = "2 tentacles +19 (1d10+6), 2 slams +19 (1d8+6)"
ranged = "integrated laser rifle +16 (2d6 fire)"
special_attacks = "electromagnetic pulse~grasping tentacles~override"
special_qualities = "advanced analytics, cling, repair robot"
abilities = ["22", "17", "-", "16", "15", "1"]
+++

_A humanoid torso and four spindly legs sprout from the top of this black-paneled orb. Buzzing
mechanical tentacles churn and writhe below its bulk._

**Director Robot**

**Challenge rating:** 10

**Type:** construct

**dv:** 60

**Initiative:** +3

**Size:** large

**Sense:** Llv

**Alignment:** Neutral

**Perception:** +15

**Subtype:** Robot

**Experience points:** 9,600

**Aav:** present

**Armor class:** 23/13/19

**Defensive abilities:** [hardness](ref/umr/hardness) 10

**Fort:** +7

**Hit points:** 121 (14d10+44)

**Immune:** [construct traits](ref/umr/construct-traits)

**Mod:** +3 Dex, +1 dodge, +10 natural, -1 size

**Ref:** +10

**Resist:** cold 10, fire 10

**Vulner:** critical hits and electricity

**Will:** +9

**Offense**

**Speed:** 40 ft., climb 30 ft.

**Melee:** 2 tentacles +19 (1d10+6), 2 slams +19 (1d8+6)

**Ranged:** integrated laser rifle +16 (2d6 fire)

**Reach:** 5

**Reach P:** 10 ft. with tentacles

**Space:** 10

**Spec Att:** electromagnetic pulse, grasping tentacles, override

**Statistics**

**Ability scores:** Str 22, Dex 17, Con -, Int 16, Wis 15, Cha 1

**Base attack bonus:** +14

**Combat maneuver bonus:** +21

**Combat maneuver defense:** 35 (39 vs. trip)

**Feats:** Dodge, Mobility, Point-Blank Shot, Power Attack, Precise Shot, Spring Attack, Toughness

**Skills:** Acrobatics +10 (+14 when jumping), Climb +15, Craft (mechanical) +15, Disable Device
+15, Knowledge (engineering) +15, Perception +15, Sense Motive +15

**Languages:** Androffan, Common, Hallit

**Special qualities:** advanced analytics, cling, repair robot

**Ecology**

**Environment:** any (Numeria)

**Organization:** solitary, patrol (1 director and 2-8
[gearsmen](ref/monster/robot-gearsman-robot)), or unit (1 director, 2-12 gearsmen, and 1
[myrmidon](ref/monster/robot-myrmidon-robot))

**Treasure:** None

### Special Abilities

**Advanced Analytics (Ex)** A director robot gains a bonus equal to its Intelligence bonus on all
saving throws.

**Cling (Ex)** A combination of magnetic pads and electrostatic emitters in its feet allow a
director robot to climb and travel on vertical or horizontal surfaces without having to attempt
Climb checks, even allowing it to traverse these surfaces while upside down.

**Electromagnetic Pulse (Ex)** Once per day as a standard action, a director robot can unleash an
electromagnetic pulse that deals 6d6 points of electricity damage to any robots or creatures with
cybernetic implants within a 20-foot radius (Reflex DC 20 half). This bypasses any active force
fields or similar effects, but doesn't harm other living creatures or the director robot. Any
technological item within this radius is drained of 1d6 charges unless it succeeds at a DC 20 Reflex
save. The save DCs are Intelligence-based.

**Grasping Tentacles (Ex)** A director robot's tentacles are primary attacks and have the grab
special ability.

**Integrated Laser Rifle (Ex)** A director robot has a built-in laser rifle. This weapon has a range
of 150 feet and deals 2d6 points of fire damage on a hit. The weapon can fire once per round as a
ranged touch attack. A laser attack can pass through force fields and force effects, such as a wall
of force, to strike a foe beyond without damaging that field. Objects like glass or other
transparent barriers don't provide cover from lasers, but unlike force barriers, a transparent
physical barrier still takes damage when a laser passes through it. Invisible creatures and objects
are immune to damage from lasers. Fog, smoke, and other clouds provide [cover](ref/rule/cover) in
addition to [concealment](ref/rule/concealment) from laser attacks. Darkness (magical or otherwise)
has no effect on lasers other than providing concealment.

**Override (Ex)** A director robot can usurp control of an otherwise functional robot. In order to
gain control of a robot, the director robot must first make a ranged touch attack against a target
robot within a range of 60 feet. If the attack is successful, the targeted robot must succeed at a
DC 20 Will saving throw to prevent the director robot from linking to the target's command
processor. On any subsequent turn after a link is established, the director robot can issue a
command to the targeted robot as a standard action. The targeted robot can attempt another Will save
(DC 20) to resist following each command.

To command its target, the director robot must be within 60 feet of the targeted robot and must
issue the command in a language the robot understands. The types of commands it can issue are
similar to those allowed by a suggestion spell-once a command is successfully issued, the robot does
its best to carry out the orders over the course of the next hour. Additionally, any robot affected
by this ability also gains a +2 competence bonus on attack and weapon damage rolls. These save DCs
are Intelligence-based.

**Repair Robot (Ex)** As a standard action that doesn't provoke an attack of opportunity, a director
robot can repair damage done to either itself or an adjacent creature with the robot subtype,
healing the target for 1d10 points of damage.

### Description

No society endures without order, and among robots that order is enforced by directors. Clad in
gleaming metal and viewing the world through a rotating array of lenses, a director is a robotic
overseer designed to maximize efficiency and command the loyalty of lesser automatons. Its torso
rests upon a utilitarian egg-shaped pod loaded with manipulators, tools, and dozens of thin
mechanical tendrils. Four long, mechanical legs support its bulk and carry it across any terrain,
even allowing the robot to cling magnetically to vertical surfaces. While the upper frame sports
human-like arms to manipulate traditional tools and weapons, two powerful tentacles extend from
below its frame to facilitate combat and handle heavy lifting. Though its humanoid torso is barely
larger than that of a human, the director's entire frame stands over 10 feet tall and weighs nearly
half a ton.

**Family:** [Robot](ref/family/robot)

### Ecology

Directors are middle managers built to ensure efficiency, productivity, and obedience. They oversee
complex projects and protect networks of robots from outside corruption. A unit of robots controlled
by a director goes about its business swiftly and with mechanical precision, taking what organic
beings might mistake for pride in conserving resources or completing projects rapidly.

Naturally, director robots need neither rest nor food, and their internal generators provide nearly
limitless power. Designed to be adaptable, they function with equal ease on the battlefield, within
winding corridors, deep underwater, and upon starship hulls in the vacuum of space. The magnetic
claws that carry the director's bulk up sheer surfaces with surprising speed and grace are also
perfectly suited to dragging damaged robots from the field.

To better analyze and respond to threats, directors are programmed with a remarkably advanced
artificial intelligence, capable of limited self-awareness and interaction with others. Their
sophisticated systems easily overwhelm and seize control of other computeroperated devices, dredging
memories and secrets from robotic minds, setting them to whatever work the director prioritizes, and
removing any corrupting outside influence.

### Habitat

A director robot's role is to break down the high-level goals of their superiors into simple
instructions for lesser robots. While not fully self-aware in ways organic beings appreciate, their
cold, clean minds take something like comfort in hard work, and experience distress if kept from
their duties or left devoid of purpose - those without a clear goal often become obsessive,
directing lesser robots to create order for its own sake. Surprisingly social, they fare poorly in
isolation without other machines to interact with and direct.

Like all robots, directors are built, not born. With neural networks almost as advanced as
androids', newly activated units undergo a learning period during which they reconcile their reams
of programmed knowledge with the unpredictable tendencies of reality. This digital "infancy" is a
confusing time, and these robots exhibit extreme frustration while learning to adapt. Other
directors are especially wary of these child units, and keep a cautious eye sensor on them, always
prepared to jump in and override the new robot if it proves incapable of translating theory into
practice.

Directors rarely stray from their heavily technological environments. On Golarion, they usually
cling to Silver Mount, but sometimes accompany a legion of the Technic League gearsmen unbidden,
ignoring orders from human masters and watching over their mechanical charges with an almost
religious devotion. Some directors operate within Starfall where they direct other robots used by
the Technic League.

Tightly guarded reports held by the Technic League claim that a rogue director robot maintains a
hidden lair somewhere in central Numeria. The robot has taken over a splintered section of Divinity
that contains a technological laboratory, and the reports claim that it's building its own army of
robotic followers.
