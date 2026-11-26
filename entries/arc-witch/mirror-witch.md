+++
id = "ref/arc-witch/mirror-witch"
kind = "archetype"
title = "Mirror Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Mirror%20Witch"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirror_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "villain-codex"
page = "152"

[fields]
kind = "archetype"
features = [
  { anchor = "patron-mirror", level = 1 },
  { anchor = "cryptic-omens", level = 1 },
  { anchor = "seek-guidance", level = 1 },
  { anchor = "greater-omens", level = 3 },
  { anchor = "specialized-knowledge", level = 5 },
  { anchor = "clairvoyance-clairaudience", level = 7 },
  { anchor = "scrying", level = 11 },
  { anchor = "mirror-casting", level = 13 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["patron-mirror"] },
]
+++

Many mirrors hold a sliver of magical potential. Some witches learn the secrets of drawing upon that
power, using it as a conduit to patrons who dwell in strange dimensions.

## Patron Mirror (Su) {#patron-mirror}

At 1st level, a [mirror](ref/eq-misc/mirror) witch creates a direct link to the power of her patron.
She chooses a patron as normal, but instead of gaining a familiar that serves as the conduit to her
patron, she uses a mirror (worth at least 10 gp) to speak to a fragment of her patron's power. This
fragment teaches her magic and acts as a counselor.

The mirror is essentially an immobile familiar. The mirror witch can activate it with a minute-long
ritual that calls the patron fragment to manifest itself through the mirror. While this connection
is open, she can prepare spells, add new spells to the mirror, and use the mirror's special
abilities. In place of the boost granted by an ordinary familiar, the mirror grants the mirror witch
a +2 bonus on Diplomacy checks regardless of whether the mirror is nearby. The mirror can't be used
for abilities that require the presence of a familiar, such as the [blight](ref/hex/blight) hex.

If the patron mirror is destroyed, the mirror witch can replace it 1 day later through a special
ritual, attuning a new mirror to a different fragment of her patron. The mirror witch must purchase
or procure a new, suitable mirror and spend 500 gp per witch level she has. The ritual takes 8 hours
to complete, and when it is finished, the mirror witch establishes a connection with a new fragment
of her patron and loses access to spells stored in the previous mirror, as normal for a lost witch's
familiar.

As the mirror witch progresses in level, the mirror's defenses increase, and the connection between
it and the mirror witch becomes stronger, allowing the patron to manifest more of its
personality—see the Patron Mirror section below.

This ability replaces the witch's familiar.

### Patron Mirror {#patron-mirror-table}

Instead of using the familiar abilities table on page 83 of the _Pathfinder RPG Core Rulebook_, use
the table below to determine the strength of a mirror witch's patron mirror.

|Witch Class Level|Hardness|Hit Points|Int|Special|
| --- | --- | --- | --- | --- |
|1st–2nd|5|2|12|Cryptic omens, seek guidance|
|3rd–4th|10|5|13|Greater omens|
|5th–6th|15|5|14|Specialized knowledge|
|7th–8th|20|5|15|Clairvoyance/clairaudience|
|9th–10th|20|5|16|—|
|11th–12th|25|10|17|Scrying|
|13th–14th|25|10|18|Mirror casting|
|15th–16th|25|10|19|—|
|17th–18th|30|10|20|—|
|19th–20th|30|15|21|—|

**Hardness:** As the connection between the witch and her patron mirror becomes more powerful, so
does the [hardness](ref/umr/hardness) of the mirror, making it more difficult to damage. This value
is the hardness of the patron mirror.

**Hit Points:** The base hit points of a mirror witch's patron mirror are based on what kind of
mirror she chooses. A steel mirror has 4 hit points and a glass mirror has 1 hit point. The patron
mirror gains the listed hit points in addition to the mirror's normal hit points, and the hit points
increase as the link between the witch and her patron mirror strengthens.

**Intelligence:** A patron is a powerful and unknowable entity, able to see great distances and
offer sage council, but the power of the fragment it manifests through a patron mirror is
proportional to the link the fragment has with the mirror witch. This column indicates the effective
Intelligence score of the patron mirror as the witch progresses in level. The patron mirror is not a
creature, and nothing can increase its Intelligence above the listed value.

**Special:** As a mirror witch increases in level, her patron mirror grants her additional powers as
indicated on the table.

## Cryptic Omens (Ex) {#cryptic-omens}

Each day, when a mirror witch consults with her patron mirror, the patron fragment can speak a few
words of cryptic advice about the witch's future. While the words are often obscure when the
fragment utters them, they nearly always make sense to the witch at just the right moment aid her in
dealing with the threats of the day. Once per day, after the witch receives this advice, she can
gain one of the following benefits without taking an action: gain a +2 insight bonus on a saving
throw she is about to attempt; gain a +2 insight bonus on a Bluff, Diplomacy, or Sense Motive check
she is about to attempt; or instead of rolling initiative, treat her initiative as if she rolled a
12 on the die. She can't use this last option if she can't act during a surprise round. She doesn't
choose which benefit she gains while consulting the mirror; instead, she does so when she would be
about to roll a saving throw, initiative check, or appropriate skill check.

## Seek Guidance (Ex) {#seek-guidance}

Whenever the mirror witch consults with her patron fragment, she can spend 10 minutes instead of the
usual 1 minute and attempt a single Knowledge check. She gains a +2 insight bonus on any Knowledge
check she attempts during such a consultation.

## Greater Omens (Ex) {#greater-omens}

The number of times per day that the mirror witch can use cryptic omens increases by an amount equal
to the Intelligence modifier of the patron mirror. Furthermore, after consulting with her patron for
1 minute, she can expend a use of cryptic omens to gain the effects of _[augury](ref/spell/augury)_
instead of one of the usual three benefits.

## Specialized Knowledge (Ex) {#specialized-knowledge}

The mirror witch chooses a number of Knowledge skills equal to the patron mirror's Intelligence
modifier (and chooses more as the mirror's Intelligence modifier increases). When the witch consults
her patron fragment with seek guidance for a Knowledge skill of one of the chosen types, the insight
bonus increases by an amount equal to the mirror's Intelligence modifier. For example, at 5th and
6th levels, she gains a +4 insight bonus on a chosen Knowledge skill instead of the normal +2.

## Clairvoyance/Clairaudience (Sp) {#clairvoyance-clairaudience}

By consulting her patron fragment for 10 minutes, the mirror witch can expend a single use of
cryptic omens to cast _[clairvoyance/clairaudience](ref/spell/clairaudience-clairvoyance)_ as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her witch level.

## Scrying (Sp) {#scrying}

By consulting with her patron fragment for 1 hour, the mirror witch can expend a single use of
cryptic omens to use _[scrying](ref/spell/scrying)_ as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her witch level,
using the patron mirror as the focus.

## Mirror Casting (Su) {#mirror-casting}

When using the mirror's [scrying](ref/spell/scrying) ability, _detect chaos_, _detect evil_, _detect
good_, _detect law_, _[detect magic](ref/spell/detect-magic)_, _[message](ref/spell/message)_,
_[read magic](ref/spell/read-magic)_, and _[tongues](ref/spell/tongues)_ all function reliably
through the sensor. Also, if the mirror witch is at least 15th level, there is a 5% chance each of
the following spells operates successfully through the sensor: _cause [fear](ref/spell/fear)_,
_[charm person](ref/spell/charm-person)_, _[command](ref/spell/command)_,
_[crushing despair](ref/spell/crushing-despair)_, _[deep slumber](ref/spell/deep-slumber)_,
_[enthrall](ref/spell/enthrall)_, _fear_, _[hold person](ref/spell/hold-person)_,
_[moonstruck](ref/spell/moonstruck)_, _[seek thoughts](ref/spell/seek-thoughts)_, and
_[sleep](ref/spell/sleep)_; a creature that succeeds at its saving throw against one of these linked
spells is forever immune to that particular mirror witch's attempts to cast that spell on that
creature through her mirror.
