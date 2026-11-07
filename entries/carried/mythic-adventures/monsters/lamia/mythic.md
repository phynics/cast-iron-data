+++
id = "ref/carried/mythic-adventures/monsters/lamia/mythic"
kind = "creature"
title = "Lamia, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Lamia"]
tags = ["monstrous humanoid", "mythic", "shapechanger", "large"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Lamia/Mythic", path = "mythic_adventures/creature/mythic/lamia_mythic.json" },
]

[fields]
kind = "creature"
cr = "7"
creature_type = "monstrousHumanoid"
subtypes = ["mythic", "shapechanger"]
size = "Large"
alignment = "CE"
ac = "24, touch 14, flat-footed 19 (+3 Dex, +2 dodge, +10 natural, -1 size)"
hp = "97 (9d10+48)"
fortitude = "+7"
reflex = "+9"
will = "+11"
melee = "+1 scimitar +13/+8 (1d6+5/18-20), 2 claws +12 (1d4+2), touch +7 (1d4 Wisdom drain)"
special_attacks = "mythic power (3/day, surge +1d6), pounce, Wisdom drain"
special_qualities = "change shape (giant constrictor snake, lamia matriarch, or lion; polymorph), undersized weapons"
abilities = ["18", "16", "14", "13", "17", "15"]
+++

::: statblock
CR: 7
XP: 3,200
Alignment: CE
Size: Large
Type: Monstrous Humanoid (mythic, shapechanger)
Init: +3
Senses: [darkvision](ref/rule/darkvision) 60 ft., [low-light vision](ref/rule/low-light-vision); Perception +15
Aura: seduction (DC 16)
AC: 24, touch 14, flat-footed 19 (+3 Dex, +2 dodge, +10 natural, -1 size)
hp: 97 (9d10+48)
Fort: +7
Ref: +9
Will: +11
DR: 5/epic
Speed: 60 ft.
Melee: +1 scimitar +13/+8 (1d6+5/18-20), 2 claws +12 (1d4+2), touch +7 (1d4 Wisdom drain)
Space: 10 ft.
Reach: 5 ft.
Special Attacks: mythic power (3/day, surge +1d6), pounce, Wisdom drain
Spell-like abilities: (CL 9th; concentration +11)\
At will-_[disguise self](ref/spell/disguise-self)_, _[ventriloquism](ref/spell/ventriloquism)_\
3/day-_[charm monster](ref/spell/charm-monster)_ (DC 16), _[major image](ref/spell/major-image)_ (DC 15), _[mirror image](ref/spell/mirror-image)_, _[suggestion](ref/spell/suggestion)_ (DC 15)\
1/day-_[deep slumber](ref/spell/deep-slumber)_ (DC 15)
Sorcerer spells known: (CL 6th; concentration +8)\
3rd (3/day)-_[haste](ref/spell/haste)_\
2nd (6/day)-_[death knell](ref/spell/death-knell)_ (DC 14), _invisibility_\
1st (7/day)-_[cure light wounds](ref/spell/cure-light-wounds)_, _[divine favor](ref/spell/divine-favor)_, _[mage armor](ref/spell/mage-armor)_, _[magic missile](ref/spell/magic-missile)_\
0 (at will)-_[dancing lights](ref/spell/dancing-lights)_, _[daze](ref/spell/daze)_ (DC 12), _[detect magic](ref/spell/detect-magic)_, _[ghost sound](ref/spell/ghost-sound)_ (DC 12), _[mage hand](ref/spell/mage-hand)_, _[mending](ref/spell/mending)_, _[prestidigitation](ref/spell/prestidigitation)_
Ability Scores: Str 18, Dex 16, Con 14, Int 13, Wis 17, Cha 15
Base Atk: +9
CMB: +14
CMD: 28 (32 vs. trip)
Feats: DodgeM, Great Fortitude, Iron Will, Mobility, Spring AttackM
Skills: Bluff +10, Diplomacy +5, Disguise +7, Intimidate +11, Knowledge (religion) +4, Perception +15, Stealth +15, Survival +12
Racial Modifiers: +4 Bluff, +4 Stealth
Languages: Abyssal, Common
SQ: change shape (giant constrictor snake, lamia matriarch, or lion; polymorph), undersized weapons
Environment: temperate desert
Organization: solitary, pair, or cult (3-12)
Treasure: double (+1 scimitar, other treasure)
MR: 3
:::

_This creature has the head and upper body of a beautiful woman, the lower body of a lion, and long,
serpentine tail._

## Special Abilities {#special-abilities}

### Aura of Seduction {#aura-of-seduction}

::: statblock
Ability Type: Supernatural
:::

Any creature within 30 feet of a mythic lamia must succeed at a DC 16 Will save or become
fascinated. A creature that succeeds at this save is immune to the lamia's aura for 24 hours. This
is a mind-affecting effect. The save DC is Charisma-based.

### Spells {#spells}

A mythic lamia casts spells as a 6th-level sorcerer, and can cast spells from the cleric list as
well as those normally available to a sorcerer. Cleric spells are considered arcane spells for a
mythic lamia.

### Wisdom Drain {#wisdom-drain}

::: statblock
Ability Type: Supernatural
:::

A lamia drains 1d4 points of Wisdom each time she hits with her melee touch attack. (Unlike with
other kinds of ability drain attacks, a lamia does not heal any damage when she uses her Wisdom
drain.) Lamias try to use this power early in an encounter to make foes more susceptible to charm
monster and suggestion.

A mythic lamia dabbled in dark pacts or strange magic in an attempt to break the ancient curse that
gives her a monstrous form, but instead gained the ability to change her shape as well as other
magical abilities. Impressed by her progress but angered by her lack of complete success, she
continues her research and plotting.

## Lamia Matriarch {#lamia-matriarch}

In most cases, a mythic lamia will permanently transform into a lamia matriarch, losing her mythic
power as she stabilizes in that form. A lamia matriarch that gains mythic power gains the mythic
lamia's aura of seduction, a tail slap attack, grab, and constrict. She increases her sorcerer
caster level to 8th and usually learns spells that aid her minions, such as
_[freedom of movement](ref/spell/freedom-of-movement)_ and _rage_. She may use her touch attack to
drain Wisdom or drain one use of mythic power from the target and regain one of her own uses of
mythic power (save negates).
