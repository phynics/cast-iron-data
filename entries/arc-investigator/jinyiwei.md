+++
id = "ref/arc-investigator/jinyiwei"
kind = "archetype"
title = "Jinyiwei"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Jinyiwei"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jinyiwei", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "divine-inspiration", level = 1 },
  { anchor = "suspicious-mind", level = 1 },
  { anchor = "celestial-insight", level = 3 },
  { anchor = "imperial-judgment", level = 4 },
]
trades = [
  { replaces = "Alchemy", feature = "alchemy", by = ["divine-inspiration"] },
  { replaces = "Trapfinding", feature = "trapfinding", by = ["suspicious-mind"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["celestial-insight"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["imperial-judgment"] },
  { alters = "Inspiration", feature = "inspiration", by = ["divine-inspiration"] },
]
+++

Lung Wa's corruption and political decay led to its eventual collapse, but the empire did not spend
its last decades in surrender. A special task force of secret police, known as the jinyiwei, was one
of Lung Wa's last bulwarks against this decline. The jinyiwei were unable to save the empire; they
failed in their mission to root out, expose, and counteract their government's existing wrongdoing,
and the organization itself ultimately fell prey to the same political decline that rotted Lung Wa's
bureaucracy. However, their legacy now inspires purists who seek out and eliminate corruption
wherever they find it. Since the earthly government of Lung Wa has failed, these new jinyiwei claim
they act under the celestial government's mandate.

## Divine Inspiration {#divine-inspiration}

A jinyiwei follows a mandate from Heaven to combat corruption in the mortal world. A jinyiwei adds
her Wisdom modifier to her inspiration pool, rather than her Intelligence modifier. Additionally,
rather than dabbling in the arcane arts of alchemy, a jinyiwei is empowered by the forces of
celestial bureaucracy. She casts spells as an [inquisitor](ref/class/inquisitor) of the same level.

This alters the inspiration class feature and replaces the alchemy class feature.

## Suspicious Mind (Ex) {#suspicious-mind}

A jinyiwei adds half her level (minimum 1) to Sense Motive checks, Linguistics checks to detect
forgeries, and Perception checks to see through disguises, locate creatures using Stealth, or locate
a secret door or compartment.

This replaces trapfinding.

## Celestial Insight (Ex) {#celestial-insight}

At 3rd level, a jinyiwei learns to see through the types of magic that often lead others astray. She
gains a +1 competence bonus on saving throws to resist enchantment and illusion effects. At 6th
level and every 3 levels thereafter, these bonuses increase by 1 (to a maximum of +6 at 18th level).

This replaces trap sense.

## Imperial Judgment (Su) {#imperial-judgment}

At 4th level, a jinyiwei can carry out trial and sentence with her own divine authority. She gains
the judgment inquisitor class feature as an inquisitor 3 levels lower than her investigator level,
and her investigator levels stack with inquisitor levels for the purposes of determining her
judgments' abilities and number of judgments per day. At 11th level, she gains the second judgment
inquisitor class feature, and at 19th level, she gains the third judgment inquisitor class feature.

This replaces swift alchemy.
