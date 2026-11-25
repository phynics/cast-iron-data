+++
id = "ref/arc-occultist/naturalist"
kind = "archetype"
title = "Naturalist"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Naturalist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "naturalist", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "66"

[fields]
kind = "archetype"
features = [
  { anchor = "natural-focus" },
  { anchor = "tree-talker", level = 8 },
  { anchor = "reflect-on-the-land", level = 12 },
]
trades = [
  { replaces = "Magic circles", feature = "magic-circles", by = ["natural-focus"] },
  { replaces = "fast circles", feature = "fast-circles", by = ["natural-focus"] },
  { replaces = "Outside contact", feature = "outside-contact", by = ["tree-talker"] },
  { replaces = "Binding circles", feature = "binding-circles", by = ["reflect-on-the-land"] },
  { alters = "Mental focus", feature = "mental-focus", by = ["natural-focus"] },
  { alters = "Class skills" },
]
+++

A naturalist eschews the contact with outsiders that other occultists use as the core of their work.
Instead, he attunes his mind to the natural spirits that exist everywhere, just out of sight for the
unawakened mind.

## Class Skills {#class-skills}

A naturalist adds Knowledge (nature) to his list of class skills instead of Knowledge (planes).

This alters the occultist's class skills.

## Natural Focus (Su) {#natural-focus}

A naturalist can always hear the spirits of nature whispering in his ears, and sometimes those
whispers contain helpful advice. As a free action, a naturalist can expend 1 point of generic mental
focus before rolling an ability check, saving throw, or skill check to add 1d6 to the result. The
naturalist must be conscious and aware to use this ability, and he can use this ability at most once
per round.

At 8th level, the naturalist's natural focus die increases to 1d8, and at 16th level it increases to
1d10.

This ability doesn't function while the naturalist is wearing metal armor or using a metal shield
(although he can wear a suit of armor or use a shield altered by the
_[ironwood](ref/spell/ironwood)_ spell). This restriction is similar to the
[druid's](ref/class/druid) armor restriction.

This alters mental focus and replaces magic circles and fast circles.

## Tree Talker (Sp) {#tree-talker}

At 8th level, a naturalist can cast _[speak with plants](ref/spell/speak-with-plants)_ three times
per day as a [spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to his
occultist level. In addition, when the naturalist uses this power, he can whisper a message of 25 or
fewer words to the surrounding plant life and designate a creature with which he is familiar. The
next time that creature is on the same plane of existence and in an area of similar vegetation, it
receives the message.

This replaces outside contact.

## Reflect on the Land (Sp) {#reflect-on-the-land}

At 12th level, a naturalist can cast _[commune with nature](ref/spell/commune-with-nature)_ once per
day as a [spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to his
occultist level.

This replaces binding circles.
