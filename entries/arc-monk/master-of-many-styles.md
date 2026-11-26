+++
id = "ref/arc-monk/master-of-many-styles"
kind = "archetype"
title = "Master of Many Styles"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Master%20of%20Many%20Styles"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "master_of_many_styles", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "59"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat", level = 1 },
  { anchor = "fuse-style", level = 1 },
  { anchor = "perfect-style", level = 20 },
]
trades = [
  { replaces = "Standard bonus feats", feature = "bonus-feat", by = ["bonus-feat"] },
  { replaces = "Flurry of blows", feature = "flurry-of-blows", by = ["fuse-style"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["perfect-style"] },
]
+++

The master of many styles is a collector. For every move, he seeks a counter. For every style, he
has a riposte. Ultimately, he seeks perfection through the fusion of styles.

## Bonus Feat {#bonus-feat}

At 1st level, 2nd level, and every four levels thereafter, a master of many styles may select a
bonus style feat or the [Elemental Fist](ref/feat/elemental-fist) feat (_Advanced Player's Guide_
158). He does not need to meet the prerequisites of that feat, except the Elemental Fist feat.
Starting at 6th level, a master of many styles can choose to instead gain a wildcard style slot.
Whenever he enters one or more styles, he can spend his wildcard style slots to gain feats in those
styles' feat paths (such as [Earth Child Topple](ref/feat/earth-child-topple)) as long as he meets
the prerequisites. Each time he changes styles, he can also change these wildcard style slots. This
ability replaces a monk's standard bonus feats.

## Fuse Style (Ex) {#fuse-style}

At 1st level, a master of many styles can fuse two of the styles he knows into a more perfect style.
The master of many styles can have two style feat stances active at once. Starting a stance provided
by a style feat is still a swift action, but when the master of many styles switches to another
style feat, he can choose one style whose stance is already active to persist. He may only have two
style feat stances active at a time.

At 8th level, the master of many styles can fuse three styles at once. He can have the stances of
three style feats active at the same time. He gains a bonus on attack rolls equal to the number of
styles whose stances he currently has active. Furthermore, he can enter up to three stances as a
swift action.

At 15th level, the master of many styles can fuse four styles at once. He can have the stances of
four style feats active at the same time. Furthermore, he can enter up to four stances as a free
action by spending 1 point from his ki pool.

This ability replaces flurry of blows.

## Perfect Style (Ex) {#perfect-style}

At 20th level, a master of many styles can have the stances of five style feats active at once, and
can change those stances as a free action. This ability replaces perfect self.
