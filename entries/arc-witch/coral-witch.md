+++
id = "ref/arc-witch/coral-witch"
kind = "archetype"
title = "Coral Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Coral%20Witch"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "coral_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "patron" },
  { anchor = "coral-familiar", level = 1 },
  { anchor = "waves-spirit-hex" },
  { anchor = "immovability", level = 8 },
]
trades = [
  { replaces = "Hex gained at 8th level", feature = "hex", levels = [8], by = ["immovability"] },
  { alters = "Familiar", feature = "witch-s-familiar", by = ["coral-familiar"] },
  { alters = "Hex", feature = "hex", by = ["waves-spirit-hex"] },
]
+++

Coral witches inhabit shallow coasts and reefs where great masses of coral grow. They use their
magic to fashion familiars from living coral and emulate the unyielding tenacity of these durable
marine organisms. Many coral witches actively patrol and protect their home reefs from predators and
help to rebuild the reefs after natural disasters. Although most coral witches are aquatic creatures
such as [gillmen](ref/race/gillman) and [locathahs](ref/race/locathah), surface creatures with a
deep connection to the sea sometimes become coral witches as well.

## Patron {#patron}

A coral witch's patron is normally [endurance](ref/patron/endurance), [healing](ref/patron/healing),
or [water](ref/patron/water), although a coral witch can select any patron other than those
associated with fire.

## Coral Familiar (Ex) {#coral-familiar}

A coral witch crafts her familiar out of living coral, coaxing the tiny organisms to grow in the
shape of a larger animal or [vermin](ref/type/vermin). The coral witch chooses a familiar as normal,
but its type changes to vermin ([aquatic](ref/subtype/aquatic)) and it gains the
[amphibious](ref/umr/amphibious) special quality. The coral witch's familiar has an Intelligence
score as normal for the witch's level, but it has immunity to mind-affecting effects. When
underwater near a coral reef of any size, a coral witch can spend 8 hours to restore her familiar to
full health at no cost, unless the familiar is killed, in which case she must follow the usual rules
for replacing her familiar. A coral witch can never gain an improved familiar.

This ability alters witch's familiar.

## Waves Spirit Hex {#waves-spirit-hex}

A coral witch can select hexes from the shaman's [waves spirit](ref/shamanspirit/waves) as if they
were witch hexes. She uses her witch level as her shaman level to determine the effect of the hex
and Intelligence instead of Wisdom to determine its DC.

This ability alters hex.

## Immovability (Ex) {#immovability}

At 8th level, a coral witch can naturally emulate coral's ability to affix itself in place. At the
end of any round in which the coral witch did not move from her space and is standing on solid
ground, she adds her class level to her CMD against any [bull rush](ref/rule/bull-rush),
[overrun](ref/rule/overrun), and [reposition](ref/rule/reposition) combat maneuvers,
[grapple](ref/rule/grapple) attempts to move her, and attempts to [pull](ref/umr/pull) or
[push](ref/umr/push) her. This bonus lasts until the start of the coral witch's next turn.

This ability replaces the hex gained at 8th level.

## Hexes {#hexes}

The following witch hexes complement the coral witch archetype: evil eye, feral speech, water lung.

## Major Hexes {#major-hexes}

The following major hexes complement the coral witch archetype: beast eye, hag's eye, weather
control.

## Grand Hexes {#grand-hexes}

The following grand hex complements the coral witch archetype: life giver.
