+++
id = "ref/arc-inquisitor/secret-seeker"
kind = "archetype"
title = "Secret Seeker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_seeker", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Intrigue pg 29\
Secret seekers are trained in the art of extracting answers from intransigent foes. Recognizing that
torture is a poor method of securing truthful intelligence, secret seekers instead prefer magical
means of inquiry.

**Occult Lore (Su)**

**Ability:** A secret seeker gains access to the [prognostication](ref/skill/sense-motive) and
[read aura](ref/skill/perception) occult skill unlocks, but not the other occult skill unlocks.

**Replaces:** Monster lore

**Special:** If she ever chooses to gain the [Psychic Sensitivity](ref/feat/psychic-sensitivity)
feat or otherwise gains access to all occult skill unlocks, she receives
[Psychic Maestro](ref/feat/psychic-maestro) as a bonus feat, with prognostication and read aura as
the two occult skill unlocks selected.

**Detect Mind (Sp)**

**Ability:** A secret seeker can [detect anxieties](ref/spell/detect-anxieties),
[detect desires](ref/spell/detect-desires), or [detect thoughts](ref/spell/detect-thoughts), as per
the spells, for a number of rounds per day equal to twice her inquisitor level. These rounds need
not be consecutive. A creature that succeeds at a saving throw against this ability is immune to
that secret seeker's detect mind ability for 24 hours. If the secret seeker has the
[secrets](ref/inquisition/secrets) inquisition, she doubles the number of rounds per day that she
can use this ability.

**At 12th Level:** A secret seeker can use her _detect mind_ ability for a number of minutes per day
equal to twice her inquisitor level, rather than rounds. These minutes need not be consecutive but
must be spent in 1-minute increments. If the secret seeker has the _secrets_ inquisition, she
doubles the number of minutes per day she can use this ability.

**Gained:** At 5th Level

**Replaces:** Bane, greater bane

**Seek Mind (Sp)**

**Ability:** A secret seeker can use her _detect mind_ ability to seek out people with particular
anxieties, desires, or thoughts. This functions as per [seek thoughts](ref/spell/seek-thoughts)
except that it works with any of the three types of mental output the secret seeker can detect with
detect mind.

**Gained:** At 14th Level

**Replaces:** Exploit weakness
