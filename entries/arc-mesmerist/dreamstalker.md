+++
id = "ref/arc-mesmerist/dreamstalker"
kind = "archetype"
title = "Dreamstalker"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Dreamstalker"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dreamstalker", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "horror-adventures"
page = "60"

[fields]
kind = "archetype"
features = [
  { anchor = "dreams-of-pain", level = 1 },
  { anchor = "somnomancer", level = 1 },
  { anchor = "sleepless", level = 2 },
  { anchor = "touch-of-night" },
  { anchor = "dreamwalker", level = 5 },
  { anchor = "traumatic-spell", level = 11 },
]
trades = [
  { replaces = "1st-level mesmerist trick", feature = "mesmerist-tricks", levels = [1], by = ["somnomancer"] },
  { replaces = "Towering ego", feature = "towering-ego", by = ["sleepless"] },
  { replaces = "Manifold tricks", feature = "manifold-tricks", by = ["dreamwalker"] },
  { replaces = "Glib lie", feature = "glib-lie", by = ["traumatic-spell"] },
  { alters = "Painful stare", feature = "painful-stare", by = ["dreams-of-pain"] },
  { alters = "Mesmerist tricks", feature = "mesmerist-tricks", by = ["somnomancer"] },
  { alters = "Touch treatment", feature = "touch-treatment", by = ["touch-of-night"] },
]
+++

Many mesmerists concentrate their studies on conscious, rational thought, but dreamstalkers instead
delve into the unleashed unconscious mind that wanders free in dreams.

## Dreams of Pain {#dreams-of-pain}

A dreamstalker's painful stare deals nonlethal damage.

This ability alters painful stare.

## Somnomancer {#somnomancer}

At 1st level, a dreamstalker gains the [slumber](ref/hex/slumber) hex. The dreamstalker's effective
witch level is equal to her mesmerist level, and she can activate them only by expending two daily
uses of mesmerist tricks. The save DCs for her hexes are Charisma-based. She can take certain
additional hexes in place of mesmerist tricks, selecting [nightmares](ref/hex/nightmares) or
[vision](ref/hex/vision) at 10th level and higher, or [eternal slumber](ref/hex/eternal-slumber) at
18th level and higher.

When she would normally gain a new mesmerist trick, she can learn additional spells instead. Each
time she does so, she adds two of the following spells of a level she can currently cast to her list
of spells known: 1st—_oneiric horror, sleep_; 2nd—_detect mindscape, greater oneiric horror,
instigate psychic duel_; 3rd—_deep slumber_, _minor dream_; 4th—_create mindscape, dream, forgetful
slumber_, _mindscape door, sleepwalk_, _sleepwalking suggestion_ (see page 127); 5th—_cloak of
dreams, dream council, dream scan, symbol of sleep, waves of fatigue_; 6th—_dream travel_, _greater
create mindscape, waves of exhaustion._

This alters mesmerist tricks and replaces the 1st-level mesmerist trick.

## Sleepless (Ex) {#sleepless}

At 2nd level, a dreamstalker gains immunity to sleep effects and a bonus equal to her Charisma bonus
on saving throws against [fatigue](ref/misc/fatigued) and [exhaustion](ref/misc/exhausted). She
loses both benefits when under an effect that would prevent her from providing an
[emotion component](ref/rule/components-oa).

This replaces towering ego.

## Touch of Night (Su) {#touch-of-night}

A dreamstalker can't remove shaken, frightened, sickened, cowering, nauseated, or panicked
conditions using her touch treatment. However, she can remove fatigue or magical sleep (other than
hard-to-remove magical sleep such as the eternal slumber hex) as a minor condition,
[staggered](ref/misc/staggered) as a moderate condition, and exhausted as a greater condition. As
normal, removing fatigue or exhaustion only removes the condition, not the underlying cause, such as
lack of sleep.

This ability alters touch treatment.

## Dreamwalker (Su) {#dreamwalker}

At 5th level, a dreamstalker treats [dreamscapes](ref/rule/dimension-of-dreams-oa) as a
[favored terrain](ref/ability/favored-terrain), as per the [ranger](ref/class/ranger) ability,
gaining a +2 bonus that increases by 2 every 4 mesmerist levels after 5th. While in a dreamscape,
she also treats any creature from the [Dimension of Dreams](ref/rule/dimension-of-dreams-oa)
(including dreamed figments) as her [favored enemy](ref/ability/favored-enemy), with a bonus equal
to 1/2 her favored terrain bonus.

This ability replaces manifold tricks.

## Traumatic Spell {#traumatic-spell}

At 11th level, a dreamstalker gains [Traumatic Spell](ref/feat/traumatic-spell) as a bonus feat.

This ability replaces glib lie.
