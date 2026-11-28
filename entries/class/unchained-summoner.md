+++
id = "ref/class/unchained-summoner"
kind = "class"
title = "Unchained Summoner"
aon = "ClassDisplay.aspx?ItemName=Summoner%20%28Unchained%29"
source_ids = ["pathfinder-unchained", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unchained_summoner", path = "json/classes8.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "25"
[[sources]]
publication = "chronicle-of-legends"
page = "28, 30"

[fields]
kind = "class"
class_type = "unchained"
hit_die = "d8"
skill_ranks = "2 + Int modifier"
features = [
  { anchor = "spells" },
  { anchor = "cantrips", level = 1 },
  { anchor = "eidolon", level = 1 },
  { anchor = "life-link", level = 1 },
  { anchor = "summon-monster-i", level = 1 },
  { anchor = "bond-senses", level = 2 },
  { anchor = "shield-ally", level = 4 },
  { anchor = "maker-s-call", level = 6 },
  { anchor = "transposition", level = 8 },
  { anchor = "aspect", level = 10 },
  { anchor = "greater-shield-ally", level = 12 },
  { anchor = "life-bond", level = 14 },
  { anchor = "merge-forms", level = 16 },
  { anchor = "greater-aspect", level = 18 },
  { anchor = "twin-eidolon", level = 20 },
]
+++

There are those who take a different path when pursuing the arcane arts, reaching across the
boundaries of the world to the far-flung planes to call forth all manner of creatures to do their
bidding. Known as summoners, these arcane practitioners form close bonds with particular outsiders,
known as eidolons, which increase in power along with their callers. In the end, summoners and their
eidolons become linked, sharing shards of the same souls.

**Unchained:** Most of the summoner's class features are the same as those of the class's original
design - the biggest change comes to the eidolon. The unchained summoner selects a subtype for his
eidolon (such as [angel](ref/eidolon/angel), [demon](ref/eidolon/demon), or
[protean](ref/eidolon/protean)), which determines a number of its evolutions and helps to shape the
eidolon's general attitude and appearance. In addition, some of the evolutions are now tied to one
or more subtypes and base forms, to make eidolons that better match the expected appearances and
abilities of such creatures. Finally, the summoner spell list has been greatly revised, removing a
number of imbalances.

**Alignment:** Any

**Hit Die:** d8

**Starting Wealth:** 2d6 × 10 gp (average 70 gp)

**Skill Points per Level:** 2 + Int modifier

**Class Skills (Dex):** Fly, Ride

**Class Skills (Int):** Craft (any), Knowledge (arcana), Knowledge (dungeoneering), Knowledge
(engineering), Knowledge (geography), Knowledge (history), Knowledge (local), Knowledge (nature),
Knowledge (nobility), Knowledge (planes), Knowledge (religion), Linguistics, Spellcraft

**Class Skills (Wis):** Profession (any)

**Class Skills (Cha):** Handle Animal, Use Magic Device

### Class Features and Spells Per Day

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|1st|2nd|3rd|4th|5th|6th|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|+0|+0|+0|+2|Cantrips, eidolon, life link, _[summon monster I](ref/spell/summon-monster-1)_|1|-|-|-|-|-|
|2nd|+1|+0|+0|+3|Bond senses|2|-|-|-|-|-|
|3rd|+2|+1|+1|+3|_[Summon monster II](ref/spell/summon-monster-2)_|3|-|-|-|-|-|
|4th|+3|+1|+1|+4|Shield ally|3|1|-|-|-|-|
|5th|+3|+1|+1|+4|_[Summon monster III](ref/spell/summon-monster-3)_|4|2|-|-|-|-|
|6th|+4|+2|+2|+5|Maker's call|4|3|-|-|-|-|
|7th|+5|+2|+2|+5|_[Summon monster IV](ref/spell/summon-monster-4)_|4|3|1|-|-|-|
|8th|+6/+1|+2|+2|+6|Transposition|4|4|2|-|-|-|
|9th|+6/+1|+3|+3|+6|_[Summon monster V](ref/spell/summon-monster-5)_|5|4|3|-|-|-|
|10th|+7/+2|+3|+3|+7|Aspect|5|4|3|1|-|-|
|11th|+8/+3|+3|+3|+7|_[Summon monster VI](ref/spell/summon-monster-6)_|5|4|4|2|-|-|
|12th|+9/+4|+4|+4|+8|Greater shield ally|5|5|4|3|-|-|
|13th|+9/+4|+4|+4|+8|_[Summon monster VII](ref/spell/summon-monster-7)_|5|5|4|3|1|-|
|14th|+10/+5|+4|+4|+9|Life bond|5|5|4|4|2|-|
|15th|+11/+6/+1|+5|+5|+9|_[Summon monster VIII](ref/spell/summon-monster-8)_|5|5|5|4|3|-|
|16th|+12/+7/+2|+5|+5|+10|Merge forms|5|5|5|4|3|1|
|17th|+12/+7/+2|+5|+5|+10|_[Summon monster IX](ref/spell/summon-monster-9)_|5|5|5|4|4|2|
|18th|+13/+8/+3|+6|+6|+11|Greater aspect|5|5|5|5|4|3|
|19th|+14/+9/+4|+6|+6|+11|_[Gate](ref/spell/gate)_|5|5|5|5|5|4|
|20th|+15/+10/+5|+6|+6|+12|Twin eidolon|5|5|5|5|5|5|

### Spells Known

|Level|0|1st|2nd|3rd|4th|5th|6th|
| --- | --- | --- | --- | --- | --- | --- | --- |
|1st|4|2|-|-|-|-|-|
|2nd|5|3|-|-|-|-|-|
|3rd|6|4|-|-|-|-|-|
|4th|6|4|2|-|-|-|-|
|5th|6|4|3|-|-|-|-|
|6th|6|4|4|-|-|-|-|
|7th|6|5|4|2|-|-|-|
|8th|6|5|4|3|-|-|-|
|9th|6|5|4|4|-|-|-|
|10th|6|5|5|4|2|-|-|
|11th|6|6|5|4|3|-|-|
|12th|6|6|5|4|4|-|-|
|13th|6|6|5|5|4|2|-|
|14th|6|6|6|5|4|3|-|
|15th|6|6|6|5|4|4|-|
|16th|6|6|6|5|5|4|2|
|17th|6|6|6|6|5|4|3|
|18th|6|6|6|6|5|4|4|
|19th|6|6|6|6|5|5|4|
|20th|6|6|6|6|6|5|5|

### Class Features {#class-features}

The following are the class features of the summoner.

#### Weapon and Armor Proficiency {#weapon-and-armor-proficiencies}

Summoners are proficient with all simple weapons and light armor. A summoner can cast summoner
spells while wearing light armor without incurring the normal arcane spell failure chance. Like any
other arcane spellcaster, a summoner wearing medium or heavy armor, or using a shield, incurs a
chance of arcane spell failure if the spell in question has a somatic component. A summoner still
incurs the normal arcane spell failure chance for arcane spells granted by other classes.

#### Spells {#spells}

A summoner casts arcane spells drawn from the summoner spell list. (The unchained summoner's spell
list on page 39 is different from that presented in the _Advanced Player's Guide_.) He can cast any
spell he knows without preparing it ahead of time.

To learn or cast a spell, a summoner must have a Charisma score equal to at least 10 + the spell
level. The Difficulty Class for a saving throw against a summoner's spell is 10 + the spell level +
the summoner's Charisma modifier.

A summoner can cast only a certain number of spells of each spell level each day. His base daily
spell allotment is given on Table 1–4: Summoner. In addition, he gains bonus spells per day if he
has a high Charisma score (see Table 1–3: Ability Modifiers and Bonus Spells on page 17 of the _Core
Rulebook_).

A summoner's selection of spells is limited. A summoner begins play knowing four 0-level spells and
two 1st-level spells of the summoner's choice. At each new summoner level, he gains one or more new
spells as indicated on Table 1–5: Summoner Spells Known. (Unlike spells per day, the number of
spells a summoner knows is not affected by his Charisma score. The numbers on Table 1–5 are fixed.)

Upon reaching 5th level, and at every third summoner level thereafter (8th, 11th, and so on), a
summoner can choose to learn a new spell in place of one he already knows. In effect, the summoner
"loses" the old spell in exchange for the new one. The new spell's level must be the same as that of
the spell being exchanged, and it must be at least 1 level lower than the highest-level summoner
spell the summoner can cast. A summoner can swap out only a single spell at any given level and must
choose whether or not to swap the spell at the same time that he gains new spells known.

A summoner doesn't need to prepare his spells in advance. He can cast any spell he knows at any
time, assuming he has not yet used up his allotment of spells per day for the level.

#### Cantrips {#cantrips}

A summoner learns a number of cantrips, or 0-level spells, as noted on Table 1–5. These spells are
cast like any other spell, but they do not consume any slots and may be used again. Cantrips
prepared using other spell slots (due to metamagic feats, for example) consume spell slots as
normal.

#### Eidolon {#eidolon}

A summoner begins play with the ability to summon to his side a powerful outsider called an
[eidolon](ref/sidekick/unchained-eidolon). The eidolon forms a link with the summoner, who forever
after summons an aspect of the same creature. Each eidolon has a subtype, chosen when the eidolon is
first summoned, that determines its origin and many of its abilities. An eidolon must be within one
alignment step of the summoner who calls it (so a neutral good summoner can call a neutral, lawful
good, or chaotic good eidolon) and can speak all of his languages. An eidolon is treated as a
[summoned creature](ref/spelldef/summoning), except it is not sent back to its home plane until
reduced to a number of negative hit points equal to or greater than its Constitution score. In
addition, due to its tie to its summoner, an eidolon can touch and attack creatures warded by
_[protection from evil](ref/spell/protection-from-evil)_ and similar effects that prevent contact
with summoned creatures.

A summoner can summon his eidolon in a ritual that takes 1 minute to perform. When summoned in this
way, the eidolon's hit points are unchanged from the last time it was summoned. The only exception
to this is if the eidolon was slain, in which case it returns with
[half](ref/misc/fractions-and-rounding) its normal hit points. The eidolon does not heal naturally.
The eidolon remains until dismissed by the summoner (a standard action). If the eidolon is sent back
to its home plane due to death, it cannot be summoned again until the following day. The eidolon
cannot be sent back to its home plane by means of _[dispel magic](ref/spell/dispel-magic)_, but
spells such as _[dismissal](ref/spell/dismissal)_ and _[banishment](ref/spell/banishment)_ function
normally. If the summoner is unconscious, asleep, or killed, his eidolon is immediately banished.

The eidolon takes a form shaped by the summoner's desires. The eidolon's Hit Dice, saving throws,
skills, feats, and abilities are tied to the summoner's class level and increase as the summoner
gains levels. In addition, each eidolon gains a pool of evolution points based on the summoner's
class level that can be used to give the eidolon different abilities and powers. Whenever the
summoner gains a level, he must decide how these points are spent, and they are set until he gains
another level of summoner.

The eidolon's physical appearance is up to the summoner, but it always appears as some sort of
fantastical creature appropriate to its subtype. This control is not fine enough to make the eidolon
appear like a specific creature. The eidolon also bears a glowing rune that is identical to a rune
that appears on the summoner's forehead as long as the eidolon is summoned. While this rune can be
hidden through mundane means, it cannot be concealed through magic that changes appearance, such as
_[alter self](ref/spell/alter-self)_ or _[polymorph](ref/spell/polymorph)_ (although
_[invisibility](ref/spell/invisibility)_ does conceal it as long as the spell lasts).

#### Life Link (Su) {#life-link}

At 1st level, a summoner forms a close bond with his eidolon. Whenever the eidolon takes enough
damage to send it back to its home plane, as a reaction to the damage, the summoner can sacrifice
any number of hit points he has without using an action. Each hit point sacrificed in this way
prevents 1 point of damage dealt to the eidolon. This can prevent the eidolon from being sent back
to its home plane.

In addition, the eidolon and the summoner must remain within 100 feet of one another for the eidolon
to remain at full strength. If the eidolon is beyond 100 feet but closer than 1,000 feet, its
current and maximum hit point totals are reduced by 50%. If the eidolon is more than 1,000 feet away
but closer than 10,000 feet, its current and maximum hit point totals are reduced by 75%. If the
eidolon is more than 10,000 feet away, it is immediately returned to its home plane. Current hit
points lost in this way are not restored when the eidolon gets closer to its summoner, but its
maximum hit point total does climb to the levels indicated and eventually returns to normal.

#### Summon Monster I (Sp) {#summon-monster-i}

At 1st level, a summoner can cast _[summon monster I](ref/spell/summon-monster-1)_ as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + his
Charisma modifier. Drawing on this ability uses up the same power that the summoner uses to call his
eidolon. As a result, he can use this ability only when his eidolon is not summoned. He can cast
this spell as a standard action, and the creatures remain for 1 minute per level (instead of 1 round
per level). At 3rd level, and every 2 levels thereafter, the power of this ability increases by 1
spell level, allowing him to summon more powerful creatures (to a maximum of
_[summon monster IX](ref/spell/summon-monster-9)_ at 17th level). At 19th level, this ability can be
used as _[gate](ref/spell/gate)_ or _[summon monster IX](ref/spell/summon-monster-9)_. If used as
_[gate](ref/spell/gate)_, the summoner must pay any required material components. A summoner cannot
have more than one _[summon monster](ref/spell/summon-monster)_ or _[gate](ref/spell/gate)_ spell
active in this way at one time. If this ability is used again, any existing
_[summon monster](ref/spell/summon-monster)_ or _[gate](ref/spell/gate)_ from this spell-like
ability immediately ends. These summon spells are considered to be part of the summoner's spell list
for the purposes of spell trigger and spell completion items. In addition, the summoner can expend
uses of this ability to fulfill the construction requirements of any magic item he creates, so long
as he can use this ability to cast the required spell.

#### Bond Senses (Su) {#bond-senses}

At 2nd level, a summoner can, as a standard action, share the senses of his eidolon, hearing,
seeing, smelling, tasting, and touching everything the eidolon does. He can use this ability a
number of rounds per day equal to his summoner level. There is no maximum range to this effect, but
the eidolon and the summoner must be on the same plane. The summoner can end this effect as a free
action.

#### Shield Ally (Ex) {#shield-ally}

At 4th level, whenever a summoner is within his eidolon's reach, the summoner gains a +2 shield
bonus to his Armor Class and a +2 circumstance bonus on his saving throws. This bonus does not apply
if the eidolon is [grappled](ref/rule/grapple-conditions), [helpless](ref/misc/helpless),
[paralyzed](ref/rule/paralyzed), [stunned](ref/misc/stunned), or
[unconscious](ref/misc/unconscious).

#### Maker's Call (Su) {#maker-s-call}

At 6th level, as a standard action, a summoner can call his eidolon to his side. This functions as
_[dimension door](ref/spell/dimension-door)_, using the summoner's caster level. When this ability
is used, the eidolon appears adjacent to the summoner (or as close as possible if all adjacent
spaces are occupied). If the eidolon is out of range, the ability is wasted. The summoner can use
this ability once per day at 6th level, plus one additional time per day for every four levels
beyond 6th.

#### Transposition (Su) {#transposition}

At 8th level, a summoner can use his maker's call ability to swap locations with his eidolon. If the
eidolon occupies more squares than the summoner, the summoner can appear in any square occupied by
the eidolon. The eidolon must occupy the square that was occupied by the summoner if able, or as
close as possible if it is not able.

#### Aspect (Su) {#aspect}

At 10th level, a summoner can divert up to 2 points from his eidolon's evolution pool to add
evolutions to himself. He cannot select any evolution that the eidolon could not possess, and he
must be able to meet the requirements as well (except for subtype requirements, so long as his
eidolon meets the subtype requirement). He cannot select the ability increase evolution through this
ability. Any points spent in this way are taken from the eidolon's evolution pool (reducing the
total number available to the eidolon). The summoner can change the evolutions granted by these
points anytime he can change the eidolon's evolutions.

#### Greater Shield Ally (Su) {#greater-shield-ally}

At 12th level, whenever an ally is within reach of the summoner's eidolon, the ally gains a +2
shield bonus to its Armor Class and a +2 circumstance bonus on its saving throws. If this ally is
the summoner, these bonuses increase to +4. This bonus does not apply if the eidolon is grappled,
helpless, paralyzed, stunned, or unconscious.

#### Life Bond (Su) {#life-bond}

At 14th level, the summoner's life becomes linked to his eidolon's. As long as the eidolon has 1 or
more hit points, the summoner is protected from harm. Damage in excess of that which would reduce
the summoner to 0 hit points is instead transferred to the eidolon. This damage is transferred 1
point at a time, meaning that as soon as the eidolon is reduced to a number of negative hit points
equal to its Constitution score, all excess damage remains with the summoner. Effects that cause
death but don't deal damage are unaffected by this ability. This ability does not affect spells such
as _[baleful polymorph](ref/spell/baleful-polymorph)_, _[flesh to stone](ref/spell/flesh-to-stone)_,
_[imprisonment](ref/spell/imprisonment)_, or other spells that don't deal damage.

#### Merge Forms (Su) {#merge-forms}

At 16th level, as a full-round action, a summoner can touch his eidolon and the two can merge forms.
This transformation includes all of the summoner's gear. While merged in this way, the summoner is
protected from harm and cannot be the target of spells or effects. All effects and spells currently
targeting the summoner are suspended until the summoner emerges from the eidolon (although durations
continue to expire).

The summoner can cast spells while inside the eidolon by taking control of the eidolon for the
duration of the casting. Any material components used for these spells are taken from the summoner's
gear, even though they are otherwise inaccessible. The summoner can direct all of the eidolon's
actions while merged, can perceive through its senses, and can speak through its voice.

The summoner can use this ability for a number of rounds per day equal to his summoner level. He can
end this effect at any time as a swift action. The summoner emerges in a square adjacent to the
eidolon if able. If the eidolon is returned to its home plane while the summoner is merged with it,
the summoner is immediately ejected, takes 4d6 points of damage, and is stunned for 1 round.

#### Greater Aspect (Su) {#greater-aspect}

At 18th level, a summoner can divert more of his eidolon's evolutions to himself. This ability
functions as the aspect ability, but the maximum number of evolution points the summoner can divert
increases to 6. In addition, the eidolon loses 1 point from its evolution pool for every 2 points
(or fraction thereof) diverted to the summoner instead of losing 1 point from the evolution pool for
each point diverted.

#### Twin Eidolon (Su) {#twin-eidolon}

At 20th level, a summoner and his eidolon share a true connection. As a standard action, the
summoner can assume the shape of his eidolon, copying all of its evolutions, form, and abilities.
His Strength, Dexterity, and Constitution scores change to match the base scores of his eidolon. He
can choose to have any gear that he carries become absorbed by his new form, as with spells from the
polymorph subschool. Items with continuous effects continue to function while absorbed in this way.
The summoner loses his natural attacks and all racial traits (except bonus feats, skills, and
languages) in favor of the abilities granted by his eidolon's evolutions. The summoner retains all
of his class features. The summoner can keep this form for a number of minutes per day equal to his
summoner level. This duration does not need to be consecutive, but it must be spent in 1-minute
increments. The summoner can end this effect as a free action.

### Eidolons {#unchained-eidolons}

An eidolon's abilities are determined by the summoner's level and by the choices made using its
evolution pool. Table 1–6: Eidolon Base Statistics determines many of the base statistics of the
eidolon. Each eidolon possesses a base form that modifies these base statistics. Eidolons are
outsiders for the purpose of determining which spells affect them.

Class Level: This is the character's summoner level.

HD: This is the total number of 10-sided (d10) Hit Dice the eidolon possesses, each of which gains a
Constitution modifier, as normal.

BAB: This is the eidolon's base attack bonus. An eidolon's base attack bonus is equal to its Hit
Dice. Eidolons do not gain additional attacks using their natural weapons for a high base attack
bonus.

Good Saves and Poor Save: These are the eidolon's base saving throw bonuses. An eidolon possesses
two good saving throws and one poor saving throw, determined by the creature's base form.

Skills: This lists the eidolon's total skill ranks. An eidolon can assign skill ranks to any skill,
but it must possess the appropriate appendages to use some skills. Eidolons with Intelligence scores
above the base value modify these totals as normal (an eidolon gains a number of skill ranks equal
to 6 + its Intelligence modifier per Hit Die). An eidolon cannot have more ranks in a skill than it
has Hit Dice. Eidolon skill ranks are set once chosen, even if the creature's evolutions change when
the summoner gains a new level.

Feats: This is the total number of feats possessed by an eidolon. Eidolons can select any feat they
qualify for, but they must possess the appropriate appendages to use some feats. Eidolon feats are
set once chosen, even if the creature changes when the summoner gains a new level. If, due to such
changes, the eidolon no longer qualifies for a feat, the feat has no effect until the eidolon once
again qualifies for the feat.

Armor Bonus: The number noted here is the eidolon's base total armor bonus. This bonus can be split
between an armor bonus and a natural armor bonus, as decided by the summoner. This number is
modified by the eidolon's base form and some options available through its evolution pool. An
eidolon cannot wear armor of any kind, as the armor interferes with the summoner's connection to the
eidolon.

Str/Dex Bonus: Add this modifier to the eidolon's Strength and Dexterity scores, which are
determined by its base form. Some options available through the eidolon's evolution pool might
modify these scores.

Evolution Pool: The value given in this column is the total number of points in the eidolon's
evolution pool. Points in this pool can be spent on a wide variety of modifications and upgrades
that add new abilities, attacks, and powers to the eidolon. Whenever the summoner gains a level, the
number of points in this pool increases and the summoner can spend these points to change the
abilities of the eidolon. These choices are not set—the summoner can change them whenever he gains a
level (and through the _transmogrify_ spell).

Max. Attacks: This indicates the maximum number of attacks that the eidolon is allowed to possess at
the given level. If the eidolon is at its maximum, it cannot take evolutions that grant additional
attacks. Attacks made with weapons, including those granted by a high base attack bonus, are counted
against this maximum.

Special: This includes a number of abilities gained by all eidolons as they increase in power (see
Table 1–6: Eidolon Base Statistics). Each of these bonuses is described below.

_Darkvision (Ex)_: The eidolon has darkvision with a range of 60 feet.

_Link (Ex)_: A summoner and his eidolon share a mental link that allows for communication across any
distance (as long as they are on the same plane). This communication is a free action, allowing the
summoner to give orders to his eidolon at any time. In addition, magic items interfere with the
summoner's connection to his eidolon. As a result, the summoner and his eidolon share magic item
slots. For example, if the summoner is wearing a ring, his eidolon can wear no more than one ring.
In case of a conflict, the items worn by the summoner remain active, and those used by the eidolon
become dormant. The eidolon must possess the appropriate appendages to use a magic item.

_Share Spells (Ex)_: The summoner can cast a spell with a target of "you" on his eidolon (as a spell
with a range of touch) instead of on himself. A summoner can cast spells on his eidolon even if the
spells normally do not affect creatures of the eidolon's type (outsider). Spells cast in this way
must come from the summoner spell list. This ability does not allow the eidolon to share abilities
that are not spells, even if they function like spells.

_Evasion (Ex)_: If the eidolon is subjected to an attack that normally allows a Reflex save for half
damage, it takes no damage if it succeeds at its saving throw.

_Ability Score Increase (Ex)_: The eidolon adds 1 to one of its ability scores.

_Devotion (Ex)_: An eidolon gains a +4 morale bonus on Will saves against enchantment spells and
effects.

_Multiattack_: An eidolon gains Multiattack as a bonus feat if it has three or more natural attacks
and does not already have that feat. If it does not have the requisite three or more natural attacks
(or it is reduced to fewer than three attacks), the eidolon instead gains a second attack with one
of its natural weapons, albeit at a -5 penalty. If the eidolon later gains three or more natural
attacks, it loses this additional attack and instead gains Multiattack.

_Improved Evasion (Ex)_: When subjected to an attack that allows a Reflex saving throw for half
damage, an eidolon takes no damage if it succeeds at its saving throw and only half damage if it
fails.

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

**Grand Eidolon (Su)**

At 20th level, the summoner's eidolon becomes an absolute monstrosity - a thing of legend and
terror. The summoner gains 4 additional evolution points to spend as he likes, not subject to
subtype - based requirements.

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

**Construct Caller**

**Class:** unchained\_summoner

**Modifies or Replaces:** Subtype; Summon Monster

**Description:** Construct callers use their mechanical and planar understandings to work planar
energies as a tinkerer works parts

**Devil Binder**

**Class:** unchained\_summoner

**Modifies or Replaces:** Alignment; Summon Monster I; Bond Senses; Shield Ally; Maker's Call;
Transposition; Greater Shield Ally; Merge Forms; Twin Eidolon; Devotion

**Description:** A devil binder borrows extraplanar quintessence from her eidolon, gaining strange
abilities for herself and evolving her eidolon's magical powers.

**Devil Impostor**

**Class:** unchained\_summoner

**Modifies or Replaces:** Class Skills; Bond Senses; Eidolon; Summon Monster; Shield Ally; Greater
Shield Ally; Transposition

**Description:** Some summoners can't abide the cruelty of devils, or simply can't outwit them, but
must appear to do so to get by in Cheliax, the Outer Planes, or similar areas of infernal influence.
Rather than risk binding true devils, they reshape their eidolons into deceptive forms.

**Fey Caller**

**Class:** unchained\_summoner

**Modifies or Replaces:** Class Skills; Summon Monster; Eidolon Subtype

**Description:** Fey callers are summoners whose voices reach out into those strange faerie realms
and call forth the fey who dwell there.

**God Caller**

**Class:** unchained\_summoner

**Modifies or Replaces:** Class Skills; Life Link; Transposition; Aspect; Greater Aspect; Twin
Eidolon

**Description:** God callers follow a fractured tradition that originated in the now-lost nation of
Sarkoris. They speak to an assortment of ancient divine powers to lead their communities and
sometimes stir up reformations in faiths with ideals similar to their personal convictions.

**Leshy Caller**

**Class:** unchained\_summoner

**Modifies or Replaces:** Eidolon; Summon Monster

**Description:** A leshy caller summons creatures from the First World and forges a bond with a
leshy eidolon.

**Morphic Savant**

**Class:** summoner

**Modifies or Replaces:** Eidolon; Summon Monster; Spells

**Description:** A morphic savant is an agent of change who draws power from the Abyss, Elysium, or
the Maelstrom to fulfill whatever goals strike his fancy.

**Soulbound Summoner**

**Class:** unchained\_summoner

**Modifies or Replaces:** Eidolon; Life Link; Summon Monster

**Description:** Soulbound summoners, as a rule, never set out to bind their soul to a dangerous and
enigmatic power. Rather, they have found themselves unintentional masters of eidolons through
incredible circumstances.

**Storm Caller**

**Class:** unchained\_summoner

**Modifies or Replaces:** Eidolon; Summon Monster; Shield Ally; Greater Shield Ally; Maker's Call;
Transposition

**Description:** Many summoners beckon monsters from the Elemental Planes, but few are as
specialized as storm callers, who channel the elemental energies of the Plane of Air.

**Twinned Summoner**

**Class:** unchained\_summoner

**Modifies or Replaces:** Shield Ally; Greater Shield Ally; Maker's Call; Transposition; Merge Forms

**Description:** Reflecting the connected nature of Imbrex, a twinned summoner and his eidolon
appear identical save for any obvious differences, such as evolutions or equipment.

### Archetypes by Feature

|Archetype|Alignment|Aspect|Greater Aspect|Bond Senses|Class Skills|Devotion|Eidolon|Life Link|Maker's Call|Merge Forms|Shield Ally|Greater Shield Ally|Summon Monster|Transposition|Twin Eidolon|Spells|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Construct Caller](ref/arc-unchained-summoner/construct-caller)|||||||X||||||X||||
|[Devil Binder](ref/arc-unchained-summoner/devil-binder)|X|||X||X|||X|X|X|X|X|X|X||
|[Devil Impostor](ref/arc-unchained-summoner/devil-impostor)||||X|X||X||||X|X|X|X|||
|[Fey Caller](ref/arc-unchained-summoner/fey-caller)|||||X||X||||||X||||
|[God Caller](ref/arc-unchained-summoner/god-caller)||X|X||X|||X||||||X|X||
|[Leshy Caller](ref/arc-unchained-summoner/leshy-caller)|||||||X||||||X||||
|[Morphic Savant](ref/arc-summoner/morphic-savant)|||||||X||||||X|||X|
|[Soulbound Summoner](ref/arc-unchained-summoner/soulbound-summoner)|||||||X|X|||||X||||
|[Storm Caller](ref/arc-unchained-summoner/storm-caller)|||||||X||X||X|X|X|X|||
|[Twinned Summoner](ref/arc-unchained-summoner/twinned-summoner)|||||||||X|X|X|X||X|||

### Favored Class Bonuses

_The favored class options for unchained\_summoner are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
