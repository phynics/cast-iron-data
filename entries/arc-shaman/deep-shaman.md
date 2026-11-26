+++
id = "ref/arc-shaman/deep-shaman"
kind = "archetype"
title = "Deep Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Deep%20Shaman"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_shaman", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "aquatic-adventures"
page = "51"

[fields]
kind = "archetype"
features = [
  { anchor = "deep-spirit", level = 1 },
  { anchor = "aquatic-hexes" },
  { anchor = "buoyancy-control" },
  { anchor = "deep-heart" },
  { anchor = "aquatic-spirit-abilities" },
  { anchor = "brine-dragon-form" },
]
trades = [
  { replaces = "Elemental form of the true spirit ability", by = ["brine-dragon-form"] },
  { alters = "Spirit", feature = "spirit", by = ["deep-spirit", "aquatic-spirit-abilities"] },
  { alters = "spirit animal", feature = "spirit-animal", by = ["deep-spirit"] },
  { alters = "Hexes", feature = "hex", by = ["aquatic-hexes"] },
  { alters = "Spirit ability", by = ["deep-spirit", "aquatic-spirit-abilities"] },
  { alters = "greater spirit ability", by = ["aquatic-spirit-abilities"] },
  { alters = "Class skills", by = ["deep-spirit"] },
]
+++

While most shamans of the _waves_ spirit have powers associated with surface waters, deep shamans
are tied to spirits from the depths. Some say that the first deep shamans served
[Besmara](ref/faith/besmara) back when she was a water spirit, before she achieved full godhood.

## Deep Spirit {#deep-spirit}

A deep shaman must choose the [waves](ref/shamanspirit/waves) spirit. The deep shaman must choose a
spirit animal with the [aquatic](ref/subtype/aquatic) subtype, and it gains the
[amphibious](ref/umr/amphibious) special quality instead of gaining the ability to breathe in water.
A deep shaman gains Swim as a class skill.

This alters spirit, spirit animal, and the shaman's class skills.

## Aquatic Hexes (Su) {#aquatic-hexes}

When a deep shaman uses beckoning chill on a creature in the water, that creature becomes
[fatigued](ref/misc/fatigued) due to hypothermia for the duration, and it also becomes
[entangled](ref/rule/entangled) if the creature takes damage from the deep shaman's spirit abilities
and from spells and abilities with the water descriptor. Her crashing waves hex applies to her
spirit abilities that deal damage as if they were spells with the water descriptor, raising her
effective shaman level for those abilities. Instead of mist's shroud and watersight, she can select
the two hexes below.

This alters hexes.

## Buoyancy Control (Sp) {#buoyancy-control}

The deep shaman touches a willing creature and changes its [buoyancy](ref/rule/buoyancy) (see page
43) to whichever of the five states she wishes for 1 minute. A creature affected by this hex can't
be affected by it again for 24 hours. The deep shaman has neutral buoyancy, regardless of what her
normal buoyancy would be, though she can end or resume the effect as a standard action.

## Deep Heart (Su) {#deep-heart}

The deep shaman gains the ability to breathe underwater and gains a swim speed equal to her
unmodified base land speed. At 8th level, she takes only half the normal amount of
[pressure damage](ref/rule/water-dangers) and she
[adjusts to a new pressure](ref/rule/oceanic-zones) all at once after succeeding at five Fortitude
saves, rather than 100 feet at a time (see Pressure on page 48).

## Aquatic Spirit Abilities (Su) {#aquatic-spirit-abilities}

When used underwater, a deep shaman's wave strike deals lethal bludgeoning damage and pushes the
target away 5 feet + an additional 5 feet for every 6 shaman levels she has. At 11th level, whenever
the deep shaman is underwater, all weapons she holds are treated as if they had the
_[impact](ref/magic-enh/impact)_ special ability instead of _[quenching](ref/magic-enh/quenching)_.
Instead of a swim speed and the ability to breathe underwater, fluid mastery provides
[tremorsense](ref/umr/tremorsense) with a range of 30 feet while in the water, and when underwater,
fluid mastery's torrent deals 1d6 points of damage per shaman level in a 30-foot cone. This alters
spirit ability and greater spirit ability.

## Brine Dragon Form (Su) {#brine-dragon-form}

When a deep shaman gains access to the true version of the waves spirit, she can assume the form of
a Large (or smaller) [brine dragon](ref/family/dragon-primal-brine) as per
_[form of the dragon II](ref/spell/form-of-the-dragon-2)_, with a line of acid breath weapon, acid
resistance 20, and a swim speed of 60 feet. She can use this ability for 1 hour per shaman level
each day, divided any way she chooses in 1 hour increments, though the spell's breath weapon limit
applies across the whole day. Time she spends underwater doesn't count against this limit, but every
minute (or fraction thereof) that she spends flying expends 1 hour of her daily uses. At 18th level,
she can assume the form of a Huge or smaller brine dragon as per
_[form of the dragon III](ref/spell/form-of-the-dragon-3)_ instead.

This ability replaces the elemental form of the true spirit ability.
