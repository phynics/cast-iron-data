+++
id = "ref/class/unchained-rogue"
kind = "class"
title = "Unchained Rogue"
aon = "ClassDisplay.aspx?ItemName=Rogue%20%28Unchained%29"
source_ids = ["pathfinder-unchained", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unchained_rogue", path = "json/classes8.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "20"
[[sources]]
publication = "chronicle-of-legends"
page = "28-29"

[fields]
kind = "class"
class_type = "unchained"
hit_die = "d8"
skill_ranks = "8 + Int modifier"
features = [
  { anchor = "sneak-attack", level = 1 },
  { anchor = "trapfinding", level = 1 },
  { anchor = "finesse-training", level = 1 },
  { anchor = "evasion", level = 2 },
  { anchor = "rogue-talents", level = 2 },
  { anchor = "danger-sense", level = 3 },
  { anchor = "debilitating-injury", level = 4 },
  { anchor = "bewildered" },
  { anchor = "disoriented" },
  { anchor = "hampered" },
  { anchor = "uncanny-dodge", level = 4 },
  { anchor = "rogue-s-edge", level = 5 },
  { anchor = "improved-uncanny-dodge", level = 8 },
  { anchor = "advanced-talents", level = 10 },
  { anchor = "master-strike", level = 20 },
]
+++

Thief, sneak, charmer, diplomat - all of these and more describe the rogue. When not skulking in the
shadows, disarming traps, and stealing from the unaware, rogues may rub shoulders with powerful
nobles or plot capers with fellow crooks. The rogue is the master of many faces, using her skills
and talents to get herself both into and out of trouble with rakish aplomb. While others may call
them charlatans and burglars, even the most larcenous rogues tend to consider themselves consummate
professionals, willing to take on any job if the price is right.

**Unchained:** While much of the unchained rogue will be familiar to those who have played the class
from the _Core Rulebook,_ there are a number of new class features that greatly enhance the power
and flexibility of the rogue. Chief among these is the debilitating injury class feature. A rogue
with this ability can severely hamper her foes, giving her a much-needed boost to her offense or
defense, depending on the situation. In addition, with finesse training, the rogue now gains
[Weapon Finesse](ref/feat/weapon-finesse) for free at 1st level. This ability also lets her add her
Dexterity to damage rolls with one weapon starting at 3rd level. Finally, the rogue's edge ability
ties into a new system called skill unlocks. With this feature, the rogue can master a small set of
chosen skills, outperforming all those characters without access to such talents.

**Alignment:** Any

**Hit Die:** d8

**Starting Wealth:** 4d6 × 10 gp (average 140 gp)

**Skill Points per Level:** 8 + Int modifier

**Class Skills (Str):** Climb, Swim

**Class Skills (Dex):** Acrobatics, Disable Device, Escape Artist, Sleight of Hand, Stealth

**Class Skills (Int):** Appraise, Craft (any), Knowledge (dungeoneering), Knowledge (local),
Linguistics

**Class Skills (Wis):** Perception, Profession (any), Sense Motive

**Class Skills (Cha):** Bluff, Diplomacy, Disguise, Intimidate, Perform (any), Use Magic Device

### Class Features

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|
| --- | --- | --- | --- | --- | --- |
|1st|+0|+0|+2|+0|Finesse training, sneak attack +1d6, trapfinding|
|2nd|+1|+0|+3|+0|Evasion, rogue talent|
|3rd|+2|+1|+3|+1|Danger sense +1, finesse training, sneak attack +2d6|
|4th|+3|+1|+4|+1|Debilitating injury, rogue talent, uncanny dodge|
|5th|+3|+1|+4|+1|Rogue's edge, sneak attack +3d6|
|6th|+4|+2|+5|+2|Danger sense +2, rogue talent|
|7th|+5|+2|+5|+2|Sneak attack +4d6|
|8th|+6/+1|+2|+6|+2|Improved uncanny dodge, rogue talent|
|9th|+6/+1|+3|+6|+3|Danger sense +3, sneak attack +5d6|
|10th|+7/+2|+3|+7|+3|Advanced talents, rogue talent, rogue's edge|
|11th|+8/+3|+3|+7|+3|Finesse training, sneak attack +6d6|
|12th|+9/+4|+4|+8|+4|Danger sense +4, rogue talent|
|13th|+9/+4|+4|+8|+4|Sneak attack +7d6|
|14th|+10/+5|+4|+9|+4|Rogue talent|
|15th|+11/+6/+1|+5|+9|+5|Danger sense +5, rogue's edge, sneak attack +8d6|
|16th|+12/+7/+2|+5|+10|+5|Rogue talent|
|17th|+12/+7/+2|+5|+10|+5|Sneak attack +9d6|
|18th|+13/+8/+3|+6|+11|+6|Danger sense +6, rogue talent|
|19th|+14/+9/+4|+6|+11|+6|Finesse training, sneak attack +10d6|
|20th|+15/+10/+5|+6|+12|+6|Master strike, rogue talent, rogue's edge|

The following are the class features of the rogue.

#### Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

Rogues are proficient with all simple weapons, plus the hand crossbow, rapier, sap, short sword, and
shortbow. They are proficient with light armor, but not with shields.

#### Sneak Attack {#sneak-attack}

If a rogue can catch an opponent when he is unable to defend himself effectively from her attack,
she can strike a vital spot for extra damage.

The rogue's attack deals extra damage anytime her target would be denied a Dexterity bonus to AC
(whether the target actually has a Dexterity bonus or not), or when the rogue flanks her target.
This extra damage is 1d6 at 1st level, and increases by 1d6 every 2 rogue levels thereafter. Ranged
attacks can count as sneak attacks only if the target is within 30 feet. This additional damage is
precision damage and is not multiplied on a critical hit.

With a weapon that deals nonlethal damage (such as a sap, unarmed strike, or whip), a rogue can make
a sneak attack that deals nonlethal damage instead of lethal damage. She cannot use a weapon that
deals lethal damage to deal nonlethal damage in a sneak attack—not even with the usual -4 penalty.

The rogue must be able to see the target well enough to pick out a vital spot and must be able to
reach such a spot. A rogue cannot sneak attack while striking a creature with total
[concealment](ref/rule/concealment).

#### Trapfinding {#trapfinding}

A rogue adds 1/2 her level on Perception checks to locate traps and on Disable Device checks
(minimum +1). A rogue can use Disable Device to disarm magic traps.

#### Finesse Training (Ex) {#finesse-training}

At 1st level, a rogue gains [Weapon Finesse](ref/feat/weapon-finesse) as a bonus feat. In addition,
starting at 3rd level, she can select any one type of weapon that can be used with Weapon Finesse
(such as rapiers or [daggers](ref/eq-weapon/dagger)). Once this choice is made, it cannot be
changed. Whenever she makes a successful melee attack with the selected weapon, she adds her
Dexterity modifier instead of her Strength modifier to the damage roll. If any effect would prevent
the rogue from adding her Strength modifier to the damage roll, she does not add her Dexterity
modifier. The rogue can select a second weapon at 11th level and a third at 19th level.

#### Evasion (Ex) {#evasion}

At 2nd level, a rogue can avoid even magical and unusual attacks with great agility. If she succeeds
at a Reflex saving throw against an attack that normally deals half damage on a successful save, she
instead takes no damage. Evasion can be used only if the rogue is wearing light armor or no armor. A
[helpless](ref/misc/helpless) rogue does not gain the benefit of evasion.

#### Rogue Talents {#rogue-talents}

As a rogue gains experience, she learns a number of talents that aid her and confound her foes.
Starting at 2nd level, a rogue gains one rogue talent. She gains an additional rogue talent for
every 2 levels of rogue attained after 2nd level. A rogue cannot select an individual talent more
than once.

Talents marked with an asterisk add effects to a rogue's sneak attack. Only one of these talents can
be applied to an individual attack, and the decision must be made before the attack roll is made.

_Bleeding Attack_\* _(Ex)_: A rogue with this ability can cause living opponents to bleed by hitting
them with a sneak attack. This attack causes the target to take 1 additional point of damage each
round for each die of the rogue's sneak attack (e.g., 4d6 equals 4 points of bleed). Bleeding
creatures take that amount of damage every round at the start of each of their turns. The bleeding
can be stopped by a successful DC 15 Heal check or the application of any effect that heals hit
point damage. Bleed damage from this ability does not stack with itself. Bleed damage bypasses any
damage reduction the creature might possess.

- [Camouflage (Ex)](ref/talent/camouflage)
- [Certainty (Ex)](ref/talent/certainty)
- [Coax Information (Ex)](ref/talent/coax-information-unchained-rogue)
- [Combat Swipe](ref/talent/combat-swipe)
- [Combat Trick](ref/talent/combat-trick)
- [Esoteric Scholar (Ex)](ref/talent/esoteric-scholar)
- [Expert Leaper (Ex)](ref/talent/expert-leaper)
- [Fast Stealth (Ex)](ref/talent/fast-stealth)
- [Follow Clues (Ex)](ref/talent/follow-clues)
- [Hold Breath (Ex)](ref/talent/hold-breath)
- [Lasting Poison (Ex)](ref/talent/lasting-poison)
- [Ledge Walker (Ex)](ref/talent/ledge-walker)
- [Major Magic (Sp)](ref/talent/major-magic)
- [Minor Magic (Sp)](ref/talent/minor-magic)
- [Multitalented (Ex)](ref/talent/multitalented)
- [Nimble Climber (Ex)](ref/talent/nimble-climber)
- [Powerful Sneak (Ex)](ref/talent/powerful-sneak)\*
- [Quick Disable (Ex)](ref/talent/quick-disable)
- [Resiliency (Ex)](ref/talent/resiliency)
- [Rogue Crawl (Ex)](ref/talent/rogue-crawl)
- [Slow Reactions (Ex)](ref/talent/slow-reactions)\*
- [Stand Up (Ex)](ref/talent/stand-up)
- [Surprise Attack (Ex)](ref/talent/surprise-attack)
- [Terrain Mastery (Ex)](ref/talent/terrain-mastery)
- [Trap Spotter (Ex)](ref/talent/trap-spotter)
- [Weapon Training](ref/talent/weapon-training)

#### Danger Sense (Ex) {#danger-sense}

At 3rd level, a rogue gains a +1 bonus on Reflex saves to avoid traps and a +1 dodge bonus to AC
against attacks made by traps. In addition, she gains a +1 bonus on Perception checks to avoid being
surprised by a foe. These bonuses increase by 1 every 3 rogue levels thereafter (to a maximum of +6
at 18th level). This ability counts as [trap sense](ref/ability/trap-sense) for the purpose of any
feat or class prerequisite, and can be replaced by any archetype class feature that replaces trap
sense. The bonuses gained from this ability stack with those gained from trap sense (from another
class).

#### Debilitating Injury (Ex) {#debilitating-injury}

At 4th level, whenever a rogue deals sneak attack damage to a foe, she can also debilitate the
target of her attack, causing it to take a penalty for 1 round (this is in addition to any penalty
caused by a rogue talent or other special ability). The rogue can choose to apply any one of the
following penalties when the damage is dealt.

#### Bewildered {#bewildered}

The target becomes bewildered, taking a -2 penalty to AC. The target takes an additional -2 penalty
to AC against all attacks made by the rogue. At 10th level and 16th level, the penalty to AC against
attacks made by the rogue increases by -2 (to a total maximum of -8).

#### Disoriented {#disoriented}

The target takes a -2 penalty on attack rolls. In addition, the target takes an additional -2
penalty on all attack rolls it makes against the rogue. At 10th level and 16th level, the penalty on
attack rolls made against the rogue increases by -2 (to a total maximum of -8).

#### Hampered {#hampered}

All of the target's speeds are reduced by half (to a minimum of 5 feet). In addition, the target
cannot [take a 5-foot step](ref/rule/take-5-foot-step).

These penalties do not stack with themselves, but additional attacks that deal sneak attack damage
extend the duration by 1 round. A creature cannot suffer from more than one penalty from this
ability at a time. If a new penalty is applied, the old penalty immediately ends. Any form of
healing applied to a target suffering from one of these penalties also removes the penalty.

#### Uncanny Dodge (Ex) {#uncanny-dodge}

At 4th level, a rogue can react to danger before her senses would normally allow her to do so. She
cannot be caught [flat-footed](ref/rule/flat-footed), nor does she lose her Dexterity bonus to AC if
the attacker is invisible. She still loses her Dexterity bonus to AC if immobilized. A rogue with
this ability can still lose her Dexterity bonus to AC if an opponent successfully uses the
[feint](ref/rule/feint) action against her.

If a rogue already has uncanny dodge from a different class, she automatically gains improved
uncanny dodge (see below) instead.

#### Rogue's Edge (Ex) {#rogue-s-edge}

At 5th level, a rogue has mastered a single skill beyond that skill's normal boundaries, gaining
results that others can only dream about. She gains the skill unlock powers (see page 82) for that
skill as appropriate for her number of ranks in that skill. At 10th, 15th, and 20th levels, she
chooses an additional skill and gains skill unlock powers for that skill as well.

#### Improved Uncanny Dodge (Ex) {#improved-uncanny-dodge}

At 8th level, a rogue can no longer be [flanked](ref/rule/flanking).

This defense denies another rogue the ability to sneak attack the character by flanking her, unless
the attacker has at least four more rogue levels than the target does.

If a character already has uncanny dodge (see above) from another class, the levels from the classes
that grant uncanny dodge stack to determine the minimum rogue level required to flank the character.

#### Advanced Talents {#advanced-talents}

At 10th level and every 2 levels thereafter, a rogue can choose one of the following advanced
talents in place of a rogue talent.

- [Crippling Strike (Ex)](ref/talent/crippling-strike)\*
- [Cutting Edge (Ex)](ref/talent/cutting-edge)
- [Deadly Sneak (Ex)](ref/talent/deadly-sneak)\*
- [Defensive Roll (Ex)](ref/talent/defensive-roll)
- [Dispelling Attack (Su)](ref/talent/dispelling-attack)\*
- [Double Debilitation (Ex)](ref/talent/double-debilitation)\*
- [Feat](ref/talent/feat)
- [Improved Evasion (Ex)](ref/talent/improved-evasion)
- [Light Walker (Ex)](ref/talent/light-walker)
- [Master of Disguise (Ex)](ref/talent/master-of-disguise)
- [Greater Multitalented (Ex)](ref/talent/greater-multitalented)
- [Opportunist (Ex)](ref/talent/opportunist)
- [Skill Mastery](ref/talent/skill-mastery-unchained-rogue)
- [Slippery Mind (Ex)](ref/talent/slippery-mind)
- [Quick Shot (Ex)](ref/talent/quick-shot)
- [Greater Terrain Mastery (Ex)](ref/talent/greater-terrain-mastery)

##### Unmodified Rogue Talents {#unmodified-rogue-talents}

The rogue talents in this chapter include replacements for all of those in the _Core Rulebook_,
along with selected revised rogue talents from other sources. The following rogue talents can be
used without modification.

##### Rogue Talents {#unmodified-core-rogue-talents}

Assault leader, black market connections, canny observer, cunning trigger, deft palm, distracting
attack\*, fast getaway, firearm training, getaway artist, grit, iron guts, ninja trick, positioning
attack, quick disguise, quick trapsmith, rope master, strong impression, strong stroke, survivalist,
swift poison, underhanded, wall scramble.

##### Advanced Rogue Talents {#advanced-rogue-talents}

Another day, confounding blades\*, deadly cocktail, familiar, fast tumble, frugal trapsmith, getaway
master, hide in plain sight, hunter's surprise, knock-out blow, redirect attack, rumormonger,
stealthy sniper, unwitting ally, weapon snatcher.

#### Master Strike (Ex) {#master-strike}

At 20th level, a rogue becomes incredibly deadly when dealing sneak attack damage. Each time the
rogue deals sneak attack damage, she can choose one of the following three effects: the target can
be put to sleep for 1d4 hours, [paralyzed](ref/rule/paralyzed) for 2d6 rounds, or slain. Regardless
of the effect chosen, the target can attempt a Fortitude save to negate the additional effect. The
DC of this save is equal to 10 + 1/2 the rogue's level + the rogue's Dexterity modifier. Once a
creature has been the target of a master strike, regardless of whether or not the save is
successful, that creature is immune to that rogue's master strike for 24 hours. Creatures that are
immune to sneak attack damage are also immune to this ability.

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

There are no official archetypes for the Unchained Rogue. You can use [rogue](ref/class/rogue)
archetypes if the features being replaced by the archetype match those of the unchained rogue.

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

**Masterful Talent (Ex)**

At 20th level, the rogue has been a thief, an actor, a merchant, a scout, a confessor, a friend, an
assassin, and a dozen more things besides. The rogue gains a +4 bonus on all of her skills.

**Also available:** The Right Spot

### Favored Class Bonuses

_The favored class options for unchained\_rogue are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
