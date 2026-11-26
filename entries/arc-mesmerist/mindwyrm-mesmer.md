+++
id = "ref/arc-mesmerist/mindwyrm-mesmer"
kind = "archetype"
title = "Mindwyrm Mesmer"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Mindwyrm%20Mesmer"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindwyrm_mesmer", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "innate-coercion", level = 1 },
  { anchor = "phantasmagoric-breath", level = 1 },
  { anchor = "draconic-trick" },
  { anchor = "masterful-draconic-trick", level = 12 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["innate-coercion"] },
  { replaces = "Painful stare", feature = "painful-stare", by = ["phantasmagoric-breath"] },
]
+++

While most mesmerists are subtle and manipulative schemers, mindwyrm mesmers emulate the confidence,
swagger, and fear inspired by dragons to bully and browbeat others into obedience. These
dragon-inspired psychic magic-users typically employ draconic imagery in their dress and the
manifestations of their powers.

## Innate Coercion {#innate-coercion}

At 1st level, a mindwyrm mesmer gains a bonus equal to 1/2 his mesmerist level (minimum 1) on
Intimidate checks. In addition, a mindwyrm mesmer never takes penalties on Intimidate checks for
being smaller than his target.

This ability replaces consummate liar.

## Phantasmagoric Breath (Su) {#phantasmagoric-breath}

At 1st level, a mindwyrm mesmer has learned to mimic a [true dragon's](ref/family/dragon-true)
destructive breath using his psychic ability. A number of times per day equal to his Charisma bonus
(minimum 1 per day), a mindwyrm mesmer can unleash his phantasmagoric breath in either a 30-foot
cone or a 60-foot line as a standard action. The breath induces a psychosomatic response in
creatures caught in the area, dealing 1d6 points of energy damage at 1st level, plus an additional
1d6 points of energy damage at 3rd level and for every 2 mesmerist levels thereafter. The mindwyrm
mesmer selects the type of energy damage this deals (acid, cold, electricity, or fire) when this
ability is first gained; once made, this choice can't be changed. Creatures affected can attempt a
Will save (DC = 10 + 1/2 the mindwyrm mesmer's mesmerist level + his Charisma modifier) to realize
the true nature of the attack, which negates all damage. This is a mind-affecting effect.

This ability replaces painful stare.

## Draconic Trick (Su) {#draconic-trick}

The following new trick can be selected by a mindwyrm mesmer.

### Threatening Mien {#threatening-mien}

The subject's actions appear to be lethal in the extreme. A mindwyrm mesmer can trigger this trick
when the subject moves adjacent to an enemy. Enemies adjacent to the subject take a -4 penalty on
attacks against targets other than the subject. This trick lasts for 1 round per mindwyrm mesmer's
mesmerist level.

## Masterful Draconic Trick (Su) {#masterful-draconic-trick}

The following new masterful trick can be selected by a mindwyrm mesmer of 12th level or higher.

### Frightful Countenance {#frightful-countenance}

The subject's appearance changes into that which frightens an attacker to the core. The mindwyrm
mesmer can trigger this trick when the subject is targeted by an attack or by a spell that requires
an attack roll. The attacker must succeed at a Will save or the attack misses and the attacker
immediately becomes [shaken](ref/misc/shaken) for 1d4 rounds. This is a mind-affecting fear effect.
