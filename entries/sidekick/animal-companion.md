+++
id = "ref/sidekick/animal-companion"
kind = "rule"
title = "Animal Companion"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_companion", path = "json/sidekicks.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook\
An animal companion's abilities are determined by the druid's level and its animal racial traits.
They remain creatures of the animal type for purposes of determining which spells can affect them.

### Base Statistics

|Class Level|HD|BAB|Fort|Ref|Will|Skills|Feats|Natural Armor Bonus|Str/Dex Bonus|Bonus Tricks|Special|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|2|+1|+3|+3|+0|2|1|+0|+0|1|Link, share spells|
|2nd|3|+2|+3|+3|+1|3|2|+0|+0|1|-|
|3rd|3|+2|+3|+3|+1|3|2|+2|+1|2|Evasion|
|4th|4|+3|+4|+4|+1|4|2|+2|+1|2|Ability score increase|
|5th|5|+3|+4|+4|+1|5|3|+2|+1|2|-|
|6th|6|+4|+5|+5|+2|6|3|+4|+2|3|Devotion|
|7th|6|+4|+5|+5|+2|6|3|+4|+2|3|-|
|8th|7|+5|+5|+5|+2|7|4|+4|+2|3|-|
|9th|8|+6|+6|+6|+2|8|4|+6|+3|4|Ability score increase, Multiattack|
|10th|9|+6|+6|+6|+3|9|5|+6|+3|4|-|
|11th|9|+6|+6|+6|+3|9|5|+6|+3|4|-|
|12th|10|+7|+7|+7|+3|10|5|+8|+4|5|-|
|13th|11|+8|+7|+7|+3|11|6|+8|+4|5|-|
|14th|12|+9|+8|+8|+4|12|6|+8|+4|5|Ability score increase|
|15th|12|+9|+8|+8|+4|12|6|+10|+5|6|Improved evasion|
|16th|13|+9|+8|+8|+4|13|7|+10|+5|6|-|
|17th|14|+10|+9|+9|+4|14|7|+10|+5|6|-|
|18th|15|+11|+9|+9|+5|15|8|+12|+6|7|-|
|19th|15|+11|+9|+9|+5|15|8|+12|+6|7|-|
|20th|16|+12|+10|+10|+5|16|8|+12|+6|7|Ability score increase|

**Class Level:** This is the character's druid level. The druid's class levels stack with levels of
any other classes that are entitled to an animal companion for the purpose of determining the
companion's statistics.

**HD:** This is the total number of eight-sided (d8) Hit Dice the animal companion possesses, each
of which gains a Constitution modifier, as normal.

**BAB:** This is the animal companion's base attack bonus. An animal companion's base attack bonus
is the same as that of a druid of a level equal to the animal's HD. Animal companions do not gain
additional attacks using their natural weapons for a high base attack bonus.

**Fort/Ref/Will:** These are the animal companion's base saving throw bonuses. An animal companion
has good Fortitude and Reflex saves.

**Skills:** This lists the animal's total skill ranks. Animal companions can assign skill ranks to
any skill listed under Animal Skills below. If an animal companion increases its Intelligence to 10
or higher, it gains bonus skill ranks as normal. Animal companions with an Intelligence of 3 or
higher can purchase ranks in any skill. An animal companion cannot have more ranks in a skill than
it has Hit Dice.

**Feats:** This is the total number of feats possessed by an animal companion. Animal companions
should select their feats from those listed under Animal Feats. Animal companions can select other
feats, although they are unable to utilize some feats (such as Martial Weapon Proficiency). Note
that animal companions cannot select a feat with a requirement of base attack bonus +1 until they
gain their second feat at 3 Hit Dice.

**Natural Armor Bonus:** The number noted here is an improvement to the animal companion's existing
natural armor bonus.

**Str/Dex Bonus:** Add this modifier to the animal companion's Strength and Dexterity scores.

**Bonus Tricks:** The value given in this column is the total number of "bonus" tricks that the
animal knows in addition to any that the druid might choose to teach it (see
[Handle Animal](ref/skill/handle-animal)). These bonus tricks don't require any training time or
Handle Animal checks, and they don't count against the normal limit of tricks known by the animal.
The druid selects these bonus [tricks](ref/ability/animal-tricks), and once selected, they can't be
changed.

An animal companion can also be taught special
[animal companion tricks](ref/ability/companion-tricks), though they may need specific
characteristics to learn them.

**Special:** This includes a number of abilities gained by animal companions as they increase in
power. Each of these bonuses is described below.

- _Link (Ex):_ A druid can handle her animal companion as a free action, or push it as a move
  action, even if she doesn't have any ranks in the Handle Animal skill. The druid gains a +4
  circumstance bonus on all [wild empathy](ref/ability/wild-empathy) checks and Handle Animal checks
  made regarding an animal companion.
- _Share Spells (Ex):_ The druid may cast a spell with a target of "You" on her animal companion (as
  a spell with a range of touch) instead of on herself. A druid may cast spells on her animal
  companion even if the spells normally do not affect creatures of the companion's type (animal).
  Spells cast in this way must come from a class that grants an animal companion. This ability does
  not allow the animal to share abilities that are not spells, even if they function like spells.
- _Evasion (Ex):_ If an animal companion is subjected to an attack that normally allows a Reflex
  save for half damage, it takes no damage if it makes a successful saving throw.
- _Ability Score Increase (Ex):_ The animal companion adds +1 to one of its ability scores.
- _Devotion (Ex):_ An animal companion gains a +4 morale bonus on Will saves against enchantment
  spells and effects.
- _Multiattack:_ An animal companion gains [Multiattack](ref/feat/multiattack) as a bonus feat if it
  has three or more natural attacks and does not already have that feat. If it does not have the
  requisite three or more natural attacks, the animal companion instead gains a second attack with
  one of its natural weapons, albeit at a -5 penalty.
- _Improved Evasion (Ex):_ When subjected to an attack that allows a Reflex saving throw for half
  damage, an animal companion takes no damage if it makes a successful saving throw and only half
  damage if the saving throw fails.

### Animal Skills

Animal companions can have ranks in any of the following skills: Acrobatics\* (Dex), Climb\* (Str),
Escape Artist (Dex), Fly\* (Dex), Intimidate (Cha), Perception\* (Wis), Stealth\* (Dex), Survival
(Wis), and Swim\* (Str). All of the skills marked with an (\*) are class skills for animal
companions. Animal companions with an Intelligence of 3 or higher can put ranks into any skill.

### Animal Feats

Animal companions can select from the following feats.

|Feat|Prerequisites|Description|
| --- | --- | --- |
|[Acrobatic](ref/feat/acrobatic)|—|+2 bonus on Acrobatics and Fly checks|
|[Agile Maneuvers](ref/feat/agile-maneuvers)|—|Use your Dex bonus when calculating your CMB|
|[Armor Proficiency, Heavy](ref/feat/armor-proficiency-heavy)|Light Armor Proficiency, Medium Armor Proficiency.|No penalties on attack rolls while wearing heavy armor|
|[Armor Proficiency, Light](ref/feat/armor-proficiency-light)|—|No penalties on attack rolls while wearing light armor|
|[Armor Proficiency, Medium](ref/feat/armor-proficiency-medium)|Light Armor Proficiency.|No penalties on attack rolls while wearing medium armor|
|[Athletic](ref/feat/athletic)|—|+2 bonus on Climb and Swim checks|
|[Blind-Fight](ref/feat/blind-fight)|—|Reroll miss chances for [concealment](ref/rule/concealment)|
|[Combat Reflexes](ref/feat/combat-reflexes)|—|Make additional attacks of opportunity|
|[Devotion Against the Unnatural](ref/feat/devotion-against-the-unnatural)|Animal companion, devotion special ability.|Gain additional resistance to certain creature's abilities|
|[Diehard](ref/feat/diehard)|Endurance.|Automatically stabilize and remain conscious below 0 hp|
|[Disruptive Companion](ref/feat/disruptive-companion)|Animal companion.|Companion hinders spellcasting|
|[Dodge](ref/feat/dodge)|Dex 13.|+1 dodge bonus to AC|
|[Endurance](ref/feat/endurance)|—|+4 bonus on checks to avoid nonlethal damage|
|[Feral Grace](ref/feat/feral-grace)|Weapon Finesse, base attack bonus +3, animal companion.|Gain bonus to damage from fighting with finesse|
|[Ferocious Beast](ref/feat/ferocious-beast)|Intimidate 1 rank, animal companion.|Gain bonuses on Intimidate checks|
|[Ferocious Feint](ref/feat/ferocious-feint)|Bluff 1 rank, animal companion.|Gain bonuses to feint|
|[Friendly Face](ref/feat/friendly-face)|Animal companion.|Animals like you have a better starting attitude towards you and your master|
|[Great Fortitude](ref/feat/great-fortitude)|—|+2 on Fortitude saves|
|[Greater Tenacious Hunter](ref/feat/greater-tenacious-hunter)|Combat Reflexes, Tenacious Hunter, Perception 3 ranks, Stealth 3 ranks, animal companion.|Deny Dexterity bonus to creatures pinpointed|
|[Hefty Brute](ref/feat/hefty-brute)|Animal companion or familiar.|You're treated as one size category larger for size-based abilities|
|[Improved Bull Rush](ref/feat/improved-bull-rush)|Str 13, Power Attack, base attack bonus +1.|+2 bonus on bull rush attempts, no attack of opportunity|
|[Improved Initiative](ref/feat/improved-initiative)|—|+4 bonus on initiative checks|
|[Improved Intercept Blow](ref/feat/improved-intercept-blow)|Intercept Blow, base attack bonus +6, animal companion.|Further reduce damage while using Intercept Blows|
|[Improved Natural Armor](ref/feat/improved-natural-armor)|Natural armor, Con 13.|Increase your natural armor by 1.|
|[Improved Natural Attack](ref/feat/improved-natural-attack)|Natural weapon, base attack bonus +4.|Increase the damage dice for one of your natural attacks.|
|[Improved Overrun](ref/feat/improved-overrun)|Str 13, Power Attack, base attack bonus +1.|+2 bonus on overrun attempts, no attack of opportunity|
|[Intercept Blow](ref/feat/intercept-blow)|Base attack bonus +1, animal companion.|Shield master from attacks|
|[Intimidating Prowess](ref/feat/intimidating-prowess)|—|Add Str to Intimidate in addition to Cha|
|[Iron Will](ref/feat/iron-will)|—|+2 bonus on Will saves|
|[Lightning Reflexes](ref/feat/lightning-reflexes)|—|+2 bonus on Reflex saves|
|[Linnorm Hunter Coordination](ref/feat/linnorm-hunter-coordination)|Cha 13, Dex 13, Dodge, Linnorm Hunter Retreat, Linnorm Hunter Style, base attack bonus +6, must have or be an animal companion.|As a full-round action, you can make a single attack that deals extra damage|
|[Linnorm Hunter Retreat](ref/feat/linnorm-hunter-retreat)|Cha 13, Dex 13, Dodge, Linnorm Hunter Style, base attack bonus +4, must have or be an animal companion.|Move 5 ft. as an immediate action when your ally attacks|
|[Linnorm Hunter Style](ref/feat/linnorm-hunter-style)|Cha 13, must have or be an animal companion.|Enemies that provoke an attack of opportunity from your ally also provoke from you|
|[Mobility](ref/feat/mobility)|Dex 13, Dodge.|+4 AC against attacks of opportunity from movement|
|[Power Attack](ref/feat/power-attack)|Str 13, base attack bonus +1.|Trade melee attack bonus for damage|
|[Reflexive Interception](ref/feat/reflexive-interception)|Intercept Blow, base attack bonus +3, animal companion, evasion.|Provide evasion to master|
|[Run](ref/feat/run)|—|Run at 5 times your normal speed|
|[Share Feature](ref/feat/share-feature)|Animal companion, master must have the chosen class feature.|Gain a class feature from master|
|[Skill Focus](ref/feat/skill-focus)|—|+3 bonus on one skill (+6 at 10 ranks)|
|[Spring Attack](ref/feat/spring-attack)|Dex 13, Dodge, Mobility, base attack bonus +4.|Move before and after melee attack|
|[Stealthy](ref/feat/stealthy)|—|+2 bonus on Escape Artist and Stealth checks|
|[Tenacious Hunter](ref/feat/tenacious-hunter)|Perception 3 ranks, Stealth 3 ranks, animal companion.|Pinpoint invisible creatures|
|[Thrill of the Hunt](ref/feat/thrill-of-the-hunt)|Survival 1 rank; base attack bonus +4 or track class feature.|Designate a creature you are tracking as your prize to gain bonuses against it|
|[Toughness](ref/feat/toughness)|—|+3 hit points, +1 per Hit Die beyond 3|
|[Weapon Focus](ref/feat/weapon-focus)|Proficiency with selected weapon, base attack bonus +1.|+1 bonus on attack rolls with one weapon|

Animal companions with an Intelligence of 3 or higher can select any feat they are physically
capable of using. GMs might expand this list to include feats from other sources.

### Archetypes

**Source** Advanced Player's Guide pg. 72\
From the noble paladin to the skillful rogue, each class draws upon a central archetype. Yet, beyond
that basic concept exists the potential for innumerable interpretations, details, and refinements;
and some archetypes prove pervasive and exciting enough to see use in play time and time again.

To help players interested in creating iconic fantasy characters, **archetypes** were introduced.
These optional features represent a unique view of what a class deliberately designed to capture a
specific character archetype might become. While the types of options presented for each class
differ, each subsystem is customized to best serve that class, emulate the abilities and talents of
classic fantasy archetypes, and expand players' freedom to design exactly the characters they
desire.

**Aberrant Companion**

**Class:** companion

**Modifies or Replaces:** Devotion, Multiattack, Natural Armor Progression, Share Spells

**Description:** Though aberrant companions are touched by eldritch magic or mutated by strange
influences, they are still loyal, if unnatural, allies.

**Accursed Companion**

**Class:** companion

**Modifies or Replaces:** See text

**Description:** When mortals fail to protect their bonded companions, so too shall those mortals
suffer.

**Ambusher**

**Class:** companion

**Modifies or Replaces:** Devotion, Evasion, Improved Evasion, Multiattack, Share Spells

**Description:** Ambushers sneak up on unsuspecting prey, pouncing on targets when they least expect
it.

**Apex Species**

**Class:** companion

**Modifies or Replaces:** Devotion, Evasion, Improved Evasion, Multiattack, Share Spells

**Description:** Some animals are masters of their habitats, perfectly evolved to take advantage of
their native terrain. They need not be predators, of course - some herbivores are just as lethally
suited to their homes.

**Augmented Companion**

**Class:** companion

**Modifies or Replaces:** Devotion, Share Spells

**Description:** Augmented companions have suffered an injury, such as the loss of a wing, and parts
of their bodies have been replaced by a master construct crafter.

**Auspice**

**Class:** companion

**Modifies or Replaces:** Evasion, Improved Evasion, Share Spells

**Description:** Auspices were born with a birthmark or other feature that seems to be in the shape
of their master's deity's holy symbol.

**Bodyguard**

**Class:** companion

**Modifies or Replaces:** Evasion, Improved Evasion, Multiattack, Share Spells

**Description:** Some companions live lives of faithful devotion and steady vigilance, standing
watch through long hours and always ready to leap into action to protect their masters.

**Bully**

**Class:** companion

**Modifies or Replaces:** Multiattack, Share Spells

**Description:** Bigger than others of its kind, a bully is used to winning fights and displays of
dominance for its choice of mates, territory, or other privileges.

**Charger**

**Class:** companion

**Modifies or Replaces:** Devotion, Evasion, Improved Evasion, Multiattack, Share Spells

**Description:** The mighty charger is a boon to heavily armored and armed champions, bearing them
and their ironmongery into battle without hesitation.

**Daredevil**

**Class:** companion

**Modifies or Replaces:** Devotion, Multiattack, Share Spells

**Description:** Daredevil companions join the fray with graceful leaps or swooping dives, heedless
of the danger.

**Deathtouched Companion**

**Class:** companion

**Modifies or Replaces:** Devotion, Share Spells

**Description:** Deathtouched companions are living animals with a trace of the undead, somewhat
like [dhampirs](ref/race/dhampir).

**Draconic Companion**

**Class:** companion

**Modifies or Replaces:** Devotion, Evasion, Improved Evasion, Multiattack, Share Spells

**Description:** Draconic companions bear a faint trace of dragon blood that grants them special
abilities.

**Elemental Companion**

**Class:** companion

**Modifies or Replaces:** Evasion, Improved Evasion, Multiattack

**Description:** The heart of this companion beats with primal energy.

**Feytouched Companion**

**Class:** companion

**Modifies or Replaces:** 4th or 7th-level Advancement, Size Advancement, Devotion, Evasion,
Improved Evasion, Multiattack, Share Spells

**Description:** Feytouched companions are strangely colored fauna native to the First World, the
primal realm of the fey.

**Precocious Companion**

**Class:** companion

**Modifies or Replaces:** 4th or 7th-level Advancement, Evasion, Improved Evasion

**Description:** Precocious companions are able to learn far more tricks than other companions.

**Racer**

**Class:** companion

**Modifies or Replaces:** Devotion, Share Spells

**Description:** Some companions have uncanny speed, providing their masters with swift transport.

**Totem Guide**

**Class:** companion

**Modifies or Replaces:** Devotion, Evasion, Improved Evasion, Multiattack

**Description:** Totem guides embody the wisdom and spirituality of the natural world, providing
guidance as well as aid in combat.

**Tracker**

**Class:** companion

**Modifies or Replaces:** Devotion, Share Spells

**Description:** Some companions are expert trackers, able to use their scent ability to follow any
trail.

**Unexpected Intellectual**

**Class:** companion

**Modifies or Replaces:** Share Spells

**Description:** Sometimes, when an insect or other vermin is chosen to be an animal companion, it
proves cleverer than expected. On occasion, it proves _much_ cleverer.

**Verdant Companion**

**Class:** companion

**Modifies or Replaces:** Devotion, Evasion, Improved Evasion, Share Spells

**Description:** Favorites of druids who balance their responsibilities between flora and fauna,
verdant companions are animals with some of the abilities and physical aspects of plants.

**Wrecker**

**Class:** companion

**Modifies or Replaces:** Share Spells, Multiattack

**Description:** Like unruly pets, some companions have a tendency to destroy nearby objects while
unsupervised, and their masters can channel these destructive impulses into an advantage in battle.
