+++
id = "ref/arc-witch/gingerbread-witch"
kind = "archetype"
title = "Gingerbread Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Gingerbread%20Witch"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gingerbread_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "horror-adventures"
page = "72"

[fields]
kind = "archetype"
features = [
  { anchor = "gingerbread-familiar" },
  { anchor = "cauldron-cook", level = 1 },
  { anchor = "tricky-treats-hex", level = 4 },
  { anchor = "confection-conjuring", level = 8 },
  { anchor = "gruesome-gobbler", level = 12 },
  { anchor = "horrible-hunger", level = 16 },
]
trades = [
  { replaces = "Hexes gained at 1st and 10th levels", feature = "hex", levels = [1, 10], by = ["cauldron-cook"] },
  { replaces = "Hex gained at 4th level", feature = "hex", levels = [4], by = ["tricky-treats-hex"] },
  { replaces = "Hex gained at 8th level", feature = "hex", levels = [8], by = ["confection-conjuring"] },
  { replaces = "Hex gained at 12th level", feature = "hex", levels = [12], by = ["gruesome-gobbler"] },
  { replaces = "Hex gained at 16th level", feature = "hex", levels = [16], by = ["horrible-hunger"] },
  { alters = "Familiar", feature = "witch-s-familiar", by = ["gingerbread-familiar"] },
]
+++

A sweet tooth lures the gingerbread witch's victims to doom.

## Gingerbread Familiar (Ex) {#gingerbread-familiar}

A gingerbread witch concocts her familiar out of gingerbread, sugar, and other confections. It has
the shape of the original animal or vermin, but its type changes to [construct](ref/type/construct).
As a construct, it gains 60-foot [darkvision](ref/rule/darkvision) and construct immunities, it
loses any special abilities the animal or vermin has other than movement speed, and it doesn't
provide the usual familiar benefit (for instance, a gingerbread [toad](ref/monster/familiar-toad)
doesn't provide 3 bonus hit points). With a supply of flour and sugar at hand, the gingerbread witch
can spend 8 hours and use her cauldron to restore her familiar to full health at no cost, unless the
familiar is destroyed, in which case she must follow the usual rules for replacing her familiar. A
gingerbread witch can never gain an improved familiar.

This ability alters familiar.

## Cauldron Cook (Ex) {#cauldron-cook}

A gingerbread witch gains the [cauldron](ref/hex/cauldron) and [child-scent](ref/hex/child-scent)
hexes at 1st level. When brewing potions with her cauldron, she can create small candies, pastries,
or similar edible items identical in effect and application to normal potions. At 10th level, she
gains the [cook people](ref/hex/cook-people) hex.

This ability replaces the hexes gained at 1st and 10th levels.

## Tricky Treats Hex (Sp) {#tricky-treats-hex}

At 4th level, a gingerbread witch learns a unique hex that lets her create a piece of candy or a
similar sweet as a full-round action. If eaten by the witch or a single creature she designates when
she creates it, the sweet functions as _[goodberry](ref/spell/goodberry)_ or a
_[polypurpose panacea](ref/spell/polypurpose-panacea)_ (as determined at creation).

Anyone else that eats the sweet becomes [nauseated](ref/misc/nauseated) (Fortitude negates); a
creature nauseated by the sweet can attempt a new saving throw each round at the end of its turn to
end this effect.

A creature that fails its initial save is also affected as per the [scar](ref/hex/scar) hex for a
number of days equal to the witch's witch level, except that at extended range, the witch can use
only harmful hexes on the creature.

She can create a number of sweets each day equal to her Intelligence modifier + her level. These
sweets retain their potency for 24 hours and then turn to crumbs.

This ability replaces the hex gained at 4th level.

## Confection Conjuring (Sp) {#confection-conjuring}

At 8th level, a gingerbread witch can use _[shadow conjuration](ref/spell/shadow-conjuration)_ as a
[spell-like ability](ref/umr/spell-like-abilities). Items and creatures she conjures appear to be
made of fanciful foodstuffs, and because of this, sentient creatures gain a +2 bonus on Will saves
to disbelieve the illusion. However, they otherwise function as described for the
_[shadow conjuration](ref/spell/shadow-conjuration)_ spell. For every 3 witch levels beyond 8th, the
gingerbread witch can duplicate conjuration (creation) and conjuration (summoning) spells of 1 level
higher, up to a maximum of 7th-level spell effects at 20th level (though they are still only 20%
real). The witch can use this ability once per day for every 4 witch levels she has.

This ability replaces the hex gained at 8th level.

## Gruesome Gobbler (Ex) {#gruesome-gobbler}

At 12th level, a gingerbread witch gains a [bite attack](ref/umr/natural-attacks) that deals 1d6
points of damage for a Medium witch. As a full-round action, she can make a single bite attack that
deals double base damage (2d6 for a Medium witch) and functions as if she had the
[grab](ref/umr/grab) and [swallow whole](ref/umr/swallow-whole) special attacks, allowing her to
grab and swallow a creature of her size or smaller. Her stomach doesn't deal damage to swallowed
creatures, but a living creature she swallows must succeed at a Fortitude save (DC = 10 + 1/2 her
witch level + Constitution modifier) at the beginning of each of its turns or become nauseated for 1
round.

If a gingerbread witch successfully swallows a creature, her torso distends grotesquely and she is
treated as if she were [carrying a heavy load](ref/rule/carrying-capacity) if the creature is the
same size and a medium load if it's one size smaller; regardless, she can swallow only one such
creature at a time. Creatures two or more sizes smaller do not distend her belly, though every four
creatures of a smaller size count as one creature one size category larger (she can swallow 4 Tiny,
16 Diminutive, or 64 Fine creatures). She can regurgitate a swallowed creature of her choice as a
move action, leaving it [prone](ref/rule/prone) in an adjacent open square. If she is struck with a
confirmed critical hit while she has a creature swallowed, the swallowed creatures each take half as
much damage as the witch does (this doesn't reduce the damage the gingerbread witch takes).

This ability replaces the hex gained at 12th level.

## Horrible Hunger (Sp) {#horrible-hunger}

At 16th level, a gingerbread witch can affect a target as if she had cast
_[feast of ashes](ref/spell/feast-of-ashes)_ on it, but with her hex DC instead of the spell's DC.
This hunger is so intense that any creature can offer the target food as a standard action and the
target is compelled to eat it, as if the creature offering it had cast
_[beguiling gift](ref/spell/beguiling-gift)_ (with a DC and caster level equal to that of the
witch's hexes). She can use this ability once per day for every 4 witch levels she has.

This ability replaces the hex gained at 16th level.
