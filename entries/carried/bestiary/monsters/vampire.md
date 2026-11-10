+++
id = "ref/carried/bestiary/monsters/vampire"
kind = "creature"
title = "Vampire"
aon = "MonsterDisplay.aspx?ItemName=Vampire"
source_ids = ["bestiary"]
section = ["Monsters"]
tags = ["undead", "augmented humanoid", "medium"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Monsters/Vampire", path = "bestiary/creature/vampire.json" },
]

[fields]
kind = "creature"
cr = "9"
creature_type = "undead"
subtypes = ["augmented humanoid"]
size = "Medium"
alignment = "CE"
ac = "23, touch 17, flat-footed 18 (+2 deflection, +4 Dex, +1 dodge, +6 natural)"
hp = "102 (8d6+72); fast healing 5"
fortitude = "+13"
reflex = "+11"
will = "+12"
melee = "slam +8 (1d4+4 plus energy drain)"
special_attacks = "blood drain, children of the night, create spawn, dominate (DC 22), energy drain (2 levels, DC 22)"
special_qualities = "change shape (dire bat or wolf, beast shape II), gaseous form, shadowless, spider climb"
abilities = ["16", "18", "-", "14", "16", "26"]
+++

::: statblock
CR: 9
XP: 6,400
Alignment: CE
Size: Medium
Type: Undead (augmented humanoid)
Race: human
Sex: female
Class Levels: sorcerer 8
Init: +8
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +13
AC: 23, touch 17, flat-footed 18 (+2 deflection, +4 Dex, +1 dodge, +6 natural)
hp: 102 (8d6+72); [fast healing](ref/umr/fast-healing) 5
Fort: +13
Ref: +11
Will: +12
Defensive Abilities: [channel resistance](ref/rule/channel-resistance) +4
DR: 10/magic and silver
Immune: undead traits
Resist: cold 10, electricity 10
Weaknesses: vampire weaknesses
Speed: 30 ft.
Melee: slam +8 (1d4+4 plus energy drain)
Special Attacks: blood drain, children of the night, create spawn, dominate (DC 22), energy drain (2 levels, DC 22)
Sorcerer spells known: (CL 8th, +8 ranged touch)\
4th (5/day)-_[greater invisibility](ref/spell/invisibility-greater)_\
3rd (5/day)-_[dispel magic](ref/spell/dispel-magic)_, _[fireball](ref/spell/fireball)_ (DC 21), _[vampiric touch](ref/spell/vampiric-touch)_\
2nd (8/day)-_[false life](ref/spell/false-life)_, _invisibility_, _[scorching ray](ref/spell/scorching-ray)_, _web_ (DC 20)\
1st (8/day)-_[burning hands](ref/spell/burning-hands)_ (DC 19), _[chill touch](ref/spell/chill-touch)_ (DC 19), _[disguise self](ref/spell/disguise-self)_, _[expeditious retreat](ref/spell/expeditious-retreat)_, _[mage armor](ref/spell/mage-armor)_, _[magic missile](ref/spell/magic-missile)_\
0-_[acid splash](ref/spell/acid-splash)_, _[detect magic](ref/spell/detect-magic)_, _[light](ref/spell/light)_, _[mage hand](ref/spell/mage-hand)_, _[mending](ref/spell/mending)_, _[message](ref/spell/message)_, _[open/close](ref/spell/open-close)_, _[read magic](ref/spell/read-magic)_\
**Bloodline** undead
Bloodline spell-like ability: (CL 8th, +7 touch); 11/day-grave touch
Ability Scores: Str 16, Dex 18, Con -, Int 14, Wis 16, Cha 26
Base Atk: +4
CMB: +7
CMD: 24
Feats: AlertnessB, Blind-Fight, Combat Casting, Combat ReflexesB, DodgeB, Eschew Materials, Extend Spell, Improved InitiativeB, Lightning ReflexesB, Silent Spell, Still Spell, ToughnessB, Weapon Finesse
Skills: Bluff +27, Knowledge (arcana) +13, Knowledge (religion) +10, Perception +21, Sense Motive +13, Spellcraft +13, Stealth +12, Use Magic Device +19
Racial Modifiers: +8 Bluff,+8 Perception, +8 Sense Motive, +8 Stealth
Languages: Abyssal, Common, Draconic
SQ: change shape (dire bat or wolf, beast shape II), gaseous form, shadowless, spider climb
Environment: any
Organization: solitary or family (vampire plus 2-8 spawn)
Treasure: NPC gear (cloak of resistance +3, headband of alluring charisma +4, ring of protection +2)
:::

_This alluring, raven-haired beauty casually wipes a trickle of blood from a pale cheek, then smiles
to reveal needle-sharp fangs._

Vampires are undead humanoid creatures that feed on the blood of the living. They look much as they
did in life, often becoming more attractive, though some have a hardened, feral look instead.

## Creating a Vampire {#creating-a-vampire}

### Vampire {#vampire}

::: statblock
Abbrev: CR +2
:::

“Vampire” is an acquired template that can be added to any living creature with 5 or more Hit Dice
(referred to hereafter as the base creature). Most vampires were once humanoids, fey, or monstrous
humanoids. A vampire uses the base creature's stats and abilities except as noted here.

#### Challenge Rating {#challenge-rating}

Same as the base creature + 2.

#### AL {#al}

Any evil.

#### Type {#type}

The creature's type changes to undead (augmented). Do not recalculate class Hit Dice, BAB, or saves.

#### Senses {#senses}

A vampire gains [darkvision](ref/rule/darkvision) 60 ft.

#### Armor Class {#armor-class}

Natural armor improves by +6.

#### Hit Dice {#hit-dice}

Change all racial Hit Dice to d8s. Class Hit Dice are unaffected. As undead, vampires use their
Charisma modifier to determine bonus hit points (instead of Constitution).

#### Defensive Abilities {#defensive-abilities}

A vampire gains [channel resistance](ref/rule/channel-resistance) +4, DR 10/magic and silver, and
resistance to cold 10 and electricity 10, in addition to all of the defensive abilities granted by
the undead type. A vampire also gains [fast healing](ref/umr/fast-healing) 5. If reduced to 0 hit
points in combat, a vampire assumes gaseous form (see below) and attempts to escape. It must reach
its coffin home within 2 hours or be utterly destroyed. (It can normally travel up to 9 miles in 2
hours.) Additional damage dealt to a vampire forced into gaseous form has no effect. Once at rest,
the vampire is helpless. It regains 1 hit point after 1 hour, then is no longer helpless and resumes
healing at the rate of 5 hit points per round.

#### Weaknesses {#weaknesses}

Vampires cannot tolerate the strong odor of garlic and will not enter an area laced with it.
Similarly, they recoil from mirrors or strongly presented holy symbols. These things don't harm the
vampire—they merely keep it at bay. A recoiling vampire must stay at least 5 feet away from the
mirror or holy symbol and cannot touch or make melee attacks against that creature. Holding a
vampire at bay takes a standard action. After 1 round, a vampire can overcome its revulsion of the
object and function normally each round it makes a DC 25 Will save.

Vampires cannot enter a private home or dwelling unless invited in by someone with the authority to
do so.

Reducing a vampire's hit points to 0 or lower incapacitates it but doesn't always destroy it (see
[fast healing](ref/umr/fast-healing)). However, certain attacks can slay vampires. Exposing any
vampire to direct sunlight staggers it on the first round of exposure and destroys it utterly on the
second consecutive round of exposure if it does not escape. Each round of immersion in running water
inflicts damage on a vampire equal to one-third of its maximum hit points—a vampire reduced to 0 hit
points in this manner is destroyed. Driving a wooden stake through a helpless vampire's heart
instantly slays it (this is a full-round action). However, it returns to life if the stake is
removed, unless the head is also severed and anointed with holy water.

#### Speed {#speed}

Same as the base creature. If the base creature has a swim speed, the vampire is not unduly harmed
by running water.

#### Melee {#melee}

A vampire gains a slam attack if the base creature didn't have one. Damage for the slam depends on
the vampire's size (see Natural Attacks). Its slam also causes energy drain (see below). Its natural
weapons are treated as magic weapons for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction).

#### Special Attacks {#special-attacks}

::: statblock
Ability Type: Supernatural
:::

A vampire gains several special attacks. Save DCs are equal to 10 + 1/2 vampire's HD + vampire's Cha
modifier unless otherwise noted.

::: paragraph indented
_[Blood Drain](ref/carried/bestiary/rules/universal-monster-rules/blood-drain)_ A vampire can suck
blood from a grappled opponent; if the vampire establishes or maintains a pin, it drains blood,
dealing 1d4 points of Constitution damage. The vampire heals 5 hit points or gains 5 temporary hit
points for 1 hour (up to a maximum number of temporary hit points equal to its full normal hit
points) each round it drains blood.
:::

::: paragraph indented
_Children of the Night (Su)_Once per day, a vampire can call forth 1d6+1 rat swarms, 1d4+1 bat
swarms, or 2d6 wolves as a standard action. (If the base creature is not terrestrial, this power
might summon other creatures of similar power.) These creatures arrive in 2d6 rounds and serve the
vampire for up to 1 hour.
:::

::: paragraph indented
_Create Spawn (Su)_A vampire can create spawn out of those it slays with blood drain or energy
drain, provided that the slain creature is of the same creature type as the vampire's base creature
type. The victim rises from death as a vampire in 1d4 days. This vampire is under the command of the
vampire that created it, and remains enslaved until its master's destruction. A vampire may have
enslaved spawn totaling no more than twice its own Hit Dice; any spawn it creates that would exceed
this limit become free-willed undead. A vampire may free an enslaved spawn in order to enslave a new
spawn, but once freed, a vampire or vampire spawn cannot be enslaved again.
:::

::: paragraph indented
_Dominate (Su)_A vampire can crush a humanoid opponent's will as a standard action. Anyone the
vampire targets must succeed on a Will save or fall instantly under the vampire's influence, as
though by a _[dominate person](ref/spell/dominate-person)_ spell (caster level 12th). The ability
has a range of 30 feet. At the GM's discretion, some vampires might be able to affect different
creature types with this power.
:::

::: paragraph indented
_Energy Drain (Su)_A creature hit by a vampire's slam (or other natural weapon) gains two negative
levels. This ability only triggers once per round, regardless of the number of attacks a vampire
makes.
:::

#### Special Qualities {#special-qualities}

::: statblock
Ability Type: Supernatural
:::

A vampire gains the following.

::: paragraph indented
_[Change Shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape)_ A vampire can use
change shape to assume the form of a dire bat or wolf, as
_[beast shape II](ref/spell/beast-shape-2)_.
:::

::: paragraph indented
_Gaseous Form (Su)_As a standard action, a vampire can assume
_[gaseous form](ref/spell/gaseous-form)_ at will (caster level 5th), but it can remain gaseous
indefinitely and has a fly speed of 20 feet with perfect maneuverability.
:::

::: paragraph indented
_Shadowless (Ex)_A vampire casts no shadows and shows no reflection in a mirror.
:::

::: paragraph indented
_Spider Climb (Ex)_A vampire can climb sheer surfaces as though under the effects of a
_[spider climb](ref/spell/spider-climb)_ spell.
:::

#### Ability Scores {#ability-scores}

Str +6, Dex +4, Int +2, Wis +2, Cha +4. As an undead creature, a vampire has no Constitution score.

#### Skills {#skills}

Vampires gain a +8 racial bonus on Bluff, Perception, Sense Motive, and Stealth checks.

#### Feats {#feats}

Vampires gain Alertness, Combat Reflexes, Dodge, Improved Initiative, Lightning Reflexes, and
Toughness as bonus feats.

## Vampire Spawn {#vampire-spawn}

A vampire can elect to create a vampire spawn instead of a full-fledged vampire when she uses her
create spawn ability on a humanoid creature only. This decision must be made as a free action
whenever a vampire slays an appropriate creature by using blood drain or energy drain. A vampire
spawn's statistics are identical to those of a wight, save for the following changes.

- It gains the blood drain and dominate vampire special attacks.
- It gains [channel resistance](ref/rule/channel-resistance) +2, DR 5/silver, resist cold and
  electricity 10, [fast healing](ref/umr/fast-healing) 2, and the vampire qualities listed above
  (gaseous form, shadowless, and spider climb).
- It does not gain the Create Spawn ability.
- A vampire spawn gains all of the standard vampire weaknesses.
- A vampire spawn is CR 4.
