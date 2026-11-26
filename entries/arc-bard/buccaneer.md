+++
id = "ref/arc-bard/buccaneer"
kind = "archetype"
title = "Buccaneer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Buccaneer"
source_ids = ["pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "buccaneer", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "pirates-of-the-inner-sea"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "hilt-bash", level = 1 },
  { anchor = "song-of-surrender", level = 4 },
  { anchor = "knock-out", level = 5 },
  { anchor = "mass-song-of-surrender", level = 16 },
]
trades = [
  { replaces = "bardic knowledge", feature = "bardic-knowledge", by = ["hilt-bash"] },
  { replaces = "suggestion", feature = "bardic-performance", power = "suggestion", by = ["song-of-surrender"] },
  { replaces = "lore master", feature = "lore-master", by = ["knock-out"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["mass-song-of-surrender"] },
]
+++

A buccaneer is a pirate who specializes in raiding ships and port towns, but who leaves his victims
alive whenever possible. Buccaneers are flashy, debonair pirates who enjoy the excitement and
rewards of piracy, but prefer not to kill; they are welcome on ships whose captains prefer to avoid
the punishments that murder would bring or who lack the heart to strike down civilians in cold
blood. Buccaneers are also popular in privateer crews—and among slave traders.

## Hilt Bash (Ex) {#hilt-bash}

A buccaneer develops the ability to fight with the hilts and flats of his weapons, aiming to leave
his victims alive. He can use a weapon that normally deals lethal damage to deal nonlethal damage
with no penalty on his attack roll. This ability replaces bardic knowledge.

## Song of Surrender (Su) {#song-of-surrender}

A buccaneer of 4th level or higher can use his performance to encourage an enemy to surrender. To be
affected, an enemy must be within 30 feet and be able to see and hear the buccaneer's performance.
An affected enemy feels the irresistible urge to drop any held weapons and fall
[prone](ref/rule/prone). This effect lasts for 1 round—essentially, the affected enemy takes no
actions on its next turn other than to lie prone, although it is not considered
[flat-footed](ref/rule/flat-footed) or [helpless](ref/misc/helpless).

A Will saving throw (DC 10 + 1/2 the buccaneer's level + the buccaneer's Charisma modifier) negates
the effect. This ability affects only a single creature. Song of surrender is an enchantment
(compulsion), mind-affecting, language-dependent ability and relies on audible components. This
ability replaces _suggestion_.

## Knock Out (Ex) {#knock-out}

At 5th level, a buccaneer may focus his blows in an attempt to knock out an opponent. Once per day
as a swift action, the buccaneer can choose one target to attempt to knock out. The buccaneer adds
his Charisma bonus (if any) on his attack roll and adds his buccaneer level on any nonlethal damage
rolls made against the target. The bonus lasts until the buccaneer deals nonlethal damage to his
target or until the buccaneer chooses a new target to attempt to knock out. He can use this ability
one additional time per day for every six levels he possesses beyond 5th, to a maximum of three
times per day at 17th level. This ability replaces lore master.

## Mass Song of Surrender (Su) {#mass-song-of-surrender}

This ability functions just like song of surrender but allows a buccaneer of 16th level or higher to
affect all enemies within 30 feet. Enemies within range of this effect still receive a saving throw.
Mass song of surrender is an enchantment (compulsion), mind-affecting, language-dependent ability
that relies on audible components. This ability replaces _mass suggestion._
