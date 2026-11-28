+++
id = "ref/class/occultist"
kind = "class"
title = "Occultist"
aon = "ClassDisplay.aspx?ItemName=Occultist"
source_ids = ["occult-adventures", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "occultist", path = "json/classes3.json" },
]
[[sources]]
publication = "occult-adventures"
page = "46"
[[sources]]
publication = "chronicle-of-legends"
page = "28-29"

[fields]
kind = "class"
class_type = "occult"
hit_die = "d8"
skill_ranks = "4 + Int modifier"
features = [
  { anchor = "spells" },
  { anchor = "knacks", level = 1 },
  { anchor = "implements", level = 1 },
  { anchor = "mental-focus", level = 1 },
  { anchor = "focus-powers", level = 1 },
  { anchor = "magic-item-skill", level = 2 },
  { anchor = "object-reading", level = 2 },
  { anchor = "shift-focus", level = 4 },
  { anchor = "aura-sight", level = 5 },
  { anchor = "magic-circles", level = 8 },
  { anchor = "outside-contact", level = 8 },
  { anchor = "binding-circles", level = 12 },
  { anchor = "fast-circles", level = 16 },
  { anchor = "implement-mastery", level = 20 },
]
+++

The occultist focuses on the world around him, grounded in the powers that flow throughout his
environment. He studies the magic that infuses everything, from psychic resonances left in everyday
items to powerful incantations that fuel the mightiest spells.

The occultist channels his psychic might through implements - items that allow him to focus his
power and produce incredible effects. For him, implements are more than simple tools. They are a
repository of history and a tie to the events of the past. The occultist uses these implements to
influence and change the present, adding his legend to theirs. Though some of these implements might
be magic items in their own right, most of them are merely of historical or personal significance to
the occultist.

**Role:** Occultists are always eager to travel in the company of adventurers, explorers, and
archaeologists, as those three groups of people have a knack for finding items with rich histories
and great significance.

**Alignment:** Any

**Hit Die:** d8

**Starting Wealth:** 4d6 × 10 gp (average 140 gp)

**Skill Points per Level:** 4 + Int modifier

**Class Skills (Dex):** Disable Device, Fly, Sleight of Hand

**Class Skills (Int):** Appraise, Craft (any), Knowledge (arcana), Knowledge (engineering),
Knowledge (history), Knowledge (planes), Knowledge (religion), Linguistics, Spellcraft

**Class Skills (Wis):** Perception, Profession (any), Sense Motive

**Class Skills (Cha):** Diplomacy, Disguise, Use Magic Device

### Class Features and Spells Per Day

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|1st|2nd|3rd|4th|5th|6th|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|+0|+2|+0|+2|Focus powers, implements 2, knacks, mental focus|1|-|-|-|-|-|
|2nd|+1|+3|+0|+3|Implements 3, magic item skill, object reading|2|-|-|-|-|-|
|3rd|+2|+3|+1|+3|Focus power|3|-|-|-|-|-|
|4th|+3|+4|+1|+4|Shift focus|3|1|-|-|-|-|
|5th|+3|+4|+1|+4|Aura sight, focus power|4|2|-|-|-|-|
|6th|+4|+5|+2|+5|Implements 4|4|3|-|-|-|-|
|7th|+5|+5|+2|+5|Focus power|4|3|1|-|-|-|
|8th|+6/+1|+6|+2|+6|Magic circles, outside contact 1|4|4|2|-|-|-|
|9th|+6/+1|+6|+3|+6|Focus power|5|4|3|-|-|-|
|10th|+7/+2|+7|+3|+7|Implements 5|5|4|3|1|-|-|
|11th|+8/+3|+7|+3|+7|Focus power|5|4|4|2|-|-|
|12th|+9/+4|+8|+4|+8|Binding circles, outside contact 2|5|5|4|3|-|-|
|13th|+9/+4|+8|+4|+8|Focus power|5|5|4|3|1|-|
|14th|+10/+5|+9|+4|+9|Implements 6|5|5|4|4|2|-|
|15th|+11/+6/+1|+9|+5|+9|Focus power|5|5|5|4|3|-|
|16th|+12/+7/+2|+10|+5|+10|Fast circles, outside contact 3|5|5|5|4|3|1|
|17th|+12/+7/+2|+10|+5|+10|Focus power|5|5|5|4|4|2|
|18th|+13/+8/+3|+11|+6|+11|Implements 7|5|5|5|5|4|3|
|19th|+14/+9/+4|+11|+6|+11|Focus power|5|5|5|5|5|4|
|20th|+15/+10/+5|+12|+6|+12|Implement mastery, outside contact 4|5|5|5|5|5|5|

### Class Features {#class-features}

The following are the class features of the occultist.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

An occultist is proficient with all simple and martial weapons, light armor, medium armor, and
shields (except tower shields).

#### Spells {#spells}

An occultist casts psychic spells drawn from the occultist spell list presented on page 58, limited
by the implement groups he knows.

He can cast any spell he knows without preparing it ahead of time. Every occultist spell has an
implement component (see Implements on page 47). To learn or cast a spell, an occultist must have an
Intelligence score equal to at least 10 + the spell level. The Difficulty Class for a saving throw
against an occultist's spell equals 10 + the spell level + the occultist's Intelligence modifier.

An occultist can cast only a certain number of spells of each spell level per day. His base daily
spell allotment is given on Table 1–6: Occultist. In addition, he gains bonus spells per day if he
has a high Intelligence score (see Table 1–3 on page 17 of the _Pathfinder RPG Core Rulebook_).

The occultist's selection of spells is limited. For each implement school he learns to use, he can
add one spell of each level he can cast to his list of spells known, chosen from that school's spell
list. If he selects the same implement school multiple times, he adds one spell of each level from
that school's list for each time he has selected that school. When the occultist learns to cast a
new level of spells, he immediately adds one spell of that level to his list of spells known from
each implement school he knows (plus any extra spells from schools he has selected multiple times).

At 5th level and every 3 occultist levels thereafter (8th, 11th, and so on), an occultist can choose
to learn a new spell in place of one he already knows. In effect, the occultist loses the old spell
in exchange for the new one. The new spell's level must be the same as that of the spell being
exchanged, and it must be at least one level lower than the highest-level occultist spell the
occultist can cast. The spell learned must come from the same list of spells provided by the
implement school of the spell lost. An occultist can swap only a single spell at any given level,
and must choose whether or not to swap the spell at the same time that he gains new spells known for
that level.

An occultist need not prepare his spells in advance. He can cast any spell he knows at any time,
assuming he has not yet used up his allotment of spells per day for the spell's level.

#### Knacks {#knacks}

An occultist learns one knack, or 0-level psychic spell, each time he selects an implement school
(including when he again selects a school that he has already learned to use). These spells are cast
like any other spell, but they can be cast any number of times per day. Knacks cast using any other
spell slots because of metamagic feats applied to them, for example, consume spell slots as normal.

#### Implements (Su) {#implements}

At 1st level, an occultist learns to use two [implement schools](ref/ability/implements). At 2nd
level and every 4 occultist levels thereafter, the occultist learns to use one additional implement
school, to a maximum of seven schools at 18th level. Each implement school adds one spell per spell
level of that school of magic to the occultist's spell list. No spells from any other school are
considered to be on the occultist's spell list until he selects the associated implement school. He
can't use spell trigger or spell completion magic items from unknown schools without succeeding at
the appropriate Use Magic Device check. An occultist can select an implement school more than once
in order to learn additional spells from the associated school.

Each implement school is represented by a small list of objects. Every day, the occultist selects
one item from that school's list to be his implement for the day for each implement school he knows.
The occultist needs only one such item to cast spells of the corresponding school, unless he
selected that implement school multiple times, in which case he needs one item for each set of
spells gained from that school. Implements don't need to be magic items, and nonmagical implements
don't take up a magic item slot even if they're worn. Implements that are not magic items are often
of some historical value or of personal significance to the occultist, such as the finger bone of a
saint, the broken scepter of a long-dead king, the skull of a mentor's familiar, or the glass eye of
an uncanny ancestor.

Whenever an occultist casts a spell, he must have the corresponding implement in his possession and
present the implement to the target or toward the area of effect. This act is part of casting the
spell and doesn't require any additional action. If the occultist lacks the corresponding implement,
he can attempt to cast the spell, but must succeed at a [concentration](ref/rule/concentration)
check (DC = 20 + the spell's level) to do so. Spells cast by an occultist without the appropriate
implement are always treated as if they were cast at the minimum caster level for the spell in
question (caster level 1st for a 1st-level spell, caster level 4th for a 2nd-level spell, and so
on).

Each implement school also grants a base focus power. This power is added to the list of focus
powers possessed by the occultist (see Mental Focus below). In addition, each implement school
grants access to a number of other focus powers that the occultist can select from using his mental
focus class feature.

See the Implement Schools section starting on page 50 for a complete list of implements associated
with each school and their focus powers.

#### Mental Focus (Su) {#mental-focus}

An occultist can invest a portion of his mental focus into his chosen implements for the day,
allowing him to utilize a variety of abilities depending on the implements and the amount of mental
focus invested in them. An occultist has a number of points of mental focus equal to his occultist
level + his Intelligence modifier; these points refresh each day. He can divide this mental focus
between his implements in any way he desires. If an implement is lost or destroyed, the focus
invested in it is lost as well, though the occultist still refreshes those points of focus normally.

Once mental focus is invested inside an implement, the implement gains the resonant power of its
implement school (see page 50), and the occultist can expend the mental focus stored in the
implement to activate the associated focus powers he knows. If a resonant power grants a bonus that
varies based on the amount of mental focus invested in the implement, the bonus is determined when
the focus is invested, and is not reduced or altered by expending the mental focus invested in the
item. Once all of the mental focus in an implement has been expended, it loses its resonant power
until mental focus is once again invested in the implement.

The implement grants its resonant power to whoever possesses it; the occultist can lend the
implement to an ally to assist that ally, but if he does so, he has difficulty casting that
implement's spells (see Implements on page 47) and can't expend that implement's focus on focus
powers until he retrieves the implement or refreshes his focus.

The occultist refreshes his mental focus once each day after receiving at least 8 hours of sleep.
After refreshing his mental focus, the occultist must spend 1 hour preparing his implements and
investing them with this power. Mental focus that is not used before the next time the occultist
refreshes his focus is lost.

The occultist can choose to save generic mental focus inside his own body instead of investing all
of it, but expending this focus comes at a higher cost.

Any focus power the occultist activates with generic focus costs twice as much mental focus to use
(and to maintain, if applicable). The occultist can expend his generic focus through an appropriate
implement on any focus power he knows, but an implement he didn't invest any focus in at the start
of the day grants no resonant power.

#### Focus Powers (Su) {#focus-powers}

At 1st level, an occultist learns the base focus power from both of his two implement schools (see
Implements below) and can select one more focus power from the list of those available to him
through those schools. Whenever the occultist learns a new implement school, he gains the base power
of that school. In addition, at 3rd level and every 2 levels thereafter, he learns a new focus power
selected from the options granted by all of the implement schools he knows. The occultist can use
focus powers only by expending mental focus (see Mental Focus on page 48).

Unless otherwise noted, the DC for any saving throw against a focus power equals 10 + 1/2 the
occultist's level + the occultist's Intelligence modifier. The occultist can't select a focus power
more than once. Some focus powers require him to reach a specific occultist level before he can
choose them.

#### Magic Item Skill (Ex) {#magic-item-skill}

At 2nd level, an occultist's knowledge of magic items grants him a bonus when attempting to use
them. He gains a bonus on all [Use Magic Device](ref/skill/use-magic-device) checks equal to 1/2 his
occultist level.

#### Object Reading (Su) {#object-reading}

At 2nd level, an occultist learns how to read information from items he examines.

Examining an item in this way requires him to spend 1 minute handling the item. If the item is a
magic item, the occultist learns its properties and command word as if he had successfully examined
the item using _[detect magic](ref/spell/detect-magic)_ and succeeded at a Spellcraft check. This
ability does not reveal whether the item is cursed unless the occultist's class level is equal to or
greater than the caster level of the item. If the item has any historical significance, the
occultist learns one piece of information about its past (as determined by the GM). Finally, if the
item was last used no longer than 1 day ago per the occultist's class level, the occultist learns
one piece of information about the last creature to use the item. This information might be a
glimpse of the creature's appearance, a brief vision of what it saw while using the item, or perhaps
its emotional state when it last used the item. The GM determines what information is gained in this
way. This functions like the [psychometry occult skill unlock](ref/skill/appraise) (see page 196),
but doesn't require a skill check and can be used at will.

#### Shift Focus (Su) {#shift-focus}

At 4th level, an occultist gains the ability to shift his mental focus from one implement to
another, though some of the focus is lost along the way. Shifting mental focus removes a number of
points of mental focus from one implement and adds the same number - 1 to another implement; this
takes 1 minute of quiet contemplation while touching both implements. The occultist can shift his
mental focus only from one implement to another implement; he can't shift generic focus into an
implement. Unlike expending focus normally, this shift can reduce the effect of a resonant power in
the implement from which the mental focus was taken. It does not, however, add to the resonant power
of the implement to which the focus is added.

#### Aura Sight (Su) {#aura-sight}

At 5th level, the occultist can read the auras of creatures around him as a standard action. This
functions as the _[aura sight](ref/spell/aura-sight)_ spell with a duration of 1 round.

#### Magic Circles (Su) {#magic-circles}

At 8th level, an occultist learns how to draw magic circles. To draw a circle, he must have chalk,
salt, blood, powdered silver, or some other appropriate substance at hand (although he can press a
[magic circle](ref/spell/magic-circle) into a softer surface such as dirt or clay). Drawing a circle
takes 1 minute and requires the occultist to expend 1 point of mental focus (either generic focus or
focus from any one of his implements). Once completed, this circle functions as a permanent _magic
circle_ against any alignment of the occultist's choosing. The circle can't be against a component
of the occultist's alignment (if he is lawful good, for example, it can't be a _magic circle against
good_ or _law_). The circle remains until its form is physically broken (for example, if the lines
are smeared or the salt is scattered). Only a living creature can break the circle; environmental
effects can't break it. An occultist can have only one circle created in this way at a time. If he
creates a second circle, the first one loses all its magic powers. This type of magic circle can't
normally be focused inward to bind an outsider.

#### Outside Contact (Su) {#outside-contact}

At 8th level, the occultist learns the true name of one particular outsider. This outsider can have
no more than 3 Hit Dice. Whenever the occultist creates a [magic circle](ref/spell/magic-circle), he
can expend 1 additional point of mental focus to focus the circle inward and lure that outsider to
the circle (similar to using _[lesser planar binding](ref/spell/planar-binding-lesser)_). The
outsider is bound for up to 10 minutes. During this time, the occultist can bargain with the
outsider for one piece of information. This requires a payment of at least 20 gp (or items of at
least that value that are of interest to the outsider). The bargaining requires the occultist to
attempt a Diplomacy or Intimidate check opposed by the outsider's Sense Motive check. Succeeding at
the check by 5 or more reduces this cost to 10 gp. Failure increases the price to 30 gp, whereas
failure by 5 or more allows the outsider to escape without giving any information (or receiving
payment). The information gained can be anything that might be learned through a
_[divination](ref/spell/divination)_ spell. The information is always correct but is frequently
cryptic. It typically takes the outsider 1d3 hours to gather the information, at which point it
returns of its own accord to deliver the information as promised. The outsider always resents being
used in this way, even if the occultist and the outsider share an alignment component. After the
occultist bargains with the outsider, the magic circle loses all power and the outsider is sent back
to its home plane.

At 12th level and every 4 levels thereafter, the occultist learns to contact one additional outsider
of the same type or a different type. Although he can call only one outsider in this way at a time,
the occultist can ask such an outsider one additional question per calling for every 4 occultist
levels he possesses beyond 8th (to a maximum of four questions at 20th level), all for the same
bargaining price. The questions must be in some way related to one another.

At 16th level, in lieu of asking questions, the occultist can demand that the outsider deliver a
message to any one friendly creature that the occultist knows personally. The occultist can also
task the outsider to deliver one object weighing no more than 1 pound. Either of these demands
requires an opposed check as described above. Delivery typically takes 1d4 hours, but this period is
reduced to 1d6 minutes if the recipient is within 1 mile of the occultist (or even less if the
recipient is within sight). The occultist must be able to accurately describe the recipient in both
name and appearance. This ability can't be used to deliver anything to a location, or to enemies or
creatures that are unfriendly to the occultist.

#### Binding Circles (Su) {#binding-circles}

At 12th level, whenever the occultist creates a magic circle he can expend 1 additional point of
mental focus to make it a binding circle. A binding circle is invisible and counts as a trap. If a
living creature of the corresponding alignment steps inside it, the trap triggers and binds the
creature inside the circle. While it can move freely within the circle, it can't leave the circle,
make attacks against targets outside the circle, cast spells that cross the circle's boundary (the
circle blocks line of effect from the inside), or use any ability that would allow it to leave the
circle or disturb the circle in any way. When the circle traps a creature in this way, the creature
can attempt a Reflex save to dive out of the circle before the magic takes hold (DC = 10 + 1/2 the
occultist's level + the occultist's Intelligence modifier). A creature that can see the circle gains
a +4 bonus on this save. If it fails its save, the creature must remain in the circle, although it
can attempt a Will save at the same DC at the end of each hour of imprisonment to escape. A binding
circle can be spotted with a successful Perception check (DC = 25 + 1/2 the occultist's level). It
can also be disarmed using Disable Device, with the same DC. Anything crossing the boundary of the
circle from the outside, such as a weapon, spell effect, or special ability, immediately breaks the
circle and frees the creature trapped inside.

#### Fast Circles (Su) {#fast-circles}

At 16th level, the occultist learns to draw magic circles very quickly. He can draw a magic circle
as a full-round action, but any circle drawn in this way has a duration of 1 minute per occultist
level (unless it's drawn in conjunction with the outside contact class feature, in which case it
lasts for 10 minutes as normal). If he draws a binding circle in this way, its duration is 1 round
per occultist level.

#### Implement Mastery (Su) {#implement-mastery}

At 20th level, an occultist learns to master one of his implements. He selects one implement school.
Whenever he uses a focus power from an implement of that school, the DC to resist any of the effects
increases by 4 and he treats his occultist level as 4 higher when determining the effects and
duration of that power. In addition, the occultist gains 4 extra points of mental focus, but these
points must always be invested in implements of the mastered school. He can't save these points or
expend them for any ability other than the focus powers of those implements. The
[hardness](ref/umr/hardness) of each of the occultist's implements of the mastered school increases
by an additional 20 as long as the item has at least 1 point of mental focus stored within.

### Implement Schools {#implement-schools}

Occultists can chose from the following implement schools, each representing a school of magic. An
occultist can select an implement school more than once, as noted in the implements class feature.

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

**Collector of the Strange (Su)**

At 20th level, the occultist has no end of odd curios hanging about his body. The occultist gains
two new focus powers and increases his mental focus pool by 6, but he can have no more than
one-third of his points invested into any one implement school.

**Also available:** Deep Magics

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

**Ancestral Aspirant**

**Class:** occultist

**Modifies or Replaces:** Class Skills; Implements; Object Reading; Outside Contact

**Description:** It is common for a noble to possess a deep pride for his family's past, but when
such self-importance gives way to obsession, an ancestral aspirant is born.

**Battle Host**

**Class:** occultist

**Modifies or Replaces:** Class Skills; Weapon/Armor Proficiency; Implements; Mental Focus;
Spellcasting; Implement Mastery; Magic Item Skill; Object Reading; Shift Focus; Magic Circles;
Binding Circles; Fast Circles; Aura Sight; Outside Contact

**Description:** Well versed in military history, battlefield lore, and the occult, a battle host
forms a supernatural bond with a chosen weapon, suit of armor, or shield, from which he can channel
psychic energy to cast spells, conjure the spirit of the object's former owner, increase his own
physical might, and produce a number of other remarkable abilities.

**Construct Collector**

**Class:** occultist

**Modifies or Replaces:** 3rd, 9th, 15th-level Focus Power; Magic Circles; Outside Contact; Binding
Circles; Fast Circles

**Description:** Construct collectors draw out a construct's spiritual presence and use it to gain
unlikely power in the battlefield.

**Curator**

**Class:** occultist

**Modifies or Replaces:** Implements; 3rd-level Focus Power; Shift Focus; Outside Contact; Magic
Circles; Binding Circles; Fast Circles

**Description:** Most occultists acquire and study antiques at a steady pace, learning new
techniques one at a time. A lucky few join wealthy organizations replete with relics or inherit
undocumented vaults full of historical treasures, and dabble in a wide variety of implements while
mastering few

**Esoteric Initiate**

**Class:** occultist

**Modifies or Replaces:** Mental Focus; Implements; Shift Focus; Aura Sight

**Description:** While most occultists learn to draw power from a variety of implements and objects,
esoteric initiates have focused their study entirely on items of antiquity connected to the
teachings of the Esoteric Order of the Palatine Eye, believing such items to be more powerful than
mundane items.

**Extemporaneous Channeler**

**Class:** occultist

**Modifies or Replaces:** Weapon Proficiencies; Mental Focus; Shift Focus; Magic Circles; Outside
Contact; Binding Circles; Fast Circles

**Description:** Extemporaneous channelers study the power of transformation and use items in
unintended ways to awaken their potential.

**Geomancer**

**Class:** occultist

**Modifies or Replaces:** Class Skills; Mental Focus; Implements; Magic Item Skill; Aura Sight; 7th
and 13th-level Focus Powers

**Description:** A geomancer studies every type of land, deriving power from the differences between
types of terrain.

**Haunt Collector**

**Class:** occultist

**Modifies or Replaces:** Implements; Aura Sight; Outside Contact; Magic Circles; Binding Circles;
Fast Circles

**Description:** Haunt collectors use items haunted by their former owners to create ghostly
presences imbued with psychic power.

**Naturalist**

**Class:** occultist

**Modifies or Replaces:** Class Skills; Mental Focus; Magic Circles; Fast Circles; Outside Contact;
Binding Circles

**Description:** A naturalist eschews the contact with outsiders that other occultists use as the
core of their work. Instead, he attunes his mind to the natural spirits that exist everywhere, just
out of sight for the unawakened mind.

**Necroccultist**

**Class:** occultist

**Modifies or Replaces:** Implements; Implement Mastery; Object Reading; Aura Sight; Outside Contact

**Description:** Necroccultists' fascination with death and the undead drives them to explore the
forbidden necromantic arts as they search for secrets they can use to manipulate the natural cycle
of life and death.

**Occult Historian**

**Class:** occultist

**Modifies or Replaces:** Object Reading; Aura Sight; 3rd-level Focus Power; Outside Contact 2, 3,
and 4

**Description:** Many wilderness areas contain the remnants of ancient civilizations, with some
waiting to be discovered and some held by fierce monsters or devious cults. An occult historian
seeks these ruins not only for their esoteric artifacts but also to learn the structures' secrets.

**Panoply Savant**

**Class:** occultist

**Modifies or Replaces:** Shift Focus; Outside Contact; Magic Circles; Binding Circles; Fast Circles

**Description:** Some occultists specialize in a particular panoply, fully dedicating themselves to
mastering the secrets of the psychic resonance of each of its component implements, as well as the
way they interact with one another.

**Planar Harmonizer**

**Class:** occultist

**Modifies or Replaces:** Implements; Implement Mastery; Magic Item Skill; Shift Focus; 5th,
7th-level Focus Power; Magic Circles; Aura Sight

**Description:** Planar harmonizers are masters of the planar symphony, forging bonds with tuning
forks to unlock the true potential of these instruments

**Psychodermist**

**Class:** occultist

**Modifies or Replaces:** Class Skills; Implements; Magic Item Skill; Object Reading; Aura Sight;
Outside Contact; Binding Circles; Fast Circles

**Description:** Rather than tapping the psychic energy residing within esoteric items,
psychodermists form supernatural bonds with trophies taken from creatures they have slain. Through
these mementos, these occultists manifest not only their own magic, but also the unique powers of
their fallen foes.

**Reliquarian**

**Class:** occultist

**Modifies or Replaces:** Weapon Proficiencies; Spells; Focus Powers; Implements; Knacks; Mental
Focus

**Description:** Not all occultists derive their power from psychic impressions left on objects.
Some find faith first, and draw out the divine potential in religious relics.

**Secret Broker**

**Class:** occultist

**Modifies or Replaces:** Class Skills; Implements; Implement Mastery; Magic Item Skill; Shift
Focus; Magic Circles; Binding Circles; Fast Circles

**Description:** Whether as spymasters, extortionists, political fixers, or puppet masters, secret
brokers use their talents with objects to gain information, then leverage that information for their
own purposes.

**Sha'ir**

**Class:** occultist

**Modifies or Replaces:** Implements; Mental Focus; Spellcasting; Implement Mastery; Magic Item
Skill; Object Reading; Aura Sight; Outside Contact

**Description:** Sha'irs delve into the occult not through power over objects but instead via their
connection with minor servitor genies from the elemental planes.

**Silksworn**

**Class:** occultist

**Modifies or Replaces:** Spellcasting; Class Skills; Knacks; Implements; Weapon and Armor
Proficiency; Outside Contact; Magic Circles; Binding Circles; Fast Circles; Implement Mastery

**Description:** Silksworn draw their power from wearing luxurious garments and can be found in many
noble courts throughout Golarion

**Talisman Crafter**

**Class:** occultist

**Modifies or Replaces:** Implements; Magic Item Skill; Object Reading; Shift Focus; Aura Sight;
5th, 17th-level Focus Powers

**Description:** Talisman crafters specialize in the creation of seals, constructing master
talismans to use as implements and inscribing wards with esoteric geometry.

**Tome Eater**

**Class:** occultist

**Modifies or Replaces:** Implements; Mental Focus; Spellcasting; Implement Mastery; Shift Focus;
6th-level Implement; Magic Circles; Outside Contact; Binding Circles; Fast Circles; Aura Sight

**Description:** Tome eaters have learned how to tap into the latent psychic energy of the written
word by physically devouring books and scrolls to create magical effects and gain mystical insights.

### Archetypes by Feature

|Archetype|Armor Proficiency|Aura Sight|Class Skills|Implements|6th-level Implement|Implement Mastery|Knacks|Magic Circles|Binding Circles|Fast Circles|Magic Item Skill|Mental Focus|Shift Focus|Focus Powers|3rd-level Focus Power|5th-level Focus Power|7th-level Focus Power|9th-level Focus Power|13th-level Focus Power|15th-level Focus Power|17th-level Focus Power|Object Reading|Outside Contact|Outside Contact 2|Outside Contact 3|Outside Contact 4|Spellcasting|Weapon Proficiency|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Ancestral Aspirant](ref/arc-occultist/ancestral-aspirant)|||X|X||||||||||||||||||X|X||||||
|[Battle Host](ref/arc-occultist/battle-host)|X|X|X|X||X||X|X|X|X|X|X|||||||||X|X||||X||
|[Construct Collector](ref/arc-occultist/construct-collector)||||||||X|X|X|||||X|||X||X|||X||||||
|[Curator](ref/arc-occultist/curator)||||X||||X|X|X|||X||X||||||||X||||||
|[Esoteric Initiate](ref/arc-occultist/esoteric-initiate)||X||X||||||||X|X||||||||||||||||
|[Extemporaneous Channeler](ref/arc-occultist/extemporaneous-channeler)||||||||X|X|X||X|X||||||||||X|||||X|
|[Geomancer](ref/arc-occultist/geomancer)||X|X|X|||||||X|X|||||X||X||||||||||
|[Haunt Collector](ref/arc-occultist/haunt-collector)||X||X||||X|X|X|||||||||||||X||||||
|[Naturalist](ref/arc-occultist/naturalist)|||X|||||X|X|X||X|||||||||||X||||||
|[Necroccultist](ref/arc-occultist/necroccultist)||X||X||X||||||||||||||||X|X||||||
|[Occult Historian](ref/arc-occultist/occult-historian)||X|||||||||||||X|||||||X||X|X|X|||
|[Panoply Savant](ref/arc-occultist/panoply-savant)||||||||X|X|X|||X||||||||||X||||||
|[Planar Harmonizer](ref/arc-occultist/planar-harmonizer)||X||X||X||X|||X||X|||X|X||||||||||||
|[Psychodermist](ref/arc-occultist/psychodermist)||X|X|X|||||X|X|X|||||||||||X|X||||||
|[Reliquarian](ref/arc-occultist/reliquarian)||||X|||X|||||X||X|||||||||||||X|X|
|[Secret Broker](ref/arc-occultist/secret-broker)|||X|X||X||X|X|X|X||X||||||||||||||||
|[Sha'ir](ref/arc-occultist/shair)||X||X||X|||||X|X||||||||||X|X||||X||
|[Silksworn](ref/arc-occultist/silksworn)|X||X|X||X|X|X|X|X|||||||||||||X||||X||
|[Talisman Crafter](ref/arc-occultist/talisman-crafter)||X||X|||||||X||X|||X|||||X|X|||||||
|[Tome Eater](ref/arc-occultist/tome-eater)||X||X|X|X||X|X|X||X|X||||||||||X||||X||

### Favored Class Bonuses

_The favored class options for occultist are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
