+++
id = "ref/arc-kineticist/kinetic-knight"
kind = "archetype"
title = "Kinetic Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Kinetic%20Knight"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kinetic_knight", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "psychic-anthology"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "courtly" },
  { anchor = "elemental-blade", level = 1 },
  { anchor = "kinetic-warrior" },
  { anchor = "elemental-bastion", level = 2 },
  { anchor = "knight-s-resolve", level = 3 },
]
trades = [
  { replaces = "Metakinesis", feature = "metakinesis", by = ["elemental-blade"] },
  { replaces = "metakinetic master", feature = "metakinetic-master", by = ["elemental-blade"] },
  { replaces = "The kineticist infusion gained at 3rd level", feature = "infusion", levels = [3], by = ["knight-s-resolve"] },
  { replaces = "supercharge", feature = "supercharge", by = ["knight-s-resolve"] },
  { alters = "Kinetic blast", feature = "kinetic-blast", by = ["elemental-blade"] },
  { alters = "infusions", feature = "infusion", by = ["elemental-blade"] },
  { alters = "Elemental defense", feature = "elemental-defense", by = ["elemental-bastion"] },
  { alters = "Class skills", by = ["courtly"] },
]
+++

A kinetic knight dons armor and wields a blade of elemental energy. The Phoenix Kindred counted many
of these resolute warriors among their number, combining the Recursion Tablets' secrets with a
warrior's ways. Today, most remaining Tian kinetic knights follow the philosophy of ichimeiyo.
Kinetic knights are rarer in the Inner Sea region, but not unknown; many realize their elemental
powers while training for battle.

## Courtly {#courtly}

The kinetic knight adds Diplomacy and Sense Motive to her list of class skills instead of Acrobatics
and Stealth.

This ability alters the kineticist's class skills.

## Elemental Blade (Su) {#elemental-blade}

At 1st level, a kinetic knight gains the [kinetic blade](ref/kinetic/kinetic-blade) form infusion,
and it costs 0 points of burn instead of 1 point. She can't use her kinetic blast without the
kinetic blade form infusion or an infusion that lists kinetic blade as a prerequisite.

At 3rd level, the kinetic knight gains the [blade rush](ref/kinetic/blade-rush) infusion (see page
20). At 5th level, she gains the [kinetic whip](ref/kinetic/kinetic-whip) infusion. Her kinetic whip
has the [disarm](ref/misc/disarm), [performance](ref/misc/performance), and [trip](ref/misc/trip)
weapon qualities. At 9th level, she gains the [blade whirlwind](ref/kinetic/blade-whirlwind)
infusion (see page 20). At 11th level, she gains the [whip hurricane](ref/kinetic/whip-hurricane)
infusion (see page 22). At 13th level as a swift action, she can accept 2 points of burn to unleash
a kinetic blast with the blade rush infusion.

This ability alters kinetic blast and infusions, and replaces metakinesis and metakinetic master.

## Kinetic Warrior (Ex) {#kinetic-warrior}

The kinetic knight can use her Constitution score in place of her Intelligence score when qualifying
for combat feats. This ability counts as having [Combat Expertise](ref/feat/combat-expertise) for
the purpose of feat prerequisites.

## Elemental Bastion (Ex) {#elemental-bastion}

At 2nd level, the kinetic knight becomes proficient with medium and heavy armor and shields (except
tower shields). In addition, the kinetic knight can accept 1 point of burn to attune herself to a
specific light or heavy shield until the next time her burn is removed. Wielding an attuned shield
doesn't prevent the kinetic knight from gathering power. A kinetic knight gains the elemental
defense ability at 4th level, rather than 2nd, and its benefits apply only while she is wearing
heavy armor and wielding an attuned shield. If the kinetic knight selects the expanded defense
talent, its benefits also apply only under these conditions. If she has the
[shroud of water](ref/kinetic/shroud-of-water) defense wild talent, whenever its bonus would be
increased by accepting burn, she instead increases the enhancement bonus of her armor or attuned
shield by an equal amount (to a maximum of +5).

This ability alters elemental defense.

## Knight's Resolve (Ex) {#knight-s-resolve}

At 3rd level, the kinetic knight gains the [samurai's](ref/class/samurai) resolve class feature, as
a samurai of her kineticist level - 2. At 11th level, she gains the samurai's greater resolve
ability (_Pathfinder RPG Ultimate Combat_ 20). If she also has samurai levels, those levels stack
with her kineticist levels to determine the benefits of this ability.

This ability replaces the kineticist infusion gained at 3rd level and supercharge.
