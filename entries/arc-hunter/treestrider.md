+++
id = "ref/arc-hunter/treestrider"
kind = "archetype"
title = "Treestrider"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "treestrider", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "55"

[fields]
kind = "archetype"
replaces = ["Animal focus", "second animal focus", "Precise companion", "Raise animal companion"]
alters = ["Animal companion"]
replaces_features = ["animal-focus", "second-animal-focus", "precise-companion", "raise-animal-companion"]
alters_features = ["animal-companion"]
+++

Some hunters are masters of the wild. Whether raised by apes or having some other link with simian
creatures, these hunters glide through the wilderness with ease.

**Animal Companion**

**Alters:** Animal companion

**Info:** A treestrider must select an [ape](ref/companion/ape) as her animal companion.

**Brachiation (Ex)**

**Free:** A treestrider can gain a climb speed equal to half her base speed. In addition, she can
use her climb speed to move through the canopies of forests or jungles, provided the limbs of the
trees are strong enough to support her weight. The treestrider's companion gains a +10-foot
enhancement bonus to its climb speed.

**At 15th Level:** She can use _brachiation_ with no limit on the duration.

**At 8th Level:** The treestrider's climb speed increases to equal her base speed, the duration of
her _brachiation_ increases to 10 minutes per hunter level per day (usable in 10-minute increments),
and the enhancement bonus to her companion's climb speed increases to +20 feet.

**Replaces:** Animal focus, second animal focus

**Usage:** 1 minute/day per hunter level; these minutes need not be consecutive, but must be spent
in 1-minute increments

**Improved Unarmed Strike (Ex)**

**Ability:** A treestrider gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a
bonus feat.

**Gained:** At 2nd Level

**Replaces:** Precise companion

**Tree Stride (Sp)**

**Fullround:** A treestrider can move between two trees, as per the spell
[tree stride](ref/spell/tree-stride). Unlike the spell, this ability has a duration of instantaneous
and the treestrider can make only a single transfer. She can bring her animal companion with her,
but if she does, her companion can't take any actions that round.

**Gained:** At 10th Level

**Replaces:** Raise animal companion

**Usage:** Wis3 modifier times/day
