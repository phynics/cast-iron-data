+++
id = "ref/arc-kineticist/elemental-purist"
kind = "archetype"
title = "Elemental Purist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Elemental%20Purist"
source_ids = ["planes-of-power"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_purist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "planes-of-power"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "limited-buffer" },
  { anchor = "elemental-impossibility", level = 7 },
  { anchor = "elemental-apocalypse", level = 20 },
]
trades = [
  { replaces = "Expanded element", feature = "expanded-element", by = ["elemental-impossibility"] },
  { replaces = "11th- and 19th-level infusions", feature = "infusion", levels = [11, 19], by = ["elemental-impossibility"] },
  { replaces = "Omnikinesis", feature = "omnikinesis", by = ["elemental-apocalypse"] },
]
+++

An elemental purist spurns all elements that are not her own, for utter devotion can allow one to
accomplish even seemingly impossible heroics.

## Limited Buffer (Su) {#limited-buffer}

An elemental purist does not gain internal buffer at 6th level. She instead gains internal buffer at
11th level and treats her kineticist level as 5 lower for the purpose of the ability.

## Elemental Impossibility (Su) {#elemental-impossibility}

At 7th level, an elemental purist learns one composite blast as if she had an expanded
[element](ref/ability/elements) that matched her primary element. In addition, she learns one
impossible infusion—a form infusion or substance infusion that does not need to be associated with
her primary element's type. If the infusion can be applied to her kinetic blasts normally, she can
use it as normal. If the infusion is not an associated infusion, she can accept 1 point of burn as a
free action to enter a state of elemental impossibility for one minute. This burn cannot be reduced
in any way. While in this state, she can apply her impossible infusions to her kinetic blast, even
if it is not an associated infusion for the blast type; however, if an infusion can be applied only
to energy blasts or only to physical blasts, she can apply it only to a kinetic blast of that type.
The elemental purist learns one additional impossible infusion at 11th, 15th, and 19th levels.

This ability replaces expanded element, as well as the 11th- and 19th-level infusions.

## Elemental Apocalypse (Su) {#elemental-apocalypse}

At 20th level, an elemental purist learns the apocalypse universal form infusion (Level 9; Burn 5;
Associated Blasts any; Saving Throw Reflex half) that she can use once per day. The apocalypse form
infusion functions as the [explosion](ref/kinetic/explosion) form infusion, except the elemental
purist can center the spread anywhere she can see within 1 mile, and she can choose to set the
radius anywhere between 5 feet and 360 feet.

This ability replaces omnikinesis.
