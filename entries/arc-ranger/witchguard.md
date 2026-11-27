+++
id = "ref/arc-ranger/witchguard"
kind = "archetype"
title = "Witchguard"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Witchguard"
source_ids = ["people-of-the-north"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "witchguard", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "people-of-the-north"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "defend-charge", level = 4 },
  { anchor = "bodyguard", level = 3 },
  { anchor = "patron", level = 4 },
  { anchor = "sworn-defender", level = 7 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["defend-charge"] },
  { replaces = "Endurance", feature = "endurance", by = ["bodyguard"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["sworn-defender"] },
]
+++

Witchguards are the sworn defenders of the White Witches of Irrisen. Although the White Witches are
spellcasters of immense power, even they cannot defend themselves against every attack. Witchguards
dedicate their lives to protecting their charges, and they gain some arcane knowledge in return.
They are trained to work closely with witches and defend their charges from harm. Witchguards learn
magical abilities from the same patrons that grant witches their powers, though they can use their
abilities to protect any kind of spellcaster, not just a witch. A witchguard is ready to face any
foe that might threaten his charge, and he is ever prepared to lay down his life to protect the life
of the person he is sworn to defend.

## Class Skills {#class-skills}

A witchguard adds Knowledge (nobility) and Sense Motive to his list of class skills, and removes
Handle Animal and Knowledge (dungeoneering) from his list of class skills.

## Defend Charge (Ex) {#defend-charge}

At 4th level, a witchguard forms a bond with a spellcaster he has sworn to defend. Once per day,
this bond allows the witchguard to spend a move action to grant an adjacent spellcaster a +2 dodge
bonus to AC and a +2 circumstance bonus on [concentration](ref/rule/concentration) checks. At 5th
level and every 5 levels thereafter, these bonuses increase by 2. The bonuses last for a number of
rounds equal to the witchguard's Wisdom modifier (minimum 1).

At 4th level and every 3 levels thereafter, the witchguard can use this ability one additional time
per day. This ability replaces hunter's bond.

## Bodyguard (Ex) {#bodyguard}

At 3rd level, a witchguard gains [Bodyguard](ref/feat/bodyguard) as a bonus feat, even if he doesn't
meet the prerequisite. This ability replaces endurance.

## Patron (Su) {#patron}

A witchguard learns something of arcane magic from the witches he defends. At 4th level, when a
witchguard gains the ability to cast spells, he must also select a patron, as the witch class
feature (_Pathfinder RPG Advanced Player's Guide_ 70). This patron is usually the same as the patron
of the witch he is sworn to protect, but the witchguard may choose any patron. The witchguard adds
the first four spells from his patron's spell list to his ranger spell list. The witchguard cannot
cast patron spells of a level he is unable to cast.

## Sworn Defender (Ex) {#sworn-defender}

At 7th level, a witchguard gains [In Harm's Way](ref/feat/in-harms-way) as a bonus feat. This
ability replaces woodland stride.
