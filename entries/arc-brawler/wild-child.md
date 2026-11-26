+++
id = "ref/arc-brawler/wild-child"
kind = "archetype"
title = "Wild Child"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Wild%20Child"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_child", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "89"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-companion", level = 1 },
  { anchor = "hunter-s-tricks", level = 5 },
  { anchor = "maneuver-training", level = 3 },
  { anchor = "wild-tricks", level = 5 },
]
trades = [
  { replaces = "Bonus combat feats gained at 2nd, 8th, 14th, and 20th levels", feature = "bonus-combat-feats", levels = [2, 8, 14, 20], by = ["animal-companion"] },
  { replaces = "Close weapon mastery", feature = "close-weapon-mastery", by = ["hunter-s-tricks"] },
  { replaces = "Bonus combat feats gained at 5th, 11th, and 17th levels", feature = "bonus-combat-feats", levels = [5, 11, 17], by = ["wild-tricks"] },
  { alters = "Maneuver training", feature = "maneuver-training", by = ["maneuver-training"] },
]
+++

The wild child works with his sworn animal friend to conquer the challenges that lay before them.
This kinship could come from being lost in the wilderness and raised by animals or growing up with
an exotic pet.

## Class Skills {#class-skills}

A wild child gains Heal as a class skill.

## Animal Companion (Ex) {#animal-companion}

At 1st level, a wild child forms a bond with a loyal companion that accompanies the wild child on
his adventures. A wild child can begin play with any of the animals available to a druid. The wild
child uses his brawler level as his effective druid level for determining the abilities of his
[animal companion](ref/sidekick/animal-companion). This ability replaces the bonus combat feats
gained at 2nd, 8th, 14th, and 20th levels.

## Hunter's Tricks {#hunter-s-tricks}

At 5th level, a wild child can expend a use of martial flexibility to use a trick from the
[ranger skirmisher archetype](ref/arc-ranger/skirmisher). Each time he activates this ability, the
wild child can use a different hunter trick. He cannot choose any tricks that rely on ranged
attacks. Activating this ability is not an action, but using the trick might require the wild child
to use an action of a different type. This ability replaces close weapon mastery.

## Maneuver Training (Ex) {#maneuver-training}

Whenever the wild child chooses a new maneuver for this ability, his animal companion also learns a
trick to make use of this combat maneuver. For example, if the wild child chooses maneuver training
(dirty trick), his animal companion also learns a trick that allows it to use the dirty trick combat
maneuver. He cannot choose any tricks that rely on ranged attacks. This bonus trick doesn't count
against the animal companion's total tricks known and does not take any time or checks to train.
Should the wild child gain a new animal companion (such as if the previous one dies), this new
animal companion begins with the same number of bonus tricks. This ability alters maneuver training.

## Wild Tricks (Ex) {#wild-tricks}

The wild child has learned a number of tricks to aid his allies and his animal companion, as well as
to hinder his opponents. At 5th level and every 6 levels thereafter, the wild child learns one
hunter's trick. He cannot choose any tricks that rely on ranged attacks. The wild child can use
these tricks a number of times per day equal to 1/2 his brawler level + his Constitution modifier.
This ability otherwise follows the rules of the hunter's tricks ability, including all action costs.
This ability replaces the bonus combat feats gained at 5th, 11th, and 17th levels.
