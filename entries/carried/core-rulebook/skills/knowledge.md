+++
id = "ref/carried/core-rulebook/skills/knowledge"
kind = "skill"
title = "Knowledge"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Knowledge", path = "core_rulebook/skill/knowledge.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Int
Trained Only: Yes
Armor Check Penalty: Yes
:::

_You are educated in a field of study and can answer both simple and complex questions. Like the
Craft, Perform, and Profession skills, Knowledge actually encompasses a number of different
specialties. Below are listed typical fields of study. Arcana (ancient mysteries, magic traditions,
arcane symbols, constructs, dragons, magical beasts) Dungeoneering (aberrations, caverns, oozes,
spelunking) Engineering (buildings, aqueducts, bridges, fortifications) Geography (lands, terrain,
climate, people) History (wars, colonies, migrations, founding of cities) Local (legends,
personalities, inhabitants, laws, customs, traditions, humanoids) Nature (animals, fey, monstrous
humanoids, plants, seasons and cycles, weather, vermin) Nobility (lineages, heraldry, personalities,
royalty) Planes (the Inner Planes, the Outer Planes, the Astral Plane, the Ethereal Plane,
outsiders, planar magic) Religion (gods and goddesses, mythic history, ecclesiastic tradition, holy
symbols, undead)_

## Check {#check}

Answering a question within your field of study has a DC of 10 (for really easy questions), 15 (for
basic questions), or 20 to 30 (for really tough questions).

You can use this skill to identify monsters and their special powers or vulnerabilities. In general,
the DC of such a check equals 10 + the monster's CR. For common monsters, such as goblins, the DC of
this check equals 5 + the monster's CR. For particularly rare monsters, such as the tarrasque, the
DC of this check equals 15 + the monster's CR, or more. A successful check allows you to remember a
bit of useful information about that monster. For every 5 points by which your check result exceeds
the DC, you recall another piece of useful information. Many of the Knowledge skills have specific
uses as noted on Table: Knowledge Skill DCs.

### Table: Knowledge Skill DCs {#table-knowledge-skill-dcs}

::: table
caption = "Table: Knowledge Skill DCs"
head = [
  [
    { text = "Task", header = true },
    { text = "Knowledge Skill", header = true },
    { text = "DC", header = true },
  ],
]
body = [
  [
    { text = "Identify auras while using _[detect magic](ref/spell/detect-magic)_" },
    { text = "Arcana" },
    { text = "15 + spell level" },
  ],
  [
    { text = "Identify a spell effect that is in place" },
    { text = "Arcana" },
    { text = "20 + spell level" },
  ],
  [
    { text = "Identify materials manufactured by magic" },
    { text = "Arcana" },
    { text = "20 + spell level" },
  ],
  [
    { text = "Identify a spell that just targeted you" },
    { text = "Arcana" },
    { text = "25 + spell level" },
  ],
  [
    { text = "Identify the spells cast using a specific material component" },
    { text = "Arcana" },
    { text = "20" },
  ],
  [
    { text = "Identify underground hazard" },
    { text = "Dungeoneering" },
    { text = "15 + hazard's CR" },
  ],
  [
    { text = "Identify mineral, stone, or metal" },
    { text = "Dungeoneering" },
    { text = "10" },
  ],
  [
    { text = "Determine slope" },
    { text = "Dungeoneering" },
    { text = "15" },
  ],
  [
    { text = "Determine depth underground" },
    { text = "Dungeoneering" },
    { text = "20" },
  ],
  [
    { text = "Identify dangerous construction" },
    { text = "Engineering" },
    { text = "10" },
  ],
  [
    { text = "Determine a structure's style or age" },
    { text = "Engineering" },
    { text = "15" },
  ],
  [
    { text = "Determine a structure's weakness" },
    { text = "Engineering" },
    { text = "20" },
  ],
  [
    { text = "Identify a creature's ethnicity or accent" },
    { text = "Geography" },
    { text = "10" },
  ],
  [
    { text = "Recognize regional terrain features" },
    { text = "Geography" },
    { text = "15" },
  ],
  [
    { text = "Know location of nearest community or noteworthy site" },
    { text = "Geography" },
    { text = "20" },
  ],
  [
    { text = "Know recent or historically significant event" },
    { text = "History" },
    { text = "10" },
  ],
  [
    { text = "Determine approximate date of a specific event" },
    { text = "History" },
    { text = "15" },
  ],
  [
    { text = "Know obscure or ancient historical event" },
    { text = "History" },
    { text = "20" },
  ],
  [
    { text = "Know local laws, rulers, and popular locations" },
    { text = "Local" },
    { text = "10" },
  ],
  [
    { text = "Know a common rumor or local tradition" },
    { text = "Local" },
    { text = "15" },
  ],
  [
    { text = "Know hidden organizations, rulers, and locations" },
    { text = "Local" },
    { text = "20" },
  ],
  [
    { text = "Identify natural hazard" },
    { text = "Nature" },
    { text = "15 + hazard's CR" },
  ],
  [
    { text = "Identify a common plant or animal" },
    { text = "Nature" },
    { text = "10" },
  ],
  [
    { text = "Identify unnatural weather phenomenon" },
    { text = "Nature" },
    { text = "15" },
  ],
  [
    { text = "Determine artificial nature of feature" },
    { text = "Nature" },
    { text = "20" },
  ],
  [
    { text = "Know current rulers and their symbols" },
    { text = "Nobility" },
    { text = "10" },
  ],
  [
    { text = "Know proper etiquette" },
    { text = "Nobility" },
    { text = "15" },
  ],
  [
    { text = "Know line of succession" },
    { text = "Nobility" },
    { text = "20" },
  ],
  [
    { text = "Know the names of the planes" },
    { text = "Planes" },
    { text = "10" },
  ],
  [
    { text = "Recognize current plane" },
    { text = "Planes" },
    { text = "15" },
  ],
  [
    { text = "Identify a creature's planar origin" },
    { text = "Planes" },
    { text = "20" },
  ],
  [
    { text = "Recognize a common deity's symbol or clergy" },
    { text = "Religion" },
    { text = "10" },
  ],
  [
    { text = "Know common mythology and tenets" },
    { text = "Religion" },
    { text = "15" },
  ],
  [
    { text = "Recognize an obscure deity's symbol or clergy" },
    { text = "Religion" },
    { text = "20" },
  ],
  [
    { text = "Identify a monster's abilities and weaknesses" },
    { text = "Varies" },
    { text = "10 + monster's CR" },
  ],
]
:::

## Action {#action}

Usually none. In most cases, a Knowledge check doesn't take an action (but see “Untrained,” below).

## Try Again {#try-again}

No. The check represents what you know, and thinking about a topic a second time doesn't let you
know something that you never learned in the first place.

## Untrained {#untrained}

You cannot make an untrained Knowledge check with a DC higher than 10. If you have access to an
extensive library that covers a specific skill, this limit is removed. The time to make checks using
a library, however, increases to 1d4 hours. Particularly complete libraries might even grant a bonus
on Knowledge checks in the fields that they cover.
