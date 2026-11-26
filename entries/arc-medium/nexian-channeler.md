+++
id = "ref/arc-medium/nexian-channeler"
kind = "archetype"
title = "Nexian Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Nexian%20Channeler"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nexian_channeler", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "occult-origins"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "legend-of-nex", level = 1 },
  { anchor = "third-eye" },
  { anchor = "impossible-eye", level = 3 },
  { anchor = "third-eye-mastery", level = 19 },
  { anchor = "living-third-eye", level = 20 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["impossible-eye"] },
  { replaces = "location channel", feature = "location-channel", by = ["impossible-eye"] },
  { replaces = "connection channel", feature = "connection-channel", by = ["impossible-eye"] },
  { replaces = "propitiation", feature = "propitiation", by = ["impossible-eye"] },
  { replaces = "ask the spirits", feature = "ask-the-spirits", by = ["impossible-eye"] },
  { replaces = "astral journey", feature = "astral-journey", by = ["impossible-eye"] },
  { replaces = "trance of three", feature = "trance-of-three", by = ["impossible-eye"] },
  { replaces = "spacious soul", feature = "spacious-soul", by = ["impossible-eye"] },
  { replaces = "Spirit mastery", feature = "spirit-mastery", by = ["third-eye-mastery"] },
  { replaces = "Astral beacon", feature = "astral-beacon", by = ["living-third-eye"] },
  { alters = "Spirit", feature = "spirit", by = ["legend-of-nex"] },
  { alters = "Knacks", feature = "knacks", by = ["third-eye"] },
  { alters = "taboo", feature = "taboo", by = ["third-eye"] },
]
+++

Normally, storied figures who simply disappear don't form legendary spirits (see _Pathfinder
Campaign Setting: Occult Realms_), but the archmage Nex long ago created an astral reflection of
himself from which he can draw additional power. This echo now serves as an appropriate spirit for
well-trained mediums to channel. Nex's legendary spirit is more powerful and willful than most
legendary spirits, however; it embraces only mediums who visit distinct locations and master opening
their third eyes.

## Legend of Nex (Su) {#legend-of-nex}

A Nexian channeler gains access to the [Nex](ref/spirit/nex) legendary spirit instead of an archmage
spirit. This ability alters the spirit ability.

## Third Eye (Sp, Su) {#third-eye}

A Nexian channeler knows one fewer knack than his level would normally indicate, but he gains
[Third Eye](ref/feat/third-eye) as a bonus feat. Beginning at 2nd level, when he selects a taboo,
the Nexian channeler can use his third eye for 2 minutes per character level each day, instead of
gaining free uses of spirit surge. This ability alters knacks and taboo.

## Impossible Eye (Su) {#impossible-eye}

Starting at 3rd level, a Nexian channeler gains additional powers from his third eye. At 3rd level,
while his third eye is open, his caster level for divination spells increases by 1 and he gains
[darkvision](ref/rule/darkvision) with a range of 60 feet. At 5th level, while his third eye is
open, he gains constant _[detect magic](ref/spell/detect-magic)_. At 7th level, while his third eye
is open, he gains constant _[arcane sight](ref/spell/arcane-sight)_ instead of
_[detect magic](ref/spell/detect-magic)_. At 9th level, while his third eye is open, his bonus on
Perception checks against invisible creatures improves to
_[see invisibility](ref/spell/see-invisibility)_. At 13th level, he can concentrate for 1 minute to
send his third eye from his body, as per _[arcane eye](ref/spell/arcane-eye)_ (this duration counts
against the daily duration for which he can open his third eye, and if the
_[arcane eye](ref/spell/arcane-eye)_ is destroyed, he loses all remaining minutes of his third eye
ability for that day). At 14th level, as a standard action while his third eye is open, he can spend
1 minute of the duration he can open his third eye to use
_[analyze dweomer](ref/spell/analyze-dweomer)_ on a single target. At 15th level, while his third
eye is open, he gains _[true seeing](ref/spell/true-seeing)_. At 18th level, while his third eye is
open, his _[arcane sight](ref/spell/arcane-sight)_ improves to
_[greater arcane sight](ref/spell/arcane-sight-greater)_. This ability replaces haunt channeler,
location channel, connection channel, propitiation, ask the spirits, astral journey, trance of
three, and spacious soul.

## Third Eye Mastery (Su) {#third-eye-mastery}

At 19th level, a Nexian channeler can open his third eye for longer than normal. He can open his
third eye for 5 minutes per medium level (increasing to 10 minutes per medium level if he selects a
taboo); this duration must be used in 5-minute increments. Uses of
_[analyze dweomer](ref/spell/analyze-dweomer)_ cost him 5-minute increments instead of 1-minute
increments, and he can use the [read aura](ref/skill/perception) occult skill unlock with his third
eye multiple times per day; each use takes only 1 minute but costs 5 minutes of the duration he can
keep his third eye open. This ability replaces spirit mastery.

## Living Third Eye (Su) {#living-third-eye}

At 20th level, a Nexian channeler is as one with his third eye. It is open at all times, he can use
_[analyze dweomer](ref/spell/analyze-dweomer)_ and the read aura occult skill unlock at will, and
the destruction of his _[arcane eye](ref/spell/arcane-eye)_ does not adversely affect him. This
ability replaces astral beacon.
