+++
id = "ref/arc-familiar/school-familiar"
kind = "archetype"
title = "School Familiar"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "school_familiar", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "familiar-folio"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "school-link" },
  { anchor = "school-cantrip" },
  { anchor = "specialty-stowaway" },
  { anchor = "lesser-school-power" },
  { anchor = "greater-school-power" },
]
+++

School familiars are tightly bound to the power of their master's chosen school of magic. A school
familiar cannot have any other familiar archetype (see page 10). At the GM's discretion, other
schools of magic (such as elemental arcane schools from _Pathfinder RPG Ultimate Magic_) may have
their own school familiars.

## School Link (Su) {#school-link}

A school familiar can use the share spells and deliver touch spells abilities only with spells of
its master's specialized arcane school.

## School Cantrip (Sp) {#school-cantrip}

A school familiar can cast at will one cantrip selected from its associated arcane school, using its
master's caster level.

## Specialty Stowaway (Sp or Su) {#specialty-stowaway}

A school familiar can use any granted abilities of its master's arcane school that have a limited
number of uses or rounds per day, expending twice the number of uses or rounds as usual.

## Lesser School Power {#lesser-school-power}

A school familiar gains the lesser school power matching its associated arcane school.

## Greater School Power {#greater-school-power}

A school familiar whose master has taken the
[Greater School Familiar](ref/feat/greater-school-familiar) feat gains the indicated greater school
power of its associated arcane school.

## Abjuration {#abjuration}

An abjurer's familiar is an invaluable defensive aid.

### Lesser—Energy Block (Su) {#lesser-energy-block}

Choose an energy type: acid, cold, electricity, fire, or sonic. The familiar gains energy resistance
equal to 1/2 its master's level (minimum 1) to the chosen energy type and can share this resistance
with one ally within 5 feet. As a standard action, the familiar's master can change this energy
type. The familiar is immune to _[magic missile](ref/spell/magic-missile)_ as if protected by
_[shield](ref/spell/shield)_.

### Greater—Disruptive Spirit (Su) {#greater-disruptive-spirit}

Whenever the familiar hits a creature with a natural attack, that creature is subject to a targeted
_[dispel magic](ref/spell/dispel-magic)_ effect at the master's caster level.

This ability can't be used while delivering a touch spell, and can't affect the same creature more
than once in 24 hours.

## Conjuration {#conjuration}

Conjurers' familiars are masters of teleportation that can inhabit the bodies of summoned creatures.

### Lesser—Master's Side (Sp) {#lesser-master-s-side}

The familiar can use _[dimension door](ref/spell/dimension-door)_ to return to its master's side a
number of times per day equal to 3 + its Intelligence modifier (minimum once per day).

### Greater—Summoned Shell (Sp) {#greater-summoned-shell}

Whenever the familiar's master casts a _[summon monster](ref/spell/summon-monster)_ spell, if the
familiar is within the spell's range, it can choose to inhabit the body of one creature summoned by
the spell. While inhabiting the body, the familiar maintains its own Intelligence, Wisdom, and
Charisma scores and its familiar powers, but otherwise gains the statistics and abilities of the
summoned creature. When the spell ends, or the summoned creature's hit points are reduced to 0, the
familiar is expelled without suffering any negative effects.

## Divination {#divination}

A diviner's familiar complements its master's prescience.

### Lesser—Ever Ready (Su) {#lesser-ever-ready}

At the start of combat, the familiar and its master each roll initiative separately, and the master
can choose to trade his initiative result with his familiar's. The familiar gains the benefits of
the [diviner's forewarned](ref/arcaneschool/divination) school power and can always act on the
surprise round.

### Greater—Greater Scry on Familiar (Sp) {#greater-greater-scry-on-familiar}

The master gains the scry on familiar ability (if he doesn't already possess it), and can use it at
will as _[greater scrying](ref/spell/scrying-greater)_.

## Enchantment {#enchantment}

Enchanters' familiars are devious manipulators capable of aiding in charms and compulsions.

### Lesser—Manipulative Abettor (Su) {#lesser-manipulative-abettor}

If the familiar's master casts an enchantment spell while targeting a creature whose square is also
occupied by his familiar, the save DC of the spell is increased by 2.

### Greater—Puppet Master (Su) {#greater-puppet-master}

The familiar can strongly influence a creature through physical contact. Once per day, the familiar
can make a melee touch attack against a creature and force it to make a Will save (DC = 10 + 1/2 the
familiar's Hit Dice + its Charisma modifier) or be affected as if by
_[charm monster](ref/spell/charm-monster)_. The effect lasts for as long as the familiar remains
conscious and within 5 feet of the target (to a maximum of 24 hours). As soon as the effect ends,
the freed victim is forever immune to that familiar's puppet master ability.

## Evocation {#evocation}

Evocation familiars boost and manipulate energy spells.

### Lesser—Energy Boost (Su) {#lesser-energy-boost}

Choose an energy type: acid, cold, electricity, or fire. The familiar gains resistance 10 to the
selected energy type. Whenever an ally casts an evocation spell that has the chosen energy type as a
descriptor while within 5 feet of the familiar, the spell deals bonus energy damage equal to its
spell level.

### Greater—Eldritch Battery (Su) {#greater-eldritch-battery}

The familiar becomes immune to the energy type chosen for its energy boost ability. If the
familiar's master casts an evocation spell that has that energy type as a descriptor, and targets
the familiar or includes it in the spell's area, the familiar can choose to absorb the spell.
Instead of the spell's normal effect, the familiar gains the spell (including any metamagic feats
applied to it) as a [spell-like ability](ref/umr/spell-like-abilities). It can use this ability
once, at [half](ref/misc/fractions-and-rounding) the spell's original caster level. If the halved
caster level is insufficient to cast a spell of that level, the familiar doesn't gain the spell as a
spell-like ability. The effect fades after 1 minute if not used.

## Illusion {#illusion}

Illusion school familiars can control their master's illusions and create impressive illusions of
their own.

### Lesser—Illusory Maestro (Su) {#lesser-illusory-maestro}

As a move action, the familiar's master can transfer control of any illusion spell that requires
concentration to the familiar. The familiar's affinity for illusions also enhances the quality of
the illusion, increasing the illusion's save DC (if any) by 1 for as long as the familiar
concentrates on the spell.

### Greater—Phantom Swarm (Su) {#greater-phantom-swarm}

As a standard action, the familiar can conjure hundreds of illusory duplicates of itself. The
familiar can direct the phantom [swarm](ref/subtype/swarm) as a normal swarm by moving along with
it. The familiar gains a swarm attack that deals 1d6 points of damage with a distraction DC equal to
10 + the familiar's Constitution modifier. Opponents who fail to disbelieve the effect (Will DC =
10 + 1/2 the master's level + the familiar's Charisma modifier) treat the familiar as if it had the
swarm subtype. The familiar takes any damage dealt to the swarm, including extra damage from area
attacks, though it takes only half damage from slashing and piercing weapons. Creatures who
successfully disbelieve the swarm are immune to the swarm's effects and can target the familiar as
an individual creature. Only Tiny or smaller familiars can use this ability. This is an illusion
(shadow) effect.

## Necromancy {#necromancy}

Necromancers' familiars are scions of undeath.

### Lesser—Spirit Warden (Su) {#lesser-spirit-warden}

Whenever the familiar successfully uses aid another to aid an attack, that attack deals full damage
to incorporeal creatures. When encountering a haunt, the familiar always acts on the surprise round,
and can make touch attacks against the haunt that deal 1d6 points of damage per 2 levels its master
possesses.

### Greater—One With the Negative (Su) {#greater-one-with-the-negative}

The familiar is healed by negative energy as if undead. It is immune to energy drain. It's
constantly affected by _[hide from undead](ref/spell/hide-from-undead)_; if it breaks this effect by
attacking, it can activate the effect again as a standard action. Whenever the familiar hits a
living creature with a natural attack, that creature gains 1 negative level. A given creature can
receive a negative level from the familiar only once per day.

## Transmutation {#transmutation}

A transmutation familiar is capable of protecting its master's effects as well as shapeshifting.

### Lesser—Dispel Bait (Su) {#lesser-dispel-bait}

As a standard action, the familiar's master can expend a spell or an open spell slot to imbue the
familiar with the ability to protect his transmutations. Whenever one of the master's transmutations
would be successfully dispelled, if the familiar is within 10 feet of the transmutation effect and
the imbued spell slot is of a level equal to or higher than the transmutation, the familiar can
choose to lose the imbued spell slot to prevent the transmutation effect from being dispelled. The
familiar can be imbued with only one dispel bait effect at a time.

### Greater—Infinite Forms (Su) {#greater-infinite-forms}

Once per day as a standard action, the familiar can transform into any animal familiar (but not an
improved familiar), losing all of its racial abilities and becoming a typical familiar of the chosen
type, including granting a different familiar bonus to its master.
