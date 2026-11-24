+++
id = "ref/arc-monk/hungry-ghost-monk"
kind = "archetype"
title = "Hungry Ghost Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Hungry%20Ghost%20Monk"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hungry_ghost_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "110"

[fields]
kind = "archetype"
features = [
  { anchor = "punishing-kick", level = 1 },
  { anchor = "steal-ki", level = 5 },
  { anchor = "life-funnel", level = 7 },
  { anchor = "life-from-a-stone", level = 11 },
  { anchor = "sipping-demon", level = 13 },
]
trades = [
  { replaces = "Stunning Fist", feature = "stunning-fist", by = ["punishing-kick"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["steal-ki"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["life-funnel"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["life-from-a-stone"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["sipping-demon"] },
]
+++

The hungry ghost monk looks to spirits that prey upon the living as models of perfection. He sees
the life energy of the universe as a resource to be manipulated, even stealing it from other
creatures. It is through this constant influx of energy that the hungry ghost monk reaches his
ultimate goal: power - personal, pure, and simple. A hungry ghost monk has the following class
features.

## Punishing Kick (Ex) {#punishing-kick}

At 1st level, a hungry ghost monk gains [Punishing Kick](ref/feat/punishing-kick) as a bonus feat,
even if he does not meet the prerequisites. At 10th level, and every five levels thereafter, the
monk can push the target of his Punishing Kick an additional 5 feet (10 feet at 10th level, 15 feet
at 15th level, and 20 feet at 20th level). At 15th level, he can instead choose to push the target 5
feet and knock the target [prone](ref/rule/prone) with the same attack. The target still gets a
saving throw to avoid being knocked prone. This ability replaces Stunning Fist.

## Steal Ki (Ex) {#steal-ki}

At 5th level, a hungry ghost monk can steal _ki_ from other creatures, though this ability is
controversial in some circles of monks, who see it as nothing less than a form of vampirism. If the
monk scores a confirmed critical hit against a living enemy or reduces a living enemy to 0 or fewer
hit points, he can steal some of that creature's _ki_. This ability replenishes 1 spent _ki_ point
to the monk's _ki_ pool, as long as the monk has at least 1 _ki_ point in his pool. He cannot exceed
his _ki_ pool's maximum. At 11th level, each time the monk successfully steals _ki_, he can make an
immediate saving throw against one disease he is suffering from. There is no penalty for failing
this saving throw. The monk gains a bonus equal to his Wisdom modifier on the saving throw. This
ability replaces purity of body.

## Life Funnel (Su) {#life-funnel}

At 7th level, a hungry ghost monk can steal a creature's life force to replenish his own. If the
monk has at least 1 _ki_ point in his _ki_ pool and scores a confirmed critical hit against a living
enemy or reduces a living enemy to 0 or fewer hit points, he heals a number of hit points equal to
his monk level. As with steal _ki_, some monks believe that life funnel is an unsavory act, no
better than what the undead do to the living. A monk with this ability cannot steal both _ki_ and
hit points at the same time. This ability replaces wholeness of body.

## Life from a Stone (Su) {#life-from-a-stone}

At 11th level, a hungry ghost monk can steal _ki_ or life force from any creature, not just living
creatures. If the monk has at least 1 ki point in his pool, he gains the benefit of life funnel and
steal _ki_ when he confirms a critical hit against any creature or reduces any creature to 0 or
fewer hit points. This ability replaces diamond body.

## Sipping Demon (Su) {#sipping-demon}

At 13th level, a hungry ghost monk gains 1 [temporary hit point](ref/rule/temporary-hit-points) each
time he hits an enemy with a melee attack. The monk gains a number of temporary hit points equal to
his Wisdom modifier when he scores a critical hit. The maximum number of temporary hit points the
monk can have is equal to his monk level. The temporary hit points disappear 1 hour later. The monk
can only use this ability when he has at least 1 _ki_ point in his _ki_ pool. This ability is a
proscribed manipulation of _ki_ considered by many good monks to be a corruption. This ability
replaces diamond soul.
