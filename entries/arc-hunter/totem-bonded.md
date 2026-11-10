+++
id = "ref/arc-hunter/totem-bonded"
kind = "archetype"
title = "Totem-Bonded"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "totem_bonded", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "adventurers-guide"
page = "131"

[fields]
kind = "archetype"
replaces = ["Animal focus"]
alters = ["Animal companion"]
replaces_features = ["animal-focus"]
alters_features = ["animal-companion"]
+++

The [Mammoth Lords](ref/rule/aff-beast-riders) coexist with the great primeval beasts that roam
their lands, surviving with the help of the animals' meat, hides, milk, bones, and more. These
fearsome and wondrous animals have made their way into Kellid culture and tradition. Tribes are
named after these creatures. Armor, clothing, weapons, and jewelry - when not fashioned from bone,
hide, or teeth harvested from these beasts - are worked into images that evoke their shape and
strength. They are even captured and trained for use as guardians, as hunters, or in the most iconic
use, as mounts - though they're rarely tamed, as the Mammoth Lords value the ferociousness of these
creatures. The sight of a Mammoth Lord atop an elephantine steed is one that few soon forget.

For some of the people of the Mammoth Lords, this adoration and respect for the megafauna that share
their realm goes one step further. Shamans, oracles, druids, and others worship these animals as
primal spirits of the world and draw great power from their faith. Others, like rangers and
barbarians, are no less faithful in their belief, even though they focus more on physical combat
than on spellcasting. Among the most devoted of these hunters are the so-called totem-bonded-hunters
who are able to form a true spiritual bond with the powerful fauna that dominate the wildlands. Such
a hunter embraces one of the realm's megafauna as a sort of spiritual guide, eventually attracting a
mighty beast that travels with her and helps keep her territory free of invaders. By doing so, the
totem-bonded hunter becomes something more than merely a guardian and provider for her tribe - she
becomes a manifestation of the tribe's spiritual belief in the power of the land itself.

**Primeval Companion (Ex)**

**Ability:** The totem-bonded adopts a powerful animal native to the region - often one suited to
the cold tundra - selected from the following list: [aurochs](ref/companion/aurochs),
[badger](ref/companion/badger), [bear](ref/companion/bear), [big cat](ref/companion/cat-big),
[elk](ref/companion/elk), [giant raven](ref/companion/raven-giant),
[mastodon](ref/companion/elephant-mastodon), [rhinoceros](ref/companion/rhinoceros),
[walrus](ref/companion/walrus), [wolf](ref/companion/wolf), or any creature categorized as
megafauna. At the GM's discretion, she can select other animal companions.

**Alters:** Animal companion

**At 7th Level:** If the animal companion's natural size is Large but it is normally available as a
Medium animal companion at 7th level (such as a bear), the totem-bonded can have the companion
increase in size. To generate statistics for such a creature, apply the following modifications:
**Size** Large; **AC** +1 natural armor; **Ability Scores** _Str_ +4, _Dex_ -2, _Con_ +2. Increase
the damage of each of the companion's natural attacks
[by one die size](ref/misc/damage-die-adjustments).

**Shared Strength (Su)**

**Action:** Ability

**At 15th Level:** The damage dealt by any natural attacks granted by this ability increases by two
die steps. The animal companion's bonuses on saving throws and skill checks increase to +2 and +4
respectively.

**At 8th Level:** The totem-bonded manifests two aspects of her animal companion. The animal
companion gains a +1 bonus on saving throws and a +2 bonus on checks with each skill in which it has
at least 1 rank.

**Gained:** At 1st Level

**Replaces:** Animal focus

**Usage:** 1 minute/day per hunter level; these minutes need not be consecutive, but must be spent
in 1-minute increments

The connection the totem-bonded has with her animal companion allows them to draw upon one another's
strength. The totem-bonded can activate this ability as a **swift action**. The effect ends
immediately if the animal companion is ever more than 100 feet away from the totem-bonded.

While the _shared strength_ ability is active, the totem-bonded manifests one aspect of her animal
companion drawn from the following list.

- [Low-light vision](ref/rule/low-light-vision)
- [Scent](ref/umr/scent)
- +1 bonus to natural armor
- +10-foot bonus to speed
- climb speed 30 feet
- swim speed 40 feet
- 2 claws (1d4)
- bite (1d6)
- gore (1d6)
- slam (1d6)

  - _The [natural attacks](ref/umr/natural-attacks) above are all primary attacks, and the listed
    damage is for a Medium creature._

At 8th-level, the following aspects become available.

- +20-foot bonus to speed
- fly speed 50 feet (average)
- increased size (as [enlarge person](ref/spell/enlarge-person))
- [powerful charge](ref/umr/powerful-charge) (doubles the damage dice dealt by the granted gore or
  slam attack)

The totem-bonded can select only a movement speed or natural attack that her animal companion also
has, and an aspect cannot cause her speed or size to exceed that of her animal companion with this
ability.

A totem-bonded's animal companion also benefits from the _shared strength_ ability, and while it is
active, the animal understands the totem-bonded's known languages and can be pushed to perform an
unfamiliar trick as a **free action**.
