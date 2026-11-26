+++
id = "ref/arc-inquisitor/secret-seeker"
kind = "archetype"
title = "Secret Seeker"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Secret%20Seeker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_seeker", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "occult-lore", level = 1 },
  { anchor = "detect-mind", level = 5 },
  { anchor = "seek-mind", level = 14 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["occult-lore"] },
  { replaces = "Bane", feature = "bane", by = ["detect-mind"] },
  { replaces = "greater bane", feature = "greater-bane", by = ["detect-mind"] },
  { replaces = "Exploit weakness", feature = "exploit-weakness", by = ["seek-mind"] },
]
+++

Secret seekers are trained in the art of extracting answers from intransigent foes. Recognizing that
torture is a poor method of securing truthful intelligence, secret seekers instead prefer magical
means of inquiry.

## Occult Lore (Su) {#occult-lore}

A secret seeker gains access to the [prognostication](ref/skill/sense-motive) and
[read aura](ref/skill/perception) occult skill unlocks (_Pathfinder RPG Occult Adventures_ 196–197),
but not the other occult skill unlocks. If she ever chooses to gain the
[Psychic Sensitivity](ref/feat/psychic-sensitivity) feat or otherwise gains access to all occult
skill unlocks, she receives [Psychic Maestro](ref/feat/psychic-maestro) as a bonus feat, with
prognostication and read aura as the two occult skill unlocks selected.

This ability replaces monster lore.

## Detect Mind (Sp) {#detect-mind}

At 5th level, a secret seeker can _[detect anxieties](ref/spell/detect-anxieties)_ (see page 211),
_[detect desires](ref/spell/detect-desires)_ (see page 211), or
_[detect thoughts](ref/spell/detect-thoughts)_, as per the spells, for a number of rounds per day
equal to twice her inquisitor level. These rounds need not be consecutive. A creature that succeeds
at a saving throw against this ability is immune to that secret seeker's detect mind ability for 24
hours. If the secret seeker has the [secrets](ref/inquisition/secrets) inquisition (see page 28),
she doubles the number of rounds per day that she can use this ability.

At 12th level, a secret seeker can use her detect mind ability for a number of minutes per day equal
to twice her inquisitor level, rather than rounds. These minutes need not be consecutive but must be
spent in 1-minute increments. If the secret seeker has the secrets inquisition, she doubles the
number of minutes per day she can use this ability.

This ability replaces bane and greater bane.

## Seek Mind (Sp) {#seek-mind}

At 14th level, a secret seeker can use her detect mind ability to seek out people with particular
anxieties, desires, or thoughts. This functions as per _[seek thoughts](ref/spell/seek-thoughts)_
except that it works with any of the three types of mental output the secret seeker can detect with
detect mind.

This ability replaces exploit weakness.
