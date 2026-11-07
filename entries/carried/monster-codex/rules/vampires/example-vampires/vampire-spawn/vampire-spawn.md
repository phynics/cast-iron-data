+++
id = "ref/carried/monster-codex/rules/vampires/example-vampires/vampire-spawn/vampire-spawn"
kind = "creature"
title = "Vampire Spawn"
source_ids = ["monster-codex"]
section = ["Rules", "Vampires", "Example Vampires", "Vampire Spawn"]
tags = ["undead", "human", "medium"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Monster Codex/Rules/Vampires/Example Vampires/Vampire Spawn/Vampire Spawn", path = "monster_codex/creature/vampire_spawn.json" },
]

[fields]
kind = "creature"
cr = "2"
creature_type = "undead"
subtypes = ["human"]
size = "Medium"
alignment = "NE"
ac = "20, touch 12, flat-footed 18 (+4 armor, +2 Dex, +4 natural)"
hp = "18 (2d8+6); fast healing 2"
fortitude = "+2"
reflex = "+5"
will = "+1"
melee = "slam +4 (1d4+4 plus energy drain)"
ranged = "dagger +3 (1d4+3/19-20)"
special_attacks = "blood drain, dominate (DC 13), energy drain (1 level, DC 13), sneak attack +1d6"
special_qualities = "gaseous form, rogue talents (strong impression), shadowless, spider climb, trapfinding +1"
abilities = ["17", "14", "-", "8", "12", "15"]
+++

::: statblock
CR: 2
XP: 600
Alignment: NE
Size: Medium
Type: Undead (human)
Race: human rogue 2
Init: +6
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +9
AC: 20, touch 12, flat-footed 18 (+4 armor, +2 Dex, +4 natural)
hp: 18 (2d8+6); [fast healing](ref/umr/fast-healing) 2
Fort: +2
Ref: +5
Will: +1
Defensive Abilities: [channel resistance](ref/rule/channel-resistance) +2, evasion
DR: 5/silver
Immune: undead traits
Resist: cold 10, electricity 10
Weaknesses: resurrection vulnerability, vampire weaknesses
Speed: 30 ft.
Melee: slam +4 (1d4+4 plus energy drain)
Ranged: dagger +3 (1d4+3/19-20)
Special Attacks: blood drain, dominate (DC 13), energy drain (1 level, DC 13), sneak attack +1d6
Ability Scores: Str 17, Dex 14, Con -, Int 8, Wis 12, Cha 15
Base Atk: +1
CMB: +4
CMD: 16
Feats: Improved Initiative, Intimidating Prowess, Power Attack, Skill Focus (Perception)
Skills: Acrobatics +13, Climb +6, Intimidate +10, Knowledge (local) +4, Perception +9, Sense Motive +6, Sleight of Hand +5, Stealth +13
Languages: Common, Halfling
SQ: gaseous form, rogue talents (strong impression), shadowless, spider climb, trapfinding +1
Environment: any
Organization: gang (2-8) or family (vampire plus 2-8)
Treasure: NPC Gear (chain shirt, dagger, other treasure)
:::

The following template can be used to create unique vampire spawn with class levels.

## Creating a Vampire Spawn {#creating-a-vampire-spawn}

"Vampire spawn" is an acquired template that can be added to any living creature with 4 or more Hit
Dice (referred to hereafter as the base creature). A vampire spawn uses the base creature's stats
and abilities except as noted here.

### CR {#cr}

::: paragraph statline
Same as the base creature + 1.
:::

### Alignment {#alignment}

::: paragraph statline
Any evil.
:::

### Type {#type}

::: paragraph statline
The creature's type changes to undead. Do not recalculate class Hit Dice, BAB, or saves.
:::

### Senses {#senses}

::: paragraph statline
A vampire spawn gains [darkvision](ref/rule/darkvision) to 60 feet.
:::

### Armor Class {#armor-class}

::: paragraph statline
Natural armor increases to +4, unless the base creature's natural armor is already +4 or higher.
:::

### Hit Dice {#hit-dice}

::: paragraph statline
Change all racial Hit Dice to d8s. Class Hit Dice are unaffected. As undead, vampire spawn use their
Cha modifier to determine bonus hit points (instead of Con).
:::

### Defensive Abilities {#defensive-abilities}

::: paragraph statline
A vampire spawn gains [channel resistance](ref/rule/channel-resistance) +2, DR 5/silver, resistance
10 against cold and electricity, and [fast healing](ref/umr/fast-healing) 2.
:::

### Weaknesses {#weaknesses}

::: paragraph statline
A vampire spawn has the same weaknesses of the vampire that created it.
:::

#### Resurrection Vulnerability {#resurrection-vulnerability}

::: statblock
Ability Type: Supernatural
:::

::: paragraph indented
: A _[raise dead](ref/spell/raise-dead)_ or similar spell cast on a vampire spawn destroys it (Will
negates). Using the spell in this way does not require a material component.
:::

### Melee {#melee}

::: paragraph statline
A vampire spawn gains a slam attack if the base creature didn't have one. Damage for the slam
depends on the vampire spawn's size (see _Bestiary_ 301).
:::

### Special Attacks {#special-attacks}

::: paragraph statline
A vampire spawn gains a vampire's blood drain and dominate special attacks. The vampire who created
the spawn can influence a spawn's dominated creature as if she had dominated it herself.
:::

#### Energy Drain {#energy-drain}

::: statblock
Ability Type: Supernatural
:::

::: paragraph indented
: A creature hit by a vampire spawn's slam (or other natural weapon) gains 1 negative level. This
ability only triggers only once per round.
:::

### Special Qualities {#special-qualities}

::: paragraph statline
A vampire spawn gains the gaseous form, shadowless, and spider climb abilities of a vampire.
:::

### Ability Scores {#ability-scores}

::: paragraph statline
Cha +2.
:::

### Skills {#skills}

::: paragraph statline
Spawn gain a +8 racial bonus on Acrobatics and Stealth checks.
:::

### Feats {#feats}

::: paragraph statline
Spawn gain Skill Focus (Perception) as a bonus feat.
:::
