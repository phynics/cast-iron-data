+++
id = "ref/carried/mythic-adventures/monsters/demon/vrock/mythic"
kind = "creature"
title = "Demon, Vrock, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Demon", "Vrock"]
tags = ["outsider", "chaotic", "demon", "evil", "extraplanar", "mythic", "large"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Demon/Vrock/Mythic", path = "mythic_adventures/creature/mythic/demon_vrock_mythic.json" },
]

[fields]
kind = "creature"
cr = "11"
creature_type = "Outsider"
subtypes = ["chaotic", "demon", "evil", "extraplanar", "mythic"]
size = "Large"
alignment = "CE"
ac = "27, touch 12, flat-footed 24 (+3 Dex, +15 natural, -1 size)"
hp = "152 (9d10+103)"
fortitude = "+13"
reflex = "+11"
will = "+6"
melee = "bite +14 (1d8+6 plus bleed), 2 claws +14 (2d6+6 plus bleed), 2 talons +14 (1d6+6 plus bleed)"
special_attacks = "bleed (1d6), entrapping vines, greater stunning screech, manic dance of ruin, mythic power (4/day, surge +1d8)"
abilities = ["23", "17", "25", "14", "16", "16"]
+++

::: statblock
CR: 11
XP: 12,800
Alignment: CE
Size: Large
Type: Outsider (chaotic, demon, evil, extraplanar, mythic)
Init: +7
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +23
AC: 27, touch 12, flat-footed 24 (+3 Dex, +15 natural, -1 size)
hp: 152 (9d10+103)
Fort: +13
Ref: +11
Will: +6
DR: 10/epic and good
Immune: electricity, poison
Resist: acid 10, cold 10, fire 10
SR: 22
Speed: 30 ft., fly 50 ft. (average)
Melee: bite +14 (1d8+6 plus bleed), 2 claws +14 (2d6+6 plus bleed), 2 talons +14 (1d6+6 plus bleed)
Space: 10 ft.
Reach: 10 ft.
Special Attacks: bleed (1d6), entrapping vines, greater stunning screech, manic dance of ruin, mythic power (4/day, surge +1d8)
Spell-like abilities: (CL 12th; concentration +15)\
At will-_[greater teleport](ref/spell/teleport-greater)_ (self plus 50 lbs. of objects only), _[telekinesis](ref/spell/telekinesis)_ (DC 18)\
1/day-_[heroism](ref/spell/heroism)_, _[mirror image](ref/spell/mirror-image)_, summon (level 3, 1 vrock 35%)
Ability Scores: Str 23, Dex 17, Con 25, Int 14, Wis 16, Cha 16
Base Atk: +9
CMB: +16
CMD: 29
Feats: CleaveM, Combat ReflexesM, Improved Initiative, Lightning Reflexes, Power Attack, Stand StillB
Skills: Fly +13, Intimidate +15, Knowledge (planes) +14, Perception +23, Sense Motive +15, Spellcraft +14, Stealth +11, Survival +15
Racial Modifiers: +8 Perception
Languages: Abyssal, Celestial, Common; telepathy 100 ft.
Environment: any (Abyss)
Organization: solitary, pair, or gang (3-10)
Treasure: standard
MR: 4
:::

_This vulture-headed demon has great filthy wings, and a beak and claws ready to rip and tear._

## Special Abilities {#special-abilities}

### Entrapping Vines {#entrapping-vines}

::: statblock
Ability Type: Extraordinary
:::

A mythic vrock can expend one use of mythic power as a swift action to release a cloud of spores
from its body, affecting all adjacent non-demons. The spores deal 2d8 points of damage on the first
round as they grow into ugly vines; for the next 10 rounds, they deal 1d6 points of damage and
entrap the affected creatures (DC 21, 10 rounds, [hardness](ref/umr/hardness) 5, hp 10). The vines
can be destroyed by casting bless on the creatures or by sprinkling them with holy water. This is a
disease effect. The save DC is Constitution-based.

### Greater Stunning Screech {#greater-stunning-screech}

::: statblock
Ability Type: Supernatural
:::

Once per hour, a mythic vrock can emit a shrill screech. All non-demons within a 30-foot-radius
spread must succeed at a DC 21 Fortitude save or be stunned for 1 round. If the vrock expends one
use of mythic power, any creature that fails its save is staggered for 1d6 rounds after the stun
ends. The save DC is Constitution-based.

### Manic Dance of Ruin {#manic-dance-of-ruin}

::: statblock
Ability Type: Supernatural
:::

A mythic vrock can expend one use of mythic power to dance and chant as a full-round action, after
which it releases a crackling wave of energy, dealing 5d6 points of electricity damage to all
creatures within 100 feet (Reflex DC 17 for half). Each additional vrock that joins in the dance
adds 1 to the DC and an additional 5d6 points of damage, up to a maximum of 20d6. The dance
immediately ends and must be started anew if any of the participating vrocks is slain, stunned, or
otherwise prevented from dancing. The save DC is Charisma-based.

A mythic vrock is a violent creature of unrestrained rage that takes out its anger on anything
weaker than itself.
