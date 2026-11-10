+++
id = "ref/arc-ranger/wilderness-medic"
kind = "archetype"
title = "Wilderness Medic"
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
replaces = ["Wild empathy", "Endurance", "evasion", "Improved evasion"]
alters = ["Hunter's bond"]
replaces_features = ["wild-empathy", "endurance", "evasion", "improved-evasion"]
alters_features = ["hunter-s-bond"]
+++

Wilderness medics know a variety of ways they can supply and preserve a rebellion or similar
movement without requiring any resources that might make them easier to track down.

**Herbalist Training (Ex)**

**Ability:** A wilderness medic can attempt Profession (herbalism) checks untrained and the
wilderness medic gains a bonus equal to 1/2 his ranger level (minimum +1) on Heal checks and
Profession (herbalism) checks. When he successfully [forages](ref/rule/foraging) for herbs, he finds
twice as many doses of any herb he would normally.

**Gained:** At 1st Level

**Replaces:** Wild empathy

**Herbal Medicine (Ex)**

**Ability:** A wilderness medic can mimic the effects of [stabilize](ref/spell/stabilize) at will in
any wilderness area by spending one use of a [healer's kit](ref/eq-misc/healers-kit) as long as he
can see the target.

**At 9th Level:** The wilderness medic can lessen the severity of additional conditions for the
target and cure other conditions that the target suffers. If the target creature is
[blinded](ref/misc/blinded), it becomes [dazzled](ref/misc/dazzled) instead. If the target is
[panicked](ref/misc/panicked), it becomes shaken instead. If it has any of the following conditions,
they are cured: [deafened](ref/misc/deafened), fatigued, shaken, and sickened.

**Gained:** At 3rd Level

**Replaces:** Endurance, evasion

**Special:** The wilderness medic is able to use the non-_[stabilize](ref/spell/stabilize)_ ability
on a given touched target once every 24 hours.

**Standard:** The wilderness medic can use encouraging words and herbs to lessen the severity of
certain conditions affecting a touched target. If the target is [exhausted](ref/misc/exhausted), it
becomes [fatigued](ref/misc/fatigued) instead. If the target is [frightened](ref/misc/frightened),
it becomes [shaken](ref/misc/shaken) instead. If the target is [nauseated](ref/misc/nauseated), it
becomes [sickened](ref/misc/sickened) instead. The duration of the effect is unchanged; the effect
is simply reduced to the lesser version.

**Usage:** Wisdom3 modifier times/day

**Rallying Bond (Sp)**

**Alters:** Hunter's bond

**At 14th Level:** When the wilderness medic uses this ability, he can instead affect all allies
that benefit from his _hunter's bond_ with [blessing of fervor](ref/spell/blessing-of-fervor), using
his ranger level as his caster level.

**At 4th Level:** A wilderness medic must choose his companions for his _hunter's bond._

**At 9th Level:** The wilderness medic can encourage all of his companions when he uses his
_hunter's bond_ to benefit his companions (see the ranger's _hunter's bond_ ability). As a **free
action** when the wilderness medic uses a **move action** to grant affected allies half his _favored
enemy_ bonus, he can also grant affected allies the benefits of
[remove fear](ref/spell/remove-fear).

**Replaces:** Improved evasion

**Usage:** Wisdom modifier times/day
