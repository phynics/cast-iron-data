+++
id = "ref/arc-alchemist/herbalist"
kind = "archetype"
title = "Herbalist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Herbalist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "herbalist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "herbalism" },
  { anchor = "natural-magic", level = 1 },
  { anchor = "seedpods", level = 1 },
]
trades = [
  { replaces = "Throw Anything", feature = "throw-anything", by = ["natural-magic"] },
  { replaces = "Bombs", feature = "bomb", by = ["seedpods"] },
  { replaces = "poison use", feature = "poison-use", by = ["seedpods"] },
  { replaces = "poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["seedpods"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [10], by = ["seedpods"] },
  { alters = "Alchemy", feature = "alchemy", by = ["herbalism"] },
  { alters = "the alchemist's key ability score", by = ["herbalism"] },
]
+++

Vine leshys who study the physical and spiritual composition of their own bodies have discovered a
strange herbal alchemy all their own.

## Herbalism (Su) {#herbalism}

An herbalist's studies allow him a unique method of creating alchemical discoveries. He can attempt
Profession (herbalist) checks in place of Craft (alchemy) checks for all purposes, and he gains a
competence bonus equal to [half](ref/misc/fractions-and-rounding) his alchemist level on Profession
(herbalist) checks to create alchemical items and to forage for and process herbs (see page 152). An
herbalist uses his Wisdom score instead of his Intelligence score for all alchemist class abilities.

This alters alchemy and the alchemist's key ability score.

## Natural Magic {#natural-magic}

An herbalist's study of the leshy spirit grants him access to natural magic that eludes other
alchemists. Each time he gains access to a new level of extracts (including 1st level), he can add
two spells from that spell level on the druid spell list to his alchemist class spell list; these
spells must target a creature or creatures or have a range of "you," and he must still add them to
his formula book as normal before he can prepare them. As always, the extracts affect the drinker as
if she were the target, so offensive touch spells are a nasty trap for the drinker.

This replaces Throw Anything.

## Seedpods (Su) {#seedpods}

An herbalist can produce and throw seedpods as ranged touch attacks, similar to the ranged attacks
of other leshys. He can create a number of seedpods each day equal to his alchemist level + his
Wisdom modifier and can throw them as a standard action with a range increment of 20 feet. A seedpod
deals 1d6 points of bludgeoning damage, plus an additional 1d6 points of damage at 3rd level and
every 2 levels thereafter (this additional damage isn't multiplied on a critical hit or from effects
like [Vital Strike](ref/feat/vital-strike)). Seedpods are considered weapons and can be selected for
feats like [Weapon Focus](ref/feat/weapon-focus), and the herbalist can take the
[Extra Bombs](ref/feat/extra-bombs) feat to gain additional daily uses of his seedpods. His seedpods
also gain one of the following additional effects unless the target succeeds at a Fortitude save (DC
= 10 + half the herbalist's alchemist level + his Wisdom modifier). At 1st level, his seedpods can
[deafen](ref/misc/deafened) their target for 1 round like a
[leaf leshy](ref/monster/leshy-leaf-leshy). At 2nd level, they can reduce the target's vision to 10
feet for 1 minute (unless the target spends a full-round action to wash the spores from its eyes
early) like the spores of a [fungus leshy](ref/monster/leshy-fungus-leshy). At 5th level, they can
[entangle](ref/rule/entangled) their target for 2d4 rounds (unless the target succeeds at a Strength
check or Escape Artist check at the save DC to break the vine early) like the seeds of a
[gourd leshy](ref/monster/leshy-gourd-leshy). At 8th level, they can [sicken](ref/misc/sickened)
their target for 1d4 rounds like the spittle of a [flytrap leshy](ref/monster/leshy-flytrap-leshy).
At 10th level, they can [blind](ref/misc/blinded) their target until the end of their next turn like
the water jets of a [seaweed leshy](ref/monster/leshy-seaweed-leshy).

This replaces bombs, poison use, poison resistance, and poison immunity.
