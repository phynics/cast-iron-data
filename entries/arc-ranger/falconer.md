+++
id = "ref/arc-ranger/falconer"
kind = "archetype"
title = "Falconer"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Falconer"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "falconer", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-combat"
page = "67"

[fields]
kind = "archetype"
features = [
  { anchor = "feathered-companion", level = 1 },
  { anchor = "hunter-s-bond", level = 4 },
  { anchor = "swoop-for-the-kill", level = 6 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["feathered-companion"] },
  { replaces = "Combat style feat the ranger gains at 6th level", feature = "combat-style-feat", levels = [6], by = ["swoop-for-the-kill"] },
]
+++

Rangers have always enjoyed a special bond with a specific animal, but the falconer takes this bond
to a deeper level. Falconers begin with their companion earlier than other rangers, and have the
ability to teach their companions special tricks.

## Feathered Companion (Ex) {#feathered-companion}

At 1st level, a falconer earns the trust and companionship of a [bird](ref/companion/bird) of prey.
The bird can be of any type of large hunting or scavenging bird (even a vulture). This ability
functions like the druid [animal companion](ref/sidekick/animal-companion) ability (which is part of
the nature bond class feature), but the falconer must take the bird animal companion, and that
companion has only half the normal hit points.

The falconer cannot teach the bird of prey the work trick, but can teach it either the roam or
distract trick for free. Whichever trick the falconer does not pick then can be picked as a trick
later.

### Roam (DC 15) {#roam-dc-15}

The falconer can let his animal companion loose to roam and forage. He must let it roam for no more
than a week. When the falconer lets it roam, it agrees to return to the place he let it loose within
the time period he designates.

### Distract (DC 20; bird only) {#distract-dc-20-bird-only}

The animal companion flutters wildly around any enemy it would normally attack with the attack
trick. It makes an attack roll against that enemy. On a hit, the enemy is [shaken](ref/misc/shaken)
for 1 round.

This ability replaces wild empathy.

## Hunter's Bond (Ex) {#hunter-s-bond}

At 4th level, a falconer must select an animal companion when he gains hunter's bond. He does not
gain a new companion at 4th level; rather, his feathered companion gains full hit points.

## Swoop for the Kill (Ex) {#swoop-for-the-kill}

At 6th level, when outdoors, a falconer can direct his feathered companion to strike an enemy from
high above. His feathered companion gains the following trick as a bonus trick.

### Swooping Charge (DC 20; bird) {#swooping-charge-dc-20-bird}

The falconer's bird companion flies up and then swoops down into a [charge](ref/rule/charge). To
perform this trick, the companion must be able to fly, and it must be outdoors or someplace with
enough room for the bird to fly great distances in (a grand cathedral may have enough room, but
dungeons usually do not). It spends a full-round action flying to a high vantage point, and on the
next round makes a charge attack upon an enemy the falconer designates. If that charge attack hits,
the bird deals 2d4 points of damage instead of 1d4 with its bite and gains a ×4 critical modifier
when making the attack. If the bird hits, the target is [staggered](ref/misc/staggered) for 1 round.

This ability replaces the combat style feat the ranger gains at 6th level.
