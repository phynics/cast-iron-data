+++
id = "ref/template/hellbound-creature"
kind = "rule"
title = "Hellbound Creature"
source_ids = ["horror-adventures", "bestiary-4"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hellbound_creature", path = "json/monster_template2.json" },
]
[[sources]]
publication = "horror-adventures"
page = "248"

[fields]
kind = "none"
+++

**Hellbound Creature**

**Acquired:** present

**Challenge rating:** +1

**Simple:** present

> _This template is a simple version of the [devilbound](ref/template/devilbound) template._

Hellbound creatures have consigned their souls to [Hell](ref/rule/hell) in exchange for infernal
power. A hellbound creature's Hit Dice determine what type of [devil](ref/family/devil) it can
summon with its summon [spell-like ability](ref/umr/spell-like-abilities) and the summon ability's
spell level. It can instead choose to summon 1d3 devils of the next weaker category, or 1d4+1 devils
of two categories weaker.

**Quick Rules:** [Darkvision](ref/rule/darkvision); [see in darkness](ref/umr/see-in-darkness); +1
to AC; +1 on rolls based on Str and Cha; contract bound; [gore attack](ref/umr/natural-attacks) that
deals 1d4 points of damage (for Medium creatures); [summon](ref/umr/summon) (see table; 100%).

**Rebuild Rules:** **Senses** [darkvision](ref/rule/darkvision), see in darkness; **AC** natural
armor bonus increases by 1; **Weaknesses** contract bound; **Melee** gore attack that deals 1d4
points of damage (for Medium creatures); **[Spell-like Abilities](ref/umr/spell-like-abilities)**
summon (see table; 100%); **Ability Scores** +2 Str, +2 Cha.

### Hellbound Summon

|Hellbound Creature HD|Devil|Spell Level|
| --- | --- | --- |
|8 or fewer|[Lemure](ref/monster/devil-lemure)|2nd|
|9-10|[Bearded devil](ref/monster/devil-bearded-devil-barbazu)|5th|
|11-12|[Erinyes](ref/monster/devil-erinyes)|6th|
|13-14|[Bone devil](ref/monster/devil-bone-devil-osyluth)|7th|
|15-16|[Barbed devil](ref/monster/devil-barbed-devil-hamatula)|8th|
|17 or more|[Ice devil](ref/monster/devil-ice-devil-gelugon)|9th|

### Contract Bound

**Sources:** Bestiary 4 pg 56\
**Contract Bound (Ex):** The creature has signed a contract of service in return for this template.
The devil must reveal its nature as a creature of [Hell](ref/rule/hell) when it offers a contract,
and it can't hide the details of the contract in any way. The creature must enter the agreement
willingly (without magical compulsion). Usually the creature must perform one or more tasks for the
devil, and in exchange the creature gains the template's abilities, whether immediately, after a
specific amount of time, or once the tasks are completed.

The contract always includes a clause that damns the creature's soul to Hell when the creature dies,
with credit for the act and possession of the soul going to the devil signing the contract. When the
creature dies, its soul is automatically imprisoned in a gem, which immediately appears in Hell as
one of the devil's belongings. If the devil is dead when the creature dies, the creature's soul is
destroyed, and can't be restored to life except by [miracle](ref/spell/miracle) or
[wish](ref/spell/wish). If the creature fails to perform the tasks in the allotted time, its soul is
still damned and the devil is not obligated to provide the promised abilities.

Many contracts state that the devil, its agents, and its allies will not attempt to kill the
creature. This doesn't protect against all devils, but does offer the creature a measure of
protection against treachery from the signatory devil.

Breaking a contract with a devil is difficult and dangerous. Furthermore, as long as the contract
remains in effect, a slain victim can't be restored to life after death except by a
_[miracle](ref/spell/miracle)_ or _[wish](ref/spell/wish)._ If the devilbound creature is restored
to life, the devil immediately senses the name and location (as
[discern location](ref/spell/discern-location)) of the creature responsible.
