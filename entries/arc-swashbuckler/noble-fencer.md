+++
id = "ref/arc-swashbuckler/noble-fencer"
kind = "archetype"
title = "Noble Fencer"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Noble%20Fencer"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "noble_fencer", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "social-panache", level = 1 },
  { anchor = "incredible-aspirations", level = 7 },
  { anchor = "unshakable-presence", level = 11 },
  { anchor = "aristocratic-discipline", level = 2 },
]
trades = [
  { replaces = "Dodging panache deed", feature = "deeds", power = "dodging panache", by = ["social-panache"] },
  { replaces = "Superior feint deed", feature = "deeds", power = "superior feint", by = ["incredible-aspirations"] },
  { replaces = "Subtle blade deed", feature = "deeds", power = "subtle blade", by = ["unshakable-presence"] },
  { replaces = "Charmed life", feature = "charmed-life", by = ["aristocratic-discipline"] },
]
+++

The noble fencer is an aristocrat or other upper-class socialite who trained in dueling from a young
age. Noble fencers fight with their own style, with distinct differences from those of alley bravos
or gladiatorial duelists. They use their quick wits and panache in both physical and social
confrontations, and they rely on their training and discipline to emerge victorious, rather than
merely trusting to luck.

## Deeds {#deeds}

A noble fencer gains the following deeds.

## Social Panache (Ex) {#social-panache}

At 1st level, a noble fencer can spend 1 panache point when he attempts a Bluff, Diplomacy,
Intimidate, or Sense Motive check to roll 1d6 and add the result to the check. He can do this after
he rolls the check but before the result is revealed. If the result of the d6 roll is a natural 6,
he rolls another 1d6 and adds it to the check. He can continue to do this as long as he rolls
natural 6s, up to a number of times equal to his Charisma modifier (minimum 1).

Just before a [verbal duel](ref/rule/verbal-duels) (see pages 176–181), a noble fencer can spend up
to 4 panache points. For each point he spends, he selects a tactic for which he has chosen Bluff,
Diplomacy, Intimidate, or Sense Motive as an associated skill and gains an edge he can only use with
that tactic.

This deed replaces the dodging panache deed.

## Incredible Aspirations (Ex) {#incredible-aspirations}

At 7th level, a noble fencer strives for truly amazing results when he uses his
[derring-do](ref/swashdeed/derring-do) and social panache deeds. As long as he has 1 panache point,
the first time he rolls a natural 5 on the 1d6 for those deeds, he can roll another 1d6, subject to
the other limitations of the respective deeds. He can still reroll as many rolls of 6 as normal.

This deed replaces the superior feint deed.

## Unshakable Presence (Ex) {#unshakable-presence}

At 11th level, a noble fencer cloaks himself in the combined bravado of a swashbuckler and a noble,
girding himself against anything that attempts to shake his impossible confidence. While he has at
least 1 panache point, he cannot be demoralized by the Intimidate skill.

This ability replaces the subtle blade deed.

## Aristocratic Discipline (Ex) {#aristocratic-discipline}

At 2nd level, a noble fencer relies on his extremely honed training and discipline to protect his
mind, rather than luck. The noble fencer gains a +1 bonus on Will saves against mind-affecting
effects. This bonus increases by 1 at 6th level and every 4 swashbuckler levels thereafter.

This ability replaces charmed life.
