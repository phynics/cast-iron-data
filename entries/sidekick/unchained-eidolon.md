+++
id = "ref/sidekick/unchained-eidolon"
kind = "rule"
title = "Unchained Eidolon"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unchained_eidolon", path = "json/sidekicks.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained\
An eidolon's abilities are determined by the [summoner's](ref/class/summoner) level and by the
choices made using its evolution pool. Each eidolon possesses a base form that modifies these base
statistics. Eidolons are outsiders for the purpose of determining which spells affect them.

The first time a summoner calls his eidolon, he must decide on its subtype. The eidolon's subtype
determines a number of its base statistics and abilities, as well as its overall look and theme. The
subtype also determines what sort of evolutions the summoner can select for his eidolon using the
evolution pool. Once the choice of subtype is made, it cannot be changed.

### Base Forms

Each eidolon has one of the following base forms that determines its starting size, speed, AC,
attacks, and ability scores. All natural attacks are made using the eidolon's full base attack bonus
unless otherwise noted (such as in the case of secondary attacks). An eidolon's attacks add the
eidolon's Strength modifier to the damage rolls, unless the eidolon has only one attack, in which
case the attack adds 1-1/2 times the eidolon's Strength modifier.

Alternatively, any one of these base forms can be used to make a Small eidolon. If the eidolon is
Small, it gains a +2 bonus to Dexterity. It takes a -4 penalty to Strength and a -2 penalty to
Constitution. It also has a +1 size bonus to AC and on attack rolls, a -1 penalty on combat maneuver
checks and to CMD, a +2 bonus on Fly checks, and a +4 bonus on Stealth checks. Reduce the damage of
all of its attacks by one step (for example, 1d6 becomes 1d4, and 1d4 becomes 1d3). If this choice
is made, the eidolon can be made Medium whenever the summoner can change the eidolon's evolution
pool (which causes it to lose these modifiers for being Small). Likewise, a Medium eidolon can be
made Small whenever the summoner can change the eidolon's evolution pool.

> #### Aberrant
>
> Starting Statistics: **Size** Medium; **Speed:** 20f ft., swim 20 ft.; **AC:** +2 natural armor;
> **Saves:** Fort (good), Ref (poor), Will (good); **Attack:** bite (1d6), tentacles (1d6);
> **Ability Scores:** Str 12, Dex 13, Con 16, Int 7, Wis 10, Cha 11
>
> #### Biped
>
> Starting Statistics: **Size** Medium; **Speed:** 30 ft.; **AC:** +2 natural armor; **Saves:** Fort
> (good), Ref (poor), Will (good); **Attack:** 2 claws (1d4); **Ability Scores:** Str 16, Dex 12,
> Con 13, Int 7, Wis 10, Cha 11
>
> #### Quadruped
>
> Starting Statistics: **Size** Medium; **Speed:** 40 ft.; **AC:** +2 natural armor; **Saves:** Fort
> (good), Ref (good), Will (poor); **Attack:** bite (1d6); **Ability Scores:** Str 14, Dex 14, Con
> 13, Int 7, Wis 10, Cha 11
>
> #### Serpentine
>
> Starting Statistics: **Size** Medium; **Speed:** 20 ft., climb 20 ft.; **AC:** +2 natural armor;
> **Saves:** Fort (poor), Ref (good), Will (good); **Attack:** bite (1d6), tail slap (1d6);
> **Ability Scores:** Str 12, Dex 16, Con 13, Int 7, Wis 10, Cha 11

### Base Statistics

|Class Level|HD|BAB|Good Saves|Bad Save|Skills|Feats|Armor Bonus|Str/Dex Bonus|Evolution Pool|Max. Attacks|Special|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|1|+1|+2|+0|4|1|+0|+0|1|3|[Darkvision](ref/rule/darkvision), link, share spells|
|2nd|2|+2|+3|+0|8|1|+2|+1|2|3|Evasion|
|3rd|3|+3|+3|+1|12|2|+2|+1|3|3|-|
|4th|3|+3|+3|+1|12|2|+2|+1|3|4|-|
|5th|4|+4|+4|+1|16|2|+4|+2|4|4|Ability score increase|
|6th|5|+5|+4|+1|20|3|+4|+2|5|4|Devotion|
|7th|6|+6|+5|+2|24|3|+6|+3|6|4|-|
|8th|6|+6|+5|+2|24|3|+6|+3|6|4|-|
|9th|7|+7|+5|+2|28|4|+6|+3|7|5|Multiattack|
|10th|8|+8|+6|+2|32|4|+8|+4|8|5|Ability score increase|
|11th|9|+9|+6|+3|36|5|+8|+4|9|5|-|
|12th|9|+9|+6|+3|36|5|+10|+5|9|5|-|
|13th|10|+10|+7|+3|40|5|+10|+5|10|5|-|
|14th|11|+11|+7|+3|44|6|+10|+5|11|6|Improved evasion|
|15th|12|+12|+8|+4|48|6|+12|+6|12|6|Ability score increase|
|16th|12|+12|+8|+4|48|6|+12|+6|12|6|-|
|17th|13|+13|+8|+4|52|7|+14|+7|13|6|-|
|18th|14|+14|+9|+4|56|7|+14|+7|14|6|-|
|19th|15|+15|+9|+5|60|8|+14|+7|15|7|-|
|20th|15|+15|+9|+5|60|8|+16|+8|15|7|-|

**Class Level:** This is the character's summoner level.

**HD:** This is the total number of 10-sided (d10) Hit Dice the eidolon possesses, each of which
gains a Constitution modifier, as normal.

**BAB:** This is the eidolon's base attack bonus. An eidolon's base attack bonus is equal to its Hit
Dice. Eidolons do not gain additional attacks using their natural weapons for a high base attack
bonus.

**Good Saves and Poor Saves:** These are the eidolon's base saving throw bonuses. An eidolon
possesses two good saving throws and one bad saving throw, determined by the creature's base form.

**Skills:** This lists the eidolon's total skill ranks. An eidolon can assign skill ranks to any
skill, but it must possess the appropriate appendages to use some skills. Eidolons with Intelligence
scores above the base value modify these totals as normal (an eidolon receives a number of skill
ranks equal to 6 + its Intelligence modifier per HD). An eidolon cannot have more ranks in a skill
than it has Hit Dice. Eidolon skill ranks are set once chosen, even if the creature changes when the
summoner gains a new level.

**Feats:** This is the total number of feats possessed by an eidolon. Eidolons can select any feat
that they qualify for, but they must possess the appropriate appendages to use some feats. Eidolon
feats are set once chosen, even if the creature changes when the summoner gains a new level. If, due
to changes, the eidolon no longer qualifies for a feat, the feat has no effect until the eidolon
once again qualifies for the feat.

**Armor Bonus:** The number noted here is the eidolon's base total armor bonus. This bonus may be
split between an armor bonus and a natural armor bonus, as decided by the summoner. This number is
modified by the eidolon's base form and some options available through its evolution pool. An
eidolon cannot wear armor of any kind, as the armor interferes with the summoner's connection to the
eidolon.

**Str/Dex Bonus:** Add this modifier to the eidolon's Strength and Dexterity scores, as determined
by its base form. Some options available through the eidolon's evolution pool might modify these
scores.

**Evolution Pool:** The value given in this column is the total number of points in the eidolon's
evolution pool. Points from this pool can be spent on a wide variety of modifications and upgrades
that add new abilities, attacks, and powers to the eidolon. Whenever the summoner gains a level, the
number in this pool increases and the summoner can spend these points to change the abilities of the
eidolon. These choices are not set. The summoner can change them whenever he gains a level (and
through the [transmogrify](ref/spell/transmogrify) spell).

**Max. Attacks:** This indicates the maximum number of natural attacks that the eidolon is allowed
to possess at the given level. If the eidolon is at its maximum, it cannot take evolutions that
grant additional attacks. Attacks made with weapons, including those granted by a high base attack
bonus, are counted against this maximum.

**Special:** This includes a number of abilities gained by all eidolons as they increase in power.
Each of these bonuses is described below.

> _Darkvision (Ex):_ The eidolon has [darkvision](ref/rule/darkvision) with a range of 60 feet.
>
> _Link (Ex):_ A summoner and his eidolon share a mental link allows for communication across any
> distance (as long as they are on the same plane). This communication is a free action, allowing
> the summoner to give orders to his eidolon at any time. In addition, magic items interfere with
> the summoner's connection to his eidolon. As a result, the summoner and his eidolon share magic
> item slots. For example, if the summoner is wearing a ring, his eidolon can wear no more than one
> ring. In case of a conflict, the items worn by the summoner remain active, and those used by the
> eidolon become dormant. The eidolon must possess the appropriate appendages to utilize a magic
> item.
>
> _Share Spells (Ex):_ The summoner may cast a spell with a target of "you" on his eidolon (as a
> spell with a range of touch) instead of on himself. A summoner can cast spells on his eidolon even
> if the spells normally do not affect creatures of the eidolon's type (outsider). Spells cast in
> this way must come from the summoner spell list. This ability does not allow the eidolon to share
> abilities that are not spells, even if they function like spells.
>
> _Evasion (Ex):_ If an eidolon is subjected to an attack that normally allows a Reflex save for
> half damage, it takes no damage if it makes a successful saving throw.
>
> _Ability Score Increase (Ex):_ The eidolon adds 1 to one of its ability scores.
>
> _Devotion (Ex):_ An eidolon gains a +4 morale bonus on Will saves against enchantment spells and
> effects.
>
> _Multiattack:_ An eidolon gains [Multiattack](ref/feat/multiattack) as a bonus feat if it has 3 or
> more natural attacks and does not already have that feat. If it does not have the requisite 3 or
> more natural attacks (or it is reduced to less than 3 attacks), the eidolon instead gains a second
> attack with one of its natural weapons, albeit at a -5 penalty. If the eidolon later gains 3 or
> more natural attacks, it loses this additional attack and instead gains Multiattack.
>
> _Improved Evasion (Ex):_ When subjected to an attack that allows a Reflex saving throw for half
> damage, an eidolon takes no damage if it makes a successful saving throw and only half damage if
> the saving throw fails.

### Eidolon Skills

The following skills are class skills for eidolons: Bluff (Cha), Craft (Int), Knowledge (planes)
(Int), Perception (Wis), Sense Motive (Wis), and Stealth (Dex). In addition, at 1st level, the
summoner can choose four additional skills to be class skills for his eidolon. Note that eidolons
with a fly speed receive Fly (Dex) as a free class skill, even if they do not gain a fly speed until
a later level.
