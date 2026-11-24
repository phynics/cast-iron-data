+++
id = "ref/arc-inquisitor/witch-hunter"
kind = "archetype"
title = "Witch Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Witch%20Hunter"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "witch_hunter", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-combat"
page = "53"

[fields]
kind = "archetype"
features = [
  { anchor = "spell-sage", level = 1 },
  { anchor = "knowledgeable-defense", level = 2 },
  { anchor = "spell-scent", level = 6 },
  { anchor = "witch-s-bane-judgment", level = 14 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["spell-sage"] },
  { replaces = "Detect alignment", feature = "detect-alignment", by = ["knowledgeable-defense"] },
  { replaces = "discern lies", feature = "discern-lies", by = ["knowledgeable-defense"] },
  { replaces = "true judgment", feature = "true-judgment", by = ["knowledgeable-defense"] },
  { replaces = "Track", feature = "track", by = ["spell-scent"] },
  { replaces = "Exploit weakness", feature = "exploit-weakness", by = ["witch-s-bane-judgment"] },
]
+++

When pursuing justice for their faith, inquisitors sometimes hunt sorcerers, witches, wizards, and
other practitioners of arcane magic—but especially witches, since their devotion to a patron is
often seen as suspect by many religions.

## Spell Sage (Ex) {#spell-sage}

At 1st level, a witch hunter adds her Wisdom modifier on Spellcraft checks in addition to her
Intelligence modifier when attempting to identify a spell as it is being cast, to identify the
properties of a magic item using _[detect magic](ref/spell/detect-magic)_, or to decipher a scroll.
This ability replaces monster lore.

## Knowledgeable Defense {#knowledgeable-defense}

At 2nd level, a witch hunter who identifies a spell with Spellcraft gains a bonus against its
effects, either a +1 bonus on saving throws or a +1 dodge bonus to AC against this spell. This bonus
increases every four levels (to a maximum of +5 at 18th level). At 20th level, once per day as a
swift action, she can grant this bonus to all her allies within 60 feet, for 1 minute. The allies
gain the bonus when the witch hunter identifies the spell, and those among the allies who have at
least 1 rank in Spellcraft can aid the witch hunter's next Spellcraft check as a swift action while
under the effect of this ability. This ability replaces _detect alignment_, _discern lies_, and true
judgment.

## Spell Scent {#spell-scent}

At 6th level, the witch hunter learns how to sense unique spell signatures, and can follow the trail
of a cast spell or spell effect cast back to its source. Once per day, when the witch hunter comes
into contact with or is exposed to a spell effect or a magic item, she can spend a full-round action
to examine the spell effect or magic item, and then gains the effect of a
_[locate creature](ref/spell/locate-creature)_ spell. She can do this even if the spell effect was
instantaneous, but must start her examination within 1 round after she experienced the spell's
effect. Instead of locating a known creature, the witch hunter locates the caster of the spell
effect or magic item she examined. Doing so does not allow the witch hunter to gain any intelligence
about the spellcaster other than its location. This ability replaces track.

## Witch's Bane Judgment (Ex) {#witch-s-bane-judgment}

At 14th level, a witch hunter gains the following judgment.

### Witch's Bane {#witch-s-bane}

Any creature that casts an arcane spell within 30 feet of the witch hunter takes a -2 penalty to AC
against her attacks and a -2 penalty on saving throws against her spells while this judgment remains
in effect. This ability replaces exploit weakness.
