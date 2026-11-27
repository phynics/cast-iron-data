+++
id = "ref/class/investigator"
kind = "class"
title = "Investigator"
aon = "ClassDisplay.aspx?ItemName=Investigator"
source_ids = ["advanced-class-guide", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "investigator", path = "json/classes2.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "30"
[[sources]]
publication = "chronicle-of-legends"
page = "28-29"

[fields]
kind = "class"
class_type = "hybrid"
hit_die = "d8"
skill_ranks = "6 + Int modifier"
features = [
  { anchor = "alchemy", level = 1 },
  { anchor = "inspiration", level = 1 },
  { anchor = "trapfinding", level = 1 },
  { anchor = "poison-lore", level = 2 },
  { anchor = "poison-resistance", level = 2 },
  { anchor = "investigator-talent", level = 3 },
  { anchor = "keen-recollection", level = 3 },
  { anchor = "trap-sense", level = 3 },
  { anchor = "studied-combat", level = 4 },
  { anchor = "studied-strike", level = 4 },
  { anchor = "swift-alchemy", level = 4 },
  { anchor = "true-inspiration", level = 20 },
]
+++

Whether on the trail of a fugitive, a long-lost treasure trove, or a criminal mastermind,
investigators are motivated by an intense curiosity about the world and use knowledge of it as a
weapon. Mixing gumption and learnedness into a personal alchemy of daring, investigators are full of
surprises. Observing the world around them, they gain valuable knowledge about the situation they're
in, process that information using inspiration and deduction, and cut to the quick of the matter in
unexpected ways. Investigators are always evaluating situations they encounter, sizing up potential
foes, and looking out for secret dangers, all while using their vast knowledge and powers of
perception to find solutions to the most perplexing problems.

**Role:** Investigators live to solve mysteries and find inventive ways to get out of jams. They
serve as advisors and support for their adventuring parties, but can take center stage when
knowledge and cunning are needed. No slouches in battle, they know how to make surprise attacks and
use inspiration to bring those attacks home.

**Alignment:** Any

**Hit Die:** d8

**Parent Class(es):** [Alchemist](ref/class/alchemist) and [rogue](ref/class/rogue).

**Starting Wealth:** 3d6 × 10 gp (average 105 gp)

**Skill Points per Level:** 6 + Int modifier

**Class Skills (Str):** Climb

**Class Skills (Dex):** Acrobatics, Disable Device, Escape Artist, Sleight of Hand, Stealth

**Class Skills (Int):** Appraise, Craft (any), Knowledge (arcana), Knowledge (dungeoneering),
Knowledge (engineering), Knowledge (geography), Knowledge (history), Knowledge (local), Knowledge
(nature), Knowledge (nobility), Knowledge (planes), Knowledge (religion), Linguistics, Spellcraft

**Class Skills (Wis):** Heal, Perception, Profession (any), Sense Motive

**Class Skills (Cha):** Bluff, Diplomacy, Disguise, Intimidate, Perform (any), Use Magic Device

### Class Features and Spells Per Day

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|1st|2nd|3rd|4th|5th|6th|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|+0|+0|+2|+2|Alchemy, inspiration, trapfinding|1|-|-|-|-|-|
|2nd|+1|+0|+3|+3|Poison lore, poison resistance +2|2|-|-|-|-|-|
|3rd|+2|+1|+3|+3|Investigator talent, keen recollection, trap sense +1|3|-|-|-|-|-|
|4th|+3|+1|+4|+4|Studied combat, studied strike +1d6, swift alchemy|3|1|-|-|-|-|
|5th|+3|+1|+4|+4|Investigator talent, poison resistance +4|4|2|-|-|-|-|
|6th|+4|+2|+5|+5|Studied strike +2d6, trap sense +2|4|3|-|-|-|-|
|7th|+5|+2|+5|+5|Investigator talent|4|3|1|-|-|-|
|8th|+6/+1|+2|+6|+6|Poison resistance +6, studied strike +3d6|4|4|2|-|-|-|
|9th|+6/+1|+3|+6|+6|Investigator talent, trap sense +3|5|4|3|-|-|-|
|10th|+7/+2|+3|+7|+7|Studied strike +4d6|5|4|3|1|-|-|
|11th|+8/+3|+3|+7|+7|Investigator talent, poison immunity|5|4|4|2|-|-|
|12th|+9/+4|+4|+8|+8|Studied strike +5d6, trap sense +4|5|5|4|3|-|-|
|13th|+9/+4|+4|+8|+8|Investigator talent|5|5|4|3|1|-|
|14th|+10/+5|+4|+9|+9|Studied strike +6d6|5|5|4|4|2|-|
|15th|+11/+6/+1|+5|+9|+9|Investigator talent, trap sense +5|5|5|5|4|3|-|
|16th|+12/+7/+2|+5|+10|+10|Studied strike +7d6|5|5|5|4|3|1|
|17th|+12/+7/+2|+5|+10|+10|Investigator talent|5|5|5|4|4|2|
|18th|+13/+8/+3|+6|+11|+11|Studied strike +8d6, trap sense +6|5|5|5|5|4|3|
|19th|+14/+9/+4|+6|+11|+11|Investigator talent|5|5|5|5|5|4|
|20th|+15/+10/+5|+6|+12|+12|Studied strike +9d6, true inspiration|5|5|5|5|5|5|

### Class Features {#class-features}

The following are the class features of the investigator.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

Investigators are proficient with simple weapons, plus the hand crossbow, rapier, sap, shortbow,
short sword, and sword cane. They are proficient in light armors, but not shields.

#### Alchemy (Su) {#alchemy}

Investigators are highly trained in the creation of mundane alchemical substances and magical
potionlike extracts.

When using Craft (alchemy) to create an alchemical item, an investigator gains a competence bonus
equal to his class level on the skill check. In addition, an investigator can use Craft (alchemy) to
identify potions as if using _[detect magic](ref/spell/detect-magic)_. He must hold the potion for 1
round to attempt such a check.

Like an alchemist, an investigator prepares his spells by mixing ingredients and a tiny fraction of
his own magical power into a number of extracts, and then effectively casts the spell by drinking
the extract. These extracts have powerful effects, but they are also bound to their creator.
Extracts behave like spells in potion form, and as such their effects can be dispelled by
_[dispel magic](ref/spell/dispel-magic)_ and similar effects, using the investigator's level as the
caster level.

An investigator can create only a certain number of extracts of each level per day. His base daily
allotment of extracts per day is given on Table 1–8: Investigator. In addition, he receives
[bonus extracts per day](ref/rule/determine-bonuses) if he has a high Intelligence score, in the
same way a wizard receives bonus spells per day.

When an investigator mixes an extract, he infuses the chemicals and reagents in the extract with
magic siphoned from his own magical aura. An extract immediately become inert if it leaves the
investigator's possession, reactivating as soon as it returns to his keeping—an investigator cannot
normally pass out his extracts for allies to use. An extract, once created, remains potent for 1 day
before losing its magic, so an investigator must reprepare his extracts every day. Mixing an extract
takes 1 minute of work.

Creating extracts consumes raw material, but the cost of those materials is insignificant—comparable
to the valueless material components of most spells. If a spell normally has a costly material
component, that component is expended during the consumption of that particular extract. Extracts
cannot be made from spells that have focus requirements; extracts that duplicate divine spells never
have a divine focus requirement.

An investigator uses the alchemist formula list (_Pathfinder RPG Advanced Player's Guide_ 32) to
determine the extracts he can know. An investigator can prepare an extract of any formula he knows.
To learn or use an extract, an investigator must have at least an Intelligence score equal to 10 +
the extract's level. The saving throw DC for an investigator's extract is equal to 10 + the
extract's level + the investigator's Intelligence modifier.

An investigator may know any number of formulae. He stores his formulae in a special tome called a
formula book. He must refer to this book whenever he prepares an extract. At 1st level, an
investigator starts with two 1st-level formulae of his choice, plus a number of additional formulae
equal to his Intelligence modifier. At each new investigator level, he gains one new formula for any
level that he can create. An investigator can also add formulae to his book just like a wizard
[adds spells to his spellbook](ref/rule/adding-spells-to-a-wizards-spellbook), using the same costs,
pages, and time requirements. A formula book costs as much as a [spellbook](ref/eq-misc/spellbook).
An investigator can study a [wizard's](ref/class/wizard) spellbook to learn any formula that is
equivalent to a spell the spellbook contains. A wizard, however, cannot learn spells from a formula
book. An investigator can also learn formulae from another investigator's or an alchemist's formula
book (and vice versa). An investigator does not need to decipher arcane writing before copying that
formulae.

#### Inspiration (Ex) {#inspiration}

An investigator is beyond knowledgeable and skilled—he also possesses keen powers of observation and
deduction that far surpass the abilities of others. An investigator typically uses these powers to
aid in their investigations, but can also use these flashes of inspiration in other situations.

An investigator has the ability to augment skill checks and ability checks through his brilliant
inspiration. The investigator has an inspiration pool equal to 1/2 his investigator level + his
Intelligence modifier (minimum 1). An investigator's inspiration pool refreshes each day, typically
after he gets a restful night's sleep. As a free action, he can expend one use of inspiration from
his pool to add 1d6 to the result of that check, including any on which he takes 10 or 20. This
choice is made after the check is rolled and before the results are revealed. An investigator can
only use inspiration once per check or roll. The investigator can use inspiration on any Knowledge,
Linguistics, or Spellcraft skill checks without expending a use of inspiration, provided he's
trained in the skill.

Inspiration can also be used on attack rolls and saving throws, at the cost of expending two uses of
inspiration each time from the investigator's pool. In the case of saving throws, using inspiration
is an immediate action rather than a free action.

#### Trapfinding {#trapfinding}

An investigator adds 1/2 his level to Perception skill checks made to locate traps and to Disable
Device checks (minimum 1). An investigator can use Disable Device to disarm magical traps.

#### Poison Lore (Ex) {#poison-lore}

An investigator has a deep understanding and appreciation for poisons. At 2nd level, he cannot
accidentally poison himself when applying poison to a weapon. If the investigator spends 1 minute
physically examining the poison, he can attempt a Knowledge (nature) check to identify any natural
poison or Knowledge (arcana) check to identify any magical poison (DC = the poison's saving throw
DC). Lastly, once a poison is identified, he can spend 1 minute and attempt a Craft (alchemy) check
(DC = the poison's saving throw DC) to neutralize 1 dose of the poison. Success renders the dose
harmless. The investigator has no chance of accidentally poisoning himself when examining or
attempting to neutralize a poison.

#### Poison Resistance (Ex) {#poison-resistance}

At 2nd level, an investigator gains a +2 bonus on all saving throws against poison. This bonus
increases to +4 at 5th level, and to +6 at 8th level. At 11th level, the investigator becomes
completely immune to poison.

#### Investigator Talent (Ex or Su) {#investigator-talent}

At 3rd level and every 2 levels thereafter, an investigator gains an investigator talent. Except
where otherwise noted, each investigator talent can only be selected once.

Investigator talents marked with an asterisk (\*) add effects to an investigator's studied combat or
studied strike. Only one of these talents can be applied to an individual attack, but the decision
can be made when the damage is dealt.

- [Alchemist Discovery (Ex)](ref/invtalent/alchemist-discovery)
- [Amazing Inspiration (Ex)](ref/invtalent/amazing-inspiration)
- [Blinding Strike (Ex)](ref/invtalent/blinding-strike)
- [Combat Inspiration (Ex)](ref/invtalent/combat-inspiration)
- [Confusing Strike (Ex)](ref/invtalent/confusing-strike)
- [Deafening Strike (Ex)](ref/invtalent/deafening-strike)
- [Device Talent (Ex)](ref/invtalent/device-talent)
- [Effortless Aid (Ex)](ref/invtalent/effortless-aid)
- [Eidetic Recollection (Su)](ref/invtalent/eidetic-recollection)
- [Empathy (Ex, Su)](ref/invtalent/empathy)
- [Expanded Inspiration (Ex)](ref/invtalent/expanded-inspiration)
- [Greater Combat Inspiration (Ex)](ref/invtalent/greater-combat-inspiration)
- [Hidden Agendas (Ex)](ref/invtalent/hidden-agendas)
- [Inspirational Expertise (Ex)](ref/invtalent/inspirational-expertise)
- [Inspired Alertness (Ex)](ref/invtalent/inspired-alertness)
- [Inspired Intelligence (Ex)](ref/invtalent/inspired-intelligence)
- [Inspired Intimidator (Ex)](ref/invtalent/inspired-intimidator)
- [Item Lore (Ex)](ref/invtalent/item-lore)
- [Perceptive Tracking (Ex)](ref/invtalent/perceptive-tracking)
- [Quick Study (Ex)](ref/invtalent/quick-study)
- [Repositioning Strike (Ex)](ref/invtalent/repositioning-strike)
- [Rogue Talent (Ex)](ref/invtalent/rogue-talent)
- [Sapping Offensive (Ex)](ref/invtalent/sapping-offensive)
- [Sickening Offensive (Ex)](ref/invtalent/sickening-offensive)
- [Stealing Strike (Ex)](ref/invtalent/stealing-strike)
- [Studied Defense (Ex)](ref/invtalent/studied-defense)
- [Tenacious Inspiration (Ex)](ref/invtalent/tenacious-inspiration)
- [Toppling Strike (Ex)](ref/invtalent/toppling-strike)
- [Unconventional Inspiration (Ex)](ref/invtalent/unconventional-inspiration)
- [Underworld Inspiration (Ex)](ref/invtalent/underworld-inspiration)

#### Keen Recollection {#keen-recollection}

At 3rd level, an investigator can attempt all Knowledge skill checks untrained.

#### Trap Sense (Ex) {#trap-sense}

At 3rd level, an investigator gains an intuitive sense that alerts him to danger from traps,
granting him a +1 bonus on Reflex saving throws to avoid traps and a +1 dodge bonus to AC against
attacks by traps. At 6th level and every 3 levels thereafter, these bonuses increase by 1 (to a
maximum of +6 at 18th level).

#### Studied Combat (Ex) {#studied-combat}

With a keen eye and calculating mind, an investigator can assess the mettle of his opponent to take
advantage of gaps in talent and training. At 4th level, an investigator can use a move action to
study a single enemy that he can see. Upon doing so, he adds 1/2 his investigator level as an
insight bonus on melee attack rolls and as a bonus on damage rolls against the creature. This effect
lasts for a number of rounds equal to his Intelligence modifier (minimum 1) or until he deals damage
with a studied strike, whichever comes first. The bonus on damage rolls is precision damage, and is
not multiplied on a critical hit.

An investigator can only have one target of studied combat at a time, and once a creature has become
the target of an investigator's studied combat, he cannot become the target of the same
investigator's studied combat again for 24 hours unless the investigator expends one use of
inspiration when taking the move action to use this ability.

#### Studied Strike (Ex) {#studied-strike}

At 4th level, an investigator can choose to make a studied strike against the target of his studied
combat as a free action, upon successfully hitting his studied target with a melee attack, to deal
additional damage. The damage is 1d6 at 4th level, and increases by 1d6 for every 2 levels
thereafter (to a maximum of 9d6 at 20th level). The damage of studied strike is precision damage and
is not multiplied on a critical hit; creatures that are immune to sneak attacks are also immune to
studied strike.

If the investigator's attack used a weapon that deals nonlethal damage (like a
[sap](ref/eq-weapon/sap), [whip](ref/eq-weapon/whip), or an unarmed strike), he may choose to have
the additional damage from studied strike be nonlethal damage instead of lethal damage. If the
investigator chose to make an attack with a lethal weapon instead deal nonlethal damage (with the
usual -4 penalty), the studied strike damage may also deal nonlethal damage.

The investigator must be able to see the target well enough to pick out a vital spot and must be
able to reach such a spot. An investigator cannot use studied strike against a creature with
[concealment](ref/rule/concealment).

#### Swift Alchemy (Ex) {#swift-alchemy}

At 4th level, an investigator can create alchemical items with astounding speed. It takes an
investigator half the normal amount of time to create alchemical items. He can also apply poison to
a weapon as a move action instead of a standard action.

#### True Inspiration (Ex) {#true-inspiration}

At 20th level, an investigator can use inspiration on all skill checks—even ones he isn't trained
in—and all ability checks without spending inspiration.

In addition, whenever he expends inspiration on an ability check, attack roll, saving throw, or
skill check, he adds 2d6 rather than 1d6 to the result. Some talents can affect this. If using the
[amazing inspiration](ref/invtalent/amazing-inspiration) investigator talent, he rolls 2d8 instead.
If using this with [empathy](ref/invtalent/empathy),
[tenacious inspiration](ref/invtalent/tenacious-inspiration),
[underworld inspiration](ref/invtalent/underworld-inspiration), or a similar talent, he rolls two
sets of inspiration dice and uses the higher of the two results.

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

**Deadly Study (Ex)**

At 20th level, the investigator knows just how to hit where it hurts. The investigator increases the
bonus from studied combat by 4, and his studied strike damage increases by 3d6.

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

**Antiquarian**

**Class:** investigator

**Modifies or Replaces:** Alchemy; Poison Lore; Poison Resistance; Poison Immunity; Swift Alchemy

**Description:** Antiquarians are collectors, explorers, and scholars who delve into ruined places
in search of lost lore and artifacts.

**Bonded Investigator**

**Class:** investigator

**Modifies or Replaces:** Poison Lore; Poison Resistance; Poison Immunity; 4th-level Studied Strike,
7th-level Investigator Talent

**Description:** Bonded investigators use intelligent familiars to assist them in their
investigations.

**Cartographer**

**Class:** investigator

**Modifies or Replaces:** Poison Lore; Poison Resistance; Keen Recollection; Swift Alchemy

**Description:** Cartographers are eager trailblazers who explore uncharted terrain, study
landmarks, and find new paths through the wilderness.

**Cipher**

**Class:** investigator

**Modifies or Replaces:** Class Skills; Inspiration; Trapfinding; Poison Lore; Poison Resistance;
Poison Immunity; Trap Sense; Swift Alchemy; 3rd, 5th, 7th, 9th, 11th-level Investigator Talent;
Studied Strike

**Description:** A cipher trains himself to remain undetected and ignored in order to conduct his
investigations without opposition or bothersome questions

**Conspirator**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Inspiration; Trap Sense; 7th-level Investigator Talent

**Description:** A conspirator uses his knowledge of investigations to make sure he avoids any
investigations that his rivals perform.

**Cryptid Scholar**

**Class:** investigator

**Modifies or Replaces:** Poison Lore; Poison Resistance; Studied Combat; Studied Strike

**Description:** Cryptid scholars research monsters that lurk secretly at the edge of civilization,
developing a deep expertise regarding their anatomy, habits, and ecology.

**Cult Hunter**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Resistance; Poison Immunity; Poison Lore; Trap Sense;
Swift Alchemy; Studied Combat; Studied Strike; 7th, 13th-level Investigator Talent

**Description:** Cult hunters seek out heretical secret societies, purging their ideological taint
and banishing summoned servants.

**Dread Investigator**

**Class:** investigator

**Modifies or Replaces:** Inspiration; Studied Combat; Studied Strike; Poison Lore; Poison
Resistance; Poison Immunity; 7th, 13th, and 19th-level Talents

**Description:** The dread investigator observes human behavior after the fact, honing their
intuition by delving into the mysteries of death.

**Empiricist**

**Class:** investigator

**Modifies or Replaces:** Poison Lore; Poison Resistance; Swift Alchemy; True Inspiration

**Description:** Champions of deductive reasoning and logical insight, empiricists put their faith
in facts, data, confirmed observations, and consistently repeatable experiments - these things are
their currency of truth.

**Engineer**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Lore; Poison Resistance; Trap Sense

**Description:** A number of investigators use their vast knowledge to build machines that replicate
the intricacies of the world

**Forensic Physician**

**Class:** investigator

**Modifies or Replaces:** Inspiration; Trapfinding; Trap Sense; 3rd, 5th-level Investigator Talent

**Description:** A forensic physician specializes in analyzing medical details in order to solve
crimes and uncover evidence.

**Gravedigger**

**Class:** investigator

**Modifies or Replaces:** Weapon and Armor Proficiency; Alchemy; Trapfinding; Trap Sense; Poison
Resistance; Poison Immunity; Studied Combat; Studied Strike; Swift Alchemy

**Description:** Gravediggers pursue long buried mysteries, figuratively and literally digging up
the truth and finding answers to secrets only moldering corpses and dry bones can tell.

**Guardian of Immortality**

**Class:** investigator

**Modifies or Replaces:** Poison Lore; Poison Resistance; 7th, 13th-level Investigator Talent;
Poison Immunity

**Description:** Guardians of immortality are Thuvian investigators charged with hunting down those
who would attempt to steal or learn for themselves the secret to creating the sun orchid elixir.

**Hallucinist**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Trap Sense; 3rd, 5th, 7th, 9th, 11th, 15th-level Investigator
Talent; Poison Lore; Poison Resistance; Poison Immunity; Keen Recollection; Studied Combat

**Description:** A hallucinist imbibes magical drugs to expand his mind into the psychedelic world,
extending his awareness to things he could not normally perceive.

**Holomog Demolitionist**

**Class:** investigator

**Modifies or Replaces:** Poison Lore; Poison Resistance; 3rd, 9th-level Investigator Talent;
Studied Strike

**Description:** Holomog is an ancient nation built on even more ancient ruins. Its renowned civil
engineers develop skills that allow them to take full advantage of their environments.

**Infiltrator**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Lore; Poison Resistance

**Description:** An infiltrator specializes in investigating or disrupting groups from within.

**Jinyiwei**

**Class:** investigator

**Modifies or Replaces:** Inspiration; Alchemy; Trapfinding; Trap Sense; Swift Alchemy

**Description:** Jinyiwei are a special task force of secret police whose mission is to root out,
expose, and counteract their government's existing wrongdoing.

**Lamplighter**

**Class:** investigator

**Modifies or Replaces:** Class Skills; Poison Lore; Poison Resistance; Poison Immunity; Keen
Recollection; Trap Sense

**Description:** Lamplighters are investigators tasked with keeping the night streets safe and lit,
and securing darkened areas against whatever dangers lurk in the shadows.

**Lepidstadt Inspector**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Trap Sense; Poison Resistance; Poison Immunity; Swift
Alchemy; 5th-level Investigator Talent

**Description:** The ability of investigators trained at the University of Lepidstadt to get to the
bottom of a mystery is legendary, and troubled settlements throughout the region often send
petitions to the university requesting the aid of a formally trained inspector when some mystery
threatens the community as a whole.

**Majordomo**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Alchemy; Swift Alchemy; Trap Sense

**Description:** In a world of intrigue where the loyalties of staff can be bought and sold,
sometimes it takes the skills of an investigator to follow the byzantine paper trails and prevent
embezzling and espionage within the estates of the elite.

**Malice Binder**

**Class:** investigator

**Modifies or Replaces:** Inspiration; Trapfinding; Trap Sense; Alchemy; Poison Resistance; Poison
Immunity

**Description:** A lock of hair, a bit of blood, even a footprint is enough to grant a wily witch
hunter an edge. Malice binders often rise from the ranks of the common folk rather than from wealthy
nobles or the church. Their magic is old and crude, but devastatingly effective against those they
hunt.

**Mastermind**

**Class:** investigator

**Modifies or Replaces:** Inspiration; Trapfinding; Trap Sense; Swift Alchemy; 9th-level
Investigator Talent

**Description:** Although some investigators use their honed senses and cunning insight for personal
gain, no one excels at such endeavors like the mastermind.

**Natural Philosopher**

**Class:** investigator

**Modifies or Replaces:** Weapon/Armor Proficiencies; Class Skills; Inspiration; Trapfinding;
Alchemy; Trap Sense; 3rd-level Investigator Talent

**Description:** Natural philosophers are scholars, explorers, and survivalists who feel at home in
nature, seldom longing for the comforts of the city.

**Portal Seeker**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Resistance; Poison Lore; Studied Strike; Poison
Immunity

**Description:** While most investigators seek answers to mundane mysteries, portal seekers chase
more unusual enigmas: portals to other planes.

**Profiler**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Lore; Trap Sense; Poison Resistance; Poison Immunity;
Swift Alchemy; 7th-level Investigator Talent

**Description:** Profilers understand the human psyche to an intense degree, allowing them to
predict the criminals they hunt.

**Psychic Detective**

**Class:** investigator

**Modifies or Replaces:** Class Skills; Alchemy; Poison Lore; Poison Resistance; Swift Alchemy;
Poison Immunity; 3rd-level Talent; Investigator Talents

**Description:** A psychic detective supplements her keen insight with occult skill to unravel
mysteries both ordinary and supernatural.

**Questioner**

**Class:** investigator

**Modifies or Replaces:** Inspiration; Alchemy; Poison Lore

**Description:** Dabblers in arcane magic and masters of stealth and guile, questioners are
investigators who often find themselves mucking about in cases for less-than-savory clientele or
that require an extra bit of subtlety.

**Reckless Epicurean**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; 5th, 13th-level Investigator Talent; Poison Resistance;
Poison Immunity

**Description:** Whether an obsessive scientist, a healer determined to ensure the safety of her
tinctures, or a seeker of new and interesting potions, a reckless epicurean's body is saturated with
experimental chemicals and magic.

**Ruthless Agent**

**Class:** investigator

**Modifies or Replaces:** Alignment; Inspiration; Trapfinding; Trap Sense; Swift Alchemy; 11th,
17th-level Investigator Talents

**Description:** Ruthless agents are often called upon for their skills at extracting information by
any means necessary.

**Scavenger**

**Class:** investigator

**Modifies or Replaces:** Alchemy; Inspiration; Poison Lore; Poison Resistance; Poison Immunity

**Description:** (Ratfolk archetype) Scavengers are masters of systems: how they fit together, why
they work, and how to make the most of their parts.

**Skeptic**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Resistance; Swift Alchemy; 7th level Investigator
Talent

**Description:** The skeptic accepts the existence of the occult world while challenging claims that
the supernatural explains all of life's problems.

**Sleuth**

**Class:** investigator

**Modifies or Replaces:** Alchemy; Swift Alchemy

**Description:** A sleuth is an investigator who relies on good fortune and guile rather than
alchemy.

**Spiritualist**

**Class:** investigator

**Modifies or Replaces:** Alchemy; Poison Lore; Poison Resistance; Trap Sense; Swift Alchemy; Poison
Immunity

**Description:** While most investigators look to the physical world to gain their knowledge, there
are those who seek out knowledge beyond the pale.

**Star Watcher**

**Class:** investigator

**Modifies or Replaces:** Weapon/Armor Proficiencies; Alchemy; Trapfinding; Trap Sense; Swift
Alchemy

**Description:** Star watchers study the movements and positions of the sun, the moon, and the
stars, searching for secrets written in the sky.

**Steel Hound**

**Class:** investigator

**Modifies or Replaces:** Weapon/Armor Proficiencies; Poison Lore; Swift Alchemy

**Description:** Steel hounds are investigators who have taken to using firearms in place of the
more mundane weapons their counterparts favor.

**Tekritanin Arbiter**

**Class:** investigator

**Modifies or Replaces:** Trapfinding; Poison Lore; Poison Resistance; Trap Sense

**Description:** The Tekritanin League facilitated trade and settled disputes between a vast array
of diverse cultures. The arbiters were the first line of diplomatic defense, solving problems before
they could become disruptive.

**Toxin Codexer**

**Class:** investigator

**Modifies or Replaces:** Alchemy; Trapfinding; 3rd-level Investigator Talent; Keen Recollection;
Trap Sense

**Description:** A toxin codexer meticulously seeks out new poisons and catalogs their effects, both
those that are harmful and those that are potentially beneficial.

### Archetypes by Feature

|Archetype|Alchemy|Alignment|Class Skills|Inspiration|Investigator Talents|3rd-level Talent|5th-level Talent|7th-level Talent|9th-level Talent|11th-level Talent|13th-level Talent|15th-level Talent|17th-level Talent|19th-level Talent|Keen Recollection|Poison Lore|Poison Resistance|Poison Immunity|Studied Combat|Studied Strike|4th-level Studied Strike|Swift Alchemy|Trapfinding|Trap Sense|True Inspiration|Weapon/_wbr_Armor Proficiency|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Antiquarian](ref/arc-investigator/antiquarian)|X|||||||||||||||X|X|X||||X|||||
|[Bonded Investigator](ref/arc-investigator/bonded-investigator)||||||||X||||||||X|X|X|||X||||||
|[Cartographer](ref/arc-investigator/cartographer)|||||||||||||||X|X|X|||||X|||||
|[Cipher](ref/arc-investigator/cipher)|||X|X||X|X|X|X|X||||||X|X|X||X||X|X|X|||
|[Conspirator](ref/arc-investigator/conspirator)||||X||||X|||||||||||||||X|X|||
|[Cryptid Scholar](ref/arc-investigator/cryptid-scholar)||||||||||||||||X|X||X|X|||||||
|[Cult Hunter](ref/arc-investigator/cult-hunter)||||||||X|||X|||||X|X|X|X|X||X|X|X|||
|[Dread Investigator](ref/arc-investigator/dread-investigator)||||X||||X|||X|||X||X|X|X|X|X|||||||
|[Empiricist](ref/arc-investigator/empiricist)||||||||||||||||X|X|||||X|||X||
|[Engineer](ref/arc-investigator/engineer)||||||||||||||||X|X||||||X|X|||
|[Forensic Physician](ref/arc-investigator/forensic-physician)||||X||X|X||||||||||||||||X|X|||
|[Gravedigger](ref/arc-investigator/gravedigger)|X||||||||||||||||X|X|X|X||X|X|X||X|
|[Guardian of Immortality](ref/arc-investigator/guardian-of-immortality)||||||||X|||X|||||X|X|X|||||||||
|[Hallucinist](ref/arc-investigator/hallucinist)||||||X|X|X|X|X||X|||X|X|X|X|X||||X|X|||
|[Holomog Demolitionist](ref/arc-investigator/holomog-demolitionist)||||||X|||X|||||||X|X|||X|||||||
|[Infiltrator](ref/arc-investigator/infiltrator)||||||||||||||||X|X||||||X||||
|[Jinyiwei](ref/arc-investigator/jinyiwei)|X|||X||||||||||||||||||X|X|X|||
|[Lamplighter](ref/arc-investigator/lamplighter)|||X||||||||||||X|X|X|X||||||X|||
|[Lepidstadt Inspector](ref/arc-investigator/lepidstadt-inspector)|||||||X||||||||||X|X||||X|X|X|||
|[Majordomo](ref/arc-investigator/majordomo)|X|||||||||||||||||||||X|X|X|||
|[Malice Binder](ref/arc-investigator/malice-binder)|X|||X|||||||||||||X|X|||||X|X|||
|[Mastermind](ref/arc-investigator/mastermind)||||X|||||X|||||||||||||X|X|X|||
|[Natural Philosopher](ref/arc-investigator/natural-philosopher)|X||X|X||X|||||||||||||||||X|X||X|
|[Portal Seeker](ref/arc-investigator/portal-seeker)||||||||||||||||X|X|X||X|||X||||
|[Profiler](ref/arc-investigator/profiler)||||||||X||||||||X|X|X||||X|X|X|||
|[Psychic Detective](ref/arc-investigator/psychic-detective)|X||X||X|X||||||||||X|X|X||||X|||||
|[Questioner](ref/arc-investigator/questioner)|X|||X||||||||||||X|||||||||||
|[Reckless Epicurean](ref/arc-investigator/reckless-epicurean)|||||||X||||X||||||X|X|||||X||||
|[Ruthless Agent](ref/arc-investigator/ruthless-agent)||X||X||||||X|||X|||||||||X|X|X|||
|[Scavenger](ref/arc-investigator/scavenger)|X|||X||||||||||||X|X|X|||||||||
|[Skeptic](ref/arc-investigator/skeptic)||||||||X|||||||||X|||||X|X||||
|[Sleuth](ref/arc-investigator/sleuth)|X|||||||||||||||||||||X|||||
|[Spiritualist](ref/arc-investigator/spiritualist)|X|||||||||||||||X|X|X||||X||X|||
|[Star Watcher](ref/arc-investigator/star-watcher)|X|||||||||||||||||||||X|X|X||X|
|[Steel Hound](ref/arc-investigator/steel-hound)||||||||||||||||X||||||X||||X|
|[Tekritanin Arbiter](ref/arc-investigator/tekritanin-arbiter)||||||||||||||||X|X||||||X|X|||
|[Toxin Codexer](ref/arc-investigator/toxin-codexer)|X|||||X|||||||||X||||||||X|X|||

### Favored Class Bonuses

_The favored class options for investigator are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
