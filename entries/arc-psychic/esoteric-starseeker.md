+++
id = "ref/arc-psychic/esoteric-starseeker"
kind = "archetype"
title = "Esoteric Starseeker"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Esoteric%20Starseeker"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "esoteric_starseeker", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "wilderness-origins"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "written-in-the-stars", level = 1 },
  { anchor = "major-amplifications", level = 15 },
]
trades = [
  { replaces = "The bonus spells normally granted by the psychic's discipline", feature = "psychic-discipline", power = "discipline spell", by = ["written-in-the-stars"] },
  { replaces = "The phrenic amplifications gained at 1st and 11th levels", feature = "phrenic-amplifications", levels = [1, 11], by = ["written-in-the-stars"] },
]
+++

The celestial bodies travel through the sky in fixed patterns, and knowledgeable astrologers rely on
these stellar constants to make accurate predictions, but the constellations can also be a source of
power. An esoteric starseeker is a psychic who focuses her studies on uncovering the secrets of the
sky and the constellations of the Cosmic Caravan, able to read the stars as well as she can read
minds. For more information on the Cosmic Caravan, see pages 36 and 37 of _Pathfinder Campaign
Setting: Occult Mysteries._

## Written in the Stars {#written-in-the-stars}

An esoteric starseeker can spend 1 hour each night in quiet contemplation of the stars to attune
herself to a constellation of the Cosmic Caravan, gaining knowledge of new spells from it. She gains
one bonus constellation spell slot for each spell level she can cast, and she can prepare a spell
associated with her attuned constellation into that slot. At 11th level, she can attune herself to
two constellations, choosing between the spells offered by both constellations when she prepares her
constellation spells. Whenever she attunes herself to a constellation, the esoteric starseeker must
also weaken her connection to one school of magic of her choice, increasing the casting time for all
spells of that school to a full-round action or an additional full-round action, as though she were
using a [metamagic feat](ref/rule/feats-basic). She can change her attuned constellations and her
weakened school each day when she prepares her constellation spells. The Cosmic Caravan and their
associated spells are as follows.

The Thrush: _comprehend languages_ (1st), _magic mouth_ (2nd), _tiny hut_ (3rd), _dream_ (4th),
_remote viewing_ (5th), _battlemind link_ (6th), _phase door_ (7th), _discern location_ (8th),
_wish_ (9th).

The Lantern Bearer: _liberating command_ (1st), _glitterdust_ (2nd), _guiding star_ (3rd),
_wandering star motes_ (4th), _true seeing_ (5th), _sonic form_ (6th), _prismatic spray_ (7th),
_sunburst_ (8th), _meteor swarm_ (9th).

The Newlyweds: _charm person_ (1st), _enthrall_ (2nd), _synesthesia_ (3rd), _break enchantment_
(4th), _reincarnate_ (5th), _joyful rapture_ (6th), _mass synesthesia_ (7th), _bilocation_ (8th),
_overwhelming presence_ (9th).

The Bridge: _endure elements_ (1st), _resist energy_ (2nd), _daylight_ (3rd), _fire shield_ (4th),
_wall of force_ (5th), _contagious flame_ (6th), _reverse gravity_ (7th), _create demiplane_ (8th),
_world wave_ (9th).

The Daughter: _bless_ (1st), _hypnotic pattern_ (2nd), _heroism_ (3rd), _freedom of movement_ (4th),
_hostile juxtaposition_ (5th), _cloak of dreams_ (6th), _greater hostile juxtaposition_ (7th),
_irresistible dance_ (8th), _freedom_ (9th).

The Rider: _anticipate peril_ (1st), _acute senses_ (2nd), _ablative barrier_ (3rd), _dimensional
anchor_ (4th), _echolocation_ (5th), _blade barrier_ (6th), _grasping hand_ (7th), _frightful
aspect_ (8th), _ride the lightning_ (9th).

The Patriarch: _command_ (1st), _spiritual weapon_ (2nd), _dispel magic_ (3rd), _telekinetic charge_
(4th), _contact other plane_ (5th), _find the path_ (6th), _mage's sword_ (7th), _brilliant
inspiration_ (8th), _gate_ (9th).

The Wagon: _expeditious retreat_ (1st), _twisted space_ (2nd), _haste_ (3rd), _mirror transport_
(4th), _teleport_ (5th), _fluid form_ (6th), _walk through space_ (7th), _etherealness_ (8th), _time
stop_ (9th).

The Pack: _calm animals_ (1st), _animal aspect_ (2nd), _rage_ (3rd), _greater animal aspect_ (4th),
_summon monster V_ (5th), _mass bear's endurance_ (6th), _summon monster VII_ (7th), _animal shapes_
(8th), _shapechange_ (9th).

The Mother: _identify_ (1st), _aid_ (2nd), _invisibility purge_ (3rd), _stoneskin_ (4th),
_[spell resistance](ref/rule/spell-resistance)_ (5th), _contingency_ (6th), _mind blank_ (7th),
_refuge_ (8th), _wall of suppression_ (9th).

The Stargazer: _know the enemy_ (1st), _augury_ (2nd), _arcane sight_ (3rd), _locate creature_
(4th), _feeblemind_ (5th), _geas/quest_ (6th), _arcane sight (greater)_ (7th), _moment of
prescience_ (8th), _dream voyage_ (9th).

The Stranger: _disguise self_ (1st), _invisibility_ (2nd), _displacement_ (3rd), _riding possession_
(4th), _prying eyes_ (5th), _veil_ (6th), _project image_ (7th), _maze_ (8th), _divide mind_ (9th).

The Follower: _forced quiet_ (1st), _darkness_ (2nd), _vision of hell_ (3rd), _enervation_ (4th),
_waves of fatigue_ (5th), _shadow walk_ (6th), _simulacrum_ (7th), _destruction_ (8th), _energy
drain_ (9th).

This replaces the bonus spells normally granted by the psychic's discipline and the phrenic
amplifications gained at 1st and 11th levels.

## Major Amplifications {#major-amplifications}

An esoteric starseeker gains this ability at 15th level.
