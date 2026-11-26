+++
id = "ref/arc-alchemist/energist"
kind = "archetype"
title = "Energist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Energist"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "planar-adventures"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "energy-focus" },
  { anchor = "energist-bombs" },
  { anchor = "healing-ampoule", level = 2 },
  { anchor = "energist-resistance", level = 2 },
]
trades = [
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["energist-bombs"] },
  { replaces = "Discovery gained at 2nd level", feature = "discovery", levels = [2], by = ["healing-ampoule"] },
  { replaces = "swift poisoning", feature = "swift-poisoning", by = ["healing-ampoule"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["energist-resistance"] },
  { alters = "Extracts", feature = "extracts", by = ["energy-focus"] },
  { alters = "Bombs", feature = "bomb", by = ["energist-bombs"] },
  { alters = "Throw anything", feature = "throw-anything", by = ["healing-ampoule"] },
]
+++

While most alchemists experiment mainly with chemicals and physical materials to create disparate
effects, energists tap into the energy of life or death: positive energy or negative energy.
Energists are more likely than most alchemists to follow strange traditions and to travel the
planes, discussing theories with jyoti, sceaduinars, and undead alike. Energists are often found in
lands with unusual variations between life and death, such as Geb, or Virlych in Ustalav.

The energist is an unusual archetype in that all who choose this specialized path must select one of
two types of energy to focus on—positive energy or negative energy. The mechanics of how this
archetype alters the basic alchemist class abilities function the same regardless of this choice,
but these two schools of thought are diametrically opposed in every way. Just as positive energy and
negative energy react violently when mixing together, energists of opposing themes traditionally
interact violently. Although most who choose positive energy tend to be of good alignment and those
who focus on negative energy gravitate toward evil, there is no underlying ethical or moral
restriction for an energist to adhere to. Positive energy can be used for evil purposes, and
negative energy to pursue good goals. But even then, energists whose alignments and philosophies
otherwise would seem to match find themselves at odds if their chosen energies oppose the other.

To energists, the curious and frustrating nature of their oppositional energy is a constant thorn in
the side of their intellects—an ever-present reminder that by choosing to specialize in one, they
have forsaken potential discoveries in the other.

## Energy Focus {#energy-focus}

An energist chooses whether to pursue the path of positive energy or the path of negative energy.
Once selected, this choice can't be changed. If he chooses negative energy, he adds
_[harm](ref/spell/harm)_ as a 6th-level formula and the inflict spells to his alchemist formulae
list and removes _[heal](ref/spell/heal)_ and the cure spells.

This alters extracts.

## Energist Bombs (Su) {#energist-bombs}

An energist's bombs deal damage based on the energy he chose at 1st level. If he chose positive
energy, his bombs damage undead creatures, dealing an amount of positive energy damage equal to his
normal bomb damage. If he chose negative energy, his bombs damage the living, dealing 1d4 points of
negative energy damage plus 1d4 additional points at every odd-numbered alchemist level beyond 1st
(instead of 1d6). He can't apply discoveries with an asterisk (\*) to his bombs. When an energist
reaches 10th level, undead damaged by his positive energy bombs must succeed at a Will save or flee
for 1 round as if affected by the [Turn Undead](ref/feat/turn-undead) feat, while living creatures
damaged by an energist's negative energy bombs must succeed at a Fortitude save or be
[sickened](ref/misc/sickened) for 1 round. An energist's bombs don't heal creatures normally healed
by the energist's chosen energy type.

This alters bombs and replaces poison immunity.

## Healing Ampoule (Su) {#healing-ampoule}

At 2nd level, as a standard action, an energist can create and throw a healing ampoule of the same
energy type as his bombs up to 30 feet, using two of his daily uses of bombs. A living creature
subject to a direct hit by a healing ampoule of positive energy regains 1d4 hit points plus an
additional 1d4 hit points for every even-numbered alchemist level an energist has beyond 2nd, while
a direct hit by a negative energy healing ampoule instead restores an equivalent number of hit
points to an undead target.

In either case, the energist adds his Intelligence modifier to the number of hit points healed, as
if the ampoule were a [splash weapon](ref/rule/throw-splash-weapon) benefiting from his throw
anything ability. A healing ampoule has no splash effect on adjacent targets unless it misses the
target; if it misses, determine where it lands as if it were a splash weapon. Healing ampoules don't
damage creatures normally damaged by the energist's chosen energy type.

This alters throw anything and replaces the discovery gained at 2nd level and swift poisoning.

## Energist Resistance (Su) {#energist-resistance}

At 2nd level, an energist gains energy resistance equal to his alchemist level to positive or
negative energy, whichever would naturally harm him. When on a positive-dominant plane such as the
[Positive Energy Plane](ref/rule/positive-energy-plane), he can apply this resistance to offset the
plane's [fast healing](ref/umr/fast-healing).

This replaces poison resistance.
