+++
id = "ref/arc-summoner/unwavering-conduit"
kind = "archetype"
title = "Unwavering Conduit"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Unwavering%20Conduit"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unwavering_conduit", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "eidolon-of-law", level = 1 },
  { anchor = "unwavering-monsters" },
  { anchor = "law-magic" },
]
trades = [
  { alters = "Eidolon", feature = "eidolon", by = ["eidolon-of-law"] },
  { alters = "Summon monster", feature = "summon-monster-i", by = ["unwavering-monsters"] },
  { alters = "Spells known", feature = "sec-spells-known", by = ["law-magic"] },
]
+++

Unwavering conduits work to keep everything ordered and regimented, drawing on power from the
Eternal City of Axis, Heaven, or Hell to enforce whichever laws the summoner finds paramount. Lawful
good unwavering conduits often work with Riftwardens to protect the integrity of the Great Beyond,
while lawful evil unwavering conduits are commonly diabolists in Cheliax.

## Alignment {#alignment}

Any lawful.

## Eidolon of Law {#eidolon-of-law}

An unwavering conduit's eidolon must be of a lawful alignment (if using the summoner from
_Pathfinder Unchained_, the eidolon must be of the archon, devil, or inevitable subtype). Once
selected, the evolutions of the unwavering conduit's eidolon cannot be changed when a new class
level is gained (though they can be altered normally with the
_[transmogrify](ref/spell/transmogrify)_ spell; see _Pathfinder RPG Advanced Player's Guide_ 250).
At least half the eidolon's skill points must be spent on skills in which the unwavering conduit
also has ranks. The eidolon gains a +1 resistance bonus on saving throws against spells and
abilities of the conjuration, enchantment, and transmutation schools. This bonus increases to +2 at
3rd level, and by an additional 1 for every 3 levels thereafter. The eidolon has 1 fewer evolution
point than normal for an eidolon of the unwavering conduit's summoner level. This ability alters
eidolon.

## Unwavering Monsters {#unwavering-monsters}

Since an unwavering conduit's power is drawn from planar energies aligned with law, all the
creatures he summons must be of a lawful alignment. If a creature would normally be celestial or
fiendish, it is instead a [resolute creature](ref/template/resolute).

This also causes the unwavering conduit's summoning power to be more set than a standard summoner's.
Beginning at 3rd level, each time he uses _[summon monster](ref/spell/summon-monster)_ to summon
multiple monsters, rather than rolling a die to see how many creatures he summons, he receives a
specific number (two creatures for 1d3, or four creatures for 1d4+1). If an item, spell, or ability
would increase the number of creatures summoned, the set number increases by that amount.

Also, starting at 2nd level, creatures summoned by the unwavering conduit receive a +1 resistance
bonus on saving throws against spells and abilities of the conjuration, enchantment, and
transmutation schools. This bonus increases to +2 at 6th level, and by an additional 1 every 4 class
levels thereafter.

This ability alters _summon monster_.

## Law Magic {#law-magic}

The unwavering conduit gains the following bonus spells known at the listed spell level:
1st—_protection from chaos_, 2nd—_arrow of law_, 3rd—_magic circle against chaos_, 4th—_order's
wrath_, 5th—_dispel chaos_, 6th—_dictum_. The unwavering conduit gains one fewer spell known per
spell level for spell levels 1–6. This ability alters the summoner's spells known.
