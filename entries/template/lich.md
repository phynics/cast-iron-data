+++
id = "ref/template/lich"
kind = "rule"
title = "Lich"
source_ids = ["bestiary", "horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lich", path = "json/monster_template2.json" },
]
[[sources]]
publication = "bestiary"
page = "188"

[fields]
kind = "none"
+++

**Lich**

**Acquired:** present

**Challenge rating:** +2

"Lich" is an acquired template that can be added to any living creature (referred to hereafter as
the base creature), provided it can create the required phylactery. A lich retains all the base
creature's statistics and special abilities except as noted here.

**CR:** Same as the base creature + 2.

**Alignment:** Any evil.

**Type:** The creature's type changes to [undead](ref/type/undead). Do not recalculate BAB, saves,
or skill ranks.

**Senses:** A lich gains [darkvision](ref/rule/darkvision) 60 ft.

**AC:** A lich has a +5 natural armor bonus or the base creature's natural armor bonus, whichever is
better.

**Hit Dice:** Change all of the creature's racial Hit Dice to d8s. All Hit Dice derived from class
levels remain unchanged. As undead, liches use their Charisma modifiers to determine bonus hit
points (instead of Constitution).

**Defensive Abilities:** A lich gains [channel resistance](ref/umr/channel-resistance) +4, DR
15/bludgeoning and magic, and [immunity](ref/umr/immunity) to cold and electricity (in addition to
those granted by its undead traits). The lich also gains the following defensive ability.

> **Rejuvenation (Su):** When a lich is destroyed, its phylactery (which is generally hidden by the
> lich in a safe place far from where it chooses to dwell) immediately begins to rebuild the undead
> spellcaster's body nearby. This process takes 1d10 days - if the body is destroyed before that
> time passes, the phylactery merely starts the process anew. After this time passes, the lich
> wakens fully healed (albeit without any gear it left behind on its old body), usually with a
> burning need for revenge against those who previously destroyed it.

**Melee Attack:** A lich has a touch attack that it can use once per round as a natural weapon. A
lich fighting without weapons uses its natural weapons (if it has any) in addition to its touch
attack (which is treated as a primary natural weapon that replaces one claw or slam attack, if the
creature has any). A lich armed with a weapon uses its weapons normally, and can use its touch
attack as a secondary natural weapon.

**Damage:** A lich's touch attack uses negative energy to deal 1d8 points of damage to living
creatures + 1 point of damage per 2 Hit Dice possessed by the lich. As negative energy, this damage
can be used to heal undead creatures. A lich can take a full-round action to infuse itself with this
energy, healing damage as if it had used its touch attack against itself.

**Special Attacks:** A lich gains the two special attacks described below. Save DCs are equal to
10 + 1/2 lich's HD + lich's Cha modifier unless otherwise noted.

> **Fear Aura (Su):** Creatures of less than 5 HD in a 60-foot radius that look at the lich must
> succeed on a Will save or become [frightened](ref/misc/frightened). Creatures with 5 HD or more
> must succeed at a Will save or be [shaken](ref/misc/shaken) for a number of rounds equal to the
> lich's Hit Dice. A creature that successfully saves cannot be affected again by the same lich's
> aura for 24 hours. This is a mind-affecting fear effect.
>
> **Paralyzing Touch (Su):** Any living creature a lich hits with its touch attack must succeed on a
> Fortitude save or be permanently [paralyzed](ref/rule/paralyzed).
> [Remove paralysis](ref/spell/remove-paralysis) or any spell that can remove a curse can free the
> victim (see the [bestow curse](ref/spell/bestow-curse) spell description, with a DC equal to the
> lich's save DC). The effect cannot be dispelled. Anyone paralyzed by a lich seems dead, though a
> DC 20 [Perception](ref/skill/perception) check or a DC 15 [Heal](ref/skill/heal) check reveals
> that the victim is still alive.

**Abilities:** Int +2, Wis +2, Cha +2. Being undead, a lich has no Constitution score.

**Skills:** Liches have a +8 racial bonus on Perception, [Sense Motive](ref/skill/sense-motive), and
[Stealth](ref/skill/stealth) checks. A lich always treats [Climb](ref/skill/climb),
[Disguise](ref/skill/disguise), [Fly](ref/skill/fly), [Intimidate](ref/skill/intimidate),
[Knowledge (arcana)](ref/skill/knowledge-arcana),
[Knowledge (religion)](ref/skill/knowledge-religion), Perception, Sense Motive,
[Spellcraft](ref/skill/spellcraft), and Stealth as class skills. Otherwise, skills are the same as
the base creature.

### Other Templates

[Lich creature](ref/template/lich-creature) is a simple template for creating liches

### Familial Lich

**Sources:** Horror Adventures pg 251

A familial lich does not have a physical body or standard phylactery. Instead, it possesses its own
kin.

In addition to the changes for the lich template, make the following adjustments to the base
creature.

**Defensive Abilities:** A familial lich gains DR 10/good instead of DR 15/bludgeoning and magic,
and loses its rejuvenation ability, but gains an amount of
[spell resistance](ref/rule/spell-resistance) equal to 11 + its CR, and the following defensive
ability.

> **Familial Possession (Su):** When a familial lich is destroyed, its spirit departs its body and
> seeks out the lich's nearest living relative, a process that takes 1d10 days. The familial lich
> then tries to possess the relative, as per [greater possession](ref/spell/possession-greater) (the
> caster level is equal to the familial lich's HD, and the save DC is Charisma-based). If the
> relative succeeds at her save, she becomes permanently immune to this ability, and the familial
> lich must spend another 1d10 days searching for the next-nearest living relative, repeating the
> process until it succeeds or until no such relatives remain and it is destroyed instead.
>
> If the relative fails her saving throw, the familial lich's spirit takes root in her body. The
> familial lich's consciousness remains within the relative even after the
> _[greater possession](ref/spell/possession-greater)_ effect ends, and it is able to share her
> senses. It can use _[greater possession](ref/spell/possession-greater)_ on her once per day
> thereafter. If the relative fails on three consecutive saving throws to resist, the familial
> lich's spirit takes over, and she physically and mentally transforms into the familial lich
> permanently. Even if the relative continues succeeding, it is impossible to remove a familial lich
> without extremely powerful magic once it has taken root.
>
> Only lineal ancestors or descendants of the familial lich, as well as siblings, are eligible
> targets for possession (aunts, uncles, nieces, nephews, cousins, and so forth are immune).
