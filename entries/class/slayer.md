+++
id = "ref/class/slayer"
kind = "class"
title = "Slayer"
aon = "ClassDisplay.aspx?ItemName=Slayer"
source_ids = ["advanced-class-guide", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "slayer", path = "json/classes4.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "53"
[[sources]]
publication = "chronicle-of-legends"
page = "28, 30"

[fields]
kind = "class"
class_type = "hybrid"
hit_die = "d10"
skill_ranks = "6 + Int modifier"
features = [
  { anchor = "studied-target", level = 1 },
  { anchor = "track", level = 1 },
  { anchor = "slayer-talents", level = 2 },
  { anchor = "sneak-attack", level = 3 },
  { anchor = "stalker", level = 7 },
  { anchor = "advanced-talents", level = 10 },
  { anchor = "swift-tracker", level = 11 },
  { anchor = "slayer-s-advance", level = 13 },
  { anchor = "quarry", level = 14 },
  { anchor = "improved-quarry", level = 19 },
  { anchor = "master-slayer", level = 20 },
]
+++

Skilled at tracking down targets, slayers are consummate hunters, living for the chase and the
deadly stroke that brings it to a close. Slayers spend most of their time honing their weapon
skills, studying the habits and anatomy of foes, and practicing combat maneuvers.

**Role:** The slayer is elusive, and good at finding the opportune time and location to strike.
Combining the deadliest talents of rangers and rogues, a slayer's abilities are all about getting
into combat, dealing with a target, and then getting back out again.

**Alignment:** Any

**Hit Die:** d10

**Parent Class(es):** [Ranger](ref/class/ranger) and [rogue](ref/class/rogue).

**Starting Wealth:** 5d6 × 10 gp (average 175 gp)

**Skill Points per Level:** 6 + Int modifier

**Class Skills (Str):** Climb, Swim

**Class Skills (Dex):** Acrobatics, Ride, Stealth

**Class Skills (Int):** Craft (any), Knowledge (dungeoneering), Knowledge (geography), Knowledge
(local)

**Class Skills (Wis):** Heal, Perception, Profession (any), Sense Motive, Survival

**Class Skills (Cha):** Bluff, Disguise, Intimidate

### Class Features

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|
| --- | --- | --- | --- | --- | --- |
|1st|+1|+2|+2|+0|1st studied target, track|
|2nd|+2|+3|+3|+0|Slayer talent|
|3rd|+3|+3|+3|+1|Sneak attack +1d6|
|4th|+4|+4|+4|+1|Slayer talent|
|5th|+5|+4|+4|+1|2nd studied target|
|6th|+6/+1|+5|+5|+2|Slayer talent, sneak attack +2d6|
|7th|+7/+2|+5|+5|+2|Stalker|
|8th|+8/+3|+6|+6|+2|Slayer talent|
|9th|+9/+4|+6|+6|+3|Sneak attack +3d6|
|10th|+10/+5|+7|+7|+3|3rd studied target, advanced talents, slayer talent|
|11th|+11/+6/+1|+7|+7|+3|Swift tracker|
|12th|+12/+7/+2|+8|+8|+4|Slayer talent, sneak attack +4d6|
|13th|+13/+8/+3|+8|+8|+4|Slayer's advance 1/day|
|14th|+14/+9/+4|+9|+9|+4|Quarry, slayer talent|
|15th|+15/+10/+5|+9|+9|+5|4th studied target, sneak attack +5d6|
|16th|+16/+11/+6/+1|+10|+10|+5|Slayer talent|
|17th|+17/+12/+7/+2|+10|+10|+5|Slayer's advance 2/day|
|18th|+18/+13/+8/+3|+11|+11|+6|Slayer talent, sneak attack +6d6|
|19th|+19/+14/+9/+4|+11|+11|+6|Improved quarry|
|20th|+20/+15/+10/+5|+12|+12|+6|5th studied target, master slayer, slayer talent|

### Class Features {#class-features}

The following are the class features of the slayer.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

A slayer is proficient with all simple and martial weapons, as well as with light armor, medium
armor, and shields (except tower shields).

#### Studied Target (Ex) {#studied-target}

A slayer can study an opponent he can see as a move action. The slayer then gains a +1 bonus on
Bluff, Knowledge, Perception, Sense Motive, and Survival checks attempted against that opponent, and
a +1 bonus on weapon attack and damage rolls against it. The DCs of slayer class abilities against
that opponent increase by 1. A slayer can only maintain these bonuses against one opponent at a
time; these bonuses remain in effect until either the opponent is dead or the slayer studies a new
target.

If a slayer deals sneak attack damage to a target, he can study that target as an immediate action,
allowing him to apply his studied target bonuses against that target (including to the normal weapon
damage roll).

At 5th, 10th, 15th, and 20th levels, the bonuses on weapon attack rolls, damage rolls, and skill
checks and to slayer DCs against a studied target increase by 1. In addition, at each such interval,
the slayer is able to maintain these bonuses against an additional studied target at the same time.
The slayer may discard this connection to a studied target as a free action, allowing him to study
another target in its place.

At 7th level, a slayer can study an opponent as a move or swift action.

#### Track (Ex) {#track}

A slayer adds 1/2 his level (minimum 1) to Survival skill checks made to follow tracks.

#### Slayer Talents {#slayer-talents}

As a slayer gains experience, he learns a number of talents that aid him and confound his foes.
Starting at 2nd level and every 2 levels thereafter, a slayer gains one slayer talent. Unless
otherwise noted, a slayer cannot select an individual talent more than once.

Talents marked with an asterisk add effects to a slayer's sneak attack. Only one of these talents
can be applied to an individual attack, and the decision of which to use must be made before the
attack roll is made.

- [Deadly Range (Ex)](ref/slayertalent/deadly-range)
- [Foil Scrutiny](ref/slayertalent/foil-scrutiny)
- [Poison Use (Ex)](ref/slayertalent/poison-use)
- [Ranger Combat Style (Ex)](ref/slayertalent/ranger-combat-style)
- [Rogue Talent](ref/slayertalent/rogue-talent)
- [Slowing Strike (Ex)](ref/slayertalent/slowing-strike)
- [Trapfinding](ref/slayertalent/trapfinding)

#### Sneak Attack {#sneak-attack}

At 3rd level, if a slayer catches an opponent unable to defend itself effectively from his attack,
he can strike a vital spot for extra damage. The slayer's attack deals extra damage anytime his
target would be denied a Dexterity bonus to AC (whether the target actually has a Dexterity bonus or
not), or when the slayer flanks his target. This additional damage is 1d6 at 3rd level, and
increases by 1d6 every 3 levels thereafter. Should the slayer score a critical hit with a
[sneak attack](ref/ability/sneak-attack), this additional damage is not multiplied. Ranged attacks
can count as sneak attacks only if the target is within 30 feet.

With a weapon that deals nonlethal damage (like a [sap](ref/eq-weapon/sap),
[whip](ref/eq-weapon/whip), or unarmed strike), a slayer can make a sneak attack that deals
nonlethal damage instead of lethal damage. He cannot use a weapon that deals lethal damage to deal
nonlethal damage in a sneak attack, not even with the usual -4 penalty.

The slayer must be able to see the target well enough to pick out a vital spot and must be able to
reach such a spot. A slayer cannot use sneak attack while striking a creature with
[concealment](ref/rule/concealment).

#### Stalker (Ex) {#stalker}

At 7th level, a slayer gains his studied target bonus on Disguise, Intimidate, and Stealth checks
against his studied opponent.

#### Advanced Talents {#advanced-talents}

At 10th level and every 2 levels thereafter, a slayer can select one of the following advanced
talents in place of a slayer talent.

- [Assassinate (Ex)](ref/slayertalent/assassinate)
- [Rogue and Ninja Advanced Talents](ref/slayertalent/rogue-and-ninja-advanced-talents)
- [Woodland Stride (Ex)](ref/slayertalent/woodland-stride)

#### Swift Tracker (Ex) {#swift-tracker}

At 11th level, a slayer can move at his normal speed while using Survival to follow tracks without
taking the normal -5 penalty. When moving at up to twice his normal speed while tracking, he takes
only a -10 penalty instead of the normal -20.

#### Slayer's Advance (Ex) {#slayer-s-advance}

At 13th level, a slayer can once per day move up to twice his base speed as a move action. He may
use Stealth as part of this movement, but takes a -10 penalty to his check for doing so. At 17th
level, he can do this twice per day.

#### Quarry (Ex) {#quarry}

At 14th level, a slayer can as a standard action denote one target within his line of sight as his
quarry. Whenever he is following the tracks of his quarry, a slayer can take 10 on his Survival
skill checks while moving at normal speed, without penalty. In addition, he gains a +2 insight bonus
on attack rolls made against his quarry, and all critical threats against his quarry are
automatically confirmed. A slayer can have no more than one quarry at a time, and the target must be
selected as a studied target. He can dismiss this effect at any time as a free action, but he cannot
select a new quarry target for 24 hours. If the slayer sees proof that his quarry is dead, he can
select a new quarry target after 1 hour.

#### Improved Quarry (Ex) {#improved-quarry}

At 19th level, the slayer's ability to hunt his quarry improves. He can now select a quarry as a
free action, and can now take 20 while using Survival to track his quarry, while moving at normal
speed without penalty. His insight bonus to attack his quarry increases to +4. If his quarry is
killed or dismissed, he can select a new one after 10 minutes have passed.

#### Master Slayer (Ex) {#master-slayer}

At 20th level, the slayer becomes a master at capturing or killing his studied targets. As a
standard action, he can make a single attack against a studied target at his full attack bonus,
choosing one of the following effects: kill, knock [unconscious](ref/misc/unconscious) for 1d4
hours, or [paralyze](ref/rule/paralyzed) for 2d6 rounds. If the attack succeeds, the target takes
damage normally and must succeed at a Fortitude saving throw or suffer the additional effect. The DC
for this save is 10 + 1/2 the slayer's level + the slayer's Intelligence modifier. Whether or not
the target succeeds, it cannot be targeted by this ability again (by any slayer) for 24 hours.

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

**Against the Odds (Ex)**

At 20th level, the slayer is used to fighting when the numbers are not in his favor. When the slayer
uses _studied target,_ he can study up to two additional foes with the same action.

**Also available:** The Right Spot

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

**Ankou's Shadow**

**Class:** slayer

**Modifies or Replaces:** Studied Target; Stalker; Quarry; Improved Quarry

**Description:** Ankou's shadow practice the deadliest skills of the First World's most feared
enforcers: terrifying, winged fey assassins dispatched by the greatest lords of the First World to
eliminate their rivals

**Avalancher**

**Class:** slayer

**Modifies or Replaces:** Studied Target; Track; Swift Tracker; Stalker; Quarry; Improved Quarry;
Master Slayer

**Description:** Avalanchers attack from overhead cliffs and mesas like a landslide of arrows and
blades.

**Bloody Jake**

**Class:** slayer

**Modifies or Replaces:** Alignment; Weapon and Armor Proficiency; Studied Target; 4th, 6th, 8th,
12th, 16th-level Slayer Talents; Swift Tracker; Slayer's Advance

**Description:** Bloody jakes are cruel backwoods folk who prey upon their country cousins while
terrorizing civilized people who venture into their rural range.

**Bounty Hunter**

**Class:** slayer

**Modifies or Replaces:** Weapon/Armor Proficiencies; 2nd, 6th, and 10th-level Slayer Talents

**Description:** Whether tasked with bringing in wanted criminals or paid to drag debtors back to
their loan sharks, bounty hunters are valued for their ability to capture targets alive.

**Butterfly Blade**

**Class:** slayer

**Modifies or Replaces:** Studied Target; Track; Sneak Attack; Stalker; Swift Tracker; Quarry;
Improved Quarry

**Description:** Butterfly blades work in the shadows, eliminating threats with their namesake
weapons and intimidating troublesome nobles.

**Cleaner**

**Class:** slayer

**Modifies or Replaces:** Track; 4th-level Slayer Talent; Stalker

**Description:** A cleaner is responsible for destroying or removing incriminating evidence from a
crime scene, disposing of corpses and eliminating witnesses to make a crime look like an accident or
a mere disappearance.

**Covenbane**

**Class:** slayer

**Modifies or Replaces:** Track; 2nd-level Slayer Talent; Stalker; Swift Tracker

**Description:** Covenbane slayers are scarred by arcane magic at a young age, and that resonance
gives them supernatural insight into the psychic bonds between others.

**Cutthroat**

**Class:** slayer

**Modifies or Replaces:** Class Skills; Track; 2nd and 6th-level Slayer Talents

**Description:** Street-smart and extremely resourceful, cutthroats stalk city streets and
alleyways, preying on those unfortunate enough to catch their eye.

**Deliverer**

**Class:** slayer

**Modifies or Replaces:** Weapon/Armor Proficiencies; 2nd, 6th, and 10th-level Slayer Talents

**Description:** Also known as a divine assassin, god's blade, or wrath-bringer, a deliverer is a
weapon chosen by a god to punish those who have committed an affront to that deity.

**Dune Rider**

**Class:** slayer

**Modifies or Replaces:** Track; Swift Tracker; Studied Target; Stalker; 4th, 8th-level Slayer
Talent; Master Slayer

**Description:** Mounted harriers, saboteurs, and skirmishers, dune riders can disrupt even the most
organized opposition.

**Family Hunter**

**Class:** slayer

**Modifies or Replaces:** 2nd, 6th-level Slayer Talent; Sneak Attack; Studied Target

**Description:** Most slayers focus their efforts on single targets, but family hunters try to root
out every branch of a tainted tree of life.

**Grave Warden**

**Class:** slayer

**Modifies or Replaces:** 2nd and 10th-level Slayer Talents; Stalker

**Description:** While paladins and inquisitors use their connection with the divine to fight undead
hordes and other horrors of the night, a grave warden relies on knowledge, skill with weapons, and
tenacity to put an end to these night-born terrors.

**Guerrilla**

**Class:** slayer

**Modifies or Replaces:** Track; Swift Tracker; 6th-level Slayer Talent; Quarry; Improved Quarry

**Description:** Slayers characterized by cunning and patience, guerrillas specialize in ambush and
harassment of enemies.

**Pureblade**

**Class:** slayer

**Modifies or Replaces:** Track; 2nd and 8th-level Slayer Talents; Stalker; Master Slayer

**Description:** In Numeria, Pureblades are skilled at slaying naturally arising aberrations and any
creatures that have been mutated by exposure to the bizarre alien technology that pervades the land.
Pureblades from Alkenstar and Nex lead forays into the magic-starved Mana Wastes to eliminate
aberrations before the creatures can threaten their lands.

**Sczarni Executioner**

**Class:** slayer

**Modifies or Replaces:** Class Skills; Studied Target; 4th-level Slayer Talent; Swift Tracker;
Quarry; Improved Quarry

**Description:** These professional killers are trained and used almost exclusively by the various
Sczarni crime families.

**Sniper**

**Class:** slayer

**Modifies or Replaces:** Track

**Description:** Whether it's with a bullet from a sling, a quarrel from a crossbow, or even an
expertly thrown dagger, the sniper ensures that a single shot disables his targets.

**Spawn Slayer**

**Class:** slayer

**Modifies or Replaces:** Studied Target; Stalker; Master Slayer

**Description:** Generations of Ninshaburian warriors fought the Spawn of Rovagug, holding the line
against impossible odds. Some of their ancient techniques persist to this day.

**Spire Diver**

**Class:** slayer

**Modifies or Replaces:** Studied Target; Stalker; Track; Swift Tracker; Slayer's Advance; Quarry;
Improved Quarry

**Description:** Peerless divers, assassins, and scouts, spire divers operate in and out of water
using the same weapons and equipment.

**Spiritslayer**

**Class:** slayer

**Modifies or Replaces:** 2nd level Slayer Talent; Stalker

**Description:** Slayers that focus in culling ghosts, shadow demons, and other incorporeal
creatures.

**Stygian Slayer**

**Class:** slayer

**Modifies or Replaces:** Armor Proficiencies; 4th and 10th-level Slayer Talents; Stalker

**Description:** A stygian slayer crawls out of the darkest shadows to strike fear into the hearts
of civilized folk.

**Toxic Sniper**

**Class:** slayer

**Modifies or Replaces:** Weapon and Armor Proficiencies; Track; Studied Target; Slayer Talents

**Description:** Followers of the daemonic harbinger Cixyron hide throughout the Mana Wastes,
scavenging for guns. With significant firepower in hand, the Furious Thunder's snipers bring
poisonous death to the wastes.

**Turncoat**

**Class:** slayer

**Modifies or Replaces:** Track; Stalker; Quarry; Improved Quarry

**Description:** The turncoat's natural talents for deception and treachery are fitting when
negotiating with the untrustworthy individuals and his ability to adapt allows him to preempt
opponents' schemes.

**Vanguard**

**Class:** slayer

**Modifies or Replaces:** Track; 2nd and 4th-level Slayer Talents; Stalker

**Description:** Vanguards are battlefield commanders who focus on the brutality of combat and lead
their allies to bloody victory.

**Velvet Blade**

**Class:** slayer

**Modifies or Replaces:** Class Skills; Armor Proficiency; Studied Target; Track; Swift Tracker

**Description:** Velvet blades specialize in infiltrating the upper echelons of society, mingling
with nobles and courtiers, and killing them.

**Witch Killer**

**Class:** slayer

**Modifies or Replaces:** Class Skills; Studied Target; 4th, 10th-level Slayer Talent

**Description:** Born into cultures where magic users are hated and feared, witch killers devote
their lives to purge the arcane taint from the world.

**Woodland Sniper**

**Class:** slayer

**Modifies or Replaces:** Track; Sneak Attack; Stalker; Swift Tracker; Slayer's Advance

**Description:** Woodland snipers are guardians of forest and grove, keeping vigil on their borders
and hunting bounties and trespassers from the shelter of sturdy branches.

### Archetypes by Feature

|Archetype|Alignment|Armor Proficiency|Class Skills|Master Slayer|Quarry|Improved Quarry|Slayer Talents|2nd-level Slayer Talent|4th-level Slayer Talent|6th-level Slayer Talent|8th-level Slayer Talent|10th-level Slayer Talent|12th-level Slayer Talent|16th-level Slayer Talent|Slayer's Advance|Sneak Attack|Stalker|Studied Target|Swift Tracker|Track|Weapon Proficiency|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Ankou's Shadow](ref/arc-slayer/ankous-shadow)|||||X|X|||||||||||X|X||||
|[Avalancher](ref/arc-slayer/avalancher)||||X|X|X|||||||||||X|X|X|X||
|[Bloody Jake](ref/arc-slayer/bloody-jake)|X|X|||||||X|X|X||X|X|X|||X|X||X|
|[Bounty Hunter](ref/arc-slayer/bounty-hunter)||X||||||X||X||X|||||||||X|
|[Butterfly Blade](ref/arc-slayer/butterfly-blade)|||||X|X||||||||||X|X|X|X|X||
|[Cleaner](ref/arc-slayer/cleaner)|||||||||X||||||||X|||X||
|[Covenbane](ref/arc-slayer/covenbane)||||||||X|||||||||X||X|X||
|[Cutthroat](ref/arc-slayer/cutthroat)|||X|||||X||X||||||||||X||
|[Deliverer](ref/arc-slayer/deliverer)||X||||||X||X||X|||||||||X|
|[Dune Rider](ref/arc-slayer/dune-rider)||||X|||||X||X||||||X|X|X|X||
|[Family Hunter](ref/arc-slayer/family-hunter)||||||||X||X||||||X||X||||
|[Grave Warden](ref/arc-slayer/grave-warden)||||||||X||||X|||||X|||||
|[Guerrilla](ref/arc-slayer/guerrilla)|||||X|X||||X|||||||||X|X||
|[Pureblade](ref/arc-slayer/pureblade)||||X||||X|||X||||||X|||X||
|[Sczarni Executioner](ref/arc-slayer/sczarni-executioner)|||X||X|X|||X|||||||||X|X|||
|[Sniper](ref/arc-slayer/sniper)||||||||||||||||||||X||
|[Spawn Slayer](ref/arc-slayer/spawn-slayer)||||X|||||||||||||X|X||||
|[Spire Diver](ref/arc-slayer/spire-diver)|||||X|X|||||||||X||X|X|X|X||
|[Spiritslayer](ref/arc-slayer/spiritslayer)||||||||X|||||||||X|||||
|[Stygian Slayer](ref/arc-slayer/stygian-slayer)||X|||||||X|||X|||||X|||||
|[Toxic Sniper](ref/arc-slayer/toxic-sniper)||X|||||X|||||||||||X||X|X|
|[Turncoat](ref/arc-slayer/turncoat)|||||X|X|||||||||||X|||X||
|[Vanguard](ref/arc-slayer/vanguard)||||||||X|X||||||||X|||X||
|[Velvet Blade](ref/arc-slayer/velvet-blade)||X|X|||||||||||||||X|X|X||
|[Witch Killer](ref/arc-slayer/witch-killer)|||X||||||X|||X||||||X||||
|[Woodland Sniper](ref/arc-slayer/woodland-sniper)|||||||||||||||X|X|X||X|X||

### Favored Class Bonuses

_The favored class options for slayer are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
