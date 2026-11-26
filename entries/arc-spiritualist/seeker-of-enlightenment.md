+++
id = "ref/arc-spiritualist/seeker-of-enlightenment"
kind = "archetype"
title = "Seeker of Enlightenment"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Seeker%20of%20Enlightenment"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seeker_of_enlightenment", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "disciples-doctrine"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "echoes-of-expertise", level = 1 },
  { anchor = "words-of-the-past", level = 5 },
  { anchor = "karmic-insight", level = 7 },
  { anchor = "pinpoint-influence", level = 9 },
  { anchor = "echoes-of-mastery", level = 10 },
  { anchor = "knowledge-of-the-ancestors", level = 16 },
]
trades = [
  { replaces = "Shared consciousness", feature = "shared-consciousness", by = ["echoes-of-expertise"] },
  { replaces = "Detect undead", feature = "detect-undead", by = ["words-of-the-past"] },
  { replaces = "Calm spirit", feature = "calm-spirit", by = ["karmic-insight"] },
  { replaces = "See invisibility", feature = "see-invisibility", by = ["pinpoint-influence"] },
  { replaces = "Fused consciousness", feature = "fused-consciousness", by = ["echoes-of-mastery"] },
  { replaces = "Call spirit", feature = "call-spirit", by = ["knowledge-of-the-ancestors"] },
]
+++

Sometimes a spiritualist is so haunted by a past life's failure to reach enlightenment that the past
life is reborn not as a new creature but as a phantom in a spiritualist's consciousness. The
spiritualist and phantom work in tandem to reach enlightenment and atone for the past life's
failures.

## Echoes of Expertise (Ex) {#echoes-of-expertise}

A seeker of enlightenment gains a bonus equal to her spiritualist level on checks attempted with the
two skills determined by her phantom's emotional focus. When the phantom is confined to the seeker
of enlightenment's consciousness, it grants a +2 bonus on saving throws against mind-affecting
effects; at 12th level, this bonus increases to +4. Once per day as a free action, the seeker of
enlightenment can attempt a check with any Knowledge skill, including one in which she is not
trained, and add her spiritualist level as a bonus on the check.

This replaces shared consciousness.

## Words of the Past (Sp) {#words-of-the-past}

At 5th level, a seeker of enlightenment's connection with her past lives becomes so strong that she
can cast _[comprehend languages](ref/spell/comprehend-languages)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities), with a caster level equal to her spiritualist
level.

This replaces detect undead.

## Karmic Insight (Sp) {#karmic-insight}

At 7th level, a seeker of enlightenment gains the ability to understand which actions will push her
toward ultimate understanding. She can cast _[augury](ref/spell/augury)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day. At 11th level and every 4 levels
thereafter, she can use this ability an additional time per day (to a maximum of four times per day
at 19th level).

This replaces calm spirit.

## Pinpoint Influence (Sp) {#pinpoint-influence}

At 9th level, a seeker of enlightenment gains the ability to track objects that are important to her
goal of enlightenment. She can cast _[locate object](ref/spell/locate-object)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day, with a duration of 10 minutes.

This replaces see invisibility.

## Echoes of Mastery (Ex) {#echoes-of-mastery}

At 10th level, a seeker of enlightenment gains the bonus on saving throws from echoes of expertise
even when her phantom is manifested. Additionally, once per day, she can take 20 on any Knowledge
check, including one in which she is not trained.

This replaces fused consciousness.

## Knowledge of the Ancestors (Sp) {#knowledge-of-the-ancestors}

At 16th level, a seeker of enlightenment learns how to tap into the knowledge of her past lives. She
can cast _[legend lore](ref/spell/legend-lore)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day.

This replaces call spirit.
