+++
id = "ref/arc-vigilante/wildsoul"
kind = "archetype"
title = "Wildsoul"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Wildsoul"
source_ids = ["ultimate-intrigue", "blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wildsoul", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "61"
[[sources]]
publication = "blood-of-the-beast"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-course" },
]
trades = [
  { replaces = "Vigilante talents gained at 2nd, 6th, 12th, and 18th levels", feature = "vigilante-talent", levels = [2, 6, 12, 18], by = ["natural-course"] },
  { alters = "Vigilante specialization", feature = "vigilante-specialization", by = ["natural-course"] },
]
+++

Within some vigilantes are incredible innate abilities that, although normally the domain of natural
beasts, inexplicably aid them in fighting their enemies. These vigilantes have ties to the creature
whose abilities they emulate, whether from a distant lycanthrope ancestor, a divine touch, unnatural
experimentation, or something else altogether.

## Natural Course (Ex) {#natural-course}

At first level, when a wildsoul chooses a vigilante specialization, he must also choose a natural
course: arachnid, falconine, or ursine. This represents the type of creature that influences his
body, granting him his remarkable abilities. Once this choice is made, it can't be changed.

At 2nd, 6th, 12th, and 18th levels, a wildsoul gains a specific ability tied to his natural course.
These abilities count as vigilante talents, as onlookers who see the wildsoul in his social identity
use them overtly might suspect him of being something more than he appears; the more obvious
animalistic abilities (like bear form and shoot webs) impart a -10 penalty on the wildsoul's
Disguise check to appear as his social identity.

This alters vigilante specialization and replaces the vigilante talents gained at 2nd, 6th, 12th,
and 18th levels.

### Arachnid {#arachnid}

These wildsouls have the blood of spiders running through their veins.

#### Heightened Senses (Ex) {#heightened-senses}

At 2nd level, an arachnid wildsoul can anticipate physical danger and react astonishingly quickly.
He gains the [stalker sense](ref/vigtalent/stalker-sense) vigilante talent, even if he is not a
stalker.

#### Shoot Webs (Ex) {#shoot-webs}

At 6th level, an arachnid wildsoul's wrists can produce thick, sticky webbing that he can shoot at
his enemies. Shooting webbing is a ranged touch attack with a range increment of 10 feet. The
webbing acts as a [tanglefoot bag](ref/eq-weapon/tanglefoot-bag) when it hits a creature, except the
DC of the Reflex save to avoid being glued to the floor or unable to fly is equal to 10 + 1/2 the
arachnid wildsoul's vigilante level + his Constitution modifier. Like a tanglefoot bag, the webbing
does not work underwater. The arachnid wildsoul can shoot webs a number of times per day equal to
3 + his Constitution modifier.

#### Web Specialist (Ex) {#web-specialist}

At 12th level, an arachnid wildsoul can coat his hands and feet in super-sticky webbing, even over
equipment such as gloves and boots. This gives him a climb speed of 30 feet. Additionally, as a move
action that provokes attacks of opportunity, an arachnid wildsoul can use his webbing to create the
equivalent of a 50-foot length of [silk rope](ref/eq-misc/silk-rope-50-ft) (hp 4, break DC 24) and
can shoot it at any flat, unoccupied surface that is at least one 5-foot square in size. If the
arachnid wildsoul succeeds at a ranged attack against AC 10, the rope sticks fast to the surface,
can only be removed if it is destroyed, and can support the weight of the arachnid wildsoul plus one
additional Medium or smaller creature. If more creatures attempt to use the webbing rope, it is
destroyed. This costs a daily use of shoot webs.

#### Web Master (Ex) {#web-master}

At 18th level, an arachnid wildsoul can use web specialist without spending a daily use of shoot
webs. Additionally, he can create numerous web-ropes as he is moving and swing from rope to rope,
essentially allowing him to move at his base speed through the air as long as he always uses at
least one hand to hold the webbing and continues to have tether points within 50 feet and above him.
The web ropes he creates in this way dissolve as soon as he is done using them to swing.

### Falconine {#falconine}

These wildsouls have the blood of falcons or other large birds of prey running through their veins.

#### Soft Landing (Ex) {#soft-landing}

At 2nd level, a falconine wildsoul can grow feathery wing-flaps under his arms that allow him to
fall slowly. He gains the [perfect fall](ref/vigtalent/perfect-fall) vigilante talent.

#### Eagle Eye (Ex) {#eagle-eye}

At 6th level, a falconine wildsoul hones his visual senses. He gains a competence bonus equal to
[half](ref/misc/fractions-and-rounding) his vigilante level on visual Perception checks.

#### Take to the Air (Ex) {#take-to-the-air}

At 12th level, a falconine wildsoul can harness the flight inherent in his blood. While in his
vigilante identity, he has feathery wings that grant him a fly speed of 40 feet (with good
maneuverability).

#### Deadly Dive (Ex) {#deadly-dive}

At 18th level, a falconine wildsoul has learned how to mimic the swooping and diving of birds of
prey. As a full-round action while he is flying at least 30 feet above the ground, a falconine
wildsoul can dive onto a creature by moving up to twice his fly speed and make a single melee
attack. The movement provokes attacks of opportunity as normal, and the attack provokes an attack of
opportunity from the attack's target. If the attack is successful, the falconine wildsoul deals the
attack's damage plus 2d6 points of damage for every 10 feet he dove (to a maximum of 20d6 damage if
he dove 100 feet or more). Even if the attack misses, the target still takes the extra damage for
the distance of the dive, but it receives a Reflex save to halve the damage (DC = 10 + 1/2 the
falconine wildsoul's vigilante level + his Strength or Dexterity modifier, whichever is higher). A
falconine vigilante can dive in this way a number of times per day equal to his Strength or
Dexterity modifier, whichever is higher.

### Ursine {#ursine}

These wildsouls have the blood of bears running through their veins.

#### Deadly Claws (Ex) {#deadly-claws}

At 2nd level, an ursine wildsoul's hands become claws in his vigilante identity, granting him two
claw attacks. These are primary [natural attacks](ref/rule/natural-attacks) that deal 1d4 points of
damage if he is Medium or [1d3 if he is Small](ref/umr/natural-attacks).

#### Bear Jaws (Ex) {#bear-jaws}

At 6th level, an ursine wildsoul gains a bite attack while in his vigilante identity. This is a
primary natural attack that deals 1d4 points of damage if he is Medium or 1d3 if he is Small.

#### Thick Hide (Ex) {#thick-hide}

At 12th level, an ursine wildsoul in his vigilante identity has skin that bristles with thick hair
like that of a bear's. He gains a natural armor bonus of +1. This natural armor bonus increases by 1
at 16th and 20th levels.

#### Bear Form (Su) {#bear-form}

At 18th level, an ursine wildsoul has learned how to take a bear's form. He can change into bear
form as a standard action, at will, and the transformation lasts until he changes back. While
transformed, he becomes a [grizzly bear](ref/monster/bear-grizzly-bear) as
_[beast shape II](ref/spell/beast-shape-2)_. An ursine wildsoul loses his ability to speak while in
bear form and is limited to the sounds that a normal bear can make, though he can communicate
normally with other bears, as _speak with animal_.

### Feline Natural Course (Blood of the Beast page 7) {#feline-natural-course}

When a vigilante with the wildsoul archetype chooses a vigilante specialization, he can choose the
following natural course. Feline wildsouls have the blood of great cats running through their veins.

_Feline Attributes (Ex)_: At 2nd level, a feline wildsoul gains the
[low-light vision](ref/umr/low-light-vision) and [scent](ref/umr/scent) special abilities and
reduces any penalty he takes on Perception checks due to distance by an amount equal to
[half](ref/misc/fractions-and-rounding) his vigilante level (minimum 0). If he also gains
[low-light vision](ref/rule/low-light-vision) or scent from a feat or racial trait, he instead gains
a +2 bonus on Perception checks for each ability he already has. In addition, he can take
[Aspect of the Beast](ref/feat/aspect-of-the-beast), ignoring the feat's prerequisites.

_Feline Grace (Ex)_: At 6th level, a feline wildsoul gains
[uncanny dodge](ref/ability/uncanny-dodge), using his vigilante level as his effective
[rogue](ref/class/rogue) level. At 12th level, he also gains
[improved uncanny dodge](ref/ability/improved-uncanny-dodge).

_Feline Pounce (Ex)_: At 12th level, a feline wildsoul can strike quickly and lethally at a moment's
notice. He gains the [mad rush](ref/vigtalent/mad-rush) avenger vigilante talent, even if he is not
an avenger.

_Nine Lives (Su)_: At 18th level, a feline wildsoul can survive attacks that would kill lesser
vigilantes. He gains the [defensive roll](ref/talent/defensive-roll) advanced rogue talent and can
use this ability eight times per day.
