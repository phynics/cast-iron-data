+++
id = "ref/arc-ranger/galvanic-saboteur"
kind = "archetype"
title = "Galvanic Saboteur"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Galvanic%20Saboteur"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "galvanic_saboteur", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "people-of-the-river"
page = "25"

[fields]
kind = "archetype"
replaces = ["Wild empathy", "Favored terrain", "Woodland stride", "Swift tracker", "camouflage", "Hide in plain sight"]
alters = ["Favored enemy"]
+++

The transformation of the great warlord Kevoth-Kul into the hedonistic Black Sovereign a few decades
ago was difficult for the people of Numeria to accept. Many Kellid locals blame Kevoth-Kul's change
on the influence of the Technic League and view both the League and their mechanical minions with a
mix of fear and distrust. Some Kellid rangers have since developed skills to defeat the League's
robotic enforcers and devious arcanists.

**Gained class skills:** dd, ka

**Lost class skills:** ha, kd

**Favored Enemy (Ex)**

**Alters:** Favored enemy

**Choice:** A galvanic saboteur must select construct creatures as his first _favored enemy._

**Gained:** At 1st Level

**Reprogram (Ex)**

**Ability:** A galvanic saboteur can improve the initial attitude of a mindless construct. This
ability functions as [wild empathy](ref/ability/wild-empathy), except only against mindless
constructs. The ranger can use this ability against constructs with an Intelligence score, but he
takes a -4 penalty on the check.

**Gained:** At 1st Level

**Replaces:** Wild empathy

**Lucky Dodge (Ex)**

**Flavor:** A galvanic saboteur can dodge the precise attacks of even the most technologically
advanced foes.

**Gained:** At 3rd Level

**Passive:** The ranger gains a luck bonus to AC against attacks that target his touch AC as long as
his opponent's type matches that of his first _favored enemy._ This luck bonus is equal to 1/2 the
ranger's _favored enemy_ bonus against that creature type.

**Replaces:** Favored terrain

**Special:** A galvanic saboteur's animal companion (if he chose one for his _hunter's bond_) also
gains this luck bonus.

At 8th level: The ranger gains this luck bonus to AC against attacks that target his touch AC as
long as his opponent's type matches his 2nd _favored enemy._

At 13th level: The ranger gains this luck bonus to AC against attacks that target his touch AC as
long as his opponent's type matches his 3rd _favored enemy._

At 18th level: The ranger gains this luck bonus to AC against attacks that target his touch AC as
long as his opponent's type matches his 4th _favored enemy._

**Technological Trapsmith (Ex)**

**Action:** Ability

**Gained:** At 7th Level

**Replaces:** Woodland stride

A galvanic saboteur can rig technological traps using the remains of destroyed constructs with the
clockwork or robot subtype. To successfully rig such a trap, the ranger must spend 1 minute working
on the destroyed construct and succeed at a Disable Device check (DC = 10 + the construct's HD). On
a failure, the trap doesn't function and the construct's remains are ruined. On a success, the
ranger creates a mechanical trap with the following statistics.

**Rigged Construct Trap**

**Type:** Mechanical

**Challenge rating:** Variable

**Perception DC:** 20

**Disable Device DC:** 20

**Trigger:** location (all spaces occupied by the construct's remains)

**Effect:** blast of electricity (1d6 electricity damage/2 HD of construct); Reflex negates (DC =
10 + 1/2 the ranger's level + his Intelligence modifier); multiple targets (all targets within 5 ft.
of construct's remains)

Other types of destroyed constructs can serve as suitable materials for a rigged construct trap (at
the GM's discretion). Constructs destroyed by [disintegrate](ref/spell/disintegrate) or similar
effects that leave no intact remains cannot be used to create a rigged construct trap.

**Static Strike (Ex)**

**Flavor:** The galvanic saboteur has gathered enough parts and scrap from his constructed enemies
that he can infuse some of his attacks with a bit of their alien energy.

**At 12th Level:** The ranger can continue to make attacks against adjacent creatures, as if he had
[Great Cleave](ref/feat/great-cleave), with each hit increasing the amount of electricity damage
dealt to the next foe in line.

**Gained:** At 8th Level

**Replaces:** Swift tracker, camouflage

**Standard:** Once per day, the ranger can make a _static strike_ as a melee attack at his full base
attack bonus. If the attack hits, it deals an additional 1d6 points of electricity damage and the
ranger can make an additional attack at his full base attack bonus against a foe that is adjacent to
the previous foe and still within his reach, as if he had [Cleave](ref/feat/cleave), except he
doesn't take a -2 penalty to his AC and the second attack deals an additional 2d6 points of
electricity damage.

**Sensor Evasion (Su)**

**Ability:** He can use the Stealth skill against constructs and magical sensors (such as those
created by [arcane eye](ref/spell/arcane-eye) or
[clairaudience/clairvoyance](ref/spell/clairaudience-clairvoyance)) even while being observed.

**Flavor:** A galvanic saboteur has mastered the art of evading technological and magical
observation.

**Gained:** At 17th Level

**Replaces:** Hide in plain sight
