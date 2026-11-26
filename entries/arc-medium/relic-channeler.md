+++
id = "ref/arc-medium/relic-channeler"
kind = "archetype"
title = "Relic Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Relic%20Channeler"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "relic_channeler", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "occult-adventures"
page = "93"

[fields]
kind = "archetype"
features = [
  { anchor = "relics" },
  { anchor = "powerful-bond" },
  { anchor = "object-reading", level = 3 },
  { anchor = "apport-relic", level = 5 },
  { anchor = "connection-specialty", level = 7 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["object-reading"] },
  { replaces = "Location channel", feature = "location-channel", by = ["apport-relic"] },
  { alters = "Spirit", feature = "spirit", by = ["relics", "powerful-bond"] },
  { alters = "Connection channel", feature = "connection-channel", by = ["connection-specialty"] },
]
+++

A relic channeler carries relics of legend around with her. She need not rely on locating the
specific spirits that she seeks, but the relics limit the number of unique spirits she can channel.

## Relics (Su) {#relics}

A relic channeler begins with one relic for each of the six spirit legends. Each relic corresponds
to a specific spirit, and could be any type of psychically resonant item—from a runestone with a
symbol related to that spirit to a bone remnant from a legendary hero. Once a relic channeler
selects a choice for taboos and spirit powers (such as archmage arcana and legendary champion),
those choices remain in effect every time she channels that legend; unlike normal mediums, she can't
select a different option each time. A relic channeler can't choose to channel a weaker spirit to
reduce her influence from spirit surge. She doesn't need to find an appropriate location to channel
her spirits, since she can simply use her relics. If she loses one of her relics, she is incapable
of channeling that legend until she recovers the relic. If the relic is destroyed, the relic
channeler can use her strong bond with the spirit of that relic to forge a new relic for that spirit
from her own essence. The process takes 1 week of intense seances and 500 gp per medium level she
possesses. This ability alters spirit.

## Powerful Bond (Su) {#powerful-bond}

Because of habitually channeling the same spirits and possessing physical links to the spirits'
former lives and legends, a relic channeler possesses a strong bond with her spirits. She receives
the benefit of the [Alertness](ref/feat/alertness) feat whenever she is suffering a spirit's
influence penalty. She chooses two spells of each level with the archmage arcana and divine surge
spirit powers instead of one, two exotic weapon proficiencies with champion's prowess instead of
one, three combat feats with legendary champion instead of two, and three skills with trickster's
edge instead of two. This ability alters spirit.

## Object Reading (Su) {#object-reading}

At 3rd level, a relic channeler gains the [occultist's](ref/class/occultist)
[object reading](ref/spell/object-reading) ability, substituting her medium level for her occultist
level for this ability. This ability replaces haunt channeler.

## Apport Relic (Su) {#apport-relic}

At 5th level, a relic channeler can call one of her relics to her once per day as though she had
cast _[apport object](ref/spell/apport-object)_ on it and was mentally completing the spell.
Furthermore, if the relic channeler gains the _[apport object](ref/spell/apport-object)_ spell, she
can use it to receive her relics without casting it on them in advance in the same way. The range at
which the relic channeler can apport her relics (both with this ability and the spell) increases by
an additional 5 feet for every 2 levels she possesses beyond 5th. This ability replaces location
channel.

## Connection Specialty (Sp) {#connection-specialty}

At 7th level, a relic channeler gains connection channel and can use that ability as a normal
medium, despite not possessing location channel. She requires familiarity to use this ability, even
if she is in an appropriate location. This ability alters connection channel.
