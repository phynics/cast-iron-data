+++
id = "ref/template/runewarped-creature"
kind = "rule"
title = "Runewarped Creature"
source_ids = ["pathfinder-133-secrets-of-roderics-cove"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "runewarped_creature", path = "json/monster_template4.json" },
]
[[sources]]
publication = "pathfinder-133-secrets-of-roderics-cove"
page = "87"

[fields]
kind = "none"
+++

**Runewarped Creature**

**Acquired:** present

**Challenge rating:** +1

Before Alaznist created the first [sinspawn](ref/monster/sinspawn) through the use of her runewell,
she experimented with several techniques to create sin-twisted servants. One foundation of the
complex magical technique used to create sinspawn was known as runewarping. Through the use of
runewarping, Alaznist and other powerful mages created horribly twisted creatures from their slaves
and prisoners. These creators valued ability over aesthetics, so runewarped creatures were
transformed by powerful magic into horrid mockeries of their previous forms. Runewarped creatures
seek out sources of magic to consume, trying in vain to complete their transformation. Although a
runewarped creature is recognizable as the creature it once was, the creature bears altered or
additional limb joints, elongated fingers, and a massive jaw capable of delivering a powerful bite.

"Runewarped creature" is an acquired template that can be added to any [animal](ref/type/animal),
[humanoid](ref/type/humanoid), or [monstrous humanoid](ref/type/monstrous-humanoid) (referred to
hereafter as the base creature). A runewarped creature uses the base creature's statistics and
special abilities except as noted here.

**CR:** Base creature's CR + 1.

**Alignment:** Any evil.

**Type:** The creature's type changes to [aberration](ref/type/aberration). Do not recalculate its
base attack bonus, saves, or skill ranks.

**Senses:** The creature gains [darkvision](ref/rule/darkvision) with a range of 60 feet,
[low-light vision](ref/rule/low-light-vision), and magic-scent.

> **Magic-Scent (Su):** Runewarped creatures have [scent](ref/umr/scent) that detects only creatures
> with the ability to cast spells. This scent allows the runewarped creature to know the location
> and power of all magic auras within range of its scent. Magic-scent always detects magic auras in
> a range of 60 feet and is not affected by wind.

**AC:** Natural armor bonus increases by 2.

**Hit Dice:** Change all the creature's racial Hit Dice to d8s. Hit Dice derived from class levels
remain unchanged.

**Defensive Abilities:** A runewarped creature with 5 Hit Dice or more gains DR 5/magic (or DR
10/magic if it has 11 Hit Dice or more) and SR equal to its new CR + 6 (or SR equal to its new CR +
11 if it has 11 Hit Dice or more).

**Melee:** A runewarped creature gains a [bite attack](ref/umr/natural-attacks) that deals damage
based on the runewarped creature's size but as if it were one size category larger than its actual
size. If the runewarped creature already has a bite attack, the bite's damage increases by one step,
as if it had increased one size category.

**Special Attacks:** A runewarped creature loses any spells or
[spell-like abilities](ref/umr/spell-like-abilities), but it retains all other special attacks and
abilities of the base creature. A runewarped creature gains the following special attack.

> **Consume Magic (Su):** A runewarped creature's bite drains magical ability from creatures capable
> of casting spells or using [spell-like abilities](ref/umr/spell-like-abilities). The struck
> creature loses its highest-level prepared spell, spell slot, or spell-like ability unless it
> succeeds at a Will save to negate the effect. A creature can be affected by this ability only once
> per round, even if attacked multiple times or by multiple runewarped creatures. The save DC is
> Constitution-based.

**Ability Scores:** Str +4, Con +2, Int -4 (minimum 1), Cha -2.

### Sinwarped Creatures

Runewarped creatures subjected to prolonged direct exposure to a runewell or sin magic gain
additional powers related to a specific sin, seeking out magic and spellcasters associated with that
sin.

Sinwarped creatures are runewarped creatures with the [advanced](ref/template/advanced) creature
simple template, _magic-scent_ with a range of 120 feet, and
[spell-like abilities](ref/umr/spell-like-abilities) determined by the creature's affinity to a
particular school of sin magic: envy ([resist energy](ref/spell/resist-energy) and
[shield](ref/spell/shield)), gluttony ([chill touch](ref/spell/chill-touch) and
[false life](ref/spell/false-life)), greed ([barkskin](ref/spell/barkskin) and
[expeditious retreat](ref/spell/expeditious-retreat)), lust ([hold person](ref/spell/hold-person)
and [hypnotism](ref/spell/hypnotism)), pride ([blur](ref/spell/blur) and
[color spray](ref/spell/color-spray)), sloth ([cure moderate wounds](ref/spell/cure-moderate-wounds)
and [grease](ref/spell/grease)), or wrath ([burning hands](ref/spell/burning-hands) and
[darkness](ref/spell/darkness)). Each spell-like ability is usable once per day. When a target loses
a prepared spell, spell slot, or spell-like ability that is at least 3rd level to a sinwarped
creature's consume magic ability, the sinwarped creature regains all of these spell-like abilities
it has used.
