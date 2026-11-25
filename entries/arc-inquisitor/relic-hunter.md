+++
id = "ref/arc-inquisitor/relic-hunter"
kind = "archetype"
title = "Relic Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Relic%20Hunter"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "relic_hunter", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "occult-adventures"
page = "119"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "relics", level = 1 },
  { anchor = "deific-focus", level = 1 },
]
trades = [
  { replaces = "Judgment", feature = "judgment", by = ["relics"] },
  { replaces = "Domain", feature = "domain", by = ["deific-focus"] },
  { replaces = "bane", feature = "bane", by = ["deific-focus"] },
  { replaces = "greater bane", feature = "greater-bane", by = ["deific-focus"] },
  { replaces = "second judgment", feature = "second-judgment", by = ["deific-focus"] },
  { replaces = "third judgment", feature = "third-judgment", by = ["deific-focus"] },
  { alters = "Spellcasting", feature = "spells", by = ["spells"] },
]
+++

Some inquisitors specialize in the use and recovery of long-lost relics of their faiths, drawing
forth divine might from the recovered items in order to restore their sanctity and wield these
artifacts against the enemies of their gods.

## Spells {#spells}

A relic hunter casts divine spells drawn from the inquisitor spell list, but her chosen relic
schools (see Relics below) limit her to schools she knows, similar in function to an occultist's
implements. Any spell or orison gained by the relic hunter has a relic component (see Relics below),
and is not considered to be on the relic hunter's spell list until she selects its school though the
relics alternate class feature. Once she chooses a school, all spells and orisons of that school are
considered to be on the relic hunter's class spell list, allowing her to use spell trigger and spell
completion magic items of those spells. A relic hunter's spells per day, daily spell allotment,
Difficulty Class, and minimum Wisdom score requirements remain unchanged from the inquisitor's
normal spellcasting class feature. This ability alters the inquisitor's spellcasting.

## Relics (Su) {#relics}

At 1st level, a relic hunter gains the [occultist's](ref/class/occultist) implements class feature
(see page 47) and learns to use two occultist [implement schools](ref/ability/implements) as relic
schools. At 4th level and every 3 levels thereafter, the relic hunter learns to use one additional
relic school drawn from the same source, gaining access to that school's resonant power and base
focus power and opening up that school's focus powers for her to select. Like an occultist, a relic
hunter can select the same school twice, but it is far less useful for her to do so.

Relics do not need to be magic items, and nonmagical relics do not take up a magic item slot. Relics
that are not magic items are often of some religious significance to the relic hunter or her church,
such as the battered shield of a saint, a bishop's robe, or the finger bone of a church martyr.

This ability replaces judgment.

## Deific Focus (Su) {#deific-focus}

At 1st level, a relic hunter learns to invest divine power into her chosen relics. This acts like
the occultist's focus powers and mental focus class features (see pages 47 and 48, respectively),
with the following adjustments.

Each day, a relic hunter has a number of points of deific focus equal to her inquisitor level + her
Wisdom modifier, and she must spend 1 hour in prayer with her relics to invest them with divine
power. These points refresh at the start of each day.

At 1st level, the relic hunter learns the two base focus powers from her chosen relic schools and
can select one more focus power from the list of those made available by her chosen schools.
Whenever she gains a new relic school, she gains the base focus power of that school. In addition,
at 4th level and every 4 levels thereafter, she learns a new focus power selected from all of the
powers granted by all of the relic schools she knows. She can use these focus powers only by
expending points of deific focus. Unless otherwise noted, the DC for any saving throws against a
focus power is equal to 10 + 1/2 the inquisitor's class level + the inquisitor's Wisdom modifier.
She cannot select a focus power more than once. She uses her inquisitor level in place of an
occultist level to qualify for focus powers.

This ability replaces domain, bane, greater bane, second judgment, and third judgment.
