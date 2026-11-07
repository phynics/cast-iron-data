+++
id = "ref/carried/bestiary-3/monsters/graveknight"
kind = "creature"
title = "Graveknight"
source_ids = ["bestiary-3"]
section = ["Monsters"]
tags = ["undead", "augmented humanoid", "medium"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 3/Monsters/Graveknight", path = "bestiary_3/creature/graveknight.json" },
]

[fields]
kind = "creature"
cr = "11"
creature_type = "undead"
subtypes = ["augmented humanoid"]
size = "Medium"
alignment = "LE"
ac = "25, touch 11, flat-footed 24 (+10 armor, +1 Dex, +4 natural)"
hp = "139 (10d10+80)"
fortitude = "+13"
reflex = "+6"
will = "+6; +3 vs. fear"
melee = "+1 greatsword +25/+20 (2d6+19 plus 2d6 acid)"
ranged = "composite longbow +14/+9 (1d8+11/×3)"
special_attacks = "channel destruction, devastating blast (6d6 acid, DC 19), undead mastery (DC 19), weapon training (heavy blades +2, bows +1)"
special_qualities = "armor training 2, phantom mount, ruinous revivification"
abilities = ["27", "12", "-", "15", "12", "18"]
+++

::: statblock
CR: 11
XP: 12,800
Alignment: LE
Size: Medium
Type: Undead (augmented humanoid)
Race: human
Class Levels: fighter 10
Init: +5
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +19
Aura: sacrilegious aura (30 ft., DC 19)
AC: 25, touch 11, flat-footed 24 (+10 armor, +1 Dex, +4 natural)
hp: 139 (10d10+80)
Fort: +13
Ref: +6
Will: +6; +3 vs. fear
Defensive Abilities: bravery +3, [channel resistance](ref/rule/channel-resistance) +4, rejuvenation
DR: 10/magic
Immune: acid, cold, electricity, undead traits
SR: 22
Speed: 30 ft.
Melee: +1 greatsword +25/+20 (2d6+19 plus 2d6 acid)
Ranged: composite longbow +14/+9 (1d8+11/×3)
Special Attacks: channel destruction, devastating blast (6d6 acid, DC 19), undead mastery (DC 19), weapon training (heavy blades +2, bows +1)
Ability Scores: Str 27, Dex 12, Con -, Int 15, Wis 12, Cha 18
Base Atk: +10
CMB: +20
CMD: 29
Feats: Cleave, Critical Focus, Dazzling Display, Greater Weapon Focus (greatsword), Improved InitiativeB, Mounted CombatB, Power Attack, Ride-By Attack^B^, Shatter Defenses, Spirited Charge, ToughnessB, Trample, Unseat, Vital Strike, Weapon Focus (greatsword), Weapon Specialization (greatsword)
Skills: Climb +13, Intimidate +25, Knowledge (nobility) +12, Perception +19, Ride +19, Swim +13
Racial Modifiers: +8 Intimidate, +8 Perception, +8 Ride
Languages: Common, Dwarven, Infernal
SQ: armor training 2, phantom mount, ruinous revivification
Environment: any land
Organization: solitary or troop (graveknight plus 12-24 skeletal champions)
Treasure: NPC gear (+1 full plate, +1 greatsword, composite longbow \[+8 Str\] with 20 arrows, belt of giant strength +2, other treasure)
:::

_Shadows veil what lurks within the dark, imposing armor of this figure, though two piercing eyes
gaze from its closed visor._

Undying tyrants and eternal champions of the undead, graveknights arise from the corpses of the most
nefarious warlords and disgraced heroes—villains too merciless to submit to the shackles of death.
They bear the same weapons and regalia they did in life, though warped or empowered by their profane
resurrection. The legions they once held also flock to them in death, ready to serve their wicked
ambitions once more. A graveknight's essence is fundamentally tied to its armor, the bloodstained
trappings of its battle lust. This armor becomes an icon of its perverse natures, transforming into
a monstrous second skin over the husk of desiccated flesh and scarred bone locked within.

## Creating a Graveknight {#creating-a-graveknight}

### Graveknight {#graveknight}

::: statblock
Abbrev: CR +2
:::

“Graveknight” is an acquired template that can be added to any living creature with 5 or more Hit
Dice (referred to hereafter as the base creature). Most graveknights were once humanoids. A
graveknight uses the base creature's statistics and abilities except as noted here.

#### Challenge Rating {#challenge-rating}

Same as base creature +2.

#### Alignment {#alignment}

Any evil.

#### Type {#type}

The graveknight's type changes to undead (augmented). Do not recalculate class Hit Dice, BAB, or
saves.

#### Senses {#senses}

A graveknight gains [darkvision](ref/rule/darkvision) 60 ft.

#### Aura {#aura}

::: statblock
Ability Type: Supernatural
:::

A graveknight emanates the following aura.

_Sacrilegious Aura_ A graveknight constantly exudes an aura of intense evil and negative energy in a
30-foot radius. This aura functions as the spell _[desecrate](ref/spell/desecrate)_ and uses the
graveknight's armor as an altar of sorts to double the effects granted. The graveknight constantly
gains the benefits of this effect (including the bonus hit points, as this aura is part of the
graveknight's creation). In addition, this miasma of fell energies hinders the channeling of
positive energy. Any creature that attempts to summon positive energy in this area—such as through a
cleric's channel energy ability, a paladin's lay on hands, or any spell with the healing
subtype—must make a concentration check with a DC equal to 10 + 1/2 the graveknight's Hit Dice + the
graveknight's Charisma modifier. If the character fails, the effect is expended but does not
function.

#### Armor Class {#armor-class}

Natural armor improves by +4.

#### Hit Dice {#hit-dice}

Change all racial Hit Dice to d8s. Class Hit Dice are unaffected. As an undead, a graveknight uses
its Charisma modifier to determine bonus hit points.

#### Defensive Abilities {#defensive-abilities}

::: statblock
Ability Type: Supernatural
:::

A graveknight gains [channel resistance](ref/rule/channel-resistance) +4; DR 10/magic; and immunity
to cold, electricity, and any additional energy type noted by its ruinous revivification special
quality. A graveknight also gains [spell resistance](ref/rule/spell-resistance) equal to its
augmented CR + 11.

The graveknight also gains the following ability.

::: paragraph indented
_Rejuvenation_ One day after a graveknight is destroyed, its armor begins to rebuild the undead
horror's body. This process takes 1d10 days—if the body is destroyed before that time passes, the
armor merely starts the process anew. After this time has elapsed, the graveknight wakens fully
healed.
:::

#### Attacks {#attacks}

A graveknight gains a slam attack if the base creature didn't have one. Damage for the slam depends
on the graveknight's size (see _Bestiary_ 302).

#### Special Attacks {#special-attacks}

::: statblock
Ability Type: Supernatural
:::

A graveknight gains the following special attacks. Save DCs are equal to 10 + 1/2 the graveknight's
HD + the graveknight's Charisma modifier unless otherwise noted.

::: paragraph indented
_Channel Destruction_ Any weapon a graveknight wields seethes with energy, and deals an additional
1d6 points of damage for every 4 Hit Dice the graveknight has. This additional damage is of the
energy type determined by the ruinous revivification special quality.
:::

::: paragraph indented
_Devastating Blast (Su)_Three times per day, the graveknight may unleash a 30-foot cone of energy as
a standard action. This blast deals 2d6 points of damage for every 3 Hit Dice a graveknight has
(Reflex for half). This damage is of the energy type determined by the graveknight's ruinous
revivification special quality.
:::

::: paragraph indented
_Undead Mastery (Su)_As a standard action, a graveknight can attempt to bend any undead creature
within 50 feet to its will. The targeted undead must succeed at a Will save or fall under the
graveknight's control. This control is permanent for unintelligent undead; an undead with an
Intelligence score is allowed an additional save every day to break free from the graveknight's
control. A creature that successfully saves cannot be affected again by the same graveknight's
undead mastery for 24 hours.
:::

A graveknight can control 5 Hit Dice of undead creatures for every Hit Die it has. If the
graveknight exceeds this number, the excess from earlier uses of the ability becomes uncontrolled,
as per _[animate dead](ref/spell/animate-dead)_.

#### Special Qualities {#special-qualities}

::: statblock
Ability Type: Supernatural
:::

A graveknight gains the following.

::: paragraph indented
_Phantom Mount_ Once per hour, a graveknight can summon a skeletal horse similar to a
_[phantom steed](ref/spell/phantom-steed)_. This mount is more real than a typical
_[phantom steed](ref/spell/phantom-steed)_, and can carry one additional rider. The mount's powers
are based on the graveknight's total Hit Dice rather than caster level. A graveknight's mount looks
distinctive and always appears the same each time it is summoned. If the mount is destroyed, it can
be summoned again with full hit points 1 hour later.
:::

::: paragraph indented
_Ruinous Revivification (Su)_At the time of its creation, the graveknight chooses one of the
following energy types: acid, cold, electricity, or fire. This energy type should be relevant to the
graveknight's life or death, defaulting to fire if none are especially appropriate. This energy type
influences the effects of several of a graveknight's special abilities.
:::

#### Ability Scores {#ability-scores}

Str +6, Int +2, Wis +4, Cha +4. As an undead creature, a graveknight has no Constitution score.

#### Skills {#skills}

Graveknights gain a +8 racial bonus on Intimidate, Perception, and Ride checks.

#### Feats {#feats}

Graveknights gain Improved Initiative, Mounted Combat, Ride-By Attack, and Toughness as bonus feats.

## Graveknight Armor {#graveknight-armor}

In death, the graveknight's life force lingers on in its armor, not its corpse, in much the same way
that a lich's essence is bound within a phylactery. Unless every part of a graveknight's armor is
ruined along with its body, a graveknight can rejuvenate after it is destroyed. A typical suit of
full plate graveknight armor has [hardness](ref/umr/hardness) 10 and 45 hit points, though armor
with enhancements or made of special materials proves more difficult to destroy. Merely breaking a
graveknight's armor does not destroy it; it must be ruined, such as by being disintegrated, taken to
the Positive Energy Plane, or thrown into the heart of a volcano.
