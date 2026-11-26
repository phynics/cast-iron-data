+++
id = "ref/arc-vigilante/serial-killer"
kind = "archetype"
title = "Serial Killer"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Serial%20Killer"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "serial_killer", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "horror-adventures"
page = "71"

[fields]
kind = "archetype"
features = [
  { anchor = "vigilante-specialization", level = 1 },
  { anchor = "thwart-pursuit", level = 3 },
  { anchor = "studied-target", level = 4 },
  { anchor = "charming", level = 5 },
  { anchor = "death-attack", level = 6 },
  { anchor = "calling-card", level = 7 },
  { anchor = "grisly-murder", level = 11 },
  { anchor = "quiet-death", level = 12 },
  { anchor = "swift-death", level = 17 },
]
trades = [
  { replaces = "Unshakable", feature = "unshakable", by = ["thwart-pursuit"] },
  { replaces = "4th- and 14th-level vigilante talents", feature = "vigilante-talent", levels = [4, 14], by = ["studied-target"] },
  { replaces = "9th- and 19th-level social talents", feature = "social-talent", levels = [9, 19], by = ["studied-target"] },
  { replaces = "Startling appearance", feature = "startling-appearance", by = ["charming"] },
  { replaces = "6th-level vigilante talent", feature = "vigilante-talent", levels = [6], by = ["death-attack"] },
  { replaces = "7th-level social talent", feature = "social-talent", levels = [7], by = ["calling-card"] },
  { replaces = "Frightening appearance", feature = "frightening-appearance", by = ["grisly-murder"] },
  { replaces = "12th-level vigilante talent", feature = "vigilante-talent", levels = [12], by = ["quiet-death"] },
  { replaces = "Stunning appearance", feature = "stunning-appearance", by = ["swift-death"] },
  { alters = "Vigilante specialization", feature = "vigilante-specialization", by = ["vigilante-specialization"] },
]
+++

Some vigilantes adopt an innocent guise to cloak their acts of brutal murder.

## Alignment {#alignment}

A serial killer's vigilante identity must be evil. A serial killer whose vigilante identity becomes
nonevil cannot gain new levels as a vigilante but retains all of her class abilities.

## Vigilante Specialization {#vigilante-specialization}

A serial killer must choose the stalker specialization. Her hidden strike is considered equivalent
to a [sneak attack](ref/ability/sneak-attack) with the same number of dice for the purpose of
meeting prerequisites or using abilities that depend on sneak attack.

This alters vigilante specialization.

## Thwart Pursuit (Ex) {#thwart-pursuit}

At 3rd level, a serial killer adds 1/2 her vigilante level as a bonus on all checks in
[a chase](ref/rule/chases) and to the DCs of Diplomacy checks to gather information about her and
checks to track her or notice her tracks (though not to the DC of the
[profiler's](ref/arc-investigator/profiler) expert profiler ability; see page 55).

This ability replaces unshakable.

## Studied Target (Ex) {#studied-target}

At 4th level, a serial killer gains the studied target ability of a [slayer](ref/class/slayer) 3
levels lower, including the ability to study multiple targets simultaneously at the appropriate
levels. The serial killer does not provoke attacks of opportunity when attempting a
[coup de grace](ref/misc/helpless) against a studied target.

This ability replaces the 4th- and 14th-level vigilante talents and the 9th- and 19th-level social
talents.

## Charming (Ex) {#charming}

At 5th level, a serial killer gains the [charm](ref/hex/charm) hex as if she were a witch of her
vigilante level, but she can't affect animals. The DC is based on her Charisma, and the ability is
nonmagical.

This ability replaces startling appearance.

## Death Attack (Ex) {#death-attack}

At 6th level, a serial killer gains the ability to make a death attack as if she were an
[assassin](ref/pclass/assassin) (DC = 10 + 1/2 her vigilante level + her Charisma modifier).

This ability replaces the 6th-level vigilante talent.

## Calling Card (Ex) {#calling-card}

At 7th level, when a serial killer slays a humanoid with a coup de grace or death attack, she can
leave a telltale token or clue behind identifying this death as her work. The serial killer chooses
her calling card when she gains this ability, and the first time she uses it in an area where she
has [renown](ref/soctalent/renown) (as per the renown social talent), it becomes associated with her
killings. After that, once citizens of a new settlement find this calling card, the serial killer
immediately establishes the settlement as an area of renown for her vigilante identity without
spending additional time to spread tales, and the Intimidate bonus from renown increases by 2. She
still must spend time to establish her social identity's renown.

This replaces the 7th-level social talent.

## Grisly Murder (Ex) {#grisly-murder}

At 11th level, a serial killer gains [Dreadful Carnage](ref/feat/dreadful-carnage) as a bonus feat,
and if she leaves a calling card, the murder is so horrifying that creatures examining the corpse
are affected as per _[nightmare](ref/spell/nightmare)_ that night (DC = 10 + 1/2 the serial killer's
vigilante level + her Charisma modifier). The [nightmare](ref/spell/nightmare) affects a number of
creatures equal to the serial killer's Charisma modifier, starting with the first creature to
examine the corpse.

This replaces frightening appearance.

## Quiet Death (Ex) {#quiet-death}

At 12th level, a serial killer gains the quiet death class feature as if she were an assassin.

This ability replaces the 12th-level vigilante talent.

## Swift Death (Ex) {#swift-death}

At 17th level, a serial killer gains the swift death class feature as an assassin.

This ability replaces the vigilante's stunning appearance.
