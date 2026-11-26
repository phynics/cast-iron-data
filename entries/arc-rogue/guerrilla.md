+++
id = "ref/arc-rogue/guerrilla"
kind = "archetype"
title = "Guerrilla"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Guerrilla"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guerrilla", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "41"

[fields]
kind = "archetype"
features = [
  { anchor = "skilled-liar", level = 1 },
  { anchor = "cover-of-night", level = 2 },
  { anchor = "secret-messenger", level = 3 },
  { anchor = "guerrilla-sniping", level = 4 },
  { anchor = "uncanny-dodge", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["skilled-liar"] },
  { replaces = "Evasion", feature = "evasion", by = ["cover-of-night"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["secret-messenger"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["guerrilla-sniping"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["uncanny-dodge"] },
]
+++

Guerrillas fight against oppressive leadership and governments—often under cover of night—including
Chelish colonization in Sargava and the power structures in Cheliax proper, Nidal, and Razmiran. Any
rogue (including the rogue from _Pathfinder Unchained_) can select the guerrilla archetype.

## Skilled Liar (Ex) {#skilled-liar}

Whenever a guerrilla uses Bluff to attempt to deceive someone, she gains a bonus on the opposed roll
equal to 1/2 her rogue level (minimum +1). A guerrilla can still use Disable Device to disarm magic
traps.

This ability replaces trapfinding.

## Cover of Night (Ex) {#cover-of-night}

At 2nd level, a guerrilla learns to use darkness to her advantage. She gains a +5 bonus on Disguise,
Sleight of Hand, and Stealth checks while she is in areas of [dim light](ref/rule/vision-and-light)
or darkness, and can create mundane disguises in dim light or darkness with a full-round action
(instead of the normal 1d3 × 10 minutes). Additionally, while in dim light or darkness, if a
guerrilla would have [concealment](ref/rule/concealment), she instead has total concealment.

This ability replaces evasion.

## Secret Messenger (Ex) {#secret-messenger}

At 3rd level, a guerrilla gains a +1 bonus on Bluff checks to convey secret messages and on Sense
Motive checks to discern secret messages. These bonuses increase by 1 every 3 rogue levels
thereafter (to a maximum of +6 at 18th level).

This ability replaces trap sense.

## Guerrilla Sniping (Ex) {#guerrilla-sniping}

At 4th level, when a guerrilla is in an area of dim light or darkness, she takes only a -10 penalty
on her Stealth check to maintain her obscured location while sniping.

This ability replaces uncanny dodge.

## Uncanny Dodge (Ex) {#uncanny-dodge}

At 8th level, a guerrilla gains [uncanny dodge](ref/ability/uncanny-dodge).

This ability replaces improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the guerrilla archetype: camouflage, fast stealth, powerful
sneak, rogue crawl, stand up, and surprise attack.

## Advanced Rogue Talents {#advanced-rogue-talents}

The following advanced rogue talents complement the guerrilla archetype: deadly sneak, master of
disguise, stealthy sniper, and opportunist.
