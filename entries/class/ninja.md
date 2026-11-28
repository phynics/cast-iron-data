+++
id = "ref/class/ninja"
kind = "class"
title = "Ninja"
aon = "ClassDisplay.aspx?ItemName=Ninja"
source_ids = ["ultimate-combat", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ninja", path = "json/classes3.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "13"
[[sources]]
publication = "chronicle-of-legends"
page = "28-29"

[fields]
kind = "class"
class_type = "alternate"
hit_die = "d8"
skill_ranks = "8 + Int modifier"
features = [
  { anchor = "poison-use", level = 1 },
  { anchor = "sneak-attack", level = 1 },
  { anchor = "ki-pool", level = 2 },
  { anchor = "ninja-tricks", level = 2 },
  { anchor = "no-trace", level = 3 },
  { anchor = "uncanny-dodge", level = 4 },
  { anchor = "light-steps", level = 6 },
  { anchor = "improved-uncanny-dodge", level = 8 },
  { anchor = "master-tricks", level = 10 },
  { anchor = "hidden-master", level = 20 },
]
+++

When the wealthy and the powerful need an enemy eliminated quietly and without fail, they call upon
the ninja. When a general needs to sabotage the siege engines of his foes before they can reach the
castle walls, he calls upon the ninja. And when fools dare to move against a ninja or her
companions, they will find the ninja waiting for them while they sleep, ready to strike. These
shadowy killers are masters of infiltration, sabotage, and assassination, using a wide variety of
weapons, practiced skills, and mystical powers to achieve their goals.

**Role:** The ninja spends almost all of her time honing her skills, practicing her art, or working
on her next assignment. Even when not specifically working, the ninja is ever vigilant and ready for
the situation to turn deadly. Her line of work earns her many enemies, but it is a list that she
frequently reduces through assassination and misdirection. The ninja is an alternate class for the
rogue core class.

**Alignment:** Any

**Hit Die:** d8

**Parent Class(es):** [Rogue](ref/class/rogue).

**Starting Wealth:** 4d6 × 10 gp (average 140 gp)

**Skill Points per Level:** 8 + Int modifier

**Class Skills (Str):** Climb, Swim

**Class Skills (Dex):** Acrobatics, Disable Device, Escape Artist, Sleight of Hand, Stealth

**Class Skills (Int):** Appraise, Craft (any), Knowledge (local), Knowledge (nobility), Linguistics

**Class Skills (Wis):** Perception, Profession (any), Sense Motive

**Class Skills (Cha):** Bluff, Diplomacy, Disguise, Intimidate, Perform (any), Use Magic Device

### Class Features

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|
| --- | --- | --- | --- | --- | --- |
|1st|+0|+0|+2|+0|Poison use, sneak attack +1d6|
|2nd|+1|+0|+3|+0|_Ki_ pool, ninja trick|
|3rd|+2|+1|+3|+1|No trace +1, sneak attack +2d6|
|4th|+3|+1|+4|+1|Ninja trick, uncanny dodge|
|5th|+3|+1|+4|+1|Sneak attack +3d6|
|6th|+4|+2|+5|+2|Light steps, ninja trick, no trace +2|
|7th|+5|+2|+5|+2|Sneak attack +4d6|
|8th|+6/+1|+2|+6|+2|Improved uncanny dodge, ninja trick|
|9th|+6/+1|+3|+6|+3|No trace +3, sneak attack +5d6|
|10th|+7/+2|+3|+7|+3|Master tricks, ninja trick|
|11th|+8/+3|+3|+7|+3|Sneak attack +6d6|
|12th|+9/+4|+4|+8|+4|Ninja trick, no trace +4|
|13th|+9/+4|+4|+8|+4|Sneak attack +7d6|
|14th|+10/+5|+4|+9|+4|Ninja trick|
|15th|+11/+6/+1|+5|+9|+5|No trace +5, sneak attack +8d6|
|16th|+12/+7/+2|+5|+10|+5|Ninja trick|
|17th|+12/+7/+2|+5|+10|+5|Sneak attack +9d6|
|18th|+13/+8/+3|+6|+11|+6|Ninja trick, no trace +6|
|19th|+14/+9/+4|+6|+11|+6|Sneak attack +10d6|
|20th|+15/+10/+5|+6|+12|+6|Hidden master, ninja trick|

The following are the class features of the ninja.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

Ninja are proficient with all simple weapons, plus the kama, katana, kusarigama, nunchaku, sai,
shortbow, short sword, shuriken, siangham, and wakizashi. They are proficient with light armor but
not with shields.

#### Poison Use {#poison-use}

At 1st level, a ninja is trained in the use of poison and cannot accidentally poison herself when
applying poison to a weapon.

#### Sneak Attack {#sneak-attack}

If a ninja can catch an opponent when he is unable to defend himself effectively from her attack,
she can strike a vital spot for extra damage.

The ninja's attacks deal extra damage anytime her target would be denied a Dexterity bonus to AC
(whether the target actually has a Dexterity bonus or not), or when the ninja flanks her target.
This extra damage is 1d6 at 1st level, and increases by 1d6 every two ninja levels thereafter. Bonus
damage from sneak attacks is precision damage. Should the ninja score a critical hit with a
[sneak attack](ref/ability/sneak-attack), this precision damage is not multiplied. Ranged attacks
count as sneak attacks only if the target is within 30 feet.

With a weapon that deals nonlethal damage (such as a sap, whip, or unarmed strike), a ninja can make
a sneak attack that deals nonlethal damage instead of lethal damage. She cannot use a weapon that
deals lethal damage to deal nonlethal damage in a sneak attack, even with the usual -4 penalty.

The ninja must be able to see the target well enough to pick out a vital spot, and must be able to
reach this spot. A ninja cannot sneak attack while striking a creature that has concealment.

#### Ki Pool (Su) {#ki-pool}

At 2nd level, a ninja gains a pool of ki points, supernatural energy she can use to accomplish
amazing feats. The number of points in the ninja's ki pool is equal to 1/2 her ninja level + her
Charisma modifier. As long as she has at least 1 point in her ki pool, she treats any
[Acrobatics](ref/skill/acrobatics) skill check made to jump as if she had a running start. At 10th
level, she also reduces the DC of Acrobatics skill checks made to jump by 1/2 (although she still
cannot move farther than her speed allows).

By spending 1 point from her ki pool, a ninja can make one additional attack at her highest attack
bonus, but she can do so only when making a full attack. In addition, she can spend 1 point to
increase her speed by 20 feet for 1 round. Finally, a ninja can spend 1 point from her ki pool to
give herself a +4 insight bonus on Stealth checks for 1 round. Each of these powers is activated as
a swift action. A ninja can gain additional powers that consume points from her ki pool by selecting
certain ninja tricks.

The ki pool is replenished each morning after 8 hours of rest or meditation; these hours do not need
to be consecutive. If the ninja possesses levels in another class that grants points to a ki pool,
ninja levels stack with the levels of that class to determine the total number of ki points in the
combined pool, but only one ability score modifier is added to the total. The choice of which score
to use is made when the second class ability is gained, and once made, the choice is set. The ninja
can now use ki points from this pool to power the abilities of every class she possesses that grants
a ki pool.

#### Ninja Tricks {#ninja-tricks}

As a ninja continues her training, she learns a number of tricks that allow her to confuse her foes
and grant her supernatural abilities. Starting at 2nd level, a ninja gains one ninja trick. She
gains one additional ninja trick for every 2 levels attained after 2nd. Unless otherwise noted, a
ninja cannot select an individual ninja trick more than once.

Tricks marked with an asterisk (\*) add effects to a ninja's sneak attack. Only one of these tricks
can be applied to an individual attack and the decision must be made before the attack is made.

- [Acrobatic Master (Su)](ref/ninjatrick/acrobatic-master)
- [Bleeding Attack (Ex)](ref/ninjatrick/bleeding-attack)\*
- [Choking Bomb (Ex)](ref/ninjatrick/choking-bomb)
- [Combat Trick](ref/ninjatrick/combat-trick)
- [Darkvision (Su)](ref/ninjatrick/darkvision)
- [Deadly Range (Ex)](ref/ninjatrick/deadly-range)
- [Deflect Arrows](ref/ninjatrick/deflect-arrows)
- [Fast Stealth (Ex)](ref/ninjatrick/fast-stealth)
- [Feather Fall (Su)](ref/ninjatrick/feather-fall)
- [Flurry of Stars (Ex)](ref/ninjatrick/flurry-of-stars)
- [Forgotten Trick (Ex)](ref/ninjatrick/forgotten-trick)
- [Hidden Weapons (Ex)](ref/ninjatrick/hidden-weapons)
- [High Jumper (Ex)](ref/ninjatrick/high-jumper)
- [Ki Block (Su)](ref/ninjatrick/ki-block)\*
- [Ki Charge (Su)](ref/ninjatrick/ki-charge)
- [Poison Bomb (Ex)](ref/ninjatrick/poison-bomb)
- [Pressure Points (Su)](ref/ninjatrick/pressure-points)\*
- [Rogue Talent](ref/ninjatrick/rogue-talent)
- [Shadow Clone (Su)](ref/ninjatrick/shadow-clone)
- [Slow Metabolism (Ex)](ref/ninjatrick/slow-metabolism)
- [Slow Reactions (Ex)](ref/ninjatrick/slow-reactions)\*
- [Smoke Bomb (Ex)](ref/ninjatrick/smoke-bomb)
- [Snatch Arrows](ref/ninjatrick/snatch-arrows)
- [Style Master](ref/ninjatrick/style-master)
- [Sudden Disguise (Su)](ref/ninjatrick/sudden-disguise)
- [Unarmed Combat Training](ref/ninjatrick/unarmed-combat-training)
- [Undetected Sabotage (Ex)](ref/ninjatrick/undetected-sabotage)
- [Vanishing Trick (Su)](ref/ninjatrick/vanishing-trick)
- [Ventriloquism (Su)](ref/ninjatrick/ventriloquism)
- [Wall Climber (Su)](ref/ninjatrick/wall-climber)
- [Weapon Training](ref/ninjatrick/weapon-training)

#### No Trace (Ex) {#no-trace}

At 3rd level, a ninja learns to cover her tracks, remain hidden, and conceal her presence. The DC to
track a ninja using the Survival skill increases by +1. In addition, her training gives her a +1
insight bonus on Disguise skill checks and on opposed Stealth checks whenever she is stationary and
does not take any action for at least 1 round. Every three levels thereafter, the increase to
Survival DCs and the bonuses on Disguise and opposed Stealth checks increase by 1.

#### Uncanny Dodge (Ex) {#uncanny-dodge}

Starting at 4th level, a ninja can react to danger before her senses would normally allow her to do
so. She cannot be caught [flat-footed](ref/rule/flat-footed), nor does she lose her Dexterity bonus
to AC if the attacker is invisible. She still loses her Dexterity bonus to AC if immobilized. A
ninja with this ability can still lose her Dexterity bonus to AC if an opponent successfully uses
the [feint](ref/rule/feint) action against her.

If a ninja already possesses uncanny dodge from a different class, she automatically gains improved
uncanny dodge instead.

#### Light Steps (Ex) {#light-steps}

At 6th level, a ninja learns to move while barely touching the surface underneath her. As a
full-round action, she can move up to twice her speed, ignoring
[difficult terrain](ref/rule/terrain-and-obstacles). While moving in this way, any surface will
support her, no matter how much she weighs. This allows her to move across water, lava, or even the
thinnest tree branches. She must end her move on a surface that can support her normally. She cannot
move across air in this way, nor can she walk up walls or other vertical surfaces. When moving in
this way, she does not take damage from surfaces or hazards that react to being touched, such as
lava or caltrops, nor does she need to make Acrobatics checks to avoid falling on slippery or rough
surfaces. Finally, when using light steps, the ninja ignores any mechanical traps that use a
location-based trigger.

#### Improved Uncanny Dodge (Ex) {#improved-uncanny-dodge}

At 8th level, a ninja can no longer be [flanked](ref/rule/flanking). This defense denies another
ninja (or rogue) the ability to sneak attack the ninja by flanking her, unless the attacker has at
least four more ninja (or rogue) levels than the target does.

If a character already has uncanny dodge from another class, the levels from the classes that grant
uncanny dodge stack when determining the minimum ninja (or rogue) level required to flank the
character.

#### Master Tricks {#master-tricks}

At 10th level, and every two levels thereafter, a ninja can select one of the following master
tricks in place of a ninja trick.

_Advanced Talents_: The ninja can select a rogue talent from the list of Advanced Talents in place
of a ninja trick. The ninja cannot select a rogue talent that has the same name as a ninja trick.
The ninja cannot select improved evasion unless she has evasion (either as a class feature or as a
ninja master trick).

- [Assassinate (Ex)](ref/ninjatrick/assassinate)
- [Blinding Bomb (Ex)](ref/ninjatrick/blinding-bomb)
- [Deadly Shuriken (Ex)](ref/ninjatrick/deadly-shuriken)
- [Evasion (Ex)](ref/ninjatrick/evasion)
- [Feat](ref/ninjatrick/feat)
- [Ghost Step (Su)](ref/ninjatrick/ghost-step)
- [Invisible Blade (Su)](ref/ninjatrick/invisible-blade)
- [Master Disguise (Su)](ref/ninjatrick/master-disguise)
- [See the Unseen (Su)](ref/ninjatrick/see-the-unseen)
- [Shadow Split (Su)](ref/ninjatrick/shadow-split)
- [Unarmed Combat Mastery](ref/ninjatrick/unarmed-combat-mastery)
- [Unbound Steps (Su)](ref/ninjatrick/unbound-steps)

#### Hidden Master (Su) {#hidden-master}

At 20th level, a ninja becomes a true master of her art. She can, as a standard action, cast
_[greater invisibility](ref/spell/invisibility-greater)_ on herself. While invisible in this way,
she cannot be detected by any means, and not even
_[invisibility purge](ref/spell/invisibility-purge)_,
_[see invisibility](ref/spell/see-invisibility)_, and _[true seeing](ref/spell/true-seeing)_ can
reveal her. She uses her ninja level as her caster level for this ability. Using this ability
consumes 3 ki points from her ki pool. In addition, whenever the ninja deals sneak attack damage,
she can sacrifice additional damage dice to apply a penalty to one ability score of the target equal
to the number of dice sacrificed for 1 minute. This penalty does not stack with itself and cannot
reduce an ability score below 1.

### Alternate Capstones

When a character reaches the 20th level of a class, she gains a powerful class feature or ability,
sometimes referred to as a capstone. The following section provides new capstones for characters to
select at 20th level. A character can select one of the following capstones in place of the capstone
provided by her class. Some capstones are for specific classes, while others are for a range of
classes that qualify for them. In some cases, a capstone specifies what ability it replaces. A
character can't select a new capstone if she has previously traded away her class capstone via an
archetype. Clerics and wizards can receive a capstone at 20th level, despite not having one to begin
with. A character that gains certain abilities may be eligible for capstones other than those listed
below.

**Slicing Wind (Su)**

At 20th level, the ninja is a creature of wind and blades. When using _light steps,_ the ninja can
move up to four times her speed and make a single attack at her highest base attack bonus at any
point during the movement.

**Also available:** Ki Sage, The Right Spot

### Archetypes

From the noble paladin to the skillful rogue, each class draws upon a central archetype. Yet, beyond
that basic concept exists the potential for innumerable interpretations, details, and refinements;
and some archetypes prove pervasive and exciting enough to see use in play time and time again.

To help players interested in creating iconic fantasy characters, **archetypes** were introduced.
These optional features represent a unique view of what a class deliberately designed to capture a
specific character archetype might become. While the types of options presented for each class
differ, each subsystem is customized to best serve that class, emulate the abilities and talents of
classic fantasy archetypes, and expand players' freedom to design exactly the characters they
desire.

**Frozen Shadow**

**Class:** ninja

**Modifies or Replaces:** Class Skills; Ki Pool; Uncanny Dodge; Improved Uncanny Dodge

**Description:** Frozen shadows belong to a rare ninja clan operating in Avistan and they work as
thieves, power brokers, and spies loosely guided by secretive masters with unknown agendas.

**Gunpowder Bombardier**

**Class:** ninja

**Modifies or Replaces:** Ki Pool; 2nd-level Ninja Trick; Uncanny Dodge; Improved Uncanny Dodge

**Description:** Ratfolk assassins and other ninjas with an affinity for gunpowder demonstrate
masterful control of bombs, using the explosives to inflict major damage or impair their foes

**Hunting Serpent**

**Class:** ninja

**Modifies or Replaces:** Class Skills; No Trace; Uncanny Dodge; Improved Uncanny Dodge; 10th, 12th,
16th-level Ninja Trick

**Description:** Hunting serpents are specially trained killers to that hunt relentlessly and fight
from the shadows.

**Mask of the Living God**

**Class:** ninja

**Modifies or Replaces:** Weapon and Armor Proficiency; Poison Use; Ki Pool; No Trace

**Description:** When the Living God needs to silence the voices of those heretics who question too
loudly, these enforcers are the tools he employs.

**Petal Ninja**

**Class:** ninja

**Modifies or Replaces:** Class Skills; 2nd-level Ninja Trick; No Trace; Uncanny Dodge; Improved
Uncanny Dodge; Light Steps

**Description:** (Ghoran Only) Petal ninjas are a secretive clan of ghoran infiltrators, in touch
with their plant-like nature to the point where they can change their forms, allowing them access
into places that were previously impossible to reach.

### Archetypes by Feature

|Archetype|Class Skills|Ki Pool|Light Steps|2nd-level Ninja Trick|10th, 12th, and 16th-level Ninja Tricks|No Trace|Poison Use|Uncanny Dodge|Improved Uncanny Dodge|Weapon/_wbr_Armor Proficiency|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Frozen Shadow](ref/arc-ninja/frozen-shadow)|X|X||||||X|X||
|[Gunpowder Bombardier](ref/arc-ninja/gunpowder-bombardier)||X||X||||X|X||
|[Hunting Serpent](ref/arc-ninja/hunting-serpent)|X||||X|X||X|X||
|[Mask of the Living God](ref/arc-ninja/mask-of-the-living-god)||X||||X|X|||X|
|[Petal Ninja](ref/arc-ninja/petal-ninja)|X||X|X||X||X|X||

### Favored Class Bonuses

_The favored class options for ninja are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
