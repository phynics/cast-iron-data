+++
id = "ref/arc-cleric/herald-caller"
kind = "archetype"
title = "Herald Caller"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "herald_caller", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]

[fields]
kind = "none"
+++

**Sources:** Monster Summoner's Handbook pg 7\
Unlike warpriests or paladins, who charge headlong into battle in the name of their patron deities,
herald callers are adept at calling powerful outsiders to aid their brethren in battle.

**Skill Ranks per Level**

**Alters:** Class skills

**Info:** 4 + Int modifier.

**Dedicated Summoner**

**Alters:** Domains, armor proficiencies

**Info:** A herald caller depends on summoned allies to overcome her foes, which affords her little
experience with the martial pursuits typical of other clerics and a narrower spiritual focus. A
herald caller can choose only one domain from her deity's list of domains, rather than the normal
two domains, and she doesn't gain proficiency with medium armor or shields.

**Call Heralds (Su)**

**Ability:** She can lose a prepared spell in order to cast any
[summon monster](ref/spell/summon-monster) spell of the same level or lower. She gains a bonus on
[concentration](ref/rule/concentration) checks to cast a
_[summon monster](ref/spell/summon-monster)_ spell defensively. This bonus is equal to 1 + one-fifth
of her cleric level.

**Flavor:** A herald caller can channel stored spell energy into summoning spells that she hasn't
prepared ahead of time.

**Divine Heralds (Su)**

**Action:** Ability

A herald caller can use _[summon monster](ref/spell/summon-monster)_ spells only to summon creatures
particularly appropriate to her deity. This includes all creatures listed as
_[summon monster](ref/spell/summon-monster)_ options for priests of her deity, creatures whose
alignment matches at least one aspect of her deity's alignment, and creatures of an elemental
subtype that matches a domain granted by the deity (if any). When summoning a creature that is
normally summoned with the [celestial](ref/template/celestial) or [fiendish](ref/template/fiendish)
template, a herald caller of a chaotic deity can instead summon it with the
[entropic](ref/template/entropic) template, and a herald caller of a lawful deity can instead summon
it with the [resolute](ref/template/resolute) template.

Because of these summoned monsters' strong ties to the herald caller's deity, the herald caller also
gains specific benefits with creatures she summons with _[summon monster](ref/spell/summon-monster)_
spells gained from her cleric spell list. The herald caller and her summoned monsters can understand
each other's spoken words as if they shared a common language (though this doesn't give summoned
monsters the ability to speak if they normally lack it). Whenever the herald caller uses _channel
energy_ to heal, she can include all of her summoned monsters, even if they are out of her normal
_channel energy_ radius or of a creature type that would not normally be affected. If she _channels
energy_ to deal damage, she can exclude any of her summoned monsters that would normally be
affected.

**Mighty Heralds**

**At 4th Level:** A herald caller receives [Augment Summoning](ref/feat/augment-summoning) as a
bonus feat, and is considered to have [Spell Focus](ref/feat/spell-focus) (conjuration) for the
purposes of prerequisites for feats that have Augment Summoning as a prerequisite (such as
[Evolved Summoned Monster](ref/feat/evolved-summoned-monster)).

**At 8th Level:** She gains [Superior Summoning](ref/feat/superior-summoning) as a bonus feat.
