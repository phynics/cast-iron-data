+++
id = "ref/arc-shaman/animist"
kind = "archetype"
title = "Animist"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Animist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animist", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "advanced-class-guide"
page = "110"

[fields]
kind = "archetype"
features = [
  { anchor = "animist-spirit-magic" },
  { anchor = "wrangle-condition", level = 2 },
  { anchor = "exorcism", level = 8 },
  { anchor = "dominate-spirit", level = 10 },
  { anchor = "contact-with-the-spirit-world", level = 12 },
  { anchor = "etherealness", level = 18 },
  { anchor = "spirit-shaman", level = 20 },
]
trades = [
  { replaces = "Spirit magic spells gained from the shaman's spirit", feature = "spirit-magic", by = ["animist-spirit-magic"] },
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["wrangle-condition"] },
  { replaces = "Hex gained at 8th level", feature = "hex", levels = [8], by = ["exorcism"] },
  { replaces = "Hex gained at 10th level", feature = "hex", levels = [10], by = ["dominate-spirit"] },
  { replaces = "Hex gained at 12th level", feature = "hex", levels = [12], by = ["contact-with-the-spirit-world"] },
  { replaces = "Hex gained at 18th level", feature = "hex", levels = [18], by = ["etherealness"] },
  { replaces = "Manifestation", feature = "manifestation", by = ["spirit-shaman"] },
]
+++

Even among mystical practitioners, the animist has a strange perspective and even stranger magic.
The animist perceives that all things have a spirit, including objects, constructs, illnesses,
buildings, and the environment.

## Animist Spirit Magic {#animist-spirit-magic}

The animist adds the following spells to the list of spells he can cast using spirit magic: _speak
with animals_ (1st), _skinsend_ (2nd), _speak with plants_ (3rd), _malfunction_ (4th), _dream_
(5th), _speak with stone_ (6th), _control construct_ (7th), _trap the soul_ (8th), _soul bind_
(9th). This ability replaces the spirit magic spells gained from the shaman's spirit.

## Wrangle Condition (Su) {#wrangle-condition}

At 2nd level, the animist interacts directly with unwholesome spirits of the ills that trouble him
or his people. To the animist, negative conditions manifest as anthropomorphic spirits or are caused
by such spirits (visited upon the creature by bad magic). Either way, the animist can attempt to
persuade the spirit to leave its victim alone, thus performing a miraculous healing. As the animist
grows in power, he can simply inform these spirits that they are unwelcome and command them to
depart.

The animist can attempt a Diplomacy check to persuade the condition's spirit to leave. Conditions
the animist can affect are ranked from minor to dire, with each category having an accompanying
Diplomacy DC (see below). The animist cannot take 10 or 20 on the check or receive aid from any
creature except another shaman. Failure by 5 or less means the condition spirit is willing to leave
the target and transfer to the animist for the rest of the duration or until cured; this happens
only if the animist is willing. Failure by 10 or more means that not only is the target inflicted
with the condition, but the animist is as well (whether or not he is willing) for the remaining
duration or until cured.

_Minor Conditions_ (DC 15): Fatigued, shaken, and sickened.

_Major Conditions_ (DC 20): Dazed and staggered.

_Severe Conditions_ (DC 25): Exhausted, frightened, and nauseated.

_Dire Conditions_ (DC 30): Blinded, deafened, paralyzed, and stunned.

The animist can use this ability a number of times per day equal to 1/2 his shaman level + his
Wisdom modifier. Using this ability is a standard action that requires no contact or shared language
with the target, but it relies on audible components and the target must be within 30 feet. If a
target is afflicted with multiple conditions, the animist targets one condition at a time (of her
choosing). The animist cannot use this ability on himself.

At 5th level, the animist can use this ability to exorcise minor conditions without needing to
attempt a Diplomacy check. He can dispatch major conditions without a roll at 9th level, severe
conditions at 13th level, and dire conditions at 17th level. Doing so still requires one use of this
ability per condition.

This ability replaces the hex gained at 2nd level.

## Exorcism (Su) {#exorcism}

At 8th level, the animist can attempt to end effects that control a creature or object, such as
_[magic jar](ref/spell/magic-jar)_, _[possess object](ref/spell/possess-object)_,
_[dominate person](ref/spell/dominate-person)_, and
_[dominate monster](ref/spell/dominate-monster)_, or possessing entities such as
[ghosts](ref/template/ghost). This is a full-round action that requires the animist to touch the
target. The possessing or dominating creature must attempt a Will save with a DC equal to 10 + 1/2
the shaman level + her Wisdom modifier. Failure means that the controlling effect ends or the entity
is immediately cast out of the target, as appropriate. If the possessing entity is exorcised, it
cannot attempt to dominate or possess that target again for 24 hours. The animist can exorcise the
same entity out of different targets, but once the entity successfully saves against the animist's
exorcism, it cannot be affected by this ability again for 24 hours. This ability replaces the hex
gained at 8th level.

## Dominate Spirit (Sp) {#dominate-spirit}

At 10th level, the animist can attempt to possess creatures or objects as
_[magic jar](ref/spell/magic-jar)_ or _[possess object](ref/spell/possess-object)_. When the animist
is attempting to possess the creature, his familiar acts as the jar and must be within 10 feet when
the animist attempts to possess a creature. The animist's soul can perceive his surroundings through
the familiar's senses, clearly evaluate potential targets for possession, and communicate with his
familiar telepathically. The familiar retains its autonomy while acting as the jar, and is not
harmed by being used as a vessel for the animist's soul. The animist can use this ability once per
day at 10th level, plus an additional time per day every 4 levels thereafter. This ability replaces
the hex gained at 10th level.

## Contact with the Spirit World (Su) {#contact-with-the-spirit-world}

At 12th level, the shaman can interact with incorporeal entities as if his unarmed strikes and melee
weapons had the _[ghost touch](ref/magic-enh/ghost-touch-weapon)_ weapon special ability. While
using this ability, he can also see nearby ethereal entities and likewise strike at them as if they
were incorporeal. He can use this ability for a number of rounds per day equal to his shaman level.
The rounds need not be consecutive. This ability replaces the hex gained at 12th level.

## Etherealness (Sp) {#etherealness}

At 18th level, the animist can cast _[etherealness](ref/spell/etherealness)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities). This ability replaces the hex gained at 18th
level.

## Spirit Shaman (Sp) {#spirit-shaman}

At 20th level, the animist can use _[ethereal jaunt](ref/spell/ethereal-jaunt)_ as at will as a
[spell-like ability](ref/umr/spell-like-abilities), and cast
_[astral projection](ref/spell/astral-projection)_ once per day as a spell-like ability. This
ability replaces manifestation.
