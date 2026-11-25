+++
id = "ref/arc-psychic/formless-adept"
kind = "archetype"
title = "Formless Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Formless%20Adept"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "formless_adept", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "occult-adventures"
page = "104"

[fields]
kind = "archetype"
features = [
  { anchor = "phrenic-charisma" },
  { anchor = "formless-body" },
  { anchor = "blurred-body", level = 1 },
  { anchor = "gaseous-body", level = 5 },
  { anchor = "incorporeal-body", level = 13 },
  { anchor = "formless-spell", level = 1 },
  { anchor = "psychic-possession", level = 15 },
  { anchor = "formless-master", level = 20 },
]
trades = [
  { replaces = "Psychic discipline", feature = "psychic-discipline", by = ["incorporeal-body"] },
  { replaces = "discipline powers", feature = "psychic-discipline", power = "discipline power", by = ["incorporeal-body"] },
  { replaces = "1st-level phrenic amplification", feature = "phrenic-amplifications", levels = [1], by = ["formless-spell"] },
  { replaces = "Discipline spells", feature = "psychic-discipline", power = "discipline spell" },
  { replaces = "15th-level phrenic amplification", feature = "phrenic-amplifications", levels = [15], by = ["psychic-possession"] },
  { replaces = "Remade self", feature = "remade-self", by = ["formless-master"] },
  { alters = "Phrenic pool", feature = "phrenic-pool", by = ["phrenic-charisma"] },
]
+++

Formless adepts master their psychic powers to unshackle themselves from the confines of the flesh
and empower their spellcasting. They learn to assume increasingly insubstantial forms until they
become like living ghosts.

## Phrenic Charisma {#phrenic-charisma}

A formless adept uses his Charisma modifier to determine the number of points in his phrenic pool.
This ability alters phrenic pool.

## Formless Body {#formless-body}

A formless adept gradually sheds his body, taking on increasingly nebulous forms. A formless adept
can assume a formless body as a standard action. He can remain in each formless body type for a
number of rounds per day equal to 3 + his Charisma modifier. The rounds don't have to be used
consecutively, but must be used in 1-round increments. Resuming his physical form takes another
standard action; otherwise, the formless adept continues spending rounds of formless body until he
runs out of them. The formless adept must return to his physical form before assuming a different
formless body.

## Blurred Body (Su) {#blurred-body}

At 1st level, a formless adept can act under the effect of a _[blur](ref/spell/blur)_ spell. At 5th
level, the formless adept can use this ability for a number of minutes per day instead of rounds per
day. These minutes don't have to be used consecutively, but must be used in 1-minute increments.

## Gaseous Body (Su) {#gaseous-body}

At 5th level, a formless adept can become gaseous as _[gaseous form](ref/spell/gaseous-form)._ At
13th level, the formless adept can use this ability for a number of minutes per day instead of
rounds per day. These minutes don't have to be used consecutively, but must be used in 1-minute
increments.

## Incorporeal Body (Su) {#incorporeal-body}

At 13th level, a formless adept can become [incorporeal](ref/umr/incorporeal).

This ability replaces the psychic discipline and discipline powers class features.

## Formless Spell {#formless-spell}

At 1st level, a formless adept gains the formless spell phrenic amplification. He can spend 1 point
from his phrenic pool to cast a spell with a standard-action casting time as part of the action he
uses to assume his formless body, expending the spell slot as normal. This ability replaces the
1st-level phrenic amplification.

## Bonus Spells {#bonus-spells}

The formless adept adds extra spells to his list of spells known while he's in a formless body
(including when he uses the formless spell phrenic amplification). Spells with a duration last for
their full duration, even if the psychic reverts to his physical form. For feats and other abilities
that require these spells as prerequisites, the psychic counts as knowing the spells but can benefit
from the feats and abilities only while in a formless body. The formless adept gains the following
spells at the appropriate levels: _chill touch_ and _expeditious retreat_ (1st), _levitate_ and
_stricken heart_ (4th), _gaseous form_ and _vampiric touch_ (6th), _shadow step_ and _telekinesis_
(8th), _dominate person_ and _synapse overload_ (10th), _disintegrate_ and _enemy hammer_ (12th),
_finger of death_ and _telekinetic sphere_ (14th), _etherealness_ and _power word stun_ (16th), and
_dominate monster_ and _telekinetic storm_ (18th). This ability replaces discipline spells.

## Psychic Possession (Su) {#psychic-possession}

At 15th level, while using his _incorporeal body_ ability, a formless adept can attempt to
psychically possess another living creature. To use this ability, the formless adept must be
adjacent to the target. This effect works as the [greater possession](ref/spell/possession-greater)
spell and can be maintained only as long as the formless adept maintains his _incorporeal body_
form. The target can attempt a Will save with a DC equal to 10 + 1/2 the formless adept's class
level + the formless adept's Intelligence modifier to resist the effect. A creature that
successfully saves is immune to the formless adept's psychic possession for 24 hours. This ability
replaces the 15th-level phrenic amplification.

## Formless Master (Su) {#formless-master}

At 20th level, a formless adept can assume any formless body as a swift action and change between
formless body types as a standard action (without returning to his physical form first). He can use
the formless spell phrenic amplification to cast any spell with a swift-action casting time when
assuming a formless body or any spell with a standard-action casting time while switching between
formless bodies. The formless adept also adds his Charisma bonus as a deflection bonus to his AC
while in a formless body. A formless adept can attempt a saving throw to bypass any spells that
prevent entry of incorporeal creatures (such as
_[anti-incorporeal shell](ref/spell/anti-incorporeal-shell)_), even if the spells don't normally
allow one. This ability replaces remade self.
