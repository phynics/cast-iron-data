+++
id = "ref/arc-monk/ki-mystic"
kind = "archetype"
title = "Ki Mystic"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Ki%20Mystic"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ki_mystic", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "111"

[fields]
kind = "archetype"
features = [
  { anchor = "ki-mystic", level = 3 },
  { anchor = "mystic-insight", level = 5 },
  { anchor = "mystic-visions", level = 11 },
  { anchor = "mystic-prescience", level = 13 },
  { anchor = "mystic-persistence", level = 19 },
]
trades = [
  { replaces = "Still mind", feature = "still-mind", by = ["ki-mystic"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["mystic-insight"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["mystic-visions"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["mystic-prescience"] },
  { replaces = "Empty body", feature = "empty-body", by = ["mystic-persistence"] },
]
+++

The ki mystic believes that violence is sometimes necessary, but knowing and understanding is the
true root of perfection. Through meditation and spiritual visions, a ki mystic can see beyond the
veil of reality to the underlying truth of all existence. A ki mystic has the following class
features.

## Ki Mystic (Su) {#ki-mystic}

At 3rd level, a _ki_ mystic gains a pool of _ki_ points equal to his Wisdom modifier. The pool
increases to 1/2 his monk level + his Wisdom modifier + 2 at level 4. If the monk has at least 1
point of _ki_ in his _ki_ pool, he gains a +2 bonus on all Knowledge skill checks. As a swift
action, the monk can spend 1 _ki_ point immediately before making an ability, or skill check to gain
a +4 insight bonus on the check. This ability replaces still mind.

## Mystic Insight (Su) {#mystic-insight}

At 5th level, a _ki_ mystic becomes apt at giving just the right word of advice in just the nick of
time. As an immediate action, the monk can spend 2 _ki_ points to grant an ally within 30 feet the
ability to reroll a single attack roll or saving throw. The ally must be able to hear the monk to
gain the reroll benefit. This ability replaces purity of body.

## Mystic Visions (Su) {#mystic-visions}

At 11th level, a _ki_ mystic may receive mystic visions when he rests. These visions can come as a
dream, an epiphany, or even as the voice of an old friend whispering in the monk's mind. The effect
is similar to a _[divination](ref/spell/divination)_ spell with a caster level equal to the monk's
level. The _divination_ has no casting time; it is just part of the normal dreams or visions that
occur every night. Using this ability costs 2 _ki_ points that are removed from the next day's
total. This ability replaces diamond body.

## Mystic Prescience (Su) {#mystic-prescience}

At 13th level, a _ki_ mystic gains a +2 insight bonus to AC and CMD. At 20th level, the bonus
increases to +4. This ability replaces diamond soul.

## Mystic Persistence (Su) {#mystic-persistence}

At 19th level, a _ki_ mystic can create an aura once per day as a swift action at the cost of at
least 2 points of _ki._ The aura emanates out to a 20-foot radius. The monk and all allies within
the aura can roll two dice when making an attack roll or a saving throw and take the better result.
The aura lasts for 1 round, plus an additional round for every 2 _ki_ points spent when the monk
created the aura. The monk can dismiss the aura at any time as a free action, but the _ki_ points
for the full duration of the aura are lost. This ability replaces empty body.
