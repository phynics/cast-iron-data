+++
id = "ref/arc-spiritualist/zeitgeist-binder"
kind = "archetype"
title = "Zeitgeist Binder"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Zeitgeist%20Binder"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "zeitgeist_binder", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "51"

[fields]
kind = "archetype"
features = [
  { anchor = "zeitgeist" },
  { anchor = "settlement-aspect" },
  { anchor = "settlement-avatar" },
]
trades = [
  { replaces = "Detect undead", feature = "detect-undead", by = ["settlement-aspect"] },
  { replaces = "calm spirit", feature = "calm-spirit", by = ["settlement-aspect"] },
  { replaces = "see invisibility", feature = "see-invisibility", by = ["settlement-aspect"] },
  { replaces = "call spirit", feature = "call-spirit", by = ["settlement-aspect"] },
  { replaces = "Bonded senses", feature = "bonded-senses", by = ["settlement-avatar"] },
  { replaces = "fused consciousness", feature = "fused-consciousness", by = ["settlement-avatar"] },
  { alters = "Phantom", feature = "phantom", by = ["zeitgeist"] },
]
+++

Not all spiritualists deal in the souls of creatures that refuse to pass into death. Zeitgeist
binders channel the emotional connections of a group of people into a unique phantom that
personifies a community.

## Zeitgeist (Su) {#zeitgeist}

A zeitgeist binder's phantom is called a zeitgeist. In addition to an emotion, a zeitgeist is tied
to one [aspect of its settlement](ref/rule/the-settlement-stat-block): corruption, crime, economy,
law, lore, or society. In order to select an aspect, that aspect of the settlement must have a
positive modifier (for instance, a settlement with a negative lore modifier or a modifier of 0 could
not manifest a lore zeitgeist). Although a zeitgeist personifies a single chosen settlement, a
zeitgeist binder can call it anywhere, but outside the bounds of its settlement, it loses the
benefits of its settlement aspect and settlement avatar abilities.

This ability alters phantom.

## Settlement Aspect (Sp) {#settlement-aspect}

A zeitgeist binder gains a number of [spell-like abilities](ref/umr/spell-like-abilities) tied to
her zeitgeist's settlement aspect. Other than being based on Wisdom instead of Charisma, these work
the same way as the [fractured mind's](ref/arc-spiritualist/fractured-mind) emotional power ability.
The _[masterwork transformation](ref/spell/masterwork-transformation)_ spell-like ability does not
ignore the material component.

### Corruption {#corruption}

_Conditional favor_ (5th), _false belief_ (7th), _charm person_ (9th), _mass suggestion_ (16th).

### Crime {#crime}

_Crime of opportunity_ (5th), _pilfering hand_ (7th), _demand offering_ (9th), _crime wave_ (16th).

### Economy {#economy}

_Crafter's fortune_ (5th), _masterwork transformation_ (7th), _beguiling gift_ (9th), _major
creation_ (16th).

### Law {#law}

_Detect chaos_ (5th), _arrow of law_ (7th), _peacebond_ (9th), _mark of justice_ (16th).

### Lore {#lore}

_Object reading_ (5th), _hypercognition_ (7th), _heightened awareness_ (9th), _legend lore_ (16th).

### Society {#society}

_Cultural adaptation_ (5th), _rumormonger_ (7th), _share language_ (9th), _coordinated effort_
(16th).

This ability replaces _detect undead_, _calm spirit_, _see invisibility_, and _call spirit_.

## Settlement Avatar (Su) {#settlement-avatar}

When a zeitgeist binder reaches 2nd level, the zeitgeist becomes a living avatar of the settlement.
As a standard action, it can project its senses out into the settlement, perceiving the general
pulse of its chosen aspect throughout the whole settlement as well as anything involving its aspect
that is occurring within 50 feet per spiritualist level. The sensing works like
_[enter image](ref/spell/enter-image)_, so the zeitgeist attempts a Perception check at a -10
penalty to notice any particular activity within range. The zeitgeist can use this ability for a
number of rounds per day equal to the zeitgeist binder's spiritualist level. These rounds need not
be consecutive.

When the zeitgeist binder reaches 10th level, the zeitgeist can project its senses to feel its
settlement aspect at will. Additionally, the zeitgeist binder gains a bonus teamwork feat as long as
she is in her zeitgeist's settlement. The zeitgeist binder must meet the teamwork feat's
prerequisites, and she grants the feat as a bonus feat to her zeitgeist, even if it doesn't meet the
prerequisites.

This ability replaces the spiritualist's bonded senses and fused consciousness.
