+++
id = "ref/arc-ranger/wilderness-medic"
kind = "archetype"
title = "Wilderness Medic"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Wilderness%20Medic"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wilderness_medic", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "healers-handbook"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "herbalist-training", level = 1 },
  { anchor = "herbal-medicine", level = 3 },
  { anchor = "rallying-bond", level = 4 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["herbalist-training"] },
  { replaces = "Endurance", feature = "endurance", by = ["herbal-medicine"] },
  { replaces = "evasion", feature = "evasion", by = ["herbal-medicine"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["rallying-bond"] },
  { alters = "Hunter's bond", feature = "hunter-s-bond", by = ["rallying-bond"] },
]
+++

Wilderness medics know a variety of ways they can supply and preserve a rebellion or similar
movement without requiring any resources that might make them easier to track down.

## Herbalist Training (Ex) {#herbalist-training}

At 1st level, a wilderness medic can attempt Profession (herbalism) checks untrained and the
wilderness medic gains a bonus equal to 1/2 his ranger level (minimum +1) on Heal checks and
Profession (herbalism) checks. When he successfully [forages](ref/rule/foraging) for herbs, he finds
twice as many doses of any herb he would normally.

This ability replaces wild empathy.

## Herbal Medicine (Ex) {#herbal-medicine}

At 3rd level, a wilderness medic can mimic the effects of _[stabilize](ref/spell/stabilize)_ at will
in any wilderness area by spending one use of a [healer's kit](ref/eq-misc/healers-kit) as long as
he can see the target.

Additionally, as a standard action a number of times per day equal to 3 + his Wisdom modifier, the
wilderness medic can use encouraging words and herbs to lessen the severity of certain conditions
affecting a touched target. If the target is [exhausted](ref/misc/exhausted), it becomes
[fatigued](ref/misc/fatigued) instead. If the target is [frightened](ref/misc/frightened), it
becomes [shaken](ref/misc/shaken) instead. If the target is [nauseated](ref/misc/nauseated), it
becomes [sickened](ref/misc/sickened) instead. The duration of the effect is unchanged; the effect
is simply reduced to the lesser version.

At 9th level, the wilderness medic can lessen the severity of additional conditions for the target
and cure other conditions that the target suffers. If the target creature is
[blinded](ref/misc/blinded), it becomes [dazzled](ref/misc/dazzled) instead. If the target is
[panicked](ref/misc/panicked), it becomes shaken instead. If it has any of the following conditions,
they are cured: [deafened](ref/misc/deafened), fatigued, shaken, and sickened.

The wilderness medic is able to use this ability on a given touched target once every 24 hours.

This ability replaces the endurance and evasion abilities.

## Rallying Bond (Sp) {#rallying-bond}

At 4th level, a wilderness medic must choose his companions for his hunter's bond.

At 9th level, the wilderness medic can encourage all of his companions when he uses his hunter's
bond to benefit his companions (see the ranger's hunter's bond ability on page 66 of the _Pathfinder
RPG Core Rulebook_ for more details).

As a free action when the wilderness medic uses a move action to grant affected allies half his
favored enemy bonus, he can also grant affected allies the benefits of
_[remove fear](ref/spell/remove-fear)_. The wilderness medic can use this ability a number of times
per day equal to his Wisdom modifier.

At 14th level, when the wilderness medic uses this ability, he can instead affect all allies that
benefit from his hunter's bond with _[blessing of fervor](ref/spell/blessing-of-fervor)_, using his
ranger level as his caster level.

This ability alters hunter's bond and replaces improved evasion.
