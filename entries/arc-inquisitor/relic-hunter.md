+++
id = "ref/arc-inquisitor/relic-hunter"
kind = "archetype"
title = "Relic Hunter"
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
replaces = ["Judgment", "Domain", "bane", "greater bane", "second judgment", "third judgment"]
alters = ["Spellcasting"]
replaces_features = ["judgment", "domain", "bane", "greater-bane", "second-judgment", "third-judgment"]
+++

Some inquisitors specialize in the use and recovery of long-lost relics of their faiths, drawing
forth divine might from the recovered items in order to restore their sanctity and wield these
artifacts against the enemies of their gods.

**Spells**

**Alters:** Spellcasting

**Info:** A relic hunter casts divine spells drawn from the inquisitor spell list, but her chosen
relic schools (see _Relics_ below) limit her to schools she knows, similar in function to an
occultist's _implements._ Any spell or orison gained by the relic hunter has a relic component (see
_Relics_ below), and is not considered to be on the relic hunter's spell list until she selects its
school though the relics alternate class feature. Once she chooses a school, all spells and orisons
of that school are considered to be on the relic hunter's class spell list, allowing her to use
spell trigger and spell completion magic items of those spells.

**Special:** A relic hunter's spells per day, daily spell allotment, Difficulty Class, and minimum
Wisdom score requirements remain unchanged from the inquisitor's normal spellcasting class feature.

**Relics (Su)**

**Ability:** A relic hunter gains the [occultist's](ref/class/occultist) _implements_ class feature
and learns to use two occultist [implement schools](ref/ability/implements) as relic schools.

**At 4th Level:** The relic hunter learns to use one additional relic school drawn from the same
source, gaining access to that school's resonant power and base focus power and opening up that
school's focus powers for her to select. Like an occultist, a relic hunter can select the same
school twice, but it is far less useful for her to do so.

**Gained:** At 1st Level

**Repeat:** She can learn a new relic school., 7, 3

**Replaces:** Judgment

**Special:** Relics do not need to be magic items, and nonmagical relics do not take up a magic item
slot. Relics that are not magic items are often of some religious significance to the relic hunter
or her church, such as the battered shield of a saint, a bishop's robe, or the finger bone of a
church martyr.

**Deific Focus (Su)**

**Action:** Ability

**Gained:** At 1st Level

**Repeat:** She learns a new focus power selected from all of the powers granted by all of the relic
schools she knows., 4, 4

**Replaces:** Domain, bane, greater bane, second judgment, third judgment

**Special:** Unless otherwise noted, the DC for any saving throws against a focus power is equal to
10 + 1/2 the inquisitor's class level + the inquisitor's Wisdom modifier. She cannot select a focus
power more than once. She uses her inquisitor level in place of an occultist level to qualify for
focus powers.

A relic hunter learns to invest divine power into her chosen relics. This acts like the occultist's
_focus powers_ and _mental focus_ class features, with the following adjustments.

Each day, a relic hunter has a number of points of _deific focus_ equal to her inquisitor level +
her Wisdom modifier, and she must spend 1 hour in prayer with her relics to invest them with divine
power. These points refresh at the start of each day.

The relic hunter learns the two base focus powers from her chosen relic schools and can select one
more focus power from the list of those made available by her chosen schools. Whenever she gains a
new relic school, she gains the base focus power of that school. She can use these focus powers only
by expending points of _deific focus._
