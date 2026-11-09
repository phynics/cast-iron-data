+++
id = "ref/template/guardian-spirit"
kind = "rule"
title = "Guardian Spirit"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guardian_spirit", path = "json/monster_template2.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "26"

[fields]
kind = "none"
+++

**Guardian Spirit**

**Acquired:** present

**Challenge rating:** Varies

A guardian spirit is bound to the fate of a mortal being (called its "ward"). This bond may be
formed by any number of beings or events carrying the weight of destiny, such as deities,
[the Eldest](ref/rule/the-eldest), [norns](ref/monster/norn), and mythic creatures and magic. A
spirit can bind itself willingly if it believes that doing so is likely to further its agenda, give
it more power, or allow it access to the world of mortals. Mortals can generally invoke a guardian
spirit only with [summoning](ref/spelldef/summoning) and [calling](ref/spelldef/calling) spells.

"Guardian spirit" is an acquired template that can be added to any [fey](ref/type/fey) or
[outsider](ref/type/outsider) that qualifies to become a familiar through the
[Improved Familiar](ref/feat/improved-familiar) feat (this template does not make it a familiar,
however). A guardian spirit uses all the base creature's statistics and special abilities except as
noted here. A guardian spirit has a rune on its forehead similar to that on an
[eidolon](ref/sidekick/eidolon) (though its ward does not gain a matching rune).

|Conjuration Spell Level|CR|Armor Class|Hit Dice|Ability Scores|Special|
| --- | --- | --- | --- | --- | --- |
|3|+0|+0|+0|+2|Smite threat 1/day, [spell-like abilities](ref/umr/spell-like-abilities)|
|4|+2|+2|+2|+2|Fated guardian, [spell-like ability](ref/umr/spell-like-abilities)|
|5|+4|+4|+4|+4|[Spell-like ability](ref/umr/spell-like-abilities)|
|6|+6|+6|+6|+4|Smite threat 2/day, [spell-like ability](ref/umr/spell-like-abilities)|
|7|+8|+8|+8|+6|[Spell-like ability](ref/umr/spell-like-abilities)|
|8|+10|+10|+10|+6|Co-walker, [spell-like ability](ref/umr/spell-like-abilities)|
|9|+12|+12|+12|+8|Smite threat 3/day, [spell-like ability](ref/umr/spell-like-abilities)|

**CR:** The guardian spirit's CR increases based on the level of spell used to summon it, as noted
on the Conjured Guardian table above.

**AC:** The guardian spirit's natural armor bonus increases based on the level of spell used to
summon it, as noted on the Conjured Guardian table.

**Hit Dice:** The guardian spirit's Hit Dice increase based on the level of spell used to summon it,
as noted on the Conjured Guardian table. It gains appropriate skill points, feats, ability score
increases, base attack bonus, and base saving throw advancements for its increased Hit Dice.

**Defensive Abilities:** The guardian spirit has an amount of
[spell resistance](ref/rule/spell-resistance) equal to 11 + its CR unless the base creature's SR was
higher.

**Ability Scores:** The guardian spirit's Charisma score becomes 18 unless the base creature's
Charisma score was higher. Each of the guardian spirit's ability scores increases when it's summoned
by higher-level spells, as noted on the Conjured Guardian table above.

**Special Attacks:** If the guardian spirit has extraordinary or supernatural abilities that deal
hit point damage measured in dice, the number of dice increases by an amount equal to the level of
spell used to conjure it - 3. If the ability requires at least a standard action to activate and has
an instantaneous duration, the damage increases by an additional die.

**Special:** The guardian spirit gains a smite and additional special abilities as noted on the
table.

> **Smite Threat (Su):** Once per day as a swift action, the guardian spirit can add its Charisma
> bonus on attack rolls and its HD on damage rolls against a foe that currently threatens its ward
> or has attacked the ward within the past 24 hours; this smite persists until the target is dead or
> the summoning of the guardian spirit ends. If the spirit is summoned by a 6th-level spell, it can
> use smite threat an additional time per day, and if the spirit is summoned by a 9th-level spell,
> it can use smite threat a third time per day.
>
> **Spell-Like Abilities:** A guardian spirit's caster level for its
> [spell-like abilities](ref/umr/spell-like-abilities) is equal to its Challenge Rating + 1, or to
> the base creature's caster level, whichever is higher. It can cast [guidance](ref/spell/guidance)
> at will. For every spell level of the conjuration spell used to call or summon it (such as
> [planar ally](ref/spell/planar-ally), [planar binding](ref/spell/planar-binding), or
> [summon monster](ref/spell/summon-monster) if the summoner has the
> [Summon Guardian Spirit](ref/feat/summon-guardian-spirit) feat), the guardian spirit gains access
> to one additional spell-like ability of the ward's choice from the following list:
>
> - **Spell Level 3:** [Chill touch](ref/spell/chill-touch), [ill omen](ref/spell/ill-omen),
>   [protection from chaos/evil/good/law](ref/spell/protection-from-law) (choose one; its alignment
>   descriptor must oppose the guardian spirit's alignment).
> - **Spell Level 4:** [Call lightning](ref/spell/call-lightning),
>   [detect thoughts](ref/spell/detect-thoughts), [invisibility](ref/spell/invisibility).
> - **Spell Level 5:** [Cure serious wounds](ref/spell/cure-serious-wounds),
>   [dispel magic](ref/spell/dispel-magic), [shout](ref/spell/shout).
> - **Spell Level 6:** [Call lightning storm](ref/spell/call-lightning-storm),
>   [death ward](ref/spell/death-ward), [freedom of movement](ref/spell/freedom-of-movement).
> - **Spell Level 7:** [Break enchantment](ref/spell/break-enchantment),
>   [breath of life](ref/spell/breath-of-life), [contagious flame](ref/spell/contagious-flame).
> - **Spell Level 8:** [Cloak of dreams](ref/spell/cloak-of-dreams),
>   [greater heroism](ref/spell/heroism-greater), [sunbeam](ref/spell/sunbeam).
> - **Spell Level 9:** [Greater shout](ref/spell/shout-greater),
>   [power word blind](ref/spell/power-word-blind), [regenerate](ref/spell/regenerate).
>
> Each chosen [spell-like ability](ref/umr/spell-like-abilities) is available once per day.
>
> **Fated Guardian (Su):** When conjured by a 4th-level or higher spell, a guardian spirit can
> protect the destiny of another creature within 30 feet as a standard action once per day. For 1
> round, any time the creature makes an attack or attempts a saving throw, it rolls twice and takes
> the better result.
>
> **Co-Walker (Sp):** When conjured by an 8th-level or higher spell, a guardian spirit can assume
> the shape of its ward as if with [alter self](ref/spell/alter-self), except it can appear to be
> only the ward (even if the ward is not of a creature type or size that can normally be assumed
> with _[alter self](ref/spell/alter-self)_) and it gains a +10 bonus on Disguise checks to appear
> to be the ward.
