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
replaces = ["Fascinate", "Suggestion", "mass suggestion", "Dirge of doom", "frightening tune", "Bardic knowledge", "well-versed"]
+++

The impervious messenger is capable of harnessing the unique qualities of bardic magic to keep,
transport, and communicate the most precious of secrets and messages, even when subject to the most
vigorous forms of observation, be they magical or mundane.

**Bardic Performance (Su)**

**Info:** An impervious messenger gains the following types of bardic performances.

**Chant of Perfect Recall (Su)**

**Ability:** An impervious messenger can spend 1 round of his bardic performance to commit something
to memory. This ability functions exactly as per [memorize page](ref/spell/memorize-page), but the
impervious messenger is the only recipient and he requires only 1 round to commit a single page to
memory. An impervious messenger can commit additional pages worth of material to memory by using
additional rounds of his bardic performance, but he can never memorize more than half his total bard
level in pages (minimum 1).

**Replaces:** Fascinate

**Song of Subterfuge (Su)**

**Ability:** An impervious messenger learns to use his performances to project various thoughts into
his own mind to disrupt divination attempts. This acts similarly to
[distraction](ref/performance/distraction), except it only affects the impervious messenger and
allows him to use the result of his Perform check in place of saving throws against attempts to read
his mind, such as [detect thoughts](ref/spell/detect-thoughts).

**At 18th Level:** If the impervious messenger succeeds on a saving throw while using _song of
subterfuge,_ the character who attempted the divination effect must succeed on a Will save (DC =
20 + the impervious messenger's Charisma modifier) or else the impervious messenger instantly learns
the nature of the effect and can allow the effect to continue, but provide whatever information he
chooses to the divining character rather than the true results of the divination effect.

**Gained:** At 6th Level

**Replaces:** Suggestion, mass suggestion

**Unbroken Stride (Su)**

**Ability:** An impervious messenger draws upon his bardic abilities to imbue himself with grace and
speed. While using this bardic performance, an impervious messenger gains an insight bonus equal to
[half](ref/misc/fractions-and-rounding) his bard level on all Acrobatics, Climb, Fly, and Ride
checks. In addition, while maintaining this performance, he gains the benefits of the ranger's
[woodland stride](ref/ability/woodland-stride) ability and a +10-foot enhancement bonus to his base
land speed.

**At 12th Level:** An impervious messenger using his _unbroken stride_ bardic performance also acts
as if under the effect of [freedom of movement](ref/spell/freedom-of-movement). In addition, the
enhancement bonus to his base land speed increases to +30 feet.

**Gained:** At 8th Level

**Replaces:** Dirge of doom, frightening tune

**Cryptic Whisper (Ex)**

**Flavor:** The impervious messenger internalizes his understanding of language and ciphers, and
filters them through his bardic abilities.

**Gained:** At 2nd Level

**Passive:** He adds half his bard level to all Linguistics checks and Bluff checks to deliver
secret messages, and he gains a +4 bonus on saving throws against glyph spells, symbol spells, and
language-dependent effects.

**Replaces:** Bardic knowledge, well-versed
