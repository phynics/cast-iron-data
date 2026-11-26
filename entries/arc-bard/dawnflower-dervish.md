+++
id = "ref/arc-bard/dawnflower-dervish"
kind = "archetype"
title = "Dawnflower Dervish"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Dawnflower%20Dervish"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dawnflower_dervish", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "inner-sea-magic"
page = "34"

[fields]
kind = "archetype"
features = [
  { anchor = "deity" },
  { anchor = "battle-dance" },
  { anchor = "dervish-dance", level = 1 },
  { anchor = "spinning-spellcaster", level = 5 },
  { anchor = "meditative-whirl", level = 8 },
]
trades = [
  { replaces = "Proficiency with the rapier and whip", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["dervish-dance"] },
  { replaces = "Lore master", feature = "lore-master", by = ["spinning-spellcaster"] },
  { replaces = "Dirge of doom bardic performance", feature = "bardic-performance", power = "dirge of doom", by = ["meditative-whirl"] },
  { alters = "Bardic performance", feature = "bardic-performance", by = ["battle-dance"] },
]
+++

Although Sarenrae is seen mainly as a goddess of healing and redemption in most parts of the Inner
Sea, her stern, evil-smiting element is more common in areas like Qadira, Osirion, and Katapesh.
Many of the Dawnflower's disciples from these lands become Dawnflower dervishes, religious mystics
who use a spinning dance as part of their worship. Many bards of her faith hone their skills with
dance and scimitar to become [dervish dancers](ref/arc-bard/dervish-dancer) (see _Ultimate Combat_),
but some tread a similar path focused more on magic and healing than swordplay. These are the
Dawnflower dervishes. A Dawnflower dervish has the following class features.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Dawnflower dervishes gain weapon proficiency with the [scimitar](ref/eq-weapon/scimitar). This
ability replaces their proficiency with the rapier and whip.

## Deity {#deity}

A Dawnflower dervish must be a worshiper of [Sarenrae](ref/faith/sarenrae). A dervish who abandons
or betrays this faith reverts to a standard bard.

## Battle Dance {#battle-dance}

A Dawnflower dervish is trained in the use of the Perform skill, especially dance, to create magical
effects on himself. This works like bardic performance, except that the Dawnflower dervish's
performances grant double their normal bonuses, but these bonuses only affect him. He does not need
to be able to see or hear his own performance. Battle dancing is treated as bardic performance for
the purposes of feats, abilities, and effects that affect bardic performance, except that battle
dancing does not benefit from the [Lingering Performance](ref/feat/lingering-performance) feat or
any other ability that allows a bardic performance to grant bonuses after it has ended. The benefits
of battle dancing apply only when the bard is wearing light or no armor. Like bardic performance,
battle dancing cannot be maintained at the same time as other performance abilities.

Starting a battle dance is a move action, but it can be maintained each round as a free action.
Changing a battle dance from one effect to another requires the Dawnflower dervish to stop the
previous performance and start the new one as a move action. Like a bard, a Dawnflower dervish's
performance ends immediately if he is killed, paralyzed, stunned, knocked unconscious, or otherwise
prevented from taking a free action each round. A Dawnflower dervish cannot perform more than one
battle dance at a time. At 10th level, a Dawnflower dervish can start a battle dance as a swift
action instead of a move action.

When the Dawnflower dervish uses the inspire courage, inspire greatness, or inspire heroics bardic
performance types as battle dances, these performance types only provide benefit to the Dawnflower
dervish himself. All other types of bardic performance work normally (affecting the bard and his
allies, or the bard's enemies, as appropriate). This ability alters the standard bardic performance
ability.

## Dervish Dance (Ex) {#dervish-dance}

A Dawnflower dervish gains the [Dervish Dance](ref/feat/dervish-dance) feat as a bonus feat. This
ability replaces bardic knowledge.

## Spinning Spellcaster (Ex) {#spinning-spellcaster}

At 5th level, a Dawnflower dervish gains a +4 bonus on [concentration](ref/rule/concentration)
checks to cast spells defensively. This ability replaces lore master.

## Meditative Whirl (Ex) {#meditative-whirl}

At 8th level, when using battle dance, the Dawnflower dervish can enter a trance-like state where
his spinning motion represents the movement of the planets around the sun, and his spirit is attuned
to the healing aspects of Sarenrae. By spending a move action focusing on his whirling, the dervish
can apply the [Quicken Spell](ref/feat/quicken-spell) feat to any cure spell he is about to cast
(effectively spending a move action and swift action to cast the spell). This does not alter the
level of the spell or the casting time. The dervish can use this ability once per day at 8th level
and one additional time per day for every two dervish levels he has beyond 8th. This ability
replaces the dirge of doom bardic performance.
