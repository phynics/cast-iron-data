+++
id = "ref/rule/armor-as-dr"
kind = "rule"
title = "Armor as DR"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "armor_as_dr", path = "json/rules_opt_combat01.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "191"

[fields]
kind = "none"
+++

Armor in this system keeps all of its normal statistics and qualities, but its armor bonus
(including any enhancement bonus added to armor bonus and natural armor bonus) is converted to
DR/armor. The DR an armor provides is equal to its total armor bonus with a +1 bonus at 5th level or
at 5 Hit Dice, with an increase to that bonus of +1 for every five levels above 5th level, or every
5 Hit Dice over 5 Hit Dice (to a maximum of +4 to DR at 20th level or at 20 or more Hit Dice),
provided that the creature wearing the armor is also proficient with the armor.

**Using Armor without Proficiency:** Creatures using armor they are not proficient with do not gain
the bonus per level or Hit Dice to the DR, on top of any of the other normal penalties for using
armor without proficiency.

**DR/Armor:** This type of DR blocks the damage of all attacks that would normally be affected by
DR, based on the composition of the armor (see Table 5-1). Unlike most forms of
[damage reduction](ref/rule/damage-reduction), DR/armor stacks with other types of DR. For
instances, when fighting a skeleton with DR 5/bludgeoning and DR 4/armor (+2 for armor, +2 for
natural armor), the skeleton's DR/armor reduces 9 points of damage from non-bludgeoning attacks, and
4 damage from bludgeoning weapon attacks. Magic weapons and attacks from Large or larger creatures
bypass the DR 4/armor, but not the DR 5/bludgeoning.

### Table 5-1: Armor Composition and DR

|Material|DR Provided|Attacker Size to Bypass DR|
| --- | --- | --- |
|Nonmagical armor^[1](ref/rule/armor-as-dr#footnote-1)^|DR/magic|Large|
|Magical armor^[1](ref/rule/armor-as-dr#footnote-1)^|DR/adamantine|Huge|
|Adamantine armor^[1](ref/rule/armor-as-dr#footnote-1)^|DR/-|Gargantuan|

**Natural Armor Bonus and DR:** Like a creature's armor bonus, a natural armor bonus is also
converted into [damage reduction](ref/rule/damage-reduction). If a creature is wearing armor and has
a natural armor bonus, the creature adds its armor bonus to its natural armor bonus to determine the
amount of DR/armor that it has (see Table 5-2).

For instance, if a creature wearing a +2 chain shirt has DR 6/armor is then subject to a
[barkskin](ref/spell/barkskin) spell cast by a 6th-level druid (gaining a +3 natural armor bonus),
its DR becomes DR 9/armor for the duration of the spell. This DR is bypassed by adamantine, or the
attacks of Huge or larger creatures.

A creature that has both DR from a source other than armor and a natural armor bonus gains the
effects of an enhanced form of DR, similar to how the composition of the armor grants special
DR/armor defenses (see Table 5-1). If a creature has magical armor, natural armor, and DR, it takes
the best form of the special protection provided by both its armor and its mix of DR and natural
armor to its DR/armor.

For instance, if a creature has natural armor and DR/magic and is wearing adamantine armor, that
creature's DR/armor functions as DR/-, and can be bypassed by Gargantuan or larger creatures, since
the adamantine armor provides the best of the two damage reductions.

### Table 5-2: Natural Armor Conversion to DR

|Armor|Type|Size|
| --- | --- | --- |
|Natural armor|DR/magic|Large|
|Natural armor with DR/magic|DR/adamantine|Huge|
|Natural armor with DR/adamantine|DR/-|Gargantuan|
|Natural armor with DR/-|DR/-^[2](ref/rule/armor-as-dr#footnote-2)^|Colossal|
|Natural armor with DR/epic|DR/epic^[2](ref/rule/armor-as-dr#footnote-2)^|n/a|

**Unusual Creatures and Armor DR:** Amorphous or incorporeal creatures have an easier time bypassing
DR/armor. When they attack a creature with DR/armor, they typically treat that DR as a fraction of
the DR/armor. Attacks by incorporeal creatures entirely ignore the DR unless that DR comes from a
force effect or from armor with the [ghost touch](ref/magic-enh/ghost-touch-armor) special armor
quality. These traits are detailed in Table 5-3.

### Table 5-3: Unusual Creatures and Armor DR

|Attacking Creature Type|DR Modifier|
| --- | --- |
|Amorphous^[3](ref/rule/armor-as-dr#footnote-3)^|× 1/2|
|Incorporeal|× 0 (×1 if DR is from force effect or _ghost touch_ armor|
|Swarm of Tiny creatures|× 1/2|
|Swarm of Diminutive creatures|× 1/4|
|Swarm of Fine creatures|× 0|

###### ^1^ {#footnote-1}

[Brilliant energy](ref/magic-enh/brilliant-energy) weapons bypass any DR provided by armor. In
addition, DR from armor is halved if a creature is grappled or entangled, and does not apply when a
creature is helpless or pinned.

###### ^2^ {#footnote-2}

A creature that already has DR/- or DR/epic increases its DR by an amount equal to its natural armor
bonus.

###### ^3^ {#footnote-3}

Elementals, oozes, ooze-like creatures, and any creature with the amorphous defensive ability.
