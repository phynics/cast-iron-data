+++
id = "ref/arc-bard/plant-speaker"
kind = "archetype"
title = "Plant Speaker"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Plant%20Speaker"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plant_speaker", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "leshy-speaker", level = 9 },
  { anchor = "plant-speech", level = 1 },
  { anchor = "mystical-allegory", level = 5 },
]
trades = [
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["leshy-speaker"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["plant-speech"] },
  { replaces = "well-versed", feature = "well-versed", by = ["plant-speech"] },
  { replaces = "Lore master", feature = "lore-master", by = ["mystical-allegory"] },
]
+++

Plant speakers build upon their racial plantspeech ability and their storytelling tendencies to
create an art form full of deep metaphors and allegory rather than specific details and facts.

## Bardic Performance {#bardic-performance}

Plant speakers gain the following bardic performance.

## Leshy Speaker (Su) {#leshy-speaker}

At 9th level, the plant speaker can speak to its disembodied brethren, the spirits of nature that
become leshys. He performs for 10 minutes and spends 7 rounds of bardic performance to gain the
effects of _[commune with nature](ref/spell/commune-with-nature)_.

This replaces inspire greatness.

## Plant Speech {#plant-speech}

A plant speaker's mind-affecting bard spells and class abilities also affect plants, ignoring
plants' immunity to mind-affecting effects. At 2nd level, a plant speaker's racial plantspeech
allows him to communicate with all plants, not just plants that match his alternate form.

This replaces bardic knowledge and well-versed.

## Mystical Allegory (Su) {#mystical-allegory}

At 5th level, the plant speaker can tell a story that matches some of the themes of the current
situation in order to gain insight, gaining the effects of _[augury](ref/spell/augury)_ by
performing for 1 minute and spending 4 rounds of bardic performance. At 11th level, he can perform
for 10 minutes and spend 7 rounds of bardic performance to gain the effects of
_[divination](ref/spell/divination)_. At 17th level, he can perform for 1 hour and spend 10 rounds
of bardic performance to gain the effects of _[legend lore](ref/spell/legend-lore)_, but the
information is always vague and incomplete.

This replaces lore master.

## Leshy Subdomain {#leshy-subdomain}

You have a strong connection to these little manifestations of nature spirits.

**Associated Domain:** Plant.

**Associated Religions:** Gozreh, Green Faith.

**Replacement Power:** The following granted power replaces the wooden fist power of the Plant
domain.

**Leshy Caller (Sp):** You can spontaneously swap out any of your domain spells for a summon
nature's ally spell of the same level or lower, to a maximum of _summon nature's ally VII_. If you
do, you must use the spell to summon one or more leshys. Add leaf leshy, gourd leshy, fungus leshy,
seaweed leshy, and lotus leshy to your _summon nature's ally I_, _II_, _III_, _IV_, and _V_ lists,
respectively. You count as a plant creature for the purpose of creating leshys (_Pathfinder RPG
Bestiary 3_ 176).

As a standard action, you can grant a single leshy within 30 feet a +4 sacred bonus on its next
attack roll before the start of your next turn. You can use this ability a number of times per day
equal to 3 + your Wisdom modifier.

**Replacement Domain Spells:** 1st—_tree shape_, 5th—_commune with nature_.
