+++
id = "ref/class/unchained-barbarian"
kind = "class"
title = "Unchained Barbarian"
aon = "ClassDisplay.aspx?ItemName=Barbarian%20%28Unchained%29"
source_ids = ["pathfinder-unchained", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unchained_barbarian", path = "json/classes7.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "8"
[[sources]]
publication = "chronicle-of-legends"
page = "28"

[fields]
kind = "class"
class_type = "unchained"
hit_die = "d12"
skill_ranks = "4 + Int modifier"
features = [
  { anchor = "fast-movement", level = 1 },
  { anchor = "rage", level = 1 },
  { anchor = "rage-powers", level = 2 },
  { anchor = "uncanny-dodge", level = 2 },
  { anchor = "danger-sense", level = 3 },
  { anchor = "improved-uncanny-dodge", level = 5 },
  { anchor = "damage-reduction", level = 7 },
  { anchor = "greater-rage", level = 11 },
  { anchor = "indomitable-will", level = 14 },
  { anchor = "tireless-rage", level = 17 },
  { anchor = "mighty-rage", level = 20 },
]
+++

For some heroes, the rage that lives within them can't be contained. Whether this fury is a product
of heritage or of nature, these adventurers have learned to harness it, turning its power against
their foes. The primal warriors known as barbarians transform their rage into a potent weapon on a
battlefield. Heedless of their wounds and possessed of unstoppable bloodlust, these savage brutes
are the embodiment of war.

**Unchained:** The unchained barbarian is similar in many regards to its counterpart in the Core
Rulebook - she still goes into a rage and gains rage powers, but many of the details have been
changed. Rage now grants [temporary hit points](ref/rule/temporary-hit-points) and static bonuses on
attack and damage rolls, rather than bonuses to ability scores that force players to recalculate a
number of statistics. Additionally, many rage powers now function whenever the barbarian is
_raging,_ as opposed to just once per rage. Finally, the overall utility of many of the rage powers
has been adjusted to make them more useful and interesting.

**Alignment:** Any nonlawful

**Hit Die:** d12

**Starting Wealth:** 3d6 × 10 gp (average 105 gp)

**Skill Points per Level:** 4 + Int modifier

**Class Skills (Str):** Climb, Swim

**Class Skills (Dex):** Acrobatics, Ride

**Class Skills (Int):** Craft (any), Knowledge (nature)

**Class Skills (Wis):** Perception, Survival

**Class Skills (Cha):** Handle Animal, Intimidate

### Class Features

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|
| --- | --- | --- | --- | --- | --- |
|1st|+1|+2|+0|+0|Fast movement, rage|
|2nd|+2|+3|+0|+0|Rage power, uncanny dodge|
|3rd|+3|+3|+1|+1|Danger sense +1|
|4th|+4|+4|+1|+1|Rage power|
|5th|+5|+4|+1|+1|Improved uncanny dodge|
|6th|+6/+1|+5|+2|+2|Danger sense +2, rage power|
|7th|+7/+2|+5|+2|+2|[Damage reduction](ref/rule/damage-reduction) 1/-|
|8th|+8/+3|+6|+2|+2|Rage power|
|9th|+9/+4|+6|+3|+3|Danger sense +3|
|10th|+10/+5|+7|+3|+3|[Damage reduction](ref/rule/damage-reduction) 2/-, rage power|
|11th|+11/+6/+1|+7|+3|+3|Greater rage|
|12th|+12/+7/+2|+8|+4|+4|Danger sense +4, rage power|
|13th|+13/+8/+3|+8|+4|+4|[Damage reduction](ref/rule/damage-reduction) 3/-|
|14th|+14/+9/+4|+9|+4|+4|Indomitable will, rage power|
|15th|+15/+10/+5|+9|+5|+5|Danger sense +5|
|16th|+16/+11/+6/+1|+10|+5|+5|[Damage reduction](ref/rule/damage-reduction) 4/-, rage power|
|17th|+17/+12/+7/+2|+10|+5|+5|Tireless rage|
|18th|+18/+13/+8/+3|+11|+6|+6|Danger sense +6, rage power|
|19th|+19/+14/+9/+4|+11|+6|+6|[Damage reduction](ref/rule/damage-reduction) 5/-|
|20th|+20/+15/+10/+5|+12|+6|+6|Mighty rage, rage power|

All of the following are class features of the barbarian.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

A barbarian is proficient with all simple and martial weapons, light armor, medium armor, and
shields (except tower shields).

#### Fast Movement (Ex) {#fast-movement}

A barbarian's base speed is faster than the norm for her race by 10 feet. This benefit applies only
when she is wearing no armor, light armor, or medium armor, and not carrying a heavy load. Apply
this bonus before modifying the barbarian's speed because of any load carried or armor worn. This
bonus stacks with any other bonuses to the barbarian's base speed.

#### Rage (Ex) {#rage}

A barbarian can call upon inner reserves of strength and ferocity, granting her additional combat
prowess. At 1st level, a barbarian can rage for a number of rounds per day equal to 4 + her
Constitution modifier. For each level after 1st she possesses, the barbarian can rage for 2
additional rounds per day. Temporary increases to Constitution, such as that gained from
_[bear's endurance](ref/spell/bears-endurance)_, do not increase the total number of rounds that a
barbarian can rage per day. A barbarian can enter a rage as a free action. The total number of
rounds of rage per day is renewed after resting for 8 hours, although these hours need not be
consecutive.

While in a rage, a barbarian gains a +2 bonus on melee attack rolls, melee damage rolls, thrown
weapon damage rolls, and Will saving throws. In addition, she takes a -2 penalty to Armor Class. She
also gains 2 [temporary hit points](ref/rule/temporary-hit-points) per Hit Die. These temporary hit
points are lost first when a character takes damage, disappear when the rage ends, and are not
replenished if the barbarian enters a rage again within 1 minute of her previous rage. While in a
rage, a barbarian cannot use any Charisma-, Dexterity-, or Intelligence-based skill (except
Acrobatics, Fly, Intimidate, and Ride) or any ability that requires patience or concentration (such
as spellcasting).

A barbarian can end her rage as a free action, and is [fatigued](ref/misc/fatigued) for 1 minute
after a rage ends. A barbarian can't enter a new rage while fatigued or
[exhausted](ref/misc/exhausted), but can otherwise enter a rage multiple times per day. If a
barbarian falls unconscious, her rage immediately ends.

#### Rage Powers (Ex) {#rage-powers}

As a barbarian gains levels, she learns to use her rage in new ways. At 2nd level and every 2 levels
thereafter, the barbarian gains a rage power. A barbarian gains the benefits of rage powers only
while raging. Some of these powers are always active during a rage, and others require the barbarian
to take an action to use them. Unless otherwise noted, a barbarian cannot select an individual power
more than once.

Some of the following rage powers are stances. Activating a stance rage power is a move action. A
barbarian can't have more than one stance rage power active at a time. If she activates a stance
rage power while another one is active, the current stance immediately ends. The stance can be
intentionally ended at the beginning of the barbarian's turn as a free action; otherwise, it lasts
until the rage ends.

- [Accurate Stance (Ex)](ref/ragepower/accurate-stance)
- [Animal Fury (Ex)](ref/ragepower/animal-fury)
- [Auspicious Mark (Su)](ref/ragepower/auspicious-mark)
- [Bleeding Blow (Ex)](ref/ragepower/bleeding-blow)
- [Calm Stance (Ex)](ref/ragepower/calm-stance)
- [Clear Mind (Ex)](ref/ragepower/clear-mind)
- [Crippling Blow (Ex)](ref/ragepower/crippling-blow)
- [Deadly Accuracy (Ex)](ref/ragepower/deadly-accuracy)
- [Eater of Magic (Su)](ref/ragepower/eater-of-magic)
- [Elemental Stance (Su)](ref/ragepower/elemental-stance)
- [Energy Absorption (Su)](ref/ragepower/energy-absorption)
- [Energy Resistance (Ex)](ref/ragepower/energy-resistance)
- [Fearless Rage (Ex)](ref/ragepower/fearless-rage)
- [Flesh Wound (Ex)](ref/ragepower/flesh-wound)
- [Ground Breaker (Ex)](ref/ragepower/ground-breaker)
- [Greater Ground Breaker (Ex)](ref/ragepower/greater-ground-breaker)
- [Guarded Stance (Ex)](ref/ragepower/guarded-stance-stance)
- [Increased Damage Reduction (Ex)](ref/ragepower/increased-damage-reduction)
- [Inspire Ferocity (Ex)](ref/ragepower/inspire-ferocity)
- [Internal Fortitude (Ex)](ref/ragepower/internal-fortitude)
- [Intimidating Glare (Ex)](ref/ragepower/intimidating-glare)
- [Knockback (Ex)](ref/ragepower/knockback)
- [Knockdown Stance (Ex)](ref/ragepower/knockdown-stance)
- [Lethal Accuracy (Ex)](ref/ragepower/lethal-accuracy)
- [Low-Light Vision (Ex)](ref/ragepower/low-light-vision)
- [Mighty Swing (Ex)](ref/ragepower/mighty-swing)
- [Night Vision (Ex)](ref/ragepower/night-vision)
- [No Escape (Ex)](ref/ragepower/no-escape)
- [Perfect Clarity (Ex)](ref/ragepower/perfect-clarity)
- [Powerful Stance (Ex)](ref/ragepower/powerful-stance)
- [Quick Reflexes (Ex)](ref/ragepower/quick-reflexes)
- [Raging Climber (Ex)](ref/ragepower/raging-climber)
- [Raging Leaper (Ex)](ref/ragepower/raging-leaper)
- [Raging Swimmer (Ex)](ref/ragepower/raging-swimmer)
- [Reckless Stance (Ex)](ref/ragepower/reckless-stance)
- [Reflexive Dodge (Ex)](ref/ragepower/reflexive-dodge)
- [Regenerative Stance (Ex)](ref/ragepower/regenerative-stance)
- [Renewed Vigor (Ex)](ref/ragepower/renewed-vigor)
- [Renewed Vitality (Ex)](ref/ragepower/renewed-vitality)
- [Roused Anger (Ex)](ref/ragepower/roused-anger)
- [Scent (Ex)](ref/ragepower/scent)
- [Sharpened Accuracy (Ex)](ref/ragepower/sharpened-accuracy)
- [Smasher (Ex)](ref/ragepower/smasher)
- [Sprint (Ex)](ref/ragepower/sprint)
- [Strength Stance (Ex)](ref/ragepower/strength-stance)
- [Superstition (Ex)](ref/ragepower/superstition)
- [Swift Foot (Ex)](ref/ragepower/swift-foot)
- [Taunting Stance (Ex)](ref/ragepower/taunting-stance)
- [Terrifying Howl (Ex)](ref/ragepower/terrifying-howl)
- [Unexpected Strike (Ex)](ref/ragepower/unexpected-strike)
- [Witch Hunter (Ex)](ref/ragepower/witch-hunter)

##### Shove Aside (Ex) {#shove-aside}

Whenever the barbarian charges, she may push past one of her allies. That ally does not block the
path of the charge as long as the ally is not adjacent to the target of the charge. This does not
move the ally's position; it simply allows the barbarian to move past.

_Shove Aside, Greater (Ex)_: This functions as shove aside, but it applies to any number of allies,
so long as they are not adjacent to the target of the charge. A barbarian must have the shove aside
rage power and be at least 8th level to select this rage power.

##### Unmodified Rage Powers {#unmodified-rage-powers}

The list of barbarian rage powers includes replacements for everything from the _Core Rulebook_,
along with select revised powers based on the rage powers from _Pathfinder RPG Advanced Player's
Guide_ and _Pathfinder RPG Ultimate Combat_. The following rage powers from the latter two books can
be used unaltered.

##### Advanced Player's Guide {#advanced-player-s-guide}

Beast totem, beast totem (greater), beast totem (lesser), boasting taunt, brawler, brawler
(greater), chaos totem, chaos totem (greater), chaos totem (lesser), disruptive, ferocious mount,
ferocious mount (greater), ferocious trample, ferocious trample (greater), fiend totem, fiend totem
(greater), fiend totem (lesser), good for what ails you, guarded life, hurling, hurling (greater),
hurling (lesser), hurling charge, liquid courage, overbearing advance, overbearing onslaught,
roaring drunk, spirit steed, spirit totem, spirit totem (greater), spirit totem (lesser), staggering
drunk.

##### Ultimate Campaign {#ultimate-campaign}

Body bludgeon, dragon totem, dragon totem resilience, ghost rager, guarded life (greater), hive
totem, hive totem resilience, hive totem toxicity, primal scent, sunder enchantment, world serpent
spirit, world serpent totem, world serpent totem unity. stack to determine the minimum level
required to flank the barbarian.

#### Uncanny Dodge (Ex) {#uncanny-dodge}

At 2nd level, a barbarian gains the ability to react to danger before her senses would normally
allow her to do so. She cannot be caught [flat-footed](ref/rule/flat-footed), nor does she lose her
Dexterity bonus to AC if immobilized. A barbarian with this ability can still lose her Dexterity
bonus to AC if an opponent successfully uses the feint action against her.

If a barbarian already has uncanny dodge from a different class, she automatically gains improved
uncanny dodge (see below) instead.

#### Danger Sense (Ex) {#danger-sense}

At 3rd level, a barbarian gains a +1 bonus on Reflex saves to avoid traps and a +1 dodge bonus to AC
against attacks by traps. In addition, she gains a +1 bonus on Perception checks to avoid being
surprised by a foe. These bonuses increase by 1 every 3 levels thereafter (to a maximum of +6 at
18th level). This ability counts as trap sense for any feat or class prerequisite, and can be
replaced by any archetype class feature that replaces trap sense. The bonuses gained from this
ability stack with those gained from trap sense (if the barbarian has trap sense from another
class).

#### Improved Uncanny Dodge (Ex) {#improved-uncanny-dodge}

At 5th level, a barbarian can no longer be [flanked](ref/rule/flanking). This defense denies enemies
the ability to [sneak attack](ref/ability/sneak-attack) the barbarian by flanking her, unless the
attacker has at least 4 more levels in a class that provides sneak attack than the barbarian has
barbarian levels.

If the barbarian also has uncanny dodge from another class, levels from the classes that grant
uncanny dodge stack to determine the minimum level required to flank the barbarian.

#### Damage Reduction (Ex) {#damage-reduction}

At 7th level, a barbarian gains [damage reduction](ref/rule/damage-reduction). Each time the
barbarian takes damage from a weapon or natural attack, subtract 1 from the damage taken. At 10th
level and every 3 levels thereafter, this damage reduction rises by 1 point (up to 5 points at 19th
level). Damage reduction can reduce damage to 0, but not below 0.

#### Greater Rage (Ex) {#greater-rage}

At 11th level, a barbarian's bonus on melee attack rolls, melee damage rolls, thrown weapon damage
rolls, and Will saves while raging increases to +3. In addition, the amount of temporary hit points
gained when entering a rage increases to 3 per Hit Die.

#### Indomitable Will (Ex) {#indomitable-will}

At 14th level, the barbarian gains a +4 bonus on Will saves to resist enchantment spells while
raging. This bonus stacks with all other modifiers, including the morale bonus on Will saves she
gains during her rage.

#### Tireless Rage (Ex) {#tireless-rage}

At 17th level, a barbarian is no longer fatigued at the end of her rage. If she enters a rage again
within 1 minute of ending a rage, she doesn't gain any temporary hit points from her rage.

#### Mighty Rage (Ex) {#mighty-rage}

At 20th level, a barbarian's bonus on melee attack rolls, melee damage rolls, thrown weapon damage
rolls, and Will saves while raging increases to +4. In addition, the amount of temporary hit points
gained when entering a rage increases to 4 per Hit Die.

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

**Unstoppable (Ex)**

At 20th level, nothing can kill the barbarian, though not for lack of trying. The barbarian gains DR
3/- or increases the value of any existing [damage reduction](ref/rule/damage-reduction) by 3. In
addition, she gains energy [resistance](ref/umr/resistance) to acid, cold, electricity, and fire
equal to her DR/- value.

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

When the _unchained_ classes were introduced, they came with a note saying "these classes should
work with any of the archetypes from previous books as long as the classes still have the
appropriate class features to replace." (_Pathfinder Unchained pg. 8_) The _deepwater rager_
archetype was printed with a note saying it works for the unchained barbarian, and _danger sense_
above explicitly says it can be treated as _trap sense_ for archetype purposes.

**Armored Hulk**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge

**Description:** Some barbarians disdain the hides and leather used as armor by most of their kin.
Instead they master the heaviest of armors, even those created by more civilized people, to gain
greater protection and stability in battle.

**Beastkin Berserker**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; 4th, 8th, 12th-level Rage Power

**Description:** While some barbarians take on bestial aspects in their _rages,_ the beastkin
berserker descends so deeply into primal fury that she actually transforms into an animal.

**Breaker**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Trap Sense

**Description:** Breakers find the need to destroy their surroundings.

**Brutal Pugilist**

**Class:** barbarian

**Modifies or Replaces:** Uncanny Dodge; Trap Sense; Improved Uncanny Dodge

**Description:** Some barbarians focus on using their bare hands to tear their opponents limb from
limb.

**Brutish Swamper**

**Class:** barbarian

**Modifies or Replaces:** Skills; Fast Movement; Uncanny Dodge; Improved Uncanny Dodge; Trap Sense;
6th-level Rage Power

**Description:** The hardy and insular denizens of the swamp produce warriors of narrow focus and
great strength.

**Cave Dweller**

**Class:** barbarian

**Modifies or Replaces:** Skills; Fast Movement; Trap Sense;
[Damage Reduction](ref/rule/damage-reduction)

**Description:** Unused to the light of the sun, cave dwellers use their subterranean expertise to
protect their clans from the manifold dangers of deep caverns and tunnels.

**Deepwater Rager**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Improved Uncanny Dodge; Indomitable Will;
Tireless Rage

**Description:** Deepwater ragers bellow ferociously as they charge their enemies, tackling them
into the raging seas.

**Drunken Brute**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement

**Description:** Drunken brutes use potent liquor to fuel their _rage_ and grant them additional
powers.

**Drunken Rager**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge;
12th-level Rage Power

**Description:** These hotheaded, hard-drinking ruffians and brawlers are as dangerous in the midst
of combat as they are in a tavern, and they wouldn't be caught dead without a libation for either
occasion.

**Elemental Kin**

**Class:** barbarian

**Modifies or Replaces:** Trap Sense

**Description:** Some barbarian tribes have strong ties to the elemental forces of nature.

**Fearsome Defender**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge

**Description:** These savage slaves feel little pain and exist only to rain terror down on the
enemies of their pitiless masters.

**Feral Gnasher**

**Class:** barbarian

**Modifies or Replaces:** Weapon/Armor Proficiency; Fast Movement; 2nd-level Rage Power; Trap Sense
1-5; Improved Uncanny Dodge

**Description:** (Goblin Only) Feral gnashers grow up in the wild, either raised by animals or
scraping by on their own, and soon learn to fend for themselves.

**Hurler**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement

**Description:** The hurler becomes skilled at throwing objects at their foes before closing in for
the kill.

**Invulnerable Rager**

**Class:** barbarian

**Modifies or Replaces:** Uncanny Dodge; Improved Uncanny Dodge;
[Damage Reduction](ref/rule/damage-reduction); Trap Sense

**Description:** Some barbarians learn to take whatever comes their way, shrugging off mortal wounds
with ease.

**Jungle Rager**

**Class:** barbarian

**Modifies or Replaces:** Uncanny Dodge; Trap Sense; Improved Uncanny Dodge;
[Damage Reduction](ref/rule/damage-reduction)

**Description:** A jungle rager can disappear from sight, strike from hiding, and use the
environment to shield herself from harm.

**Mounted Fury**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Improved Uncanny Dodge

**Description:** Many barbarian tribes are masters of the horse, teaching their members how to ride
from a young age.

**Numerian Liberator**

**Class:** barbarian

**Modifies or Replaces:** Class Skills; Uncanny Dodge; Improved Uncanny Dodge; Indomitable Will

**Description:** While many native Kellids oppose the Technic League and its espousal of foul alien
artifacts, the most stalwart and staunchly dedicated of these technophobic traditionalists refer to
themselves as Numerian liberators.

**Pack Hunter**

**Class:** barbarian

**Modifies or Replaces:** Rage Powers; Trap Sense; 6th-level Rage Power

**Description:** Pack hunter barbarians team up to hunt dangerous prey to feed, to protect their
camps, and as a rite of passage.

**Pack Rager**

**Class:** barbarian

**Modifies or Replaces:** 2nd, 6th, 10th, 14th, and 18th-level Rage Powers;
[Damage Reduction](ref/rule/damage-reduction)

**Description:** Barbarian _rages_ can be a thing of savage beauty, exhibiting a lethal grace. While
such uncontrolled displays of carnage often disregard group tactics, there are those barbarians
whose _rages_ inspire and spur on their allies during the ferocious dance of death.

**Raging Cannibal**

**Class:** barbarian

**Modifies or Replaces:** 2nd-level Rage Power; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge;
[Damage Reduction](ref/rule/damage-reduction)

**Description:** While savagery is not inherently evil, some barbaric cultures thrive on depravity
and welcome the act of feeding on their own kind.

**Savage Barbarian**

**Class:** barbarian

**Modifies or Replaces:** Trap Sense; [Damage Reduction](ref/rule/damage-reduction)

**Description:** The savage barbarian learns to avoid blows and toughen up their skin.

**Scarred Rager**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge

**Description:** The scarred rager believes each wound tells the tales of her prowess and bravery.

**Sea Reaver**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge

**Description:** Some sea reavers are no more than hunters of the open sea, while others are raiders
striking fear into coastal settlements within reach of the sea reavers' longships.

**Sharptooth**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Improved Uncanny Dodge; Trap Sense; 6th and
12th-level Rage Powers

**Description:** Coastal hunters and agents of the ocean's rage, sharptooth barbarians emulate the
greatest predators of the sea.

**Shoanti Burn Rider**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; 4th, 8th, 12th, 16th-level Rage
Powers; Improved Uncanny Dodge

**Description:** The Shoanti tribes who live in the Cinderlands have turned the deadly emberstorms
that plague the region into a rite of passage. A few who survive the experience begin to embrace the
adrenaline and surge of joy that comes from dancing along the edge of a whirling firestorm. These
thrill-seekers are known as burn riders, and their exploits are celebrated by all Shoanti.

**Superstitious**

**Class:** barbarian

**Modifies or Replaces:** Trap Sense; [Damage Reduction](ref/rule/damage-reduction)

**Description:** The superstitious barbarian is naturally distrusting, developing keen senses to
protect themselves from harm.

**Titan Mauler**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Uncanny Dodge; Trap Sense; Improved Uncanny Dodge;
Indomitable Will

**Description:** In lands overrun by giants, dragons, and other hulking beasts, entire fellowships
of barbarians hone tactics and traditions with one purpose - to bring low these massive foes.

**Totem Warrior**

**Class:** barbarian

**Modifies or Replaces:** None

**Description:** The totem warrior has a special totem that is the patron of her tribe.

**True Primitive**

**Class:** barbarian

**Modifies or Replaces:** Fast Movement; Trap Sense

**Description:** Isolated and xenophobic tribes that dwell in areas untouched by civilization often
see anything from cities and organized settlements as strange, dangerous, and decadent.

**Untamed Rager**

**Class:** barbarian

**Modifies or Replaces:** Uncanny Dodge; Trap Sense; Improved Uncanny Dodge;
[Damage Reduction](ref/rule/damage-reduction)

**Description:** There are no rules in the wild. Some barbarians enter combat with only victory in
mind and do anything in their power to achieve it.

**Wildborn**

**Class:** barbarian

**Modifies or Replaces:** Weapon/Armor Proficiency; Trap Sense; Rage Powers;
[Damage Reduction](ref/rule/damage-reduction)

**Description:** Some barbarians are born or bred outside the reach of civilization. These wildborn
fight and survive without ever seeing a forge or worked stone, and only dare a trip into the city
when no other option is available.

### Archetypes by Feature

|Archetype|Alignment|Class Skills|Damage Reduction|Fast Movement|Indomitable Will|Rage Powers|2nd-level Rage Power|4th-level Rage Power|6th-level Rage Power|8th-level Rage Power|10th-level Rage Power|12th-level Rage Power|14th-level Rage Power|16th-level Rage Power|18th-level Rage Power|20th-level Rage Power|Tireless Rage|Trap Sense|Uncanny Dodge|Improved Uncanny Dodge|Weapon/_wbr_Armor Proficiency|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Armored Hulk](ref/arc-barbarian/armored-hulk)||||X||||||||||||||X|X|X||
|[Beastkin Berserker](ref/arc-barbarian/beastkin-berserker)||||X||||X||X||X||||||||||
|[Breaker](ref/arc-barbarian/breaker)||||X||||||||||||||X||||
|[Brutal Pugilist](ref/arc-barbarian/brutal-pugilist)||||||||||||||||||X|X|X||
|[Brutish Swamper](ref/arc-barbarian/brutish-swamper)||X||X|||||X|||||||||X|X|X||
|[Cave Dweller](ref/arc-barbarian/cave-dweller)||X|X|X||||||||||||||X||||
|[Deepwater Rager](ref/arc-barbarian/deepwater-rager)||||X|X||||||||||||X||X|X||
|[Drunken Brute](ref/arc-barbarian/drunken-brute)||||X||||||||||||||||||
|[Drunken Rager](ref/arc-barbarian/drunken-rager)||||X||||||||X||||||X|X|X||
|[Elemental Kin](ref/arc-barbarian/elemental-kin)||||||||||||||||||X||||
|[Fearsome Defender](ref/arc-barbarian/fearsome-defender)||||X||||||||||||||X|X|X||
|[Feral Gnasher](ref/arc-barbarian/feral-gnasher)||||X|||X|||||||||||X||X|X|
|[Hurler](ref/arc-barbarian/hurler)||||X||||||||||||||||||
|[Invulnerable Rager](ref/arc-barbarian/invulnerable-rager)|||X|||||||||||||||X|X|X||
|[Jungle Rager](ref/arc-barbarian/jungle-rager)|||X|||||||||||||||X|X|X||
|[Mounted Fury](ref/arc-barbarian/mounted-fury)||||X|||||||||||||||X|X||
|[Numerian Liberator](ref/arc-barbarian/numerian-liberator)||X|||X||||||||||||||X|X||
|[Pack Hunter](ref/arc-barbarian/pack-hunter)||||||X|||X|||||||||X||||
|[Pack Rager](ref/arc-barbarian/pack-rager)|||X||||X||X||X||X||X|||||||
|[Raging Cannibal](ref/arc-barbarian/raging-cannibal)|||X||||X|||||||||||X|X|X||
|[Savage Barbarian](ref/arc-barbarian/savage-barbarian)|||X|||||||||||||||X||||
|[Scarred Rager](ref/arc-barbarian/scarred-rager)||||X||||||||||||||X|X|X||
|[Sea Reaver](ref/arc-barbarian/sea-reaver)||||X||||||||||||||X|X|X||
|[Sharptooth](ref/arc-barbarian/sharptooth)||||X|||||X|||X||||||X|X|X||
|[Shoanti Burn Rider](ref/arc-barbarian/shoanti-burn-rider)||||X||||X||X||X||X||||X|X|X||
|[Superstitious](ref/arc-barbarian/superstitious)|||X|||||||||||||||X||||
|[Titan Mauler](ref/arc-barbarian/titan-mauler)||||X|X|||||||||||||X|X|X||
|Totem Warrior||||||||||||||||||||||
|[True Primitive](ref/arc-barbarian/true-primitive)||||X||||||||||||||X||||
|[Untamed Rager](ref/arc-barbarian/untamed-rager)|||X|||||||||||||||X|X|X||
|[Wildborn](ref/arc-barbarian/wildborn)|||X|||X||||||||||||X|||X|

### Favored Class Bonuses

_The favored class options for unchained\_barbarian are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
