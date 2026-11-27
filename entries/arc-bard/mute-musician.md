+++
id = "ref/arc-bard/mute-musician"
kind = "archetype"
title = "Mute Musician"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Mute%20Musician"
source_ids = ["horror-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mute_musician", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "horror-realms"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "mute" },
  { anchor = "eschew-materials", level = 1 },
  { anchor = "symphony-of-silence", level = 3 },
  { anchor = "maddening-harmonics", level = 14 },
  { anchor = "ceaseless-performance", level = 15 },
  { anchor = "song-of-the-conjunction", level = 18 },
  { anchor = "insights-from-beyond", level = 2 },
  { anchor = "dulled-horror", level = 2 },
  { anchor = "eldritch-caesura", level = 10 },
  { anchor = "ex-mute-musicians" },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["eschew-materials"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["symphony-of-silence"] },
  { replaces = "Frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["maddening-harmonics"] },
  { replaces = "Inspire heroics", feature = "bardic-performance", power = "inspire heroics", by = ["ceaseless-performance"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["song-of-the-conjunction"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["insights-from-beyond"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["dulled-horror"] },
  { replaces = "Jack-of-all-trades", feature = "jack-of-all-trades", by = ["eldritch-caesura"] },
]
+++

A mute musician forswears speech for the unnatural songs and thunderous silences of the depths of
space. She learns to blend light and sound in seemingly impossible ways. Some mute musicians look to
the darker aspects of [Desna](ref/faith/desna) as their inspiration for these performances, but most
mute musicians find their muse in the alien sounds of the Elder Mythos and the entities that orbit
the blind idiot god [Azathoth](ref/faith/azathoth), who floats in the heart of the Dark Tapestry.

## Mute (Ex) {#mute}

A mute musician has a disability or injury (possibly self-inflicted or even psychological) that
prevents her from speaking or vocalizing. Language-dependent effects (including Perform \[oratory\])
require the bard to be able to use telepathy, nonverbal languages, or writing to communicate. She
cannot use Perform (sing) or speak languages, though she can still create audible bardic
performances by means of a musical instrument. A mute musician can provide verbal and somatic
components for spells she casts via any musical instrument in which she has ranks in the appropriate
Perform skill.

## Eschew Materials (Ex) {#eschew-materials}

A mute musician gains [Eschew Materials](ref/feat/eschew-materials) as a bonus feat at 1st level.

This ability replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

A mute musician gains the following bardic performances.

## Symphony of Silence (Su) {#symphony-of-silence}

At 3rd level, the mute musician's music muffles all other sounds within a 30-foot radius. All
creatures in the area of effect gain a +2 bonus on all saving throws made against sonic attacks or
language-dependent effects. This bonus increases to +3 at 7th level, +4 at 11th level, +5 at 15th
level, and +6 at 19th level. Symphony of silence relies on audible components.

This bardic performance replaces inspire competence.

## Maddening Harmonics (Su) {#maddening-harmonics}

At 14th level, the mute musician can create a performance so baffling and discordant that it usurps
all thought within a 30-foot radius with chaos and entropy. The mute musician can select which
creatures in this area are affected by the maddening harmonics and which are not. All targeted
creatures within this area must succeed at a Will saving throw (DC = 10 + 1/2 the bard's level + the
bard's Charisma modifier) or be confused for as long as they can hear the performance. If the
creature succeeds at its saving throw, it is immune to this ability for 24 hours. This performance
relies on audible components.

This bardic performance replaces frightening tune.

## Ceaseless Performance (Su) {#ceaseless-performance}

At 15th level, the mute musician can continue taking the free action to maintain a bardic
performance even while confused, cowering in fear, dazed, nauseated, panicked, paralyzed, petrified,
silenced, staggered, stunned, or unconscious. Even if the mute musician is killed, she can continue
to take the free action to maintain her performance as long as she has rounds remaining. Only the
utter [destruction](ref/spell/destruction) of the mute musician's body (such as via _destruction_ or
_[disintegrate](ref/spell/disintegrate)_, or by reducing the bard to a negative hit point total
equal to 10 × her Constitution score) causes the performance to end.

This ability replaces inspire heroics.

## Song of the Conjunction (Su) {#song-of-the-conjunction}

At 18th level, the mute musician can harmonize with the alien chorus beyond the music of the
spheres, creating a portentous cosmic alignment. This effect duplicates a _[gate](ref/spell/gate)_
used to travel, save that the destination point must be on the same plane as the bard, but it is not
otherwise limited by distance.

This bardic performance replaces mass suggestion.

## Insights from Beyond (Ex) {#insights-from-beyond}

At 2nd level, a mute musician adds two abjuration, conjuration (calling), conjuration (summoning),
or conjuration (teleportation) spells from the sorcerer/wizard spell list to her list of bard spells
known. At 6th level and every 4 bard levels thereafter, she can choose two more spells to add to her
spells known.

This class feature replaces versatile performance.

## Dulled Horror (Ex) {#dulled-horror}

At 2nd level, a mute musician gains a +4 bonus on saves against confusion, fear, insanity effects,
and the supernatural abilities of aberrations.

This class feature replaces well-versed.

## Eldritch Caesura (Su) {#eldritch-caesura}

At 10th level, a mute musician can insert unsettling silences into her otherworldly music by
spending an additional 1 round of bardic performance per round. This supernatural technique
impossibly blurs the line between music and light, transmitting audible performances and sonic bard
spells through most barriers save lead. This allows the music and sonic spells to affect creatures
across planar boundaries (including on the [Ethereal](ref/rule/ethereal-plane) or
[Shadow Planes](ref/rule/shadow-plane)), vacuums, and areas of magical silence.

This class feature replaces jack-of-all-trades.

## Ex-Mute Musicians {#ex-mute-musicians}

A mute musician who regains the ability to speak or chooses to speak aloud loses all abilities
granted by this archetype. She can regain the archetype's abilities by spending 24 hours without
speaking.
