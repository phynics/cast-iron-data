+++
id = "ref/arc-shaman/serendipity-shaman"
kind = "archetype"
title = "Serendipity Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Serendipity%20Shaman"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "serendipity_shaman", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "luck-magic" },
  { anchor = "channel-luck" },
  { anchor = "fortune" },
  { anchor = "misfortune" },
  { anchor = "spirit-magic" },
  { anchor = "tweak-the-odds" },
]
trades = [
  { alters = "Spirit", feature = "spirit", by = ["luck-magic"] },
]
+++

Although some [catfolk](ref/race/catfolk) venerate elven and human deities, the traditional worship
of the so-called "spirits of creation" is by far the most prevalent religion among their kind,
especially in the catfolk nation of Murraseth. The serendipitous, shamanistic rites associated with
this faith focus upon attracting good fortune and banishing ill fortune in the name of these
spirits. Although the ancient practices of the serendipity shaman were once exclusive to the
mysterious catfolk nation, the catfolk's curiosity and willingness to travel have spread them across
Golarion, where today many with a tendency toward good fortune embrace the faith.

## Limited Calling {#limited-calling}

A shaman must have a racial trait with "luck" in its name to select this archetype, such as cat's
luck or halfling luck. A character with the Defiant Luck feat also qualifies for this archetype.

## Luck Magic {#luck-magic}

A serendipity shaman adds the domain spells from the [Luck](ref/domain/luck) cleric domain to the
list of spells she can cast with the spirit magic ability instead of her spirit's spirit magic
spells.

This ability alters spirit.

## Luck Hexes {#luck-hexes}

A serendipity shaman can select from any of the following hexes, in addition to general shaman hexes
and the hexes granted by her spirit. When she gains the wandering spirit class feature, she can
select one of these hexes in place of a wandering hex.

## Channel Luck (Su) {#channel-luck}

A serendipity shaman gains the ability to channel luck, as the cleric
[variant channeling](ref/ability/variant-channeling) ability of the same name, using her shaman
level to determine her effective cleric level for the purpose of her
[channel energy](ref/ability/channel-energy) ability. She does not count as having the channel
energy ability for the purpose of meeting feat prerequisites or prestige class requirements with the
exception of [Selective Channeling](ref/feat/selective-channeling), which the shaman can take as
normal. A shaman must be at least 8th level before selecting this hex.

## Fortune (Ex) {#fortune}

This hex functions as the dual-cursed oracle revelation of the same name (_Ultimate Magic_ 58),
using the shaman's class level as her effective oracle level.

### Fortune (Ultimate Magic page 58) {#fortune-ultimate-magic}

At 5th level, as an immediate action, you can reroll any one d20 roll that you have just made before
the results of the roll are revealed. You must take the result of the reroll, even if it's worse
than the original roll. You can use this ability once per day at 5th level, and one additional time
per day for every six oracle levels beyond 5th.

## Misfortune (Ex) {#misfortune}

As a standard action, a serendipity shaman can afflict one target within 30 feet with misfortune,
causing it to take a -2 penalty on all saving throws against the shaman's spells. The effect lasts
for 1 minute or until the target hits the shaman with an attack.

## Spirit Magic {#spirit-magic}

A serendipity shaman adds both her spirit's spirit magic spells and the domain spells from the Luck
cleric domain to the list of spells she can cast with the spirit magic ability. This hex cannot be
taken as a wandering hex.

## Tweak the Odds (Su) {#tweak-the-odds}

Whenever the serendipity shaman or one of her allies within 30 feet rolls an ability check, attack
roll, saving throw, or skill check, the shaman can use this ability as an immediate action to tweak
the odds in her favor, increasing the result of the die roll or check by 1. This can turn a normal
hit into a critical threat, but it cannot make an attack roll an automatic hit (this bonus does not
stack with effects that increase a weapon's critical threat range, such as
[Improved Critical](ref/feat/improved-critical) or _keen edge_).

The shaman can use this ability a number of times per day equal to her shaman level. At 4th level
and every 4 shaman levels thereafter, she can spend an additional use of this ability to further
increase the die result of the target's roll by an additional 1.

For example, a 12th-level shaman can spend up to three uses of this ability to increase an ally's
roll by 1 per use expended.
