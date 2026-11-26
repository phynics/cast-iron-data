+++
id = "ref/arc-witch/nexian-spellspy"
kind = "archetype"
title = "Nexian Spellspy"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Nexian%20Spellspy"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nexian_spellspy", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "nondetection" },
  { anchor = "infiltrating-vessel", level = 3 },
  { anchor = "prepare-results", level = 4 },
]
trades = [
  { replaces = "Familiar's ability to deliver touch spells", by = ["infiltrating-vessel"] },
  { replaces = "4th-level hex", feature = "hex", levels = [4], by = ["prepare-results"] },
  { alters = "Familiar", feature = "witch-s-familiar", by = ["infiltrating-vessel"] },
]
+++

Among that nation's highly competitive arcane communities, Nexian spellspies are witches who use
their familiars and divining talents to spy on their rivals and protect themselves from similar
intrusions.

## Nondetection {#nondetection}

A Nexian spellspy treats _[nondetection](ref/spell/nondetection)_ as a 4th-level witch spell.

## Infiltrating Vessel (Su) {#infiltrating-vessel}

At 3rd-level, a Nexian spellspy cannot use her familiar to deliver touch spells for her. Instead,
the Nexian spellspy can cast divination spells through her familiar. When the Nexian spellspy does
this, she casts the spell as normal, but she treats her familiar's location as hers for purpose of
determining the spell's area of effect or range. The Nexian spellspy receives the spell's results as
normal. This ability does not allow her to see through her familiar's eyes; for example, the Nexian
spellspy would know about a powerful magic item detected through her familiar, but she would not
know its exact location or exactly what the item looked like. Whenever a familiar would be able to
deliver a hex, the Nexian spellspy can use the familiar as a vessel for her divinations in this way.

This alters the witch's familiar.

## Prepare Results (Su) {#prepare-results}

At 4th level, a Nexian spellspy's familiar can store the results of divinations for the purposes of
providing false results to a rival diviner who has targeted the spellspy. As a standard action, the
spellspy can store the results of one or more divinations she has cast within the past 24 hours. She
can store results from any number of spells with a total spell level equal to the highest spell she
can cast.

The next time a rival spellcaster would receive results from any of the specific divinations whose
results are stored in her familiar in this manner, the stored results are transmitted to the rival
caster (and are removed from the familiar) in place of any real results.

The rival spellcaster receives a Will saving throw (DC = 10 + 1/2 the Nexian spellspy's witch
level + her Intelligence modifier) to recognize that the results are falsified. Depending on the
spell, the stored results from the familiar might make this falsification obvious (and thus no Will
saving throw is necessary to determine the falsification).

This ability replaces the witch's 4th-level hex.

## Hexes {#hexes}

The following witch hexes complement the Nexian spellspy archetype: beast of ill-omen, evil eye, and
tongues.

## Major Hexes {#major-hexes}

The following major hexes complement the Nexian spellspy witch archetype: beast eye, hag's eye, and
vision.

## Grand Hex {#grand-hex}

The following grand hex complements the Nexian spellspy archetype: dire prophecy.
