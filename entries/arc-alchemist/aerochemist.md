+++
id = "ref/arc-alchemist/aerochemist"
kind = "archetype"
title = "Aerochemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Aerochemist"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aerochemist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "aeromantic-concoction", level = 1 },
  { anchor = "bombs-away", level = 2 },
  { anchor = "aerodynamic-prowess", level = 2 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["aeromantic-concoction"] },
  { replaces = "swift poisoning", feature = "swift-poisoning", by = ["aeromantic-concoction"] },
  { replaces = "persistent mutagen", feature = "persistent-mutagen", by = ["aeromantic-concoction"] },
  { replaces = "Poison use", feature = "poison-use", by = ["bombs-away"] },
  { replaces = "swift alchemy", feature = "swift-alchemy", by = ["bombs-away"] },
  { replaces = "Poison resistance", feature = "poison-resistance", by = ["aerodynamic-prowess"] },
]
+++

Although the specifics of the Aeromantic Infadibulum are lost to time, aerochemists are able to
emulate and replicate aspects of this lost magic. Aerochemists use scraps of Shory's magic in their
concoctions to gain personal powers of flight.

## Aeromantic Concoction (Su) {#aeromantic-concoction}

An aerochemist learns to craft a special alchemical concoction. It takes 10 minutes to brew a dose
of this concoction, and once brewed, it remains potent until used. An aerochemist can maintain only
1 dose of this concoction at a time—if he brews a second dose, any existing concoction becomes
inert. As with an extract or bomb, an aeromantic concoction that is not in the aerochemist's
possession becomes inert until he picks it up again. Anyone other than the aerochemist who attempts
to drink his aeromantic concoction is affected in the same fashion as is a non-alchemist who drinks
an alchemist's mutagen.

When consumed, an aerochemist's aeromantic concoction makes his body become incredibly buoyant for
10 minutes per alchemist level. The concoction grants the aerochemist a +5 bonus on Acrobatics
checks to attempt high jumps or long jumps, and he is always treated as having a running start when
attempting long jumps. In addition, the aerochemist gains the benefits of
_[feather fall](ref/spell/feather-fall)_ for the concoction's duration. At 6th level, the
aerochemist gains the benefits of _[fly](ref/spell/fly)_ for the concoction's duration. At 10th
level, the aerochemist can choose to gain the benefits of _[air walk](ref/spell/air-walk)_ instead
of _[fly](ref/spell/fly)_ for the concoction's duration. At 14th level, the duration of the
concoction increases to 1 hour per alchemist level.

An aerochemist with the [infusion](ref/discovery/infusion) discovery can instead create a shared
alchemical concoction intended for his allies. This shared concoction grants the same benefits as
the normal aeromantic concoction, except the duration is only 1 minute per alchemist level its
creator has. At 14th level, the duration increases to 10 minutes per alchemist level. An aerochemist
can have only a standard concoction or shared concoction in effect, not both.

This replaces mutagen, swift poisoning, and persistent mutagen. An aeromantic alchemist can never
gain the mutagen, cognatogen, or inspired cognatogen ability, even from a discovery or another
class.

## Bombs Away (Ex) {#bombs-away}

At 2nd level, an aerochemist becomes an expert at attacking from above. He gains a +1 bonus on
attack rolls made with thrown weapons against targets that are at least 10 feet below him. This
bonus increases to +2 at 6th level, and increases by an additional 1 every 4 levels thereafter, to a
maximum bonus of +5 at 18th level.

This replaces poison use and swift alchemy.

## Aerodynamic Prowess (Su) {#aerodynamic-prowess}

At 2nd level, an aerochemist gains a +2 bonus on Fly checks. This bonus increases to +4 at 5th
level, and +6 at 8th level.

This replaces poison resistance.
