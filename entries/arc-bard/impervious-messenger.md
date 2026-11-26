+++
id = "ref/arc-bard/impervious-messenger"
kind = "archetype"
title = "Impervious Messenger"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Impervious%20Messenger"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "impervious_messenger", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "chant-of-perfect-recall", level = 1 },
  { anchor = "song-of-subterfuge", level = 6 },
  { anchor = "unbroken-stride", level = 8 },
  { anchor = "cryptic-whisper", level = 2 },
]
trades = [
  { replaces = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["chant-of-perfect-recall"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["song-of-subterfuge"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["song-of-subterfuge"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["unbroken-stride"] },
  { replaces = "frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["unbroken-stride"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["cryptic-whisper"] },
  { replaces = "well-versed", feature = "well-versed", by = ["cryptic-whisper"] },
]
+++

The impervious messenger is capable of harnessing the unique qualities of bardic magic to keep,
transport, and communicate the most precious of secrets and messages, even when subject to the most
vigorous forms of observation, be they magical or mundane.

## Bardic Performance (Su) {#bardic-performance}

An impervious messenger gains the following types of bardic performances.

## Chant of Perfect Recall (Su) {#chant-of-perfect-recall}

At 1st level, an impervious messenger can spend 1 round of his bardic performance to commit
something to memory. This ability functions exactly as per
_[memorize page](ref/spell/memorize-page)_, but the impervious messenger is the only recipient and
he requires only 1 round to commit a single page to memory. An impervious messenger can commit
additional pages worth of material to memory by using additional rounds of his bardic performance,
but he can never memorize more than half his total bard level in pages (minimum 1).

This ability replaces fascinate.

## Song of Subterfuge (Su) {#song-of-subterfuge}

At 6th level, an impervious messenger learns to use his performances to project various thoughts
into his own mind to disrupt divination attempts. This acts similarly to
[distraction](ref/performance/distraction), except it only affects the impervious messenger and
allows him to use the result of his Perform check in place of saving throws against attempts to read
his mind, such as _[detect thoughts](ref/spell/detect-thoughts)_. At 18th level, if the impervious
messenger succeeds on a saving throw while using song of subterfuge, the character who attempted the
divination effect must succeed on a Will save (DC = 20 + the impervious messenger's Charisma
modifier) or else the impervious messenger instantly learns the nature of the effect and can allow
the effect to continue, but provide whatever information he chooses to the divining character rather
than the true results of the divination effect.

This ability replaces suggestion and mass suggestion.

## Unbroken Stride (Su) {#unbroken-stride}

At 8th level, an impervious messenger draws upon his bardic abilities to imbue himself with grace
and speed. While using this bardic performance, an impervious messenger gains an insight bonus equal
to [half](ref/misc/fractions-and-rounding) his bard level on all Acrobatics, Climb, Fly, and Ride
checks. In addition, while maintaining this performance, he gains the benefits of the ranger's
[woodland stride](ref/ability/woodland-stride) ability and a +10-foot enhancement bonus to his base
land speed. At 12th level, an impervious messenger using his unbroken stride bardic performance also
acts as if under the effect of _[freedom of movement](ref/spell/freedom-of-movement)_. In addition,
the enhancement bonus to his base land speed increases to +30 feet.

This ability replaces dirge of doom and frightening tune.

## Cryptic Whisper (Ex) {#cryptic-whisper}

At 2nd level, the impervious messenger internalizes his understanding of language and ciphers, and
filters them through his bardic abilities. He adds half his bard level to all Linguistics checks and
Bluff checks to deliver secret messages, and he gains a +4 bonus on saving throws against _glyph_
spells, _symbol_ spells, and language-dependent effects.

This ability replaces bardic knowledge and well-versed.
