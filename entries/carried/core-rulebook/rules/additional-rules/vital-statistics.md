+++
id = "ref/carried/core-rulebook/rules/additional-rules/vital-statistics"
kind = "rule"
title = "Vital Statistics"
source_ids = ["core-rulebook"]
section = ["Rules", "Additional Rules"]
parent = "ref/carried/core-rulebook/rules/additional-rules"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Additional Rules/Vital Statistics", path = "core_rulebook/rules/additional_rules.json" },
]

[fields]
kind = "none"
+++

The following section determines a character's starting age, height, and weight. The character's
race and class influence these statistics. Consult your GM before making a character that does not
conform to these statistics.

## Age {#age}

You can choose or randomly generate your character's age. If you choose it, it must be at least the
minimum age for the character's race and class. Alternatively, roll the dice indicated for your
class on Table: Random Starting Ages and add the result to the minimum age of adulthood for your
race to determine how old your character is.

### Table: Random Starting Ages {#table-random-starting-ages}

::: table
caption = "Table: Random Starting Ages"
head = [
  [
    { text = "Race", header = true },
    { text = "Adulthood", header = true },
    { text = "Barbarian, Rogue, Sorcerer", header = true },
    { text = "Bard, Fighter, Paladin, Ranger", header = true },
    { text = "Cleric, Druid, Monk, Wizard", header = true },
  ],
]
body = [
  [
    { text = "Human" },
    { text = "15 years" },
    { text = "+1d4" },
    { text = "+1d6" },
    { text = "+2d6" },
  ],
  [
    { text = "Dwarf" },
    { text = "40 years" },
    { text = "+3d6" },
    { text = "+5d6" },
    { text = "+7d6" },
  ],
  [
    { text = "Elf" },
    { text = "110 years" },
    { text = "+4d6" },
    { text = "+6d6" },
    { text = "+10d6" },
  ],
  [
    { text = "Gnome" },
    { text = "40 years" },
    { text = "+4d6" },
    { text = "+6d6" },
    { text = "+9d6" },
  ],
  [
    { text = "Half-elf" },
    { text = "20 years" },
    { text = "+1d6" },
    { text = "+2d6" },
    { text = "+3d6" },
  ],
  [
    { text = "Half-orc" },
    { text = "14 years" },
    { text = "+1d4" },
    { text = "+1d6" },
    { text = "+2d6" },
  ],
  [
    { text = "Halfling" },
    { text = "20 years" },
    { text = "+2d4" },
    { text = "+3d6" },
    { text = "+4d6" },
  ],
]
:::

With age, a character's physical ability scores decrease and his mental ability scores increase (see
Table: Aging Effects). The effects of each aging step are cumulative. However, none of a character's
ability scores can be reduced below 1 in this way.

When a character reaches venerable age, secretly roll his maximum age and record the result, which
the player does not know. A character who reaches his maximum age dies of old age sometime during
the following year.

The maximum ages are for player characters. Most people in the world at large die from pestilence,
accidents, infections, or violence before getting to venerable age.

### Table: Aging Effects {#table-aging-effects}

::: table
caption = "Table: Aging Effects"
head = [
  [
    { text = "Race", header = true },
    { text = "Middle Age^1^", header = true },
    { text = "Old^2^", header = true },
    { text = "Venerable^3^", header = true },
    { text = "Maximum Age", header = true },
  ],
]
body = [
  [
    { text = "Human" },
    { text = "35 years" },
    { text = "53 years" },
    { text = "70 years" },
    { text = "70 + 2d20 years" },
  ],
  [
    { text = "Dwarf" },
    { text = "125 years" },
    { text = "188 years" },
    { text = "250 years" },
    { text = "250 + 2d% years" },
  ],
  [
    { text = "Elf" },
    { text = "175 years" },
    { text = "263 years" },
    { text = "350 years" },
    { text = "350 + 4d% years" },
  ],
  [
    { text = "Gnome" },
    { text = "100 years" },
    { text = "150 years" },
    { text = "200 years" },
    { text = "200 + 3d% years" },
  ],
  [
    { text = "Half-elf" },
    { text = "62 years" },
    { text = "93 years" },
    { text = "125 years" },
    { text = "125 + 3d20 years" },
  ],
  [
    { text = "Half-orc" },
    { text = "30 years" },
    { text = "45 years" },
    { text = "60 years" },
    { text = "60 + 2d10 years" },
  ],
  [
    { text = "Halfling" },
    { text = "50 years" },
    { text = "75 years" },
    { text = "100 years" },
    { text = "100 + 5d20 years" },
  ],
]
foot = [
  [
    { text = "1 At middle age, –1 to Str, Dex, and Con; +1 to Int, Wis, and Cha.", colspan = 5 },
  ],
  [
    { text = "2 At old age, –2 to Str, Dex, and Con; +1 to Int, Wis, and Cha.", colspan = 5 },
  ],
  [
    { text = "3 At venerable age, –3 to Str, Dex, and Con; +1 to Int, Wis, and Cha.", colspan = 5 },
  ],
]
:::

## Height and Weight {#height-and-weight}

To determine a character's height, roll the modifier dice indicated on Table: Random Height and
Weight and add the result, in inches, to the base height for your character's race and gender. To
determine a character's weight, multiply the result of the modifier dice by the weight multiplier
and add the result to the base weight for your character's race and gender.

### Table: Random Height and Weight {#table-random-height-and-weight}

::: table
caption = "Table: Random Height and Weight"
head = [
  [
    { text = "Race", header = true },
    { text = "Base Height", header = true },
    { text = "Base Weight", header = true },
    { text = "Modifier", header = true },
    { text = "Weight Multiplier", header = true },
  ],
]
body = [
  [
    { text = "Human, male" },
    { text = "4 ft. 10 in." },
    { text = "120 lbs." },
    { text = "2d10" },
    { text = "×5 lbs." },
  ],
  [
    { text = "Human, female" },
    { text = "4 ft. 5 in." },
    { text = "85 lbs." },
    { text = "2d10" },
    { text = "×5 lbs." },
  ],
  [
    { text = "Dwarf, male" },
    { text = "3 ft. 9 in." },
    { text = "150 lbs." },
    { text = "2d4" },
    { text = "×7 lbs." },
  ],
  [
    { text = "Dwarf, female" },
    { text = "3 ft. 7 in." },
    { text = "120 lbs." },
    { text = "2d4" },
    { text = "×7 lbs." },
  ],
  [
    { text = "Elf, male" },
    { text = "5 ft. 4 in." },
    { text = "100 lbs." },
    { text = "2d8" },
    { text = "×3 lbs." },
  ],
  [
    { text = "Elf, female" },
    { text = "5 ft. 4 in." },
    { text = "90 lbs." },
    { text = "2d6" },
    { text = "×3 lbs." },
  ],
  [
    { text = "Gnome, male" },
    { text = "3 ft. 0 in." },
    { text = "35 lbs." },
    { text = "2d4" },
    { text = "×1 lb." },
  ],
  [
    { text = "Gnome, female" },
    { text = "2 ft. 10 in." },
    { text = "30 lbs." },
    { text = "2d4" },
    { text = "×1 lb." },
  ],
  [
    { text = "Half-elf, male" },
    { text = "5 ft. 2 in." },
    { text = "110 lbs." },
    { text = "2d8" },
    { text = "×5 lbs." },
  ],
  [
    { text = "Half-elf, female" },
    { text = "5 ft. 0 in." },
    { text = "90 lbs." },
    { text = "2d8" },
    { text = "×5 lbs." },
  ],
  [
    { text = "Half-orc, male" },
    { text = "4 ft. 10 in." },
    { text = "150 lbs." },
    { text = "2d12" },
    { text = "×7 lbs." },
  ],
  [
    { text = "Half-orc, female" },
    { text = "4 ft. 5 in." },
    { text = "110 lbs." },
    { text = "2d12" },
    { text = "×7 lbs." },
  ],
  [
    { text = "Halfling, male" },
    { text = "2 ft. 8 in." },
    { text = "30 lbs." },
    { text = "2d4" },
    { text = "×1 lb." },
  ],
  [
    { text = "Halfling, female" },
    { text = "2 ft. 6 in." },
    { text = "25 lbs." },
    { text = "2d4" },
    { text = "×1 lb." },
  ],
]
:::

## Carrying Capacity {#carrying-capacity}

These carrying capacity rules determine how much a character's equipment slows him down. Encumbrance
comes in two parts: encumbrance by armor and encumbrance by total weight.

Encumbrance by Armor: A character's armor determines his maximum Dexterity bonus to AC, armor check
penalty, speed, and running speed. Unless your character is weak or carrying a lot of gear, that's
all you need to know; the extra gear your character carries won't slow him down any more than the
armor already does.

If your character is weak or carrying a lot of gear, however, then you'll need to calculate
encumbrance by weight. Doing so is most important when your character is trying to carry some heavy
object.

### Table: Carrying Capacity {#table-carrying-capacity}

::: table
caption = "Table: Carrying Capacity"
head = [
  [
    { text = "Strength Score", header = true },
    { text = "Light Load", header = true },
    { text = "Medium Load", header = true },
    { text = "Heavy Load", header = true },
  ],
]
body = [
  [
    { text = "1" },
    { text = "3 lbs. or less" },
    { text = "4–6 lbs." },
    { text = "7–10 lbs." },
  ],
  [
    { text = "2" },
    { text = "6 lbs. or less" },
    { text = "7–13 lbs." },
    { text = "14–20 lbs." },
  ],
  [
    { text = "3" },
    { text = "10 lbs. or less" },
    { text = "11–20 lbs." },
    { text = "21–30 lbs." },
  ],
  [
    { text = "4" },
    { text = "13 lbs. or less" },
    { text = "14–26 lbs." },
    { text = "27–40 lbs." },
  ],
  [
    { text = "5" },
    { text = "16 lbs. or less" },
    { text = "17–33 lbs." },
    { text = "34–50 lbs." },
  ],
  [
    { text = "6" },
    { text = "20 lbs. or less" },
    { text = "21–40 lbs." },
    { text = "41–60 lbs." },
  ],
  [
    { text = "7" },
    { text = "23 lbs. or less" },
    { text = "24–46 lbs." },
    { text = "47–70 lbs." },
  ],
  [
    { text = "8" },
    { text = "26 lbs. or less" },
    { text = "27–53 lbs." },
    { text = "54–80 lbs." },
  ],
  [
    { text = "9" },
    { text = "30 lbs. or less" },
    { text = "31–60 lbs." },
    { text = "61–90 lbs." },
  ],
  [
    { text = "10" },
    { text = "33 lbs. or less" },
    { text = "34–66 lbs." },
    { text = "67–100 lbs." },
  ],
  [
    { text = "11" },
    { text = "38 lbs. or less" },
    { text = "39–76 lbs." },
    { text = "77–115 lbs." },
  ],
  [
    { text = "12" },
    { text = "43 lbs. or less" },
    { text = "44–86 lbs." },
    { text = "87–130 lbs." },
  ],
  [
    { text = "13" },
    { text = "50 lbs. or less" },
    { text = "51–100 lbs." },
    { text = "101–150 lbs." },
  ],
  [
    { text = "14" },
    { text = "58 lbs. or less" },
    { text = "59–116 lbs." },
    { text = "117–175 lbs." },
  ],
  [
    { text = "15" },
    { text = "66 lbs. or less" },
    { text = "67–133 lbs." },
    { text = "134–200 lbs." },
  ],
  [
    { text = "16" },
    { text = "76 lbs. or less" },
    { text = "77–153 lbs." },
    { text = "154–230 lbs." },
  ],
  [
    { text = "17" },
    { text = "86 lbs. or less" },
    { text = "87–173 lbs." },
    { text = "174–260 lbs." },
  ],
  [
    { text = "18" },
    { text = "100 lbs. or less" },
    { text = "101–200 lbs." },
    { text = "201–300 lbs." },
  ],
  [
    { text = "19" },
    { text = "116 lbs. or less" },
    { text = "117–233 lbs." },
    { text = "234–350 lbs." },
  ],
  [
    { text = "20" },
    { text = "133 lbs. or less" },
    { text = "134–266 lbs." },
    { text = "267–400 lbs." },
  ],
  [
    { text = "21" },
    { text = "153 lbs. or less" },
    { text = "154–306 lbs." },
    { text = "307–460 lbs." },
  ],
  [
    { text = "22" },
    { text = "173 lbs. or less" },
    { text = "174–346 lbs." },
    { text = "347–520 lbs." },
  ],
  [
    { text = "23" },
    { text = "200 lbs. or less" },
    { text = "201–400 lbs." },
    { text = "401–600 lbs." },
  ],
  [
    { text = "24" },
    { text = "233 lbs. or less" },
    { text = "234–466 lbs." },
    { text = "467–700 lbs." },
  ],
  [
    { text = "25" },
    { text = "266 lbs. or less" },
    { text = "267–533 lbs." },
    { text = "534–800 lbs." },
  ],
  [
    { text = "26" },
    { text = "306 lbs. or less" },
    { text = "307–613 lbs." },
    { text = "614–920 lbs." },
  ],
  [
    { text = "27" },
    { text = "346 lbs. or less" },
    { text = "347–693 lbs." },
    { text = "694–1,040 lbs." },
  ],
  [
    { text = "28" },
    { text = "400 lbs. or less" },
    { text = "401–800 lbs." },
    { text = "801–1,200 lbs." },
  ],
  [
    { text = "29" },
    { text = "466 lbs. or less" },
    { text = "467–933 lbs." },
    { text = "934–1,400 lbs." },
  ],
  [
    { text = "+10" },
    { text = "×4" },
    { text = "×4" },
    { text = "×4" },
  ],
]
:::

Encumbrance by Weight: If you want to determine whether your character's gear is heavy enough to
slow him down more than his armor already does, total the weight of all the character's items,
including armor, weapons, and gear. Compare this total to the character's Strength on Table:
Carrying Capacity. Depending on the character's carrying capacity, he or she may be carrying a
light, medium, or heavy load. Like armor, a character's load affects his maximum Dexterity bonus to
AC, carries a check penalty (which works like an armor check penalty), reduces the character's
speed, and affects how fast the character can run, as shown on Table: Encumbrance Effects. A medium
or heavy load counts as medium or heavy armor for the purpose of abilities or skills that are
restricted by armor. Carrying a light load does not encumber a character.

If your character is wearing armor, use the worse figure (from armor or from load) for each
category. Do not stack the penalties.

### Table: Encumbrance Effects {#table-encumbrance-effects}

::: table
caption = "Table: Encumbrance Effects"
head = [
  [
    { text = "Load", header = true, rowspan = 2 },
    { text = "Max Dex", header = true, rowspan = 2 },
    { text = "Check Penalty", header = true, rowspan = 2 },
    { text = "Speed", header = true, colspan = 2 },
    { text = "Run", header = true, rowspan = 2 },
  ],
  [
    { text = "(30 ft.)", header = true },
    { text = "(20 ft.)", header = true },
  ],
]
body = [
  [
    { text = "Medium" },
    { text = "+3" },
    { text = "-3" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "×4" },
  ],
  [
    { text = "Heavy" },
    { text = "+1" },
    { text = "-6" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "×3" },
  ],
]
:::

Lifting and Dragging: A character can lift as much as his maximum load over his head. A character's
maximum load is the highest amount of weight listed for a character's Strength in the heavy load
column of Table: Carrying Capacity.

A character can lift as much as double his maximum load off the ground, but he or she can only
stagger around with it. While overloaded in this way, the character loses any Dexterity bonus to AC
and can move only 5 feet per round (as a full-round action).

A character can generally push or drag along the ground as much as five times his maximum load.
Favorable conditions can double these numbers, and bad circumstances can reduce them by half or
more.

Bigger and Smaller Creatures: The figures on Table: Carrying Capacity are for Medium bipedal
creatures. A larger bipedal creature can carry more weight depending on its size category, as
follows: Large ×2, Huge ×4, Gargantuan ×8, Colossal ×16. A smaller creature can carry less weight
depending on its size category, as follows: Small ×3/4, Tiny ×1/2, Diminutive ×1/4, Fine ×1/8.

Quadrupeds can carry heavier loads than bipeds can. Multiply the values corresponding to the
creature's Strength score from Table: Carrying Capacity by the appropriate modifier, as follows:
Fine ×1/4, Diminutive ×1/2, Tiny ×3/4, Small ×1, Medium ×1-1/2, Large ×3, Huge ×6, Gargantuan ×12,
Colossal ×24.

Tremendous Strength: For Strength scores not shown on Table: Carrying Capacity, find the Strength
score between 20 and 29 that has the same number in the “ones” digit as the creature's Strength
score does and multiply the numbers in that row by 4 for every 10 points the creature's Strength is
above the score for that row.

### Armor and Encumbrance for Other Base Speeds {#armor-and-encumbrance-for-other-base-speeds}

The table below provides reduced speed figures for all base speeds from 5 feet to 120 feet (in
5-foot increments).

#### Base Speed {#base-speed}

|Base Speed|Reduced Speed|
| --- | --- |
|5 ft.|5 ft.|
|10 ft.–15 ft.|10 ft.|
|20 ft.|15 ft.|
|25 ft.–30 ft.|20 ft.|
|35 ft.|25 ft.|
|40 ft.–45 ft.|30 ft.|
|50 ft.|35 ft.|
|55 ft.–60 ft.|40 ft.|
|65 ft.|45 ft.|
|70 ft.–75 ft.|50 ft.|
|80 ft.|55 ft.|
|85 ft.–90 ft.|60 ft.|
|95 ft.|65 ft.|
|100 ft.–105 ft.|70 ft.|
|110 ft.|75 ft.|
|115 ft.–120 ft.|80 ft.|
