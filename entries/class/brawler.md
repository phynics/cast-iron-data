+++
id = "ref/class/brawler"
kind = "class"
title = "Brawler"
aon = "ClassDisplay.aspx?ItemName=Brawler"
source_ids = ["advanced-class-guide", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brawler", path = "json/classes8.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "23"
[[sources]]
publication = "chronicle-of-legends"
page = "28"

[fields]
kind = "class"
class_type = "hybrid"
hit_die = "d10"
skill_ranks = "4 + Int modifier"
features = [
  { anchor = "brawler-s-cunning", level = 1 },
  { anchor = "martial-flexibility", level = 1 },
  { anchor = "martial-training", level = 1 },
  { anchor = "unarmed-strike", level = 1 },
  { anchor = "bonus-combat-feats", level = 2 },
  { anchor = "brawler-s-flurry", level = 2 },
  { anchor = "maneuver-training", level = 3 },
  { anchor = "ac-bonus", level = 4 },
  { anchor = "knockout", level = 4 },
  { anchor = "brawler-s-strike", level = 5 },
  { anchor = "close-weapon-mastery", level = 5 },
  { anchor = "awesome-blow", level = 16 },
  { anchor = "improved-awesome-blow", level = 20 },
]
+++

Deadly even with nothing in her hands, a brawler eschews using the fighter's heavy armor and the
monk's mysticism, focusing instead on perfecting many styles of brutal unarmed combat. Versatile,
agile, and able to adapt to most enemy attacks, a brawler's body is a powerful weapon.

**Role:** Brawlers are maneuverable and well suited for creating flanking situations or dealing with
lightly armored enemies, as well as quickly adapting to a rapidly changing battlefield.

**Alignment:** Any

**Hit Die:** d10

**Parent Class(es):** [Fighter](ref/class/fighter) and [monk](ref/class/monk).

**Starting Wealth:** 3d6 × 10 gp (average 105 gp)

**Skill Points per Level:** 4 + Int modifier

**Class Skills (Str):** Climb, Swim

**Class Skills (Dex):** Acrobatics, Escape Artist, Ride

**Class Skills (Int):** Craft (any), Knowledge (dungeoneering), Knowledge (local)

**Class Skills (Wis):** Perception, Profession (any), Sense Motive

**Class Skills (Cha):** Handle Animal, Intimidate

### Class Features

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|Unarmed Damage|
| --- | --- | --- | --- | --- | --- | --- |
|1st|+1|+2|+2|+0|Brawler's cunning, martial flexibility, martial training, unarmed strike|1d6|
|2nd|+2|+3|+3|+0|Bonus combat feat, brawler's flurry (Two-Weapon Fighting)|1d6|
|3rd|+3|+3|+3|+1|Maneuver training 1|1d6|
|4th|+4|+4|+4|+1|AC bonus +1, knockout 1/day|1d8|
|5th|+5|+4|+4|+1|Bonus combat feat, brawler's strike (magic), close weapon mastery|1d8|
|6th|+6/+1|+5|+5|+2|Martial flexibility (swift action)|1d8|
|7th|+7/+2|+5|+5|+2|Maneuver training 2|1d8|
|8th|+8/+3|+6|+6|+2|Bonus combat feat, brawler's flurry (Improved Two-Weapon Fighting)|1d10|
|9th|+9/+4|+6|+6|+3|AC bonus +2, brawler's strike (cold iron and silver)|1d10|
|10th|+10/+5|+7|+7|+3|Martial flexibility (free action), knockout 2/day|1d10|
|11th|+11/+6/+1|+7|+7|+3|Bonus combat feat, maneuver training 3|1d10|
|12th|+12/+7/+2|+8|+8|+4|Brawler's strike (alignment), martial flexibility (immediate action)|2d6|
|13th|+13/+8/+3|+8|+8|+4|AC bonus +3|2d6|
|14th|+14/+9/+4|+9|+9|+4|Bonus combat feat|2d6|
|15th|+15/+10/+5|+9|+9|+5|Brawler's flurry (Greater Two-Weapon Fighting), maneuver training 4|2d6|
|16th|+16/+11/+6/+1|+10|+10|+5|Awesome blow, knockout 3/day|2d8|
|17th|+17/+12/+7/+2|+10|+10|+5|Bonus combat feat, brawler's strike (adamantine)|2d8|
|18th|+18/+13/+8/+3|+11|+11|+6|AC bonus +4|2d8|
|19th|+19/+14/+9/+4|+11|+11|+6|Maneuver training 5|2d8|
|20th|+20/+15/+10/+5|+12|+12|+6|Bonus combat feat, improved awesome blow, martial flexibility (any number)|2d10|

### Class Features {#class-features}

The following are the class features of the brawler.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

A brawler is proficient with all simple weapons plus the handaxe, short sword, and weapons from the
close [fighter weapon group](ref/ability/weapon-groups). She is proficient with light armor and
shields (except tower shields).

#### Brawler's Cunning (Ex) {#brawler-s-cunning}

If the brawler's Intelligence score is less than 13, it counts as 13 for the purpose of meeting the
prerequisites of combat feats.

#### Martial Flexibility (Ex) {#martial-flexibility}

A brawler can take a move action to gain the benefit of a combat feat she doesn't possess. This
effect lasts for 1 minute. The brawler must meet all the feat's prerequisites. She may use this
ability a number of times per day equal to 3 + 1/2 her brawler level (minimum 1).

The brawler can use this ability again before the duration expires in order to replace the previous
combat feat with another choice.

If a combat feat has a daily use limitation (such as [Stunning Fist](ref/feat/stunning-fist)), any
uses of that combat feat while using this ability count toward that feat's daily limit.

At 6th level, a brawler can use this ability to gain the benefit of two combat feats at the same
time. She may select one feat as a swift action or two feats as a move action. She may use one of
these feats to meet a prerequisite of the second feat; doing so means that she cannot replace a feat
currently fulfilling another's prerequisite without also replacing those feats that require it. Each
individual feat selected counts toward her daily uses of this ability.

At 10th level, a brawler can use this ability to gain the benefit of three combat feats at the same
time. She may select one feat as a free action, two feats as a swift action, or three feats as a
move action. She may use one of the feats to meet a prerequisite of the second and third feats, and
use the second feat to meet a prerequisite of the third feat. Each individual feat selected counts
toward her daily uses of this ability.

At 12th level, a brawler can use this ability to gain the benefit of one combat feat as an immediate
action or three combat feats as a swift action. Each individual feat selected counts toward her
daily uses of this ability.

At 20th level, a brawler can use this ability to gain the benefit of any number of combat feats as a
swift action. Each feat selected counts toward her daily uses of this ability.

#### Martial Training (Ex) {#martial-training}

At 1st level, a brawler counts her total brawler levels as both fighter levels and monk levels for
the purpose of qualifying for feats. She also counts as both a fighter and a monk for feats and
magic items that have different effects based on whether the character has levels in those classes
(such as Stunning Fist and a _[monk's robe](ref/magic-wondrous/monks-robe)_). This ability does not
automatically grant feats normally granted to fighters and monks based on class level, namely
Stunning Fist.

#### Unarmed Strike {#unarmed-strike}

At 1st level, a brawler gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus
feat. A brawler may attack with fists, elbows, knees, and feet. This means that a brawler may make
unarmed strikes with her hands full. A brawler applies her full Strength modifier (not half) on
damage rolls for all her unarmed strikes.

Usually, a brawler's unarmed strikes deal lethal damage, but she can choose to deal nonlethal damage
instead with no penalty on her attack roll. She has the same choice to deal lethal or nonlethal
damage while grappling.

A brawler's unarmed strike is treated as both a manufactured weapon and a natural weapon for the
purpose of spells and effects that modify either manufactured weapons or natural weapons.

A brawler also deals more damage with her unarmed strikes than others, as shown on Table 1–5:
Brawler. The unarmed damage values listed on that table are for Medium brawlers. A Small brawler
deals less damage than the amount given there with her unarmed attacks, while a Large brawler deals
more damage; see the following table.

|Level|Damage (Small Brawler)|Damage (Large Brawler)|
| --- | --- | --- |
|1st–3rd|1d4|1d8|
|4th–7th|1d6|2d6|
|8th–11th|1d8|2d8|
|12th–15th|1d10|3d6|
|16th–19th|2d6|3d8|
|20th|2d8|4d8|

#### Bonus Combat Feats {#bonus-combat-feats}

At 2nd level and every 3 levels thereafter, a brawler gains a bonus combat feat in addition to those
gained from normal advancement. These bonus feats must be ones that affect or improve her defenses
or melee attacks. The brawler must meet the prerequisites of the selected bonus combat feat.

Upon reaching 5th level and every 3 levels thereafter, a brawler can choose to learn a new bonus
combat feat in place of a bonus combat feat she has already learned. In effect, the brawler loses
the bonus combat feat in exchange for the new one. The old feat cannot be one that was used as a
prerequisite for another feat, prestige class, or other ability. A brawler can only change one feat
at any given level, and must choose whether or not to swap the feat at the time she gains a new
bonus combat feat for the level.

#### Brawler's Flurry (Ex) {#brawler-s-flurry}

Starting at 2nd level, a brawler can make a brawler's flurry as a full-attack action. When doing so,
a brawler has the [Two-Weapon Fighting](ref/feat/two-weapon-fighting) feat when attacking with any
combination of unarmed strikes, weapons from the close fighter weapon group, or weapons with the
"monk" special feature. She does not need to use two different weapons to use this ability.

A brawler applies her full Strength modifier to her damage rolls for all attacks made with brawler's
flurry, whether the attacks are made with an off-hand weapon or a weapon wielded in both hands. A
brawler can substitute [disarm](ref/rule/disarm), [sunder](ref/rule/sunder), and
[trip](ref/rule/trip) combat maneuvers for unarmed attacks as part of brawler's flurry. A brawler
with natural weapons can't use such weapons as part of brawler's flurry, nor can she make natural
weapon attacks in addition to her brawler's flurry attacks.

At 8th level, the brawler gains use of the
[Improved Two-Weapon Fighting](ref/feat/improved-two-weapon-fighting) feat when using brawler's
flurry. At 15th level, she gains use of the
[Greater Two-Weapon Fighting](ref/feat/greater-two-weapon-fighting) feat when using brawler's
flurry.

#### Maneuver Training (Ex) {#maneuver-training}

At 3rd level, a brawler can select one [combat maneuver](ref/rule/combat-maneuvers) to receive
additional training. She gains a +1 bonus on combat maneuver checks when performing that combat
maneuver and a +1 bonus to her CMD when defending against that maneuver.

At 7th level and every 4 levels thereafter, the brawler becomes further trained in another combat
maneuver, gaining the above +1 bonus combat maneuver checks and to CMD. In addition, the bonuses
granted by all previous maneuver training increase by 1 each. (For example, if a brawler chooses
grapple at 3rd level and sunder at 7th level, her bonuses to grapple are +2 and bonuses to sunder
are +1. If she then chooses bull rush upon reaching 11th level, her bonuses to grapple are +3, to
sunder are +2, and to bull rush are +1.)

#### AC Bonus (Ex) {#ac-bonus}

At 4th level, when a brawler wears light or no armor, she gains a +1 dodge bonus to AC and CMD. This
bonus increases by 1 at 9th, 13th, and 18th levels.

These bonuses to AC apply against touch attacks. She loses these bonuses while immobilized or
[helpless](ref/misc/helpless), wearing medium or heavy armor, or carrying a medium or heavy load.

#### Knockout (Ex) {#knockout}

At 4th level, once per day a brawler can unleash a devastating attack that can instantly knock a
target unconscious. She must announce this intent before making her attack roll. If the brawler hits
and the target takes damage from the blow, the target must succeed at a Fortitude saving throw (DC =
10 + 1/2 the brawler's level + the higher of the brawler's Strength or Dexterity modifier) or fall
unconscious for 1d6 rounds. Each round on its turn, the unconscious target may attempt a new saving
throw to end the effect as a full-round action that does not provoke attacks of opportunity.
Creatures immune to critical hits or nonlethal damage are immune to this ability. At 10th level, the
brawler may use this ability twice per day; at 16th level, she may use it three times per day.

#### Brawler's Strike (Ex) {#brawler-s-strike}

At 5th level, a brawler's unarmed strikes are treated as magic weapons for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). At 9th level, her unarmed attacks are also treated as
cold iron and silver for the purpose of overcoming [damage reduction](ref/rule/damage-reduction). At
12th level, she chooses one alignment component: chaotic, evil, good, or lawful; her unarmed strikes
also count as this alignment for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). (This alignment component cannot be the opposite of
the brawler's actual alignment, such as a good brawler choosing evil strikes.) At 17th level, her
unarmed attacks are also treated as [adamantine](ref/eq-material/adamantine) weapons for the purpose
of overcoming [damage reduction](ref/rule/damage-reduction) and bypassing
[hardness](ref/umr/hardness).

#### Close Weapon Mastery (Ex) {#close-weapon-mastery}

At 5th level, a brawler's damage with close weapons increases. When wielding a close weapon, she
uses the unarmed strike damage of a brawler 4 levels lower instead of the base damage for that
weapon (for example, a 5th-level Medium brawler wielding a
[punching dagger](ref/eq-weapon/punching-dagger) deals 1d6 points of damage instead of the weapon's
normal 1d4). If the weapon normally deals more damage than this, its damage is unchanged. This
ability does not affect any other aspect of the weapon. The brawler can decide to use the weapon's
base damage instead of her adjusted unarmed strike damage—this must be declared before the attack
roll is made.

#### Awesome Blow (Ex) {#awesome-blow}

At 16th level, the brawler can as a standard action perform an awesome blow combat maneuver against
a corporeal creature of her size or smaller. If the combat maneuver check succeeds, the opponent
takes damage as if the brawler hit it with the close weapon she is wielding or an unarmed strike, it
is knocked flying 10 feet in a direction of the brawler's choice, and it falls
[prone](ref/rule/prone). The brawler can only push the opponent in a straight line, and the opponent
can't move closer to the brawler than the square it started in. If an obstacle prevents the
completion of the opponent's move, the opponent and the obstacle each take 1d6 points of damage, and
the opponent is knocked prone in the space adjacent to the obstacle. (Unlike the
[Awesome Blow](ref/feat/awesome-blow) monster feat, the brawler can be of any size to use this
ability.)

#### Improved Awesome Blow (Ex) {#improved-awesome-blow}

At 20th level, the brawler can use her awesome blow ability as an attack rather than as a standard
action. She may use it on creatures of any size. If the maneuver roll is a natural 20, the brawler
can immediately attempt to confirm the critical by rolling another combat maneuver check with all
the same modifiers as the one just rolled; if the confirmation roll is successful, the attack deals
double damage, and the damage from hitting an obstacle (if any) is also doubled.

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

**Perfect Warrior (Ex)**

At 20th level, the brawler has reached the highest levels of her art. The brawler's _maneuver
training_ increases by 2 and her dodge bonus to AC improves by 2. This replaces the 20th-level
improvement to _martial flexibility._

**Also available:** Old Dog, New Tricks

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

**Battle Dancer**

**Class:** brawler

**Modifies or Replaces:** Class Skills; Armor Proficiencies; Brawler's Cunning; Brawler's Flurry; AC
Bonus; Knockout

**Description:** Battle dancers practice a martial art that emphasizes constant motion

**Bouncer**

**Class:** brawler

**Modifies or Replaces:** Martial Flexibility; 2nd-level Bonus Feat; Close Weapon Mastery

**Description:** Some taverns employ bouncers to keep out undesirables or for when their customers
get too rowdy.

**Constructed Pugilist**

**Class:** brawler

**Modifies or Replaces:** Class Skills; Martial Flexibility; Bonus Combat Feats

**Description:** Brawlers that develop combat skills that use their prostheses so they always have a
weapon at hand

**Exemplar**

**Class:** brawler

**Modifies or Replaces:** Unarmed Strike; Close Weapon Mastery; Maneuver Training; AC Bonus;
Brawler's Strike

**Description:** A versatile soldier who inspires her companions with her fighting prowess, an
exemplar is at home on the front lines of battles anywhere.

**Feral Striker**

**Class:** brawler

**Modifies or Replaces:** Martial Flexibility

**Description:** A feral striker taps into a reservoir of druidic power hidden inside herself,
allowing her to take animalistic characteristics.

**Hinyasi**

**Class:** brawler

**Modifies or Replaces:** Armor Proficiencies; 2nd-level Bonus Feat; Knockout; Close Weapon Mastery

**Description:** The hinyasi's martial traditions are centered on the use of farming tools and on
other improvised weapons.

**Living Avalanche**

**Class:** brawler

**Modifies or Replaces:** 2nd and 5th-level Bonus Feats; Maneuver Training; AC Bonus; Awesome Blow;
Improved Awesome Blow

**Description:** When a living avalanche is on the move, no one can stand in her way.

**Mutagenic Mauler**

**Class:** brawler

**Modifies or Replaces:** Martial Flexibility; AC Bonus

**Description:** Not content with perfecting her body with natural methods, a mutagenic mauler
resorts to alchemy to unlock the primal beast within.

**Shield Champion**

**Class:** brawler

**Modifies or Replaces:** Weapon/Armor Proficiencies; Maneuver Training; Brawler's Strike

**Description:** Stalwart in battle, a shield champion has perfected an entire martial discipline
relying on only her hand-to-hand fighting skills and her ever-present shield.

**Snakebite Striker**

**Class:** brawler

**Modifies or Replaces:** Class Skills; Martial Flexibility; 3rd, 7th, 11th, and 19th-level Maneuver
Training

**Description:** With her lightning quickness and guile, a snakebite striker keeps her foes'
attention focused on her, because any one of her feints might be an actual attack.

**Steel-Breaker**

**Class:** brawler

**Modifies or Replaces:** Class Skills; Brawler's Strike; Maneuver Training

**Description:** The steel-breaker studies destruction and practices it as an art form.

**Strangler**

**Class:** brawler

**Modifies or Replaces:** Class Skills; Brawler's Flurry; AC Bonus; Knockout; Awesome Blow; Improved
Awesome Blow

**Description:** A strangler is trained to choke the life out of her victims with her vise-like
grip.

**Strong-Side Boxer**

**Class:** brawler

**Modifies or Replaces:** AC Bonus; Maneuver Training; Close Weapon Mastery

**Description:** A strong-side boxer employs a unique fighting style that incorporates a rope or
cord wound around her hand.

**Turfer**

**Class:** brawler

**Modifies or Replaces:** Maneuver Training; Knockout

**Description:** A turfer has a mastery over particular types of terrain.

**Ulfen Beast-Wrestler**

**Class:** brawler

**Modifies or Replaces:** Maneuver Training; AC Bonus

**Description:** For these mighty grapplers, wrestling normal opponents has lost its challenge -
they seek greater targets for glory.

**Venomfist**

**Class:** brawler

**Modifies or Replaces:** Unarmed Strike; Knockout; Close Weapon Mastery

**Description:** Thanks to alchemical experiments and rigorous study of venomous creatures, a
venomfist has toxic unarmed strikes.

**Verdant Grappler**

**Class:** brawler

**Modifies or Replaces:** 2nd and 11th-level Bonus Feats; Maneuver Training; Close Weapon Mastery

**Description:** By accepting spirits of nature into her soul, a verdant grappler can entangle her
foes with tangled undergrowth.

**Wild Child**

**Class:** brawler

**Modifies or Replaces:** Class Skills; Bonus Combat Feats; Close Weapon Mastery; Maneuver Training

**Description:** The wild child works with his sworn animal friend to conquer the challenges that
lay before them.

**Winding Path Renegade**

**Class:** brawler

**Modifies or Replaces:** 2nd, 8th, 14th-level Bonus Feat; AC Bonus

**Description:** Winding path renegades studied at the Houses of Perfection in Jalmeray, but while
they grasped the mechanical aspects of the forms, they lacked the mental discipline required by the
masters of the school.

### Archetypes by Feature

|Archetype|AC Bonus|Armor Proficiency|Awesome Blow|Improved Awesome Blow|Bonus Feats|2nd-level Bonus Feat|5th-level Bonus Feat|8th-level Bonus Feat|11th-level Bonus Feat|14th-level Bonus Feat|Brawler's Cunning|Brawler's Flurry|Brawler's Strike|Class Skills|Close Weapon Mastery|Knockout|Maneuver Training|3rd-level Maneuver Training|7th-level Maneuver Training|11th-level Maneuver Training|19th-level Maneuver Training|Martial Flexibility|Unarmed Strike|Weapon Proficiency|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Battle Dancer](ref/arc-brawler/battle-dancer)|X|X|||||||||X|X||X||X|||||||||
|[Bouncer](ref/arc-brawler/bouncer)||||||X|||||||||X|||||||X|||
|[Constructed Pugilist](ref/arc-brawler/constructed-pugilist)|||||X|||||||||X||||||||X|||
|[Exemplar](ref/arc-brawler/exemplar)|X||||||||||||X||X||X||||||X||
|[Feral Striker](ref/arc-brawler/feral-striker)||||||||||||||||||||||X|||
|[Hinyasi](ref/arc-brawler/hinyasi)||X||||X|||||||||X|X|||||||||
|[Living Avalanche](ref/arc-brawler/living-avalanche)|X||X|X||X|X||||||||||X||||||||
|[Mutagenic Mauler](ref/arc-brawler/mutagenic-mauler)|X|||||||||||||||||||||X|||
|[Shield Champion](ref/arc-brawler/shield-champion)||X|||||||||||X||||X|||||||X|
|[Snakebite Striker](ref/arc-brawler/snakebite-striker)||||||||||||||X||||X|X|X|X|X|||
|[Steel-Breaker](ref/arc-brawler/steel-breaker)|||||||||||||X|X|||X||||||||
|[Strangler](ref/arc-brawler/strangler)|X||X|X||||||||X||X||X|||||||||
|[Strong-Side Boxer](ref/arc-brawler/strong-side-boxer)|X||||||||||||||X||X||||||||
|[Turfer](ref/arc-brawler/turfer)||||||||||||||||X|X||||||||
|[Ulfen Beast-Wrestler](ref/arc-brawler/ulfen-beast-wrestler)|X||||||||||||||||X||||||||
|[Venomfist](ref/arc-brawler/venomfist)|||||||||||||||X|X|||||||X||
|[Verdant Grappler](ref/arc-brawler/verdant-grappler)||||||X|||X||||||X||X||||||||
|[Wild Child](ref/arc-brawler/wild-child)|||||X|||||||||X|X||X||||||||
|[Winding Path Renegade](ref/arc-brawler/winding-path-renegade)|X|||||X||X||X|||||||||||||||

### Favored Class Bonuses

_The favored class options for brawler are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
