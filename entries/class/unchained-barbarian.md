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
- [Calm Stance (Ex)](ref/ragepower/calm-stance)
- [Elemental Stance (Su)](ref/ragepower/elemental-stance)
- [Fearless Rage (Ex)](ref/ragepower/fearless-rage)
- [Greater Ground Breaker (Ex)](ref/ragepower/greater-ground-breaker)
- [Guarded Stance (Ex)](ref/ragepower/guarded-stance-stance)
- [Internal Fortitude (Ex)](ref/ragepower/internal-fortitude)
- [Knockdown Stance (Ex)](ref/ragepower/knockdown-stance)
- [Low-Light Vision (Ex)](ref/ragepower/low-light-vision)
- [Quick Reflexes (Ex)](ref/ragepower/quick-reflexes)
- [Reckless Stance (Ex)](ref/ragepower/reckless-stance)
- [Regenerative Stance (Ex)](ref/ragepower/regenerative-stance)
- [Scent (Ex)](ref/ragepower/scent)
- [Strength Stance (Ex)](ref/ragepower/strength-stance)
- [Taunting Stance (Ex)](ref/ragepower/taunting-stance)

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
spirit, world serpent totem, world serpent totem unity.

##### Animal Fury (Ex) {#animal-fury}

The barbarian gains a bite attack. This is a primary natural attack that deals 1d4 points of damage
(if the barbarian is Medium; 1d3 if the barbarian is Small) plus the barbarian's Strength modifier.
If made as part of a full-attack action with manufactured weapons, the bite attack is made at the
barbarian's full base attack bonus - 5, and she adds only 1/2 her Strength modifier to the damage
roll. The barbarian can make a bite attack as part of the action to maintain or break free from a
grapple. If the bite attack hits, grapple checks attempted by the barbarian against the target until
the end of the round gain a +2 bonus.

##### Auspicious Mark (Su) {#auspicious-mark}

The barbarian has been marked by the spirits, as indicated by an impressive tattoo, scar, or
birthmark she possesses. As a swift action, she can call upon the spirits' favor to increase any d20
roll she just made by rolling 1d6 and adding it to the result. This bonus increases by 1 for every 4
levels she has. She can call on the auspicious mark after seeing the result of the d20 roll. This
ability can be used only once per day.

##### Bleeding Blow (Ex) {#bleeding-blow}

While in the powerful stance, the barbarian can make an attack that causes her enemies to bleed
profusely. Once per round, she can have one of her attacks deal an amount of bleed damage equal to
1/2 her bonus damage from powerful stance. This bleed damage bypasses damage reduction. This bleed
damage doesn't stack with itself. A barbarian must have the powerful stance rage power and be at
least 8th level to select this rage power.

##### Clear Mind (Ex) {#clear-mind}

When the barbarian fails a Will saving throw, she can attempt another Will saving throw at the end
of her next turn (using the original DC). If the second saving throw is successful, the barbarian is
treated as if she succeeded at the first saving throw, negating or reducing the effect as determined
by the spell or effect. If this second saving throw fails, the barbarian suffers the full effects of
the spell or effect as normal. A barbarian must be at least 8th level to select this rage power.

##### Crippling Blow (Ex) {#crippling-blow}

Once per day when the barbarian hits with an attack, she can deal 1 point of ability damage to the
target's Strength or Dexterity score. This damage increases by 1 point for every 4 levels the
barbarian has. A barbarian must be at least 8th level to select this rage power.

##### Deadly Accuracy (Ex) {#deadly-accuracy}

If the barbarian scores a critical threat while in the accurate stance, she applies double the
accurate stance's bonus when rolling to confirm the critical. A barbarian must have the accurate
stance rage power and be at least 4th level to select this rage power.

##### Eater of Magic (Su) {#eater-of-magic}

When the barbarian succeeds at a saving throw to resist a spell, supernatural ability, or spell-like
ability, she gains temporary hit points equal to the spell's level (in the case of spells or
spell-like abilities) or 1/2 the CR of the effect's creator (in the case of supernatural abilities).
These temporary hit points disappear when the barbarian's rage ends, and they stack with her
temporary hit points from rage but not with other temporary hit points gained from this rage power.
A barbarian must have the superstition rage power and be at least 10th level to select this rage
power.

##### Energy Absorption (Su) {#energy-absorption}

Once per day, the barbarian can absorb the energy from a single attack that deals damage of the
energy type she resists with the energy resistance rage power. She takes no damage from the attack
and doesn't attempt a saving throw. Instead, she increases the temporary hit points from her rage by
an amount equal to 1/2 the damage she would have taken (ignoring her energy resistance). If the
barbarian is at least 16th level, once before her rage ends, she can unleash the stored energy as a
breath weapon in either a 60-foot line or a 30-foot cone. The breath weapon deals an amount of
damage equal to the full amount the barbarian would have taken from the absorbed effect. Creatures
affected by the breath weapon can attempt a Reflex save for half damage (DC = 10 + 1/2 the
barbarian's level + her Constitution modifier). She retains the temporary hit points from this
ability even if she unleashes this breath weapon. A barbarian must have the energy resistance rage
power and be at least 12th level to select this rage power.

##### Energy Resistance (Ex) {#energy-resistance}

The barbarian gains resistance to one energy type (acid, cold, electricity, fire, or sonic) equal to
1/2 her barbarian level (minimum 1). At 8th level, she gains limited immunity to the same type of
energy, as _protection from energy_. She can absorb 2 points of damage per level, and she applies
her energy resistance first. The energy type is chosen when this rage power is selected, and it
can't be changed. This rage power can be selected more than once; each time, it applies to a
different energy type.

##### Flesh Wound (Ex) {#flesh-wound}

Once per day, the barbarian can avoid serious harm from an attack. She attempts a Fortitude save
with a DC equal to the damage that would be dealt by the attack. If she succeeds, she takes no
damage from the attack. If she fails, she takes half damage from the attack and the damage is
nonlethal. The barbarian must elect to use this ability after the attack roll is made, but before
the damage is rolled. A barbarian must be at least 10th level to select this rage power.

##### Ground Breaker (Ex) {#ground-breaker}

The barbarian can attack the floor around her as a full-round action. This attack automatically hits
and deals damage normally. If the barbarian deals more damage than the floor's hardness, the space
she occupies and all of the squares adjacent to her become difficult terrain. Creatures in those
squares, except the barbarian, must succeed at DC 15 Reflex saves or be knocked prone. A barbarian
must be at least 6th level to select this rage power.

##### Increased Damage Reduction (Ex) {#increased-damage-reduction}

The barbarian's damage reduction increases by 2/— whenever she is raging. A barbarian can select
this rage power up to three times. Its effects stack. A barbarian must be at least 8th level to
select this rage power.

##### Inspire Ferocity (Ex) {#inspire-ferocity}

While in the reckless stance, the barbarian imparts the stance's bonus and penalty to all willing
allies within 30 feet of her. A barbarian must have the reckless stance rage power to select this
rage power.

##### Intimidating Glare (Ex) {#intimidating-glare}

The barbarian adds her Strength modifier in place of her Charisma modifier on all Intimidate checks
to demoralize a foe. She can attempt an Intimidate check to demoralize an adjacent foe as a move
action instead of a standard action. If the barbarian successfully demoralizes an adjacent foe, that
foe is shaken for the remainder of the barbarian's current rage.

##### Knockback (Ex) {#knockback}

Once per round, the barbarian can attempt a bull rush against one target in place of a melee attack,
using her full CMB regardless of the attack it replaces. If the bull rush is successful, the target
takes an amount of damage equal to the barbarian's Strength modifier and is knocked back as normal.
The barbarian doesn't move with the target. This bull rush doesn't provoke an attack of opportunity.

##### Lethal Accuracy (Ex) {#lethal-accuracy}

While in the accurate stance, the barbarian's critical multiplier for damage increases by 1 (a ×2
multiplier becomes ×3, a ×3 multiplier becomes ×4, and a ×4 multiplier becomes ×5). A barbarian must
have the accurate stance and deadly accuracy rage powers and be at least 16th level to select this
rage power.

##### Mighty Swing (Ex) {#mighty-swing}

The barbarian automatically confirms a critical hit. This power is used as an immediate action once
a critical threat has been determined. This ability can be used only once per day. A barbarian must
be at least 12th level to select this rage power.

##### Night Vision (Ex) {#night-vision}

The barbarian's senses grow incredibly sharp, and she gains darkvision out to a range of 60 feet. If
she already has darkvision, the range of that darkvision increases by 60 feet. A barbarian must have
a darkvision racial trait, low-light vision racial trait, or the low-light vision rage power to
select this rage power.

##### No Escape (Ex) {#no-escape}

The barbarian can move up to double her base speed as an immediate action. She can use this ability
only when an adjacent foe uses a withdraw action to move away from her. She must end her movement
adjacent to the enemy that used the withdraw action. The barbarian provokes attacks of opportunity
as normal during this movement.

##### Perfect Clarity (Ex) {#perfect-clarity}

While in the calm stance, the barbarian can roll twice for any miss chances or Will saving throws to
disbelieve illusions, taking the better result. A barbarian must have the calm stance rage power to
select this rage power.

##### Powerful Stance (Ex) {#powerful-stance}

The barbarian can focus her ferocity. She gains a +1 bonus on melee damage rolls and thrown weapon
damage rolls. This bonus increases by 1 for every 4 levels the barbarian has. This is a stance rage
power.

_Protect Vitals (Ex)_: While in the guarded stance, the barbarian gains an additional +4 dodge bonus
to AC against attack rolls made to confirm critical hits. A barbarian must have the guarded stance
rage power and be at least 8th level to select this rage power.

##### Raging Climber (Ex) {#raging-climber}

The barbarian gains a climb speed equal to 1/2 her base land speed, taking into account her fast
movement class feature. She can't use this climb speed to climb any surface with a DC higher
than 20. She also gains a +8 enhancement bonus on Climb checks.

##### Raging Leaper (Ex) {#raging-leaper}

The barbarian is always considered to have a running start when attempting an Acrobatics check to
jump. In addition, she gains a +8 bonus on Acrobatics checks to jump. Finally, if the barbarian
falls, she halves the total distance fallen for the purposes of determining damage taken from the
fall.

##### Raging Swimmer (Ex) {#raging-swimmer}

The barbarian gains a swim speed equal to 1/2 her base land speed (taking into account her fast
movement class feature). She also gains a +8 enhancement bonus on Swim checks.

##### Reflexive Dodge (Ex) {#reflexive-dodge}

While in the guarded stance, the barbarian can apply her dodge bonus to AC as a bonus on Reflex
saving throws. A barbarian must have the guarded stance rage power and be at least 6th level to
select this rage power.

##### Renewed Vigor (Ex) {#renewed-vigor}

As a standard action, the barbarian heals 1d8 points of damage + her Constitution modifier. For
every 4 levels the barbarian has beyond 4th, the amount healed increases by 1d8 (to a maximum of 5d8
at 20th level). This ability can be used only once per day. The barbarian must be at least 4th level
to select this rage power.

##### Renewed Vitality (Ex) {#renewed-vitality}

The barbarian ignores the effect of 1 point of ability penalty or ability damage per 2 levels she
has (maximum 10). At 6th level, the barbarian can also ignore 1 negative level per 4 levels she has.
She takes the full effects of the ability penalties, ability damage, or negative levels once her
rage ends.

##### Roused Anger (Ex) {#roused-anger}

The barbarian can enter a rage even when fatigued. If the barbarian enters a rage while fatigued,
she loses the fatigued condition and she does not gain temporary hit points from rage. Once this
rage ends, the barbarian is exhausted for 10 minutes.

##### Sharpened Accuracy (Ex) {#sharpened-accuracy}

While in the accurate stance, the barbarian ignores the miss chance for concealment and treats total
concealment as concealment. She also ignores cover penalties except those from total cover. A
barbarian must have the accurate stance rage power and be at least 8th level to select this rage
power.

##### Smasher (Ex) {#smasher}

Whenever the barbarian attempts a sunder combat maneuver or makes an attack against an unattended
object, she ignores 1 point of the object's hardness per barbarian level she has.

##### Sprint (Ex) {#sprint}

The barbarian adds 1/2 her speed to the distance she can move when she runs or charges. A barbarian
must have the swift foot rage power and be at least 4th level to select this rage power.

##### Superstition (Ex) {#superstition}

The barbarian gains a +2 competence bonus on saving throws made to resist spells and spell-like
abilities. This bonus increases by 1 for every 4 levels the barbarian has. The barbarian cannot be
the willing target of any spell and must attempt saving throws to resist all spells, even those cast
by allies.

##### Swift Foot (Ex) {#swift-foot}

The barbarian gains a 10-foot enhancement bonus to her base speed. A barbarian can select this rage
power up to three times; its effects stack.

##### Terrifying Howl (Ex) {#terrifying-howl}

The barbarian unleashes a terrifying howl as a standard action. All enemies that have been shaken by
the barbarian (usually through the Intimidate skill) within 30 feet must succeed at a Will save (DC
= 10 + 1/2 the barbarian's level + her Strength modifier) or be panicked for 1d4+1 rounds. Once an
enemy has attempted a save versus this ability (whether successful or not), it's immune to this
power for 24 hours. A barbarian must be at least 8th level and have the intimidating glare rage
power to select this rage power.

##### Unexpected Strike (Ex) {#unexpected-strike}

The barbarian can make an attack of opportunity against a foe that moves into any square threatened
by the barbarian, regardless of whether that movement would normally provoke an attack of
opportunity. The barbarian can use this ability only when there are no other foes in a square
threatened by the barbarian. A barbarian must be at least 8th level to select this rage power.

##### Witch Hunter (Ex) {#witch-hunter}

The barbarian gains a +1 bonus on damage rolls against creatures possessing spells or spell-like
abilities. This damage bonus increases by 1 for every 4 levels the barbarian has. In addition, if
she confirms a critical hit against a creature affected by an ongoing beneficial spell effect, that
effect is suppressed for 1 round (determined randomly if the creature is currently affected by more
than one effect). A barbarian must have the superstition rage power to select this rage power.

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
