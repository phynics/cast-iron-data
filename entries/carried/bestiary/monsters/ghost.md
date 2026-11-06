+++
id = "ref/carried/bestiary/monsters/ghost"
kind = "creature"
title = "Ghost"
source_ids = ["bestiary"]
section = ["Monsters"]
tags = ["undead", "augmented humanoid", "incorporeal", "medium"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Monsters/Ghost", path = "bestiary/creature/ghost.json" },
]

[fields]
kind = "creature"
cr = "7"
creature_type = "Undead"
subtypes = ["augmented humanoid", "incorporeal"]
size = "Medium"
alignment = "CE"
ac = "17, touch 17, flat-footed 15 (+1 Dex, +1 dodge, +5 deflection)"
hp = "73 (7d8+42)"
fortitude = "+7"
reflex = "+5"
will = "+7"
melee = "corrupting touch +6 (7d6, Fort. DC 18 half)"
special_attacks = "frightful moan (DC 18)"
abilities = ["-", "12", "-", "10", "11", "20"]
+++

::: statblock
CR: 7
XP: 3,200
Alignment: CE
Size: Medium
Type: Undead (augmented humanoid, incorporeal)
Race: human
Class Levels: aristocrat 7
Init: +5
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +18
AC: 17, touch 17, flat-footed 15 (+1 Dex, +1 dodge, +5 deflection)
hp: 73 (7d8+42)
Fort: +7
Ref: +5
Will: +7
Defensive Abilities: [channel resistance](ref/rule/channel-resistance) +4, incorporeal, rejuvenation
Immune: undead traits
Speed: fly 30 ft. (perfect)
Melee: corrupting touch +6 (7d6, Fort. DC 18 half)
Special Attacks: frightful moan (DC 18)
Ability Scores: Str -, Dex 12, Con -, Int 10, Wis 11, Cha 20
Base Atk: +5
CMB: +5
CMD: 22
Feats: Dodge, Improved Initiative, Iron Will, Lightning Reflexes, Toughness
Skills: Fly +9, Knowledge (history) +10, Knowledge (nobility) +10, Perception +18, Sense Motive +10, Stealth +9
Racial Modifiers: +8 Perception, +8 Stealth
Languages: Common
Environment: any
Organization: solitary
Treasure: NPC gear
:::

_This spectral, horrifying figure glides silently through the air, passing through solid objects as
if they didn't exist._

When a soul is not allowed to rest due to some great injustice, either real or perceived, it
sometimes comes back as a ghost. Such beings are in eternal anguish, lacking in substance and unable
to set things right. Although ghosts can be any alignment, the majority cling to the living world
out of a powerful sense of rage and hatred, and as a result are chaotic evil—even the ghost of a
good or lawful creature can become hateful and cruel in its afterlife.

More than most of the monsters in this book, a ghost benefits from a strong and detailed backstory.
Why did this character become a ghost? What are the legends surrounding the ghost? An encounter with
a ghost should never happen completely out of the blue—there are plenty of other incorporeal undead
like wraiths and spectres to fill that role. A proper encounter with a ghost should be a climactic
scene after a lengthy period of tension building with lesser minions or manifestations of the undead
spirit. The sample ghost above is that of a human princess who was murdered by an unfaithful
lover—after she confronted him, he murdered her by wrapping her in chains and throwing her into the
castle well, where she drowned. The ghost's abilities were selected to fit this backstory, and it
shows how potent a villain you can create with a simple NPC class. Applying the template to
creatures with class levels or creatures with significant racial abilities can create even more
powerful ghosts.

When a ghost is created, it retains incorporeal “copies” of any items that it particularly valued in
life (provided the originals are not in another creature's possession). The equipment works normally
for the ghost but passes harmlessly through material objects or creatures. A weapon of +1 or better
magical enhancement, however, can harm material creatures, but any such attack deals only half as
much damage (50%) unless it is a _ghost touch weapon_. A ghost can use shields or armor only if they
have the _ghost touch_ quality.

The original items remain behind, just as the ghost's physical remains do. If another creature
seizes the original, the incorporeal copy fades away. This loss invariably angers the ghost, who
stops at nothing to return the item to its original resting place (and thus regain the item's use).

## Creating a Ghost {#creating-a-ghost}

### Ghost {#ghost}

::: statblock
Abbrev: CR +2
:::

“Ghost” is an acquired template that can be added to any living creature that has a Charisma score
of at least 6. A ghost retains all the base creature's statistics and special abilities except as
noted here.

#### Challenge Rating {#challenge-rating}

Same as the base creature +2.

#### Type {#type}

The creature's type changes to undead. Do not recalculate the creature's base attack bonus, saves,
or skill points. It gains the incorporeal subtype.

#### Armor Class {#armor-class}

A ghost gains a deflection bonus equal to its Charisma modifier. It loses the base creature's
natural armor bonus, as well as all armor and shield bonuses not from force effects or _ghost touch_
items.

#### Hit Dice {#hit-dice}

Change all of the creature's racial Hit Dice to d8s. All Hit Dice derived from class levels remain
unchanged. Ghosts use their Charisma modifiers to determine bonus hit points (instead of
Constitution).

#### Defensive Abilities {#defensive-abilities}

::: statblock
Ability Type: Supernatural
:::

A ghost retains all of the defensive abilities of the base creature save those that rely on a
corporeal form to function. Ghosts gain [channel resistance](ref/rule/channel-resistance) +4,
[darkvision](ref/rule/darkvision) 60 ft., the incorporeal ability, and all of the immunities granted
by its undead traits. Ghosts also gain the rejuvenation ability.

::: paragraph indented
_Rejuvenation_ In most cases, it's difficult to destroy a ghost through simple combat: the
“destroyed” spirit restores itself in 2d4 days. Even the most powerful spells are usually only
temporary solutions. The only way to permanently destroy a ghost is to determine the reason for its
existence and set right whatever prevents it from resting in peace. The exact means varies with each
spirit and may require a good deal of research, and should be created specifically for each
different ghost by the GM.
:::

#### Speed {#speed}

Ghosts lose their previous speeds and gain a fly speed of 30 feet (perfect), unless the base
creature has a higher fly speed.

#### Melee and Ranged Attacks {#melee-and-ranged-attacks}

A ghost loses all of the base creature's attacks. If it could wield weapons in life, it can wield
_ghost touch weapons_ as a ghost.

#### Special Attacks {#special-attacks}

A ghost retains all the special attacks of the base creature, but any relying on physical contact do
not function. In addition, a ghost gains one ghost special attack from the list below for every 3
points of CR (minimum 1—the first ability chosen must always be corrupting touch). The save DC
against a ghost's special attack is equal to 10 + 1/2 ghost's HD + ghost's Charisma modifier unless
otherwise noted. Additional ghost abilities beyond these can be designed at the GM's discretion.

::: paragraph indented
_Corrupting Gaze (Su)_The ghost is disfigured through age or violence, and has a gaze attack with a
range of 30 feet that causes 2d10 damage and 1d4 Charisma damage (Fortitude save negates Charisma
damage but not physical damage).
:::

::: paragraph indented
_Corrupting Touch (Su)_All ghosts gain this incorporeal touch attack. By passing part of its
incorporeal body through a foe's body as a standard action, the ghost inflicts a number of d6s equal
to its CR in damage. This damage is not negative energy—it manifests in the form of physical wounds
and aches from supernatural aging. Creatures immune to magical aging are immune to this damage, but
otherwise the damage bypasses all forms of [damage reduction](ref/rule/damage-reduction). A
Fortitude save halves the damage inflicted.
:::

::: paragraph indented
_Draining Touch (Su)_The ghost died while insane or diseased. It gains a touch attack that drains
1d4 points from any one ability score it selects on a hit. On each such successful attack, the ghost
heals 5 points of damage to itself. When a ghost makes a draining touch attack, it cannot use its
standard ghostly touch attack.
:::

::: paragraph indented
_Frightful Moan (Su)_The ghost died in the throes of crippling terror. It can emit a frightful moan
as a standard action. All living creatures within a 30-foot spread must succeed on a Will save or
become panicked for 2d4 rounds. This is a sonic mind-affecting fear effect. A creature that
successfully saves against the moan cannot be affected by the same ghost's moan for 24 hours.
:::

::: paragraph indented
_Malevolence (Su)_The ghost's jealousy of the living is particularly potent. Once per round, the
ghost can merge its body with a creature on the Material Plane. This ability is similar to a
_[magic jar](ref/spell/magic-jar)_ spell (caster level 10th or the ghost's Hit Dice, whichever is
higher), except that it does not require a receptacle. To use this ability, the ghost must be
adjacent to the target. The target can resist the attack with a successful Will save. A creature
that successfully saves is immune to that same ghost's malevolence for 24 hours.
:::

::: paragraph indented
_Telekinesis (Su)_The ghost's death involved great physical trauma. The ghost can use
_[telekinesis](ref/spell/telekinesis)_ as a standard action once every 1d4 rounds (caster level 12th
or equal to the ghost's HD, whichever is higher).
:::

#### Abilities {#abilities}

Cha +4; as an incorporeal undead creature, a ghost has no Strength or Constitution score.

#### Skills {#skills}

Ghosts have a +8 racial bonus on Perception and Stealth skill checks. A ghost always treats Climb,
Disguise, Fly, Intimidate, Knowledge (arcana), Knowledge (religion), Perception, Sense Motive,
Spellcraft, and Stealth as class skills. Otherwise, skills are the same as the base creature.
