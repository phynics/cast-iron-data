+++
id = "ref/carried/bestiary/rules/monster-creation/building-the-monster"
kind = "rule"
title = "Building the Monster"
source_ids = ["bestiary"]
section = ["Rules", "Monster Creation"]
parent = "ref/rule/monster-creation"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Rules/Monster Creation/Building the Monster", path = "bestiary/rules/monster_creation.json" },
]

[fields]
kind = "none"
+++

The following guidelines are provided to assist in monster creation and to help balance a creation
for its CR.

## Step 1: Concept {#step-1-concept}

The first step in creating a new monster is to define its concept and role in the game. Generally,
this involves picking the monster's CR, type, physical appearance, and manner of fighting. Once you
have these basic pieces of information, you should find a number of similar monsters of the same
type and roughly the same CR for comparison purposes.

### Table: Monster Statistics by CR {#table-monster-statistics-by-cr}

::: table
caption = "Table: Monster Statistics by CR"
head = [
  [
    { text = "CR", header = true, rowspan = 2 },
    { text = "Hit Points", header = true, rowspan = 2 },
    { text = "Armor Class", header = true, rowspan = 2 },
    { text = "High Attack", header = true, rowspan = 2 },
    { text = "Low Attack", header = true, rowspan = 2 },
    { text = "Average Damage", header = true, colspan = 2 },
    { text = "Primary Ability DC", header = true, rowspan = 2 },
    { text = "Secondary Ability DC", header = true, rowspan = 2 },
    { text = "Good Save", header = true, rowspan = 2 },
    { text = "Poor Save", header = true, rowspan = 2 },
  ],
  [
    { text = "High", header = true },
    { text = "Low", header = true },
  ],
]
body = [
  [
    { text = "1/2" },
    { text = "10" },
    { text = "11" },
    { text = "1" },
    { text = "0" },
    { text = "4" },
    { text = "3" },
    { text = "11" },
    { text = "8" },
    { text = "3" },
    { text = "0" },
  ],
  [
    { text = "1" },
    { text = "15" },
    { text = "12" },
    { text = "2" },
    { text = "1" },
    { text = "7" },
    { text = "5" },
    { text = "12" },
    { text = "9" },
    { text = "4" },
    { text = "1" },
  ],
  [
    { text = "2" },
    { text = "20" },
    { text = "14" },
    { text = "4" },
    { text = "3" },
    { text = "10" },
    { text = "7" },
    { text = "13" },
    { text = "9" },
    { text = "5" },
    { text = "1" },
  ],
  [
    { text = "3" },
    { text = "30" },
    { text = "15" },
    { text = "6" },
    { text = "4" },
    { text = "13" },
    { text = "9" },
    { text = "14" },
    { text = "10" },
    { text = "6" },
    { text = "2" },
  ],
  [
    { text = "4" },
    { text = "40" },
    { text = "17" },
    { text = "8" },
    { text = "6" },
    { text = "16" },
    { text = "12" },
    { text = "15" },
    { text = "10" },
    { text = "7" },
    { text = "3" },
  ],
  [
    { text = "5" },
    { text = "55" },
    { text = "18" },
    { text = "10" },
    { text = "7" },
    { text = "20" },
    { text = "15" },
    { text = "15" },
    { text = "11" },
    { text = "8" },
    { text = "4" },
  ],
  [
    { text = "6" },
    { text = "70" },
    { text = "19" },
    { text = "12" },
    { text = "8" },
    { text = "25" },
    { text = "18" },
    { text = "16" },
    { text = "11" },
    { text = "9" },
    { text = "5" },
  ],
  [
    { text = "7" },
    { text = "85" },
    { text = "20" },
    { text = "13" },
    { text = "10" },
    { text = "30" },
    { text = "22" },
    { text = "17" },
    { text = "12" },
    { text = "10" },
    { text = "6" },
  ],
  [
    { text = "8" },
    { text = "100" },
    { text = "21" },
    { text = "15" },
    { text = "11" },
    { text = "35" },
    { text = "26" },
    { text = "18" },
    { text = "12" },
    { text = "11" },
    { text = "7" },
  ],
  [
    { text = "9" },
    { text = "115" },
    { text = "23" },
    { text = "17" },
    { text = "12" },
    { text = "40" },
    { text = "30" },
    { text = "18" },
    { text = "13" },
    { text = "12" },
    { text = "8" },
  ],
  [
    { text = "10" },
    { text = "130" },
    { text = "24" },
    { text = "18" },
    { text = "13" },
    { text = "45" },
    { text = "33" },
    { text = "19" },
    { text = "13" },
    { text = "13" },
    { text = "9" },
  ],
  [
    { text = "11" },
    { text = "145" },
    { text = "25" },
    { text = "19" },
    { text = "14" },
    { text = "50" },
    { text = "37" },
    { text = "20" },
    { text = "14" },
    { text = "14" },
    { text = "10" },
  ],
  [
    { text = "12" },
    { text = "160" },
    { text = "27" },
    { text = "21" },
    { text = "15" },
    { text = "55" },
    { text = "41" },
    { text = "21" },
    { text = "15" },
    { text = "15" },
    { text = "11" },
  ],
  [
    { text = "13" },
    { text = "180" },
    { text = "28" },
    { text = "22" },
    { text = "16" },
    { text = "60" },
    { text = "45" },
    { text = "21" },
    { text = "15" },
    { text = "16" },
    { text = "12" },
  ],
  [
    { text = "14" },
    { text = "200" },
    { text = "29" },
    { text = "23" },
    { text = "17" },
    { text = "65" },
    { text = "48" },
    { text = "22" },
    { text = "16" },
    { text = "17" },
    { text = "12" },
  ],
  [
    { text = "15" },
    { text = "220" },
    { text = "30" },
    { text = "24" },
    { text = "18" },
    { text = "70" },
    { text = "52" },
    { text = "23" },
    { text = "16" },
    { text = "18" },
    { text = "13" },
  ],
  [
    { text = "16" },
    { text = "240" },
    { text = "31" },
    { text = "26" },
    { text = "19" },
    { text = "80" },
    { text = "60" },
    { text = "24" },
    { text = "17" },
    { text = "19" },
    { text = "14" },
  ],
  [
    { text = "17" },
    { text = "270" },
    { text = "32" },
    { text = "27" },
    { text = "20" },
    { text = "90" },
    { text = "67" },
    { text = "24" },
    { text = "18" },
    { text = "20" },
    { text = "15" },
  ],
  [
    { text = "18" },
    { text = "300" },
    { text = "33" },
    { text = "28" },
    { text = "21" },
    { text = "100" },
    { text = "75" },
    { text = "25" },
    { text = "18" },
    { text = "20" },
    { text = "16" },
  ],
  [
    { text = "19" },
    { text = "330" },
    { text = "34" },
    { text = "29" },
    { text = "22" },
    { text = "110" },
    { text = "82" },
    { text = "26" },
    { text = "19" },
    { text = "21" },
    { text = "16" },
  ],
  [
    { text = "20" },
    { text = "370" },
    { text = "36" },
    { text = "30" },
    { text = "23" },
    { text = "120" },
    { text = "90" },
    { text = "27" },
    { text = "20" },
    { text = "22" },
    { text = "17" },
  ],
]
:::

## Step 2: Target Statistics {#step-2-target-statistics}

Once you have a creature's type and CR determined, use Table: Monster Statistics by CR to determine
its approximate statistics by CR. These values are a rough guideline only. You will notice that many
of the existing monsters in this book do not follow these guidelines exactly. Most monsters excel in
one of these areas, usually in the amount of damage dealt, but lag in one or two other areas to help
balance them out. When referring to Table: Monster Statistics by CR, keep the following points in
mind.

### CR {#cr}

This is the approximate CR of the monster. This number might change as design progresses.

### Hit Points {#hit-points}

This is the approximate hit point total for the monster. Note that creatures with particularly high
Armor Classes or saving throws, or a number of resistances, might have a lower number. Outsiders and
constructs typically have lower hit point totals.

### Armor Class {#armor-class}

This is the average Armor Class for a creature of this CR. When it comes time to design the
creature's protections, keep this number in mind. Creatures with hit points above the average often
have lower Armor Class values to compensate.

### High Attack {#high-attack}

This is the average total attack bonus for a creature of this CR. This value is for creatures that
are primarily melee or ranged combatants. Creatures with a higher than normal average damage
typically have a lower attack value to compensate.

### Low Attack {#low-attack}

This is the average total attack bonus for a creature of this CR that does not rely upon melee or
ranged attacks to deal damage. This includes most creatures that rely on spells and
[spell-like abilities](ref/umr/spell-like-abilities) in combat.

### Average Damage {#average-damage}

This is the average amount of damage dealt by a creature of this CR if all of its attacks are
successful. To determine a creature's average damage, add the average value for all of the damage
dice rolled (as determined by Table: Average Die Results) to the damage modifier for each attack.

A creature that relies on melee or ranged weapons in combat should have average damage within the
range of high and low damage.

A creature with higher than normal attack bonuses will often deal lower damage, while a creature
with lower than normal attack bonuses will often deal higher damage.

### Primary Ability DC {#primary-ability-dc}

This is the average difficulty class (DC) for any spells,
[spell-like abilities](ref/umr/spell-like-abilities), and special abilities (such as breath weapons)
possessed by a creature of this CR that relies on such attacks in combat. If an ability is
particularly powerful, it might have a lower DC to compensate.

### Secondary Ability DC {#secondary-ability-dc}

This is the average DC for spells and special abilities for a creature that does not rely on such
attacks in combat. Generally, a DC should not be lower than this number.

### Good Save {#good-save}

This is the average saving throw bonus for a creature of this CR if the saving throw is one of the
creature's good saving throws.

### Poor Save {#poor-save}

This is the average saving throw bonus for a creature of this CR if the saving throw is one of the
creature's poor saving throws.

#### Table: Average Die Results {#table-average-die-results}

::: table
caption = "Table: Average Die Results"
head = [
  [
    { text = "Die Type", header = true },
    { text = "Average Result\\*", header = true },
  ],
]
body = [
  [
    { text = "d4" },
    { text = "2.5" },
  ],
  [
    { text = "d6" },
    { text = "3.5" },
  ],
  [
    { text = "d8" },
    { text = "4.5" },
  ],
  [
    { text = "d10" },
    { text = "5.5" },
  ],
  [
    { text = "d12" },
    { text = "6.5" },
  ],
  [
    { text = "d20" },
    { text = "10.5" },
  ],
]
foot = [
  [
    { text = "\\*Always round down after multiplying. For example, treat the average of 1d4 as 2, and the average of 2d4 as 5.", colspan = 2 },
  ],
]
:::

## Step 3: Hit Dice {#step-3-hit-dice}

The next step in creating a monster is to determine the approximate number of Hit Dice it has. Hit
Dice determine a wide variety of other statistics, including the creature's feats, skills, hit
points, attack bonuses, and special ability DCs.

A creature's total number of Hit Dice depends on a number of factors, but the two most important are
its CR and its type. Table: Creature Hit Dice lists the average number of Hit Dice for each creature
type, depending on its CR. While many of the monsters in this book are close to these values, some
are not. This is because they have higher or lower average hit points to balance out their Armor
Class or resistances.

### Table: Creature Hit Dice {#table-creature-hit-dice}

::: table
caption = "Table: Creature Hit Dice"
head = [
  [
    { text = "Creature Type", header = true, rowspan = 2 },
    { text = "Challenge Rating", header = true, colspan = 21 },
  ],
  [
    { text = "1/2", header = true },
    { text = "1", header = true },
    { text = "2", header = true },
    { text = "3", header = true },
    { text = "4", header = true },
    { text = "5", header = true },
    { text = "6", header = true },
    { text = "7", header = true },
    { text = "8", header = true },
    { text = "9", header = true },
    { text = "10", header = true },
    { text = "11", header = true },
    { text = "12", header = true },
    { text = "13", header = true },
    { text = "14", header = true },
    { text = "15", header = true },
    { text = "16", header = true },
    { text = "17", header = true },
    { text = "18", header = true },
    { text = "19", header = true },
    { text = "20", header = true },
  ],
]
body = [
  [
    { text = "Aberration" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "34" },
  ],
  [
    { text = "Animal" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "34" },
  ],
  [
    { text = "Construct" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "6" },
    { text = "8" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "13" },
    { text = "14" },
    { text = "16" },
    { text = "18" },
    { text = "19" },
    { text = "20" },
    { text = "21" },
    { text = "23" },
    { text = "25" },
    { text = "28" },
    { text = "31" },
  ],
  [
    { text = "Dragon" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "6" },
    { text = "7" },
    { text = "8" },
    { text = "9" },
    { text = "11" },
    { text = "12" },
    { text = "13" },
    { text = "14" },
    { text = "16" },
    { text = "17" },
    { text = "18" },
    { text = "19" },
    { text = "21" },
    { text = "23" },
    { text = "25" },
    { text = "29" },
  ],
  [
    { text = "Fey" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "6" },
    { text = "8" },
    { text = "10" },
    { text = "12" },
    { text = "13" },
    { text = "15" },
    { text = "17" },
    { text = "18" },
    { text = "20" },
    { text = "22" },
    { text = "23" },
    { text = "25" },
    { text = "26" },
    { text = "28" },
    { text = "31" },
    { text = "33" },
    { text = "37" },
  ],
  [
    { text = "Humanoid" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "34" },
  ],
  [
    { text = "Magical beast" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "6" },
    { text = "8" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "13" },
    { text = "14" },
    { text = "16" },
    { text = "18" },
    { text = "19" },
    { text = "20" },
    { text = "21" },
    { text = "23" },
    { text = "25" },
    { text = "28" },
    { text = "31" },
  ],
  [
    { text = "Monstrous humanoid" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "6" },
    { text = "8" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "13" },
    { text = "14" },
    { text = "16" },
    { text = "18" },
    { text = "19" },
    { text = "20" },
    { text = "21" },
    { text = "23" },
    { text = "25" },
    { text = "28" },
    { text = "31" },
  ],
  [
    { text = "Ooze" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "34" },
  ],
  [
    { text = "Outsider" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "6" },
    { text = "8" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "13" },
    { text = "14" },
    { text = "16" },
    { text = "18" },
    { text = "19" },
    { text = "20" },
    { text = "21" },
    { text = "23" },
    { text = "25" },
    { text = "28" },
    { text = "31" },
  ],
  [
    { text = "Plant" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "34" },
  ],
  [
    { text = "Undead" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "34" },
  ],
  [
    { text = "Vermin" },
    { text = "1" },
    { text = "2" },
    { text = "3" },
    { text = "4" },
    { text = "5" },
    { text = "7" },
    { text = "9" },
    { text = "10" },
    { text = "12" },
    { text = "14" },
    { text = "15" },
    { text = "16" },
    { text = "17" },
    { text = "19" },
    { text = "20" },
    { text = "22" },
    { text = "24" },
    { text = "26" },
    { text = "28" },
    { text = "30" },
    { text = "32" },
  ],
]
:::

### Table: Size {#table-size}

::: table
caption = "Table: Size"
head = [
  [
    { text = "Size", header = true },
    { text = "Minimum CR", header = true },
    { text = "Maximum CR", header = true },
    { text = "Base Str", header = true },
    { text = "Base Dex", header = true },
    { text = "Base Con", header = true },
  ],
]
body = [
  [
    { text = "Fine" },
    { text = "—" },
    { text = "2" },
    { text = "1" },
    { text = "18" },
    { text = "8" },
  ],
  [
    { text = "Diminutive" },
    { text = "—" },
    { text = "4" },
    { text = "1" },
    { text = "16" },
    { text = "8" },
  ],
  [
    { text = "Tiny" },
    { text = "—" },
    { text = "6" },
    { text = "2" },
    { text = "14" },
    { text = "8" },
  ],
  [
    { text = "Small" },
    { text = "—" },
    { text = "—" },
    { text = "6" },
    { text = "12" },
    { text = "8" },
  ],
  [
    { text = "Medium" },
    { text = "—" },
    { text = "—" },
    { text = "10" },
    { text = "10" },
    { text = "10" },
  ],
  [
    { text = "Large" },
    { text = "2" },
    { text = "—" },
    { text = "18" },
    { text = "8" },
    { text = "14" },
  ],
  [
    { text = "Huge" },
    { text = "4" },
    { text = "—" },
    { text = "26" },
    { text = "6" },
    { text = "18" },
  ],
  [
    { text = "Gargantuan" },
    { text = "6" },
    { text = "—" },
    { text = "34" },
    { text = "6" },
    { text = "22" },
  ],
  [
    { text = "Colossal" },
    { text = "8" },
    { text = "—" },
    { text = "42" },
    { text = "6" },
    { text = "26" },
  ],
]
:::

## Step 4: Size {#step-4-size}

Now that you have the creature's average statistics, it's time to pick its size. Most creatures
range in size from Small to Huge, but other sizes are not uncommon. A creature's size sets a
baseline for its physical ability scores and its natural weapon damage (as noted in the Natural
Attacks description in the Universal Monster Rules—see Appendix 3, pages 297–306). You should pick a
size that fits well with the creature's intended role in the game and Challenge Rating. If you
decide to give a creature an unusual size for its CR or HD, you should justify the unusual choice in
the monster's description to account for the discrepancy—in most cases, such unusually sized
monsters should be highly magical in nature. See Table: Size for more information on creature sizes
and expected scores.

### Minimum/Maximum CR {#minimum-maximum-cr}

These values list the minimum and the maximum challenge ratings a creature of the indicated size
should fall between.

### Base Str, Base Dex, Base Con {#base-str-base-dex-base-con}

These list the average scores for a creature of this size. Your specific monster's Strength,
Dexterity, or Constitution might vary greatly from these numbers, but if they do, you should pay
close attention to how these variances affect its other statistics.

## Step 5: Abilities {#step-5-abilities}

Once you have determined a creature's size, type, and Hit Dice, it's time to move on to its ability
scores. The bonuses granted from these ability scores should increase a creature's hit points,
attack bonuses, and saving throws to the approximate values presented on Table: Monster Statistics
by CR.

A creature's physical ability scores (Strength, Dexterity, and Constitution) should be relatively
close to the base values presented on Table: Size, depending on its size. Creatures with a few Hit
Dice but a high average hit point total should have a higher than normal Constitution.

A creature's mental ability scores (Intelligence, Wisdom, and Charisma) are largely defined by the
creature's concept. The base for all of these abilities is 10. Creatures that rely on spells and
[spell-like abilities](ref/umr/spell-like-abilities) in combat should have one mental ability score
that stands out (usually Charisma). Creatures incapable of speech have an Intelligence score of 2 or
lower. Unintelligent undead, constructs, oozes, plants, and vermin rarely have an Intelligence
score.

## Step 6: Skills and Feats {#step-6-skills-and-feats}

Using Table: Creature Statistics by Type, determine how many skill ranks your creature has based on
its type and Hit Dice. Assign these ranks as determined by the creature's concept. A creature's
class skill is determined by its type. Creatures with a low Intelligence typically only have ranks
in Dexterity- and Strength-based skills.

After you have assigned skills, it's time to assign the creature's feats. Each creature with an
Intelligence score receives a number of feats equal to 1 + 1 per every 2 Hit Dice after the first
(so, 1 at 1 HD, 2 at 3 HD, etc.). A creature must qualify to take a feat as normal. See Table 1–6
for a quick feat calculation chart.

### Table: Statistics Summary {#table-statistics-summary}

::: table
caption = "Table: Statistics Summary"
head = [
  [
    { text = "HD", header = true },
    { text = "Fast BAB", header = true },
    { text = "Medium BAB", header = true },
    { text = "Slow BAB", header = true },
    { text = "Good Save", header = true },
    { text = "Bad Save", header = true },
    { text = "Feats", header = true },
  ],
]
body = [
  [
    { text = "1" },
    { text = "+1" },
    { text = "+0" },
    { text = "+0" },
    { text = "+2" },
    { text = "+0" },
    { text = "1" },
  ],
  [
    { text = "2" },
    { text = "+2" },
    { text = "+1" },
    { text = "+1" },
    { text = "+3" },
    { text = "+0" },
    { text = "1" },
  ],
  [
    { text = "3" },
    { text = "+3" },
    { text = "+2" },
    { text = "+1" },
    { text = "+3" },
    { text = "+1" },
    { text = "2" },
  ],
  [
    { text = "4" },
    { text = "+4" },
    { text = "+3" },
    { text = "+2" },
    { text = "+4" },
    { text = "+1" },
    { text = "2" },
  ],
  [
    { text = "5" },
    { text = "+5" },
    { text = "+3" },
    { text = "+2" },
    { text = "+4" },
    { text = "+1" },
    { text = "3" },
  ],
  [
    { text = "6" },
    { text = "+6" },
    { text = "+4" },
    { text = "+3" },
    { text = "+5" },
    { text = "+2" },
    { text = "3" },
  ],
  [
    { text = "7" },
    { text = "+7" },
    { text = "+5" },
    { text = "+3" },
    { text = "+5" },
    { text = "+2" },
    { text = "4" },
  ],
  [
    { text = "8" },
    { text = "+8" },
    { text = "+6" },
    { text = "+4" },
    { text = "+6" },
    { text = "+2" },
    { text = "4" },
  ],
  [
    { text = "9" },
    { text = "+9" },
    { text = "+6" },
    { text = "+4" },
    { text = "+6" },
    { text = "+3" },
    { text = "5" },
  ],
  [
    { text = "10" },
    { text = "+10" },
    { text = "+7" },
    { text = "+5" },
    { text = "+7" },
    { text = "+3" },
    { text = "5" },
  ],
  [
    { text = "11" },
    { text = "+11" },
    { text = "+8" },
    { text = "+5" },
    { text = "+7" },
    { text = "+3" },
    { text = "6" },
  ],
  [
    { text = "12" },
    { text = "+12" },
    { text = "+9" },
    { text = "+6" },
    { text = "+8" },
    { text = "+4" },
    { text = "6" },
  ],
  [
    { text = "13" },
    { text = "+13" },
    { text = "+9" },
    { text = "+6" },
    { text = "+8" },
    { text = "+4" },
    { text = "7" },
  ],
  [
    { text = "14" },
    { text = "+14" },
    { text = "+10" },
    { text = "+7" },
    { text = "+9" },
    { text = "+4" },
    { text = "7" },
  ],
  [
    { text = "15" },
    { text = "+15" },
    { text = "+11" },
    { text = "+7" },
    { text = "+9" },
    { text = "+5" },
    { text = "8" },
  ],
  [
    { text = "16" },
    { text = "+16" },
    { text = "+12" },
    { text = "+8" },
    { text = "+10" },
    { text = "+5" },
    { text = "8" },
  ],
  [
    { text = "17" },
    { text = "+17" },
    { text = "+12" },
    { text = "+8" },
    { text = "+10" },
    { text = "+5" },
    { text = "9" },
  ],
  [
    { text = "18" },
    { text = "+18" },
    { text = "+13" },
    { text = "+9" },
    { text = "+11" },
    { text = "+6" },
    { text = "9" },
  ],
  [
    { text = "19" },
    { text = "+19" },
    { text = "+14" },
    { text = "+9" },
    { text = "+11" },
    { text = "+6" },
    { text = "10" },
  ],
  [
    { text = "20" },
    { text = "+20" },
    { text = "+15" },
    { text = "+10" },
    { text = "+12" },
    { text = "+6" },
    { text = "10" },
  ],
  [
    { text = "21" },
    { text = "+21" },
    { text = "+15" },
    { text = "+10" },
    { text = "+12" },
    { text = "+7" },
    { text = "11" },
  ],
  [
    { text = "22" },
    { text = "+22" },
    { text = "+16" },
    { text = "+11" },
    { text = "+13" },
    { text = "+7" },
    { text = "11" },
  ],
  [
    { text = "23" },
    { text = "+23" },
    { text = "+17" },
    { text = "+11" },
    { text = "+13" },
    { text = "+7" },
    { text = "12" },
  ],
  [
    { text = "24" },
    { text = "+24" },
    { text = "+18" },
    { text = "+12" },
    { text = "+14" },
    { text = "+8" },
    { text = "12" },
  ],
  [
    { text = "25" },
    { text = "+25" },
    { text = "+18" },
    { text = "+12" },
    { text = "+14" },
    { text = "+8" },
    { text = "13" },
  ],
  [
    { text = "26" },
    { text = "+26" },
    { text = "+19" },
    { text = "+13" },
    { text = "+15" },
    { text = "+8" },
    { text = "13" },
  ],
  [
    { text = "27" },
    { text = "+27" },
    { text = "+20" },
    { text = "+13" },
    { text = "+15" },
    { text = "+9" },
    { text = "14" },
  ],
  [
    { text = "28" },
    { text = "+28" },
    { text = "+21" },
    { text = "+14" },
    { text = "+16" },
    { text = "+9" },
    { text = "14" },
  ],
  [
    { text = "29" },
    { text = "+29" },
    { text = "+21" },
    { text = "+14" },
    { text = "+16" },
    { text = "+9" },
    { text = "15" },
  ],
  [
    { text = "30" },
    { text = "+30" },
    { text = "+22" },
    { text = "+15" },
    { text = "+17" },
    { text = "+10" },
    { text = "15" },
  ],
]
:::

## Step 7: Other Statistics {#step-7-other-statistics}

Using Table: Monster Statitics by CR, Table: Creature Statistics by Type, and Table: Statistics
Summary, you can now determine many of the creature's other statistics.

When building a creature's Armor Class, start by adding armor, shield, and natural armor bonuses to
its Dexterity modifier. If a creature does not wear armor, give it a tougher hide to get it near its
average AC. Remember that creatures with higher hit point totals might have a lower Armor Class,
whereas creatures with fewer hit points might have a higher Armor Class. If a creature's Armor Class
deviates from the average by more than 5 points, it might not be the right CR.

When determining a creature's attack bonuses, refer to the guidelines from Table: Monster Statistics
by CR based on the creature's CR. If the bonus is too low, consider increasing the creature's
Strength or Dexterity, or increasing the amount of damage it deals to above the average. If the
bonus is too high, consider decreasing the creature's Strength or Dexterity, or decrease the amount
of damage it deals. If this value is significantly different, and the creature is intended to rely
on melee or ranged attacks, consider adjusting the creature's CR.

Use Table: Average Die Results to determine the number of damage dice, combined with damage bonuses,
that the creature needs to reach the average damage for its CR. The creature might need additional
or more damaging attacks to approach the average. Remember that creatures that primarily deal damage
with other abilities, such as spells, do not need to meet the average damage for their attacks. You
can also use Table: Average Die Results to determine a creature's average hit points. Remember that
PC class levels provide the maximum number of hit points at 1st level.

Repeat this process for a creature's saving throws. If the saving throws are too high, consider
altering the ability scores on which they are based.

When determining a creature's speed, first decide if it has any alternative modes of movement, such
as burrow, climb, fly, or swim. Most Medium creatures have a base speed of 30 feet. Quadrupeds and
Large creatures increase this by 10 feet each. Smaller creatures decrease this base speed by 10
feet. If a creature is particularly fast or slow, modify the base speed by 10 feet. Burrow and climb
speeds are usually half a creature's base speed, while flying speeds are roughly double. Remember to
give a creature the appropriate skills for any unusual movement methods.

### Table: Creature Statistics by Type {#table-creature-statistics-by-type}

::: table
caption = "Table: Creature Statistics by Type"
head = [
  [
    { text = "Type", header = true },
    { text = "Hit Die", header = true },
    { text = "Base Attack Bonus (BAB)", header = true },
    { text = "Good Saving Throws", header = true },
    { text = "Skill Ranks\\*", header = true },
  ],
]
body = [
  [
    { text = "Aberration" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "Will" },
    { text = "4 + Int mod per HD" },
  ],
  [
    { text = "Animal" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "Fort, Ref" },
    { text = "2 + Int mod per HD" },
  ],
  [
    { text = "Construct" },
    { text = "d10" },
    { text = "HD (Fast BAB)" },
    { text = "—" },
    { text = "2 + Int mod per HD" },
  ],
  [
    { text = "Dragon" },
    { text = "d12" },
    { text = "HD (Fast BAB)" },
    { text = "Fort, Ref, Will" },
    { text = "6 + Int mod per HD" },
  ],
  [
    { text = "Fey" },
    { text = "d6" },
    { text = "HD × 1/2 (Slow BAB)" },
    { text = "Ref, Will" },
    { text = "6 + Int mod per HD" },
  ],
  [
    { text = "Humanoid" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "Varies (any one)" },
    { text = "2 + Int mod per HD" },
  ],
  [
    { text = "Magical beast" },
    { text = "d10" },
    { text = "HD (Fast BAB)" },
    { text = "Fort, Ref" },
    { text = "2 + Int mod per HD" },
  ],
  [
    { text = "Monstrous humanoid" },
    { text = "d10" },
    { text = "HD (Fast BAB)" },
    { text = "Ref, Will" },
    { text = "4 + Int mod per HD" },
  ],
  [
    { text = "Ooze" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "—" },
    { text = "2 + Int mod per HD" },
  ],
  [
    { text = "Outsider" },
    { text = "d10" },
    { text = "HD (Fast BAB)" },
    { text = "Varies (any two)" },
    { text = "6 + Int mod per HD" },
  ],
  [
    { text = "Plant" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "Fort" },
    { text = "2 + Int mod per HD" },
  ],
  [
    { text = "Undead" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "Will" },
    { text = "4 + Int mod per HD" },
  ],
  [
    { text = "Vermin" },
    { text = "d8" },
    { text = "HD × 3/4 (Medium BAB)" },
    { text = "Fort" },
    { text = "2 + Int mod per HD" },
  ],
]
foot = [
  [
    { text = "\\* As long as a creature has an Intelligence of at least 1, it gains a minimum of 1 skill point per Hit Die. Creatures with an Intelligence score of “—” gain no skill points or feats.", colspan = 5 },
  ],
]
:::

## Step 8: Special Abilities and Qualities {#step-8-special-abilities-and-qualities}

Monsters are different from characters in that they can have all sorts of different special
abilities and qualities. Each of these is tied closely to the creature's concept, allowing it to
fill a specific role in the game. For examples, look at monsters in this book. Monsters should use
abilities from the Universal Monster Rules whenever possible, instead of creating new yet similar
abilities—when you do create new abilities, use the Universal Monster Rules as a template for how to
present and create the new abilities.

Most special abilities that cause damage, such as breath weapons, give a save (Fortitude, Reflex, or
Will depending on the ability). The DC for almost all special abilities is equal to 10 + 1/2 the
creature's Hit Dice + a relevant ability modifier (usually Constitution or Charisma depending on the
ability). Special abilities that add to melee and ranged attacks generally do not allow a save, as
they rely on the attacks hitting to be useful.

Special senses and resistances to certain energy types are common in creatures of CR 5 and lower.
[Damage reduction](ref/rule/damage-reduction), energy immunities, and regeneration are more common
in creatures above CR 5. [Spell resistance](ref/rule/spell-resistance) and immunities become more
common above CR 10. As a general rule a creature's spell resitance should equal its CR + 11.

### Table: XP and GP Values by CR {#table-xp-and-gp-values-by-cr}

::: table
caption = "Table: XP and GP Values by CR"
head = [
  [
    { text = "CR", header = true },
    { text = "XP", header = true },
    { text = "Slow GP", header = true },
    { text = "Medium GP", header = true },
    { text = "Fast GP", header = true },
  ],
]
body = [
  [
    { text = "1/8" },
    { text = "50 XP" },
    { text = "20 gp" },
    { text = "35 gp" },
    { text = "50 gp" },
  ],
  [
    { text = "1/6" },
    { text = "65 XP" },
    { text = "30 gp" },
    { text = "45 gp" },
    { text = "65 gp" },
  ],
  [
    { text = "1/4" },
    { text = "100 XP" },
    { text = "40 gp" },
    { text = "65 gp" },
    { text = "100 gp" },
  ],
  [
    { text = "1/3" },
    { text = "135 XP" },
    { text = "55 gp" },
    { text = "85 gp" },
    { text = "135 gp" },
  ],
  [
    { text = "1/2" },
    { text = "200 XP" },
    { text = "85 gp" },
    { text = "130 gp" },
    { text = "200 gp" },
  ],
  [
    { text = "1" },
    { text = "400 XP" },
    { text = "170 gp" },
    { text = "260 gp" },
    { text = "400 gp" },
  ],
  [
    { text = "2" },
    { text = "600 XP" },
    { text = "350 gp" },
    { text = "550 gp" },
    { text = "800 gp" },
  ],
  [
    { text = "3" },
    { text = "800 XP" },
    { text = "550 gp" },
    { text = "800 gp" },
    { text = "1,200 gp" },
  ],
  [
    { text = "4" },
    { text = "1,200 XP" },
    { text = "750 gp" },
    { text = "1,150 gp" },
    { text = "1,700 gp" },
  ],
  [
    { text = "5" },
    { text = "1,600 XP" },
    { text = "1,000 gp" },
    { text = "1,550 gp" },
    { text = "2,300 gp" },
  ],
  [
    { text = "6" },
    { text = "2,400 XP" },
    { text = "1,350 gp" },
    { text = "2,000 gp" },
    { text = "3,000 gp" },
  ],
  [
    { text = "7" },
    { text = "3,200 XP" },
    { text = "1,750 gp" },
    { text = "2,600 gp" },
    { text = "3,900 gp" },
  ],
  [
    { text = "8" },
    { text = "4,800 XP" },
    { text = "2,200 gp" },
    { text = "3,350 gp" },
    { text = "5,000 gp" },
  ],
  [
    { text = "9" },
    { text = "6,400 XP" },
    { text = "2,850 gp" },
    { text = "4,250 gp" },
    { text = "6,400 gp" },
  ],
  [
    { text = "10" },
    { text = "9,600 XP" },
    { text = "3,650 gp" },
    { text = "5,450 gp" },
    { text = "8,200 gp" },
  ],
  [
    { text = "11" },
    { text = "12,800 XP" },
    { text = "4,650 gp" },
    { text = "7,000 gp" },
    { text = "10,500 gp" },
  ],
  [
    { text = "12" },
    { text = "19,200 XP" },
    { text = "6,000 gp" },
    { text = "9,000 gp" },
    { text = "13,500 gp" },
  ],
  [
    { text = "13" },
    { text = "25,600 XP" },
    { text = "7,750 gp" },
    { text = "11,600 gp" },
    { text = "17,500 gp" },
  ],
  [
    { text = "14" },
    { text = "38,400 XP" },
    { text = "10,000 gp" },
    { text = "15,000 gp" },
    { text = "22,000 gp" },
  ],
  [
    { text = "15" },
    { text = "51,200 XP" },
    { text = "13,000 gp" },
    { text = "19,500 gp" },
    { text = "29,000 gp" },
  ],
  [
    { text = "16" },
    { text = "76,800 XP" },
    { text = "16,500 gp" },
    { text = "25,000 gp" },
    { text = "38,000 gp" },
  ],
  [
    { text = "17" },
    { text = "102,400 XP" },
    { text = "22,000 gp" },
    { text = "32,000 gp" },
    { text = "48,000 gp" },
  ],
  [
    { text = "18" },
    { text = "153,600 XP" },
    { text = "28,000 gp" },
    { text = "41,000 gp" },
    { text = "62,000 gp" },
  ],
  [
    { text = "19" },
    { text = "204,800 XP" },
    { text = "35,000 gp" },
    { text = "53,000 gp" },
    { text = "79,000 gp" },
  ],
  [
    { text = "20" },
    { text = "307,200 XP" },
    { text = "44,000 gp" },
    { text = "67,000 gp" },
    { text = "100,000 gp" },
  ],
  [
    { text = "21" },
    { text = "409,600 XP" },
    { text = "56,000 gp" },
    { text = "84,000 gp" },
    { text = "126,000 gp" },
  ],
  [
    { text = "22" },
    { text = "615,000 XP" },
    { text = "70,000 gp" },
    { text = "105,000 gp" },
    { text = "158,000 gp" },
  ],
  [
    { text = "23" },
    { text = "820,000 XP" },
    { text = "88,000 gp" },
    { text = "132,000 gp" },
    { text = "198,000 gp" },
  ],
  [
    { text = "24" },
    { text = "1,230,000 XP" },
    { text = "110,000 gp" },
    { text = "165,000 gp" },
    { text = "248,000 gp" },
  ],
  [
    { text = "25" },
    { text = "1,640,000 XP" },
    { text = "138,000 gp" },
    { text = "208,000 gp" },
    { text = "312,000 gp" },
  ],
]
:::

## Step 9: Treasure {#step-9-treasure}

A creature should have an amount of treasure appropriate to its CR. See Table: XP and GP Values by
CR for a list of treasure totals based on CR. For some creatures, their treasure consists of the
loot from their recent meals strewn across their lairs, while for others it consists of a
greed-fueled hoard or even gear it uses in combat. Make sure to account for any weapons or armor
that the creature is using, as determined by step 7.

## Step 10: Details {#step-10-details}

Now that you have all of the creature's statistics sorted out, it's time to fill in all the
details—such as name, alignment, space, reach, environment, and ecology—as you see fit.
