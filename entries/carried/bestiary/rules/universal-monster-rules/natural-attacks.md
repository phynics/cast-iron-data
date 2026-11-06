+++
id = "ref/carried/bestiary/rules/universal-monster-rules/natural-attacks"
kind = "rule"
title = "Natural Attacks"
source_ids = ["bestiary"]
section = ["Rules", "Universal Monster Rules"]
parent = "ref/carried/bestiary/rules/universal-monster-rules"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Rules/Universal Monster Rules/Natural Attacks", path = "bestiary/rules/universal_monster_rules.json" },
]

[fields]
kind = "none"
+++

Most creatures possess one or more natural attacks (attacks made without a weapon). These attacks
fall into one of two categories, primary and secondary attacks. Primary attacks are made using the
creature's full base attack bonus and add the creature's full Strength bonus on damage rolls.
Secondary attacks are made using the creature's base attack bonus –5 and add only 1/2 the creature's
Strength bonus on damage rolls. If a creature has only one natural attack, it is always made using
the creature's full base attack bonus and adds 1-1/2 times the creature's Strength bonus on damage
rolls. This increase does not apply if the creature has multiple attacks but only takes one. If a
creature has only one type of attack, but has multiple attacks per round, that attack is treated as
a primary attack, regardless of its type. Table: Natural Attacks by Size lists some of the most
common types of natural attacks and their classifications.

Some creatures treat one or more of their attacks differently, such as dragons, which always receive
1-1/2 times their Strength bonus on damage rolls with their bite attack. These exceptions are noted
in the creature's description.

Creatures with natural attacks and attacks made with weapons can use both as part of a full attack
action (although often a creature must forgo one natural attack for each weapon clutched in that
limb, be it a claw, tentacle, or slam). Such creatures attack with their weapons normally but treat
all of their available natural attacks as secondary attacks during that attack, regardless of the
attack's original type.

Some creatures do not have natural attacks. These creatures can make unarmed strikes just like
humans do. See the natural attacks by size table for typical damage values for natural attacks by
creature size.

## Table: Natural Attacks by Size {#table-natural-attacks-by-size}

::: table
caption = "Table: Natural Attacks by Size"
head = [
  [
    { text = "Natural Attack", header = true, rowspan = 2 },
    { text = "Base Damage by Size\\*", header = true, colspan = 9 },
    { text = "Damage Type", header = true, rowspan = 2 },
    { text = "Attack Type", header = true, rowspan = 2 },
  ],
  [
    { text = "Fine", header = true },
    { text = "Dim.", header = true },
    { text = "Tiny", header = true },
    { text = "Small", header = true },
    { text = "Medium", header = true },
    { text = "Large", header = true },
    { text = "Huge", header = true },
    { text = "Garg.", header = true },
    { text = "Col.", header = true },
  ],
]
body = [
  [
    { text = "Bite" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "4d6" },
    { text = "B/S/P" },
    { text = "Primary" },
  ],
  [
    { text = "Claw" },
    { text = "—" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "B/S" },
    { text = "Primary" },
  ],
  [
    { text = "Gore" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "4d6" },
    { text = "P" },
    { text = "Primary" },
  ],
  [
    { text = "Hoof, Tentacle, Wing" },
    { text = "—" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "B" },
    { text = "Secondary" },
  ],
  [
    { text = "Pincers, Tail Slap" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "4d6" },
    { text = "B" },
    { text = "Secondary" },
  ],
  [
    { text = "Slam" },
    { text = "—" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "B" },
    { text = "Primary" },
  ],
  [
    { text = "Sting" },
    { text = "—" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "P" },
    { text = "Primary" },
  ],
  [
    { text = "Talons" },
    { text = "—" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "S" },
    { text = "Primary" },
  ],
  [
    { text = "Other" },
    { text = "—" },
    { text = "1" },
    { text = "1d2" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "2d6" },
    { text = "2d8" },
    { text = "B/S/P" },
    { text = "Secondary" },
  ],
]
foot = [
  [
    { text = "\\* Individual creatures vary from this value as appropriate.", colspan = 12 },
  ],
]
:::

The Damage Type column refers to the sort of damage that the natural attack typically deals:
bludgeoning (B), slashing (S), or piercing (P). Some attacks deal damage of more than one type,
depending on the creature. In such cases all the damage is considered to be of all listed types for
the purpose of overcoming [damage reduction](ref/rule/damage-reduction).

Some fey, humanoids, monstrous humanoids, and outsiders do not possess natural attacks. These
creatures can make unarmed strikes, but treat them as weapons for the purpose of determining attack
bonuses, and they must use the two-weapon fighting rules when making attacks with both hands. See
Table: Natural Attacks by Size for typical damage values for natural attacks by creature size.

## Format {#format}

bite +5 (1d6+1), 2 claws +5 (1d4+2), 4 tentacles +0 (1d4+1); _Location_: Melee and Ranged.
