+++
id = "ref/carried/mythic-adventures/monsters/mummy/mythic"
kind = "creature"
title = "Mummy, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Mummy"]
tags = ["undead", "mythic", "medium"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Mummy/Mythic", path = "mythic_adventures/creature/mythic/mummy_mythic.json" },
]

[fields]
kind = "creature"
cr = "7"
creature_type = "Undead"
subtypes = ["mythic"]
size = "Medium"
alignment = "LE"
ac = "23, touch 10, flat-footed 23 (+13 natural)"
hp = "92 (8d8+56); fast healing 5"
fortitude = "+4"
reflex = "+2"
will = "+8"
melee = "slam +15 (1d8+12 plus mummy rot)"
special_attacks = "create spawn, mythic power (3/day, surge +1d6)"
special_qualities = "change shape (any humanoid; alter self), desert mastery"
abilities = ["26", "10", "-", "6", "15", "15"]
+++

::: statblock
CR: 7
XP: 3,200
Alignment: LE
Size: Medium
Type: Undead (mythic)
Init: +0
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +16
Aura: despair (30 ft., paralyzed for 1d4 rounds, Will DC 16 negates)
AC: 23, touch 10, flat-footed 23 (+13 natural)
hp: 92 (8d8+56); [fast healing](ref/umr/fast-healing) 5
Fort: +4
Ref: +2
Will: +8
DR: 5/-
Immune: undead traits
Weaknesses: vulnerable to fire
Speed: 20 ft.
Melee: slam +15 (1d8+12 plus mummy rot)
Special Attacks: create spawn, mythic power (3/day, surge +1d6)
Ability Scores: Str 26, Dex 10, Con -, Int 6, Wis 15, Cha 15
Base Atk: +6
CMB: +14
CMD: 24
Feats: Power AttackM, Skill Focus (Perception), ToughnessM, Weapon Focus (slam)
Skills: Perception +16, Stealth +11
Languages: Common
SQ: change shape (any humanoid; alter self), desert mastery
Environment: any
Organization: solitary, warden squad (2-6), or guardian detail (7-12)
Treasure: standard
MR: 3
:::

_This regal mummy reeks of preservative spices and wears the clothing and jewelry of a wealthy
pharaoh._

## Special Abilities {#special-abilities}

### Create Spawn {#create-spawn}

::: statblock
Ability Type: Supernatural
:::

As a swift action, a mythic mummy can expend one use of mythic power to transform a slain opponent
into a non-mythic mummy with the advanced simple template. The new mummy is under the command of the
mummy that created it, and remains enslaved until the mythic mummy's death, at which time it becomes
a free-willed creature. The spawn retains none of the abilities it had in life

### Desert Mastery {#desert-mastery}

::: statblock
Ability Type: Supernatural
:::

A mythic mummy can command earth and sand within 100 feet to create a variety of spell-like effects.
As a standard action, a mummy can reduce rock to sand (as transmute rock to mud) or create lifelike
shapes made from sand (as major image, though these shapes collapse if disbelieved or attacked). The
mummy can expend one use of mythic power to summon a giant advanced sandman. The mummy's caster
level equals its Hit Dice for these effects.

### Despair {#despair}

::: statblock
Ability Type: Supernatural
:::

All creatures within a 30-foot radius that see a mummy must succeed at a DC 18 Will save or be
paralyzed by fear for 1d4 rounds. A creature only has to attempt this save against a particular
mummy's despair ability once every 24 hours. This is a paralysis and mind-affecting fear effect. The
save DC is Charisma-based and includes a +2 racial bonus.

### Mummy Rot {#mummy-rot}

::: statblock
Ability Type: Supernatural
:::

Curse and disease—slam; save Fort DC 18; onset 1 minute; frequency 1/day; effect 1d6 Con and 1d6
Cha; cure —. This otherwise functions like standard mummy rot. The DC is Charisma-based and includes
a +2 racial bonus.

A mythic mummy is the preserved and animated remains or royalty—the honored dead a common mummy is
compelled to protect. Wielding powers over sand and able to create new minions to replace the
fallen, a mythic mummy is a formidable opponent. Its used to absolute obedience from living and
undead subjects. If awakened from its eternal rest, a mythic mummy uses its magic to appear as it
did in life, though if angered or surprised it may reveal its undead form.
