+++
id = "ref/carried/ultimate-magic/rules/words-of-power/effect-words"
kind = "rule"
title = "Effect Words"
source_ids = ["ultimate-magic"]
section = ["Rules", "Words of Power"]
parent = "ref/rule/words-of-power"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Rules/Words of Power/Effect Words", path = "ultimate_magic/rules/words_of_power.json" },
]

[fields]
kind = "none"
+++

Effect words determine the overall outcome of a wordspell. A wordspell can contain more than one
effect word, and it is possible for their effects to counteract one another. Effect words use the
following format.

## Name {#name}

This is the name of the effect word. Each word belongs to a group of similar words, noted in
parentheses. Unless otherwise noted, an individual wordspell cannot contain two effect words from
the same group.

## School {#school}

This entry lists the school of magic that the effect word belongs to.

## Level {#level}

This entry lists the classes that can learn the effect word and what level the word is for members
of that class. Note that an individual wordspell can contain no words of a level higher than the
wordspell.

## Duration {#duration}

This line lists the duration of the effect word.

## Saving Throw {#saving-throw}

If the effect allows a saving throw, it is noted here along with the effect of a successful save.

## Spell Resistance {#spell-resistance}

If the effect word allows [spell resistance](ref/rule/spell-resistance), it is noted here.

## Target Restrictions {#target-restrictions}

Some effect words can only be combined with specific target words when arranging wordspells. If this
is the case, the specific target words are noted here.

## Description {#description}

This paragraph describes the effects of the word when arranged in a wordspell.

## Boost {#boost}

If the effect word can be boosted by the _boost_ meta word, the effects are listed here. See the
meta word section for more details.

## Acid Words {#acid-words}

These words create caustic acid that scorches and burns all that it comes in contact with.

### Acid Burn {#acid-burn}

::: statblock
Abbrev: Acid
:::

::: paragraph statline
**School **conjuration (creation) \[acid\]
:::

::: paragraph statline
**Level **druid 0, inquisitor 0, magus 0, sorcerer/wizard 0, summoner 0
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **no
:::

A wordspell with this effect word deals 1d3 points of acid damage. If the wordspell has only a
single target, it requires a melee or ranged touch attack to hit and does not allow a saving throw.

### Corrosive Bolt {#corrosive-bolt}

::: statblock
Abbrev: Acid
:::

::: paragraph statline
**School **conjuration (creation) \[acid\]
:::

::: paragraph statline
**Level **magus 2, sorcerer/wizard 2
:::

::: paragraph statline
**Duration **2 rounds
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

A wordspell with this effect word deals 1d4 points of acid damage per level of the wordcaster
(maximum 5d4). On the following round, the target takes this damage again. Hitting a target with a
wordspell with this effect word requires a ranged touch attack.

### Acid Wave {#acid-wave}

::: statblock
Abbrev: Acid
:::

::: paragraph statline
**School **conjuration (creation) \[acid\]
:::

::: paragraph statline
**Level **magus 4, sorcerer/wizard 4
:::

::: paragraph statline
**Duration **2 rounds
:::

::: paragraph statline
**Saving Throw **Reflex half and partial (see below)
:::

::: paragraph statline
**Spell Resistance **no
:::

A wordspell with this effect word deals 1d6 points of acid damage per caster level (maximum 10d6).
Targets damaged by this effect word are sickened for 1 round per caster level, or 1 round if the
saving throw against the wordspell with this effect word was successful.

### Caustic Cloud {#caustic-cloud}

::: statblock
Abbrev: Acid
:::

::: paragraph statline
**School **conjuration (creation) \[acid\]
:::

::: paragraph statline
**Level **sorcerer/wizard 7, witch 6
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Fortitude half
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst
:::

A wordspell with this effect word creates a cloud of noxious green vapor that obscures vision.
Creatures caught in the cloud take 1d6 points of acid damage per caster level (maximum 20d6) and are
fatigued. Creatures caught in the cloud receive a Fortitude save to halve the damage and to negate
the fatigued effect. Creatures that remain in the cloud take a cumulative –2 penalty on the save
each round they remain in the cloud, but spending just 1 round outside the cloud's area resets this
penalty. Creatures in the cloud that are fatigued become exhausted on a failed saving throw. A
strong wind, such as that created by a _[gust of wind](ref/spell/gust-of-wind)_, disperses this
cloud immediately.

## Alignment Words {#alignment-words}

Words from this family deal specifically with alignment, detecting, damaging, or protecting
creatures based on their moral compass.

### Alignment Shield {#alignment-shield}

::: statblock
Abbrev: Alignment
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **cleric 1, inquisitor 1, paladin 1, sorcerer/wizard 1
:::

::: paragraph statline
**Duration **1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

When a wordspell with this effect word is cast, the wordcaster selects one alignment: good, evil,
chaotic, or lawful. The target of this wordspell is protected from that alignment and receives a +2
deflection bonus to AC on attacks made from creatures of that alignment and a +2 resistance bonus on
saving throws made on spells and effects from creatures of that alignment. The target of a wordspell
with this effect word can choose to end this effect as an immediate action to reroll any one saving
throw made against a spell or effect from the chosen alignment, but must take the second result,
even if it is worse.

### Alignment Assault {#alignment-assault}

::: statblock
Abbrev: Alignment
:::

::: paragraph statline
**School **evocation
:::

::: paragraph statline
**Level **cleric 5, inquisitor 5, paladin 4
:::

::: paragraph statline
**Duration **instantaneous, see text
:::

::: paragraph statline
**Saving Throw **Will partial
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **burst, cone, line
:::

If a wordspell with this effect word is cast, the wordcaster selects one alignment: good, evil,
chaotic, or lawful. All creatures of that alignment take 1d8 points of damage per two caster levels
(maximum 8d8). Outsiders of that alignment take 1d6 points of damage per caster level (maximum
15d6). In addition, creatures of the affected alignment are staggered for 1 round per caster level
if they fail their saving throws.

### Alignment Aura {#alignment-aura}

::: statblock
Abbrev: Alignment
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **cleric 8
:::

::: paragraph statline
**Duration **1 round/level (D)
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

A wordspell with this effect word functions as _alignment shield_, but the bonus to AC and on saving
throws increases to +4. In addition, the creature gains SR 25 against spells cast by creatures of
the chosen alignment. Finally, creatures of the chosen alignment find it painful to touch the warded
creature, taking 2d6 points of damage for each successful hit with a melee weapon or natural weapon.

## Animal Words {#animal-words}

Words from this family speak directly to wild creatures, soothing and controlling them.

### Nature's Calm {#natures-calm}

::: statblock
Abbrev: Animal
:::

::: paragraph statline
**School **enchantment (charm) \[mind-affecting\]
:::

::: paragraph statline
**Level **druid 1, ranger 1, witch 1
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word becomes calm and docile. Though the target will not
attack while subject to this effect, the wordspell immediately ends if the target is attacked.
Creatures affected by this effect word do not flee, but they are not helpless. This effect word only
affects creatures of the animal or magical beast type, although magical beasts receive a +4 bonus on
the saving throw.

### Wild Lure {#wild-lure}

::: statblock
Abbrev: Animal
:::

::: paragraph statline
**School **enchantment (charm) \[mind-affecting\]
:::

::: paragraph statline
**Level **druid 2, ranger 2, witch 2
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word treats the caster as a trusted ally. The creature
will defend the caster and will not attack her allies while this effect persists. If at any time the
target of a wordspell with this effect word is attacked by the wordcaster or her allies, the
wordspell's duration ends immediately. A wordspell with this effect word only affects creatures of
the animal or magical beast type, although magical beasts receive a +4 bonus on the saving throw.

### Nature's Command {#natures-command}

::: statblock
Abbrev: Animal
:::

::: paragraph statline
**School **enchantment (compulsion) \[mind-affecting\]
:::

::: paragraph statline
**Level **druid 4, ranger 4, summoner 5, witch 4
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word obeys any simple commands given by the caster. These
commands are sent through a mental link that does not require speech, but they must be able to be
understood by the target. The target ignores any commands that are suicidal or self-destructive. A
wordspell with this effect word only affects creatures of the animal or magical beast type, although
magical beasts receive a +4 bonus on the saving throw.

## Armor Words {#armor-words}

These words create translucent armor made of solid magic, protecting without weight or obstruction.

### Force Block {#force-block}

::: statblock
Abbrev: Armor
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **cleric 0, magus 0, sorcerer/wizard 0, summoner 0
:::

::: paragraph statline
**Duration **1 round
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word receives a +1 armor bonus to its AC. This armor is
made of force and provides protection against the attacks of incorporeal creatures.

#### Boost {#boost-2}

::: paragraph statline
A wordspell with this effect word can be cast as an immediate action. In this case, the effect lasts
until the end of your next turn. This boost cannot be used if the wordspell includes another effect
word (unless that word can also be cast as an immediate action). This boost increases this effect
word's level by 1.
:::

### Force Shield {#force-shield}

::: statblock
Abbrev: Armor
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **alchemist 1, magus 1, sorcerer/wizard 1, summoner 1, witch 1
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word receives a +4 armor bonus to its AC. This armor is
made of force and provides protection against the attacks of incorporeal creatures.

### Force Armor {#force-armor}

::: statblock
Abbrev: Armor
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **cleric 3, magus 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word receives a +4 armor bonus to its AC + 1 point for
every four levels of the caster. This armor is made of force and provides protection against the
attacks of incorporeal creatures. If the target has a greater armor bonus from another source, a
wordspell with this effect word instead increases that armor bonus by +1 and allows it to provide
protection against the attacks of incorporeal creatures.

### Force Ward {#force-ward}

::: statblock
Abbrev: Armor
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **magus 6, sorcerer/wizard 6
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

This effect word functions as _force armor_, but it grants a +6 armor bonus to AC + 1 point for
every four levels of the caster. If the target has greater armor bonus from another source, a
wordspell with this effect word increases that armor bonus by +2.

## Binding Words {#binding-words}

Words from this family cause objects to become stationary and creatures to become paralyzed.

### Lock Ward {#lock-ward}

::: statblock
Abbrev: Binding
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **sorcerer/wizard 1
:::

::: paragraph statline
**Duration **permanent
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word causes one unattended object to close, such as a door, chest, or book. If the
object possesses a lock, the object is also locked. If the wordspell includes other effect words,
the effects of those words are suspended until a creature other than the wordcaster attempts to
unlock or otherwise open the object. That creature becomes the target of the other effect words, as
if those effect words had the _selected_ target word. Only consider the other effect words when
determining the duration of this secondary effect.

### Paralyze Humanoid {#paralyze-humanoid}

::: statblock
Abbrev: Binding
:::

::: paragraph statline
**School **enchantment (compulsion) \[mind-affecting\]
:::

::: paragraph statline
**Level **bard 2, cleric 2, inquisitor 2, sorcerer/wizard 3, witch 2
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word is paralyzed and cannot move. It is aware and can
breathe normally, but cannot take any actions. At the end of each of the creature's turns, it can
attempt a new saving throw to end the effect. Flying creatures that rely on wings to fly fall, and
swimmers cannot swim and may drown. Wordspells with this effect word only affect creatures of the
humanoid type.

### Paralyze Creature {#paralyze-creature}

::: statblock
Abbrev: Binding
:::

::: paragraph statline
**School **enchantment (compulsion) \[mind-affecting\]
:::

::: paragraph statline
**Level **bard 4, druid 4, inquisitor 4, sorcerer/wizard 5, summoner 5, witch 5
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as the _paralyze humanoid_ word except that it can affect creatures of
any type.

### Permanent Paralysis {#permanent-paralysis}

::: statblock
Abbrev: Binding
:::

::: paragraph statline
**School **enchantment (compulsion) \[mind-affecting\]
:::

::: paragraph statline
**Level **sorcerer/wizard 8, summoner 6, witch 8
:::

::: paragraph statline
**Duration **permanent
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as the _paralyze humanoid_ word except that it can affect creatures of
any type and the duration is permanent. A creature affected by a wordspell with this effect word
receives one additional Will saving throw at the end of its first turn after initially failing the
save. This saving throw is made to relieve this word's effects, not any others included in the
original wordspell. If this save fails as well, the effect of this word can only be undone with
_[greater dispel magic](ref/spell/dispel-magic-greater)_, _[miracle](ref/spell/miracle)_, or
_[wish](ref/spell/wish)_.

## Body Words {#body-words}

Body words enhance the form of their targets, making them stronger, more agile, and more resilient.

### Fortify {#fortify}

::: statblock
Abbrev: Body
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **alchemist 1, cleric 1, inquisitor 1, paladin 1, ranger 1, sorcerer/wizard 1, summoner 1
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal, selected
:::

The target of a wordspell with this effect word receives a +1 resistance bonus on saving throws. In
addition, the target receives a number of temporary hit points equal to its Hit Dice.

### Energy Resistance {#energy-resistance}

::: statblock
Abbrev: Body
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **alchemist 2, cleric 2, druid 2, inquisitor 2, paladin 2, ranger 1, sorcerer/wizard 2,
summoner 2
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal, selected
:::

The target of a wordspell with this effect word gains resistance 10 to one energy type (acid, cold,
electricity, fire, or sonic). The target still suffers any other side effects that might accompany
the energy damage.

#### Boost {#boost-3}

::: paragraph statline
The target gains resistance 20 to one energy type.
:::

### Enhance Form {#enhance-form}

::: statblock
Abbrev: Body
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 2, bard 2, cleric 2, druid 2, magus 2, paladin 2, ranger 2, sorcerer/wizard 2,
summoner 2
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal, selected
:::

The target of a wordspell with this effect receives a +4 enhancement bonus to either Strength,
Dexterity, or Constitution (caster's choice). The target can end a wordspell with this effect word
prematurely as a swift action, gaining a +8 enhancement bonus to the ability score until the end of
the target's turn.

### Perfect Form {#perfect-form}

::: statblock
Abbrev: Body
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 4, bard 4, cleric 4, druid 4, magus 4, sorcerer/wizard 4, summoner 4
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal, selected
:::

The target of a wordspell with this effect word receives a +4 enhancement to Strength, Dexterity,
and Constitution.

### Energy Immunity {#energy-immunity}

::: statblock
Abbrev: Body
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **alchemist 6, cleric 6, druid 6, inquisitor 6, sorcerer/wizard 6, summoner 6
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal, selected
:::

The target of a wordspell with this effect word gains immunity to one energy type (acid, cold,
electricity, fire, or sonic). The target still suffers any other side effects that might accompany
the energy damage.

## Change Words {#change-words}

Words from this family change the target's form, granting special attacks and powers.

### Altered Form {#altered-form}

::: statblock
Abbrev: Change
:::

::: paragraph statline
**School **transmutation (polymorph)
:::

::: paragraph statline
**Level **alchemist 3, druid 3, magus 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal
:::

The target of a wordspell with this effect word receives a +2 size bonus to Strength and two of the
following benefits: a pair of claw attacks that each deals 1d6 points of damage if Medium (1d4 if
Small), a bite attack that deals 1d8 points of damage if Medium (1d6 if Small), a climb speed of 30
feet, a swim speed of 30 feet, [darkvision](ref/rule/darkvision) out to 60 feet,
[low-light vision](ref/rule/low-light-vision), scent, or a +2 natural armor bonus.

#### Boost {#boost-4}

::: paragraph statline
The target receives three benefits instead of two.
:::

#### Boost {#boost-5}

::: paragraph statline
This wordspell can use the _selected_ target word. Boosting this effect word increases its level
by 1.
:::

### Bestial Form {#bestial-form}

::: statblock
Abbrev: Change
:::

::: paragraph statline
**School **transmutation (polymorph)
:::

::: paragraph statline
**Level **alchemist 4, druid 4, magus 4, sorcerer/wizard 4
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal
:::

This effect word functions as _altered form_ except that the target of this wordspell receives a +4
size bonus to Strength and can select three benefits. In addition to those available in _altered
form_, the target can select from among the following benefits: a fly speed of 30 feet (average
maneuverability), grab (with any one natural attack), pounce, trip (with any one natural attack), or
a +4 natural armor bonus.

#### Boost {#boost-6}

::: paragraph statline
The target receives four benefits instead of three.
:::

#### Boost {#boost-7}

::: paragraph statline
This wordspell can use the _selected_ target word. Boosting this effect word increases its level
by 1.
:::

### Monstrous Form {#monstrous-form}

::: statblock
Abbrev: Change
:::

::: paragraph statline
**School **transmutation (polymorph)
:::

::: paragraph statline
**Level **alchemist 5, druid 5, magus 5, sorcerer/wizard 5
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restriction **personal
:::

This effect word functions as _bestial form_ except that the target of this wordspell receives a +6
size bonus. In addition to those benefits available in _altered form_ and _bestial form_, the target
can select from the following: a burrow speed of 30 feet,
[blindsense](ref/rule/blindsight-and-blindsense) out to a range of 30 feet, constrict (dealing the
same damage as the grab attack + the target's Str modifier), ferocity, resist 20 against one energy
type, or a +4 natural armor bonus.

#### Boost {#boost-8}

::: paragraph statline
The target receives four benefits instead of three.
:::

#### Boost {#boost-9}

::: paragraph statline
This wordspell can use the _selected_ target word. Boosting this effect word increases its level
by 1.
:::

## Cold Words {#cold-words}

Spells using these words drain the warmth from the surrounding environment, leaving everything
frozen and rimed with frost.

### Cold Snap {#cold-snap}

::: statblock
Abbrev: Cold
:::

::: paragraph statline
**School **evocation \[cold\]
:::

::: paragraph statline
**Level **druid 0, magus 0, sorcerer/wizard 0
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

A wordspell with this effect word deals 1d3 points of cold damage. If the wordspell with this effect
word has only a single target, it requires a melee or ranged touch attack to hit and does not allow
a saving throw.

### Frost Fingers {#frost-fingers}

::: statblock
Abbrev: Cold
:::

::: paragraph statline
**School **evocation \[cold\]
:::

::: paragraph statline
**Level **druid 2, magus 2, sorcerer/wizard 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

A wordspell with this effect word deals 1d6 points of cold damage per caster level (maximum 5d6). A
target that fails its saving throw is also staggered for 1 round.

### Ice Blast {#ice-blast}

::: statblock
Abbrev: Cold
:::

::: paragraph statline
**School **evocation \[cold\]
:::

::: paragraph statline
**Level **druid 4, magus 4, sorcerer/wizard 4, witch 4
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect deals 1d6 points of cold damage per caster level (maximum 10d6). A target that fails its
saving throw is entangled by the ice for 1d4 rounds.

### Winter's Wrath {#winters-wrath}

::: statblock
Abbrev: Cold
:::

::: paragraph statline
**School **evocation \[cold\]
:::

::: paragraph statline
**Level **druid 8, sorcerer/wizard 8
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Fortitude half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **burst
:::

A wordspell with this effect word creates an area of blizzardlike conditions. Anyone inside the area
when it forms, and at the start of the caster's turn, takes 1d6 points of cold damage per caster
level (maximum 20d6) and 1d4 points of Dexterity damage. A Fortitude save halves this damage and
negates the Dexterity damage. Creatures immune to cold damage do not take the Dexterity damage.
Because of the heavy snow and winds, visibility is reduced to 5 feet inside the blizzard. Effects
that deal fire damage do not harm anyone inside this blizzard unless they are of a level equal to or
higher than the wordspell with this effect word.

## Command Words {#command-words}

These words demand action from those that hear them, with near-irresistible force.

### Friendship {#friendship}

::: statblock
Abbrev: Command
:::

::: paragraph statline
**School **enchantment (charm) \[mind-affecting\]
:::

::: paragraph statline
**Level **bard 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word treats the caster as a trusted ally. The creature
will defend the caster and will not attack the caster's allies while the wordspell persists. If the
creature is attacked by the caster or his allies, this effect immediately ends (though other effects
of the wordspell may continue). A wordspell with this effect word only affects creatures of the
humanoid type; targets receive a +4 bonus on the saving throw if a wordspell with the effect word
has its target boosted to affect more than one creature.

### Simple Order {#simple-order}

::: statblock
Abbrev: Command
:::

::: paragraph statline
**School **enchantment (compulsion) \[language-dependent, mind affecting\]
:::

::: paragraph statline
**Level **bard 1, cleric 1, inquisitor 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **1 round
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word must follow one of five simple commands to the best
of its ability on its next turn. If the target cannot take the specified action on its next turn,
this effect of the wordspell fails. The possible commands are as follows.

#### Approach {#approach}

::: paragraph indented
The target must move toward the caster as quickly and directly as possible, provoking attacks of
opportunity as normal. The target avoids obvious hazards, such as fire, pits, or traps that it is
aware of (other creatures do not count).
:::

#### Drop {#drop}

::: paragraph indented
The target drops whatever it is holding and does not pick up anything this round. It can otherwise
act normally.
:::

#### Fall {#fall}

::: paragraph indented
The target falls to the ground and remains prone until its next turn. It can otherwise act normally.
:::

#### Flee {#flee}

::: paragraph indented
The target moves away from the caster as quickly and directly as possible. This otherwise functions
as approach.
:::

#### Halt {#halt}

::: paragraph indented
The target does not move and takes no other action on its turn, although it is not considered
flat-footed or helpless.
:::

#### Boost {#boost-10}

::: paragraph statline
This wordspell can use any target word. Boosting this effect word increases its level by 3.
:::

### Complex Order {#complex-order}

::: statblock
Abbrev: Command
:::

::: paragraph statline
**School **enchantment (compulsion) \[language-dependent, mind affecting\]
:::

::: paragraph statline
**Level **bard 3, sorcerer/wizard 3, witch 4
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word must follow the wordcaster's instructions. The
wordcaster must be able to convey the orders within 1 round and the actions must be possible to
complete within the wordspell's duration. The instructions cannot include anything that is obviously
dangerous or harmful to the target. The instructions do not have to take the entire duration, and
once completed, a wordspell with this effect word ends. If the instructions are not completed by the
time the duration expires, the target is under no compulsion to finish enacting them.

### Crush Will {#crush-will}

::: statblock
Abbrev: Command
:::

::: paragraph statline
**School **enchantment (compulsion) \[language-dependent, mind-affecting\]
:::

::: paragraph statline
**Level **bard 4, sorcerer/wizard 5, witch 5
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word obeys any commands given by the caster. These
commands are sent through a mental link that does not require speech. The target ignores any
commands that are suicidal or self-destructive. A wordspell with this effect word only affects
creatures of the humanoid type; targets receive a +4 bonus on the saving throw if a wordspell with
the effect word has its target boosted to affect more than one creature.

## Concealing Words {#concealing-words}

Words from this family hide creatures and objects from observation and detection.

### Fade {#fade}

::: statblock
Abbrev: Concealing
:::

::: paragraph statline
**School **illusion (glamer)
:::

::: paragraph statline
**Level **alchemist 1, bard 1, inquisitor 1, magus 1, sorcerer/wizard 1, summoner 1, witch 1
:::

::: paragraph statline
**Duration **1 round
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word becomes invisible until the beginning of the
caster's next turn. If the target attacks or otherwise takes an offensive action, this effect ends.

#### Boost {#boost-11}

::: paragraph statline
The target does not become visible if it attacks or takes an offensive action.
:::

### Disappear {#disappear}

::: statblock
Abbrev: Concealing
:::

::: paragraph statline
**School **illusion (glamer)
:::

::: paragraph statline
**Level **alchemist 2, bard 2, inquisitor 2, magus 2, sorcerer/wizard 2, summoner 2, witch 2
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _fade_, but with a longer duration.

#### Boost {#boost-12}

::: paragraph statline
The target does not become visible if it attacks or takes an offensive action. Boosting this effect
word increases its level by 2.
:::

### Unseen Shell {#unseen-shell}

::: statblock
Abbrev: Concealing
:::

::: paragraph statline
**School **illusion (glamer)
:::

::: paragraph statline
**Level **bard 4, sorcerer/wizard 4, witch 4
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

When cast, a wordspell with this effect word makes any objects or creatures designated by the caster
within the area invisible so long as they remain in the area and do not attack or otherwise take
offensive actions. All possessions carried by the creatures remain invisible as long as they remain
in the area, so an arrow fired from a bow would become visible when it leaves the area.

#### Boost {#boost-13}

::: paragraph statline
The target does not become visible if it attacks or takes an offensive action. Boosting this effect
word increases its level by 2.
:::

## Death Words {#death-words}

Words from this family destroy life and create undead abominations.

### Undeath {#undeath}

::: statblock
Abbrev: Death
:::

::: paragraph statline
**School **necromancy \[evil\]
:::

::: paragraph statline
**Level **cleric 2, sorcerer/wizard 3
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word can only target the corpses of dead creatures. These creatures rise as either
skeletons or zombies, as decided by the caster. These undead follow the caster's commands to the
best of their limited ability. They remain undead creatures until destroyed. The caster can create
at most 2 Hit Dice worth of undead per caster level with each casting of a wordspell with this
effect word. The caster can control no more than 4 HD per caster level of undead creatures. If
additional undead are created, the caster chooses which undead to lose control of to get back under
the limit.

### Grave Bane {#grave-bane}

::: statblock
Abbrev: Death
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **cleric 4, druid 5, inquisitor 5, paladin 4
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word receives a +4 sacred bonus on saves against all
death spells and magic death effects. The subject cannot gain any negative levels while the
wordspell with this effect word persists, but any existing before this wordspell is cast remain. The
subject automatically stabilizes if brought below 0 hit points and is not slain.

### Life Leech {#life-leech}

::: statblock
Abbrev: Death
:::

::: paragraph statline
**School **necromancy \[evil\]
:::

::: paragraph statline
**Level **magus 4, sorcerer/wizard 4, witch 4
:::

::: paragraph statline
**Duration **1 hour/level
:::

::: paragraph statline
**Saving Throw **Fortitude negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes 1d4 temporary negative levels. If these
negative levels cause the subject to die, it rises as a ghost 1d4 days later unless buried in
consecrated ground.

#### Boost {#boost-14}

The negative levels from a wordspell with this effect word are permanent. Boosting this effect word
increases its level by 5.

### Slay {#slay}

::: statblock
Abbrev: Death
:::

::: paragraph statline
**School **necromancy \[death, evil\]
:::

::: paragraph statline
**Level **cleric 6, druid 7, sorcerer/wizard 6, witch 6
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Fortitude partial
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes 10 points of damage per caster level, to a
maximum of 150 points of damage. If the save is successful, the target instead takes 3d6 points of
damage + 1 per caster level (maximum +15). A wordspell with this effect word only affects living
creatures.

## Destruction Words {#destruction-words}

These words cause catastrophe when they are uttered, breaking and destroying all they encounter.

### Damage {#damage}

::: statblock
Abbrev: Destruction
:::

::: paragraph statline
**School **evocation
:::

::: paragraph statline
**Level **bard 3, cleric 3, sorcerer/wizard 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates (object)
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word causes one object within range to lose half of its maximum hit points and gains the
broken condition. This item can weigh no more than 10 pounds per caster level. Magic items gain a +4
bonus on the saving throw to resist this effect + their normal bonus. Items in another creature's
possession use the save of the creature or the item, whichever is better. Artifacts are not affected
by this word.

### Rumble {#rumble}

::: statblock
Abbrev: Destruction
:::

::: paragraph statline
**School **evocation \[earth\]
:::

::: paragraph statline
**Level **cleric 8, druid 8
:::

::: paragraph statline
**Duration **1 round
:::

::: paragraph statline
**Saving Throw **see text
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

This effect word causes the ground within the area to shake and rumble, like an earthquake. Each
creature in the area must make a Reflex save or be knocked prone and take 8d6 points of damage. If
the creature makes its save, it takes half damage and is not knocked prone. Caves, cliffs, tunnels,
and other natural surfaces collapse in this area, triggering a landslide and possibly burying
creatures underneath. Structures take 100 points of damage from this effect, typically enough to
cause wooden and masonry buildings to collapse, but not stone or reinforced masonry buildings. See
page 429 of the _Core Rulebook_ for more information on landslides and collapses.

### Catastrophe {#catastrophe}

::: statblock
Abbrev: Destruction
:::

::: paragraph statline
**School **evocation \[air\]
:::

::: paragraph statline
**Level **cleric 9, druid 9, witch 9
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **see text
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

This effect word causes heavy clouds to form in the sky above the area of wordspell with this effect
word. The area is pelted by heavy rain and hail, obscuring vision and making ranged attacks
impossible. Melee attacks take a 20% miss chance. Creatures in the area take 4d6 points of damage
from pounding hail at the start of their turn. In addition, the caster can call down a bolt of
lightning once per turn that deals 1d6 points of electricity damage per caster level. The caster can
split this bolt to hit as many targets as she likes and can divide the damage dice up among the
targets as she sees fit. The targets receive a Reflex save to halve the damage. Targets that fail
are also knocked prone by the force of the blast. The ground in the area of a wordspell with this
effect word is considered difficult terrain for the duration, but not for the caster.

## Detection Words {#detection-words}

Detection words are used to learn things that simple observation cannot. They reveal secrets and
uncover hidden things. Detection words are special in that they can be combined with other words
from the Detection group in the same wordspell. Detection words cannot be combined with any other
group's effect words within the same wordspell.

### Sense Magic {#sense-magic}

::: statblock
Abbrev: Detection
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **bard 0, cleric 0, druid 0, inquisitor 0, magus 0, sorcerer/wizard 0, summoner 0, witch 0
:::

::: paragraph statline
**Duration **concentration, up to 1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **cone
:::

A wordspell with this effect word detects magic auras. By concentrating each round, the caster can
determine the number and location of each aura in the target area. He can make a Knowledge (arcana)
skill check to determine the school of each aura (one check per aura, the DC of this check is 15 +
the spell level or 15 + 1/2 the caster level for a nonspell effect). If the aura radiates from a
magic item, the caster can attempt to identify the item's properties as if using
_[detect magic](ref/spell/detect-magic)_ (see Spellcraft). If the aura emanates from a spell of 7th
level or higher, or is a nonspell effect with a caster level of 12th or higher, the caster knows
that the aura is strong, even if the Knowledge check to identify the school is unsuccessful.

### Sense Alignment {#sense-alignment}

::: statblock
Abbrev: Detection
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **cleric 1, inquisitor 1, paladin 1
:::

::: paragraph statline
**Duration **concentration, up to 1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **cone
:::

This effect word detects one or more alignments. When cast, the wordcaster selects one of the
following alignments: chaos, evil, good, or law. By concentrating, he can sense the presence and
source of that alignment in the wordspell area. If the source is a creature with more than 25 Hit
Dice, an outsider, cleric, or paladin with more than 4 Hit Dice, or a magic item or spell with a
caster level greater than 16th, the caster knows that aura is strong.

#### Boost {#boost-15}

::: paragraph statline
The caster can select two alignments to detect. Boosting this effect word increases its level by 1.
:::

#### Boost {#boost-16}

::: paragraph statline
The caster can detect all four alignments (although this does not allow him to detect neutral
objects or creatures). Boosting this effect word increases its level by 2.
:::

### Sense Thoughts {#sense-thoughts}

::: statblock
Abbrev: Detection
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **alchemist 2, bard 2, inquisitor 2, sorcerer/wizard 2, summoner 2, witch 2
:::

::: paragraph statline
**Duration **concentration, up to 1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **cone
:::

This effect word allows the caster to detect the surface thoughts of creatures in the target area.
By focusing on one creature in the area, the caster can read the surface thoughts of that creature.
The caster must be otherwise aware of the creature to focus on it. A Will save prevents the caster
from reading the creature's thoughts for the duration of a wordspell with this effect word. If the
target has an Intelligence score at least 10 higher than the caster and it makes its Will save, the
target can instead read the surface thoughts of the caster for the duration of the of the wordspell
with this effect word, while the wordcaster receives no insight. Each round, the caster can focus on
a new creature if he desires.

### Sense Hidden {#sense-hidden}

::: statblock
Abbrev: Detection
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **alchemist 2, bard 2, cleric 2, inquisitor 2, sorcerer/wizard 2, summoner 2, witch 2
:::

::: paragraph statline
**Duration **concentration, up to 1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **cone
:::

This effect word allows the caster to see invisible creatures and objects. The caster can sense that
the objects and creatures are hidden in this way, but he can still see them normally.

#### Boost {#boost-17}

::: paragraph statline
The caster can see through illusions, see the true form of polymorphed creatures and objects, and
locate creatures protected by spells and effects that grant concealment. The caster also receives a
+4 circumstance bonus on saves against illusion spells and effects. Boosting this effect word
increases its level by 4.
:::

## Dispelling Words {#dispelling-words}

Dispelling words have the power to unmake magic or suppress its effects.

### Suppress {#suppress}

::: statblock
Abbrev: Dispelling
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **bard 2, cleric 2, druid 2, inquisitor 2, magus 2, paladin 2, sorcerer/wizard 2, summoner
2, witch 2
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The caster of a wordspell with this effect word selects one spell effect that affects a willing
target. The caster must then make a caster level check with a DC of 11 + the caster level of the
spell effect. If successful, that spell effect is suppressed for the duration of this spell. If the
suppressed spell has a limited duration, that duration continues to expire while this spell is in
effect.

#### Boost {#boost-18}

::: paragraph statline
The caster can target creatures that are not willing. The targets receive a saving throw to negate
this effect word, and the caster must overcome the target's
[spell resistance](ref/rule/spell-resistance). Boosting this effect word increases its level by 1.
:::

### Resist Arcana {#resist-arcana}

::: statblock
Abbrev: Dispelling
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **alchemist 5, cleric 5, inquisitor 5, sorcerer/wizard 6, summoner 6
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word gains [spell resistance](ref/rule/spell-resistance)
equal to 12 + the caster's level.

### Unmake {#unmake}

::: statblock
Abbrev: Dispelling
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **bard 5, cleric 5, druid 5, inquisitor 6, magus 6, sorcerer/wizard 5, summoner 6, witch 5
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will partial
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The caster of a wordspell with this effect word unravels all of the magic effects affecting the
target of the wordspell with this effect word. The caster must make a caster level check. The result
of this check is compared to the caster level + 11 of every spell affecting the target. If
successful, that spell effect immediately ends. The target can make a Will saving throw. If
successful, this wordspell only attempts to unmake the highest-level spell affecting the target.

### Negation {#negation}

::: statblock
Abbrev: Dispelling
:::

::: paragraph statline
**School **abjuration
:::

::: paragraph statline
**Level **cleric 8, sorcerer/wizard 6
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst
:::

This effect word creates an area in which magic does not function. All magic effects are suppressed
while inside the area. As a result, this word cannot be combined with other effect words. Magic
effects cannot cross through the area. Time spent within the field counts against the duration of
the suppressed effects. Summoned and incorporeal creatures cannot enter the area and are immediately
forced to the nearest edge if inside the area when it forms. Objects still maintain their function
while in the area, so a sword still cuts, even if it loses its magical properties.

## Divination Words {#divination-words}

Words from this family uncover answers and scry across vast distances.

### Beacon {#beacon}

::: statblock
Abbrev: Divination
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **bard 0, druid 0, ranger 1
:::

::: paragraph statline
**Duration **1 hour/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

When a wordspell with this effect word is cast, the exact location of the caster becomes a fixed
point. For the duration of the wordspell, the caster always knows the direction and distance to the
point where this wordspell was cast. If this word is cast again, the original casting immediately
ends. This effect does not instruct the caster on how to reach the point, but rather merely
indicates the direction to the point, even if that direction leads through solid objects and other
hazards.

### Far Sight {#far-sight}

::: statblock
Abbrev: Divination
:::

::: paragraph statline
**School **divination (scrying)
:::

::: paragraph statline
**Level **bard 3, cleric 3, druid 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The caster of a wordspell with this effect word creates an invisible eye at any point within 400
feet + 40 feet per caster level. This sensor cannot move, but for the duration of the wordspell, the
caster can look through this eye as if it were her own. The eye uses her senses, including magical
ones, to allow her to see, including [darkvision](ref/rule/darkvision),
[low-light vision](ref/rule/low-light-vision), or other effects, such as _sense magic_. The eye can
view in all directions and cannot be destroyed if discovered.

#### Boost {#boost-19}

This sensor can be placed anywhere on the same plane of existence as the caster, with no limit to
range. The caster can place it to within 10 feet of a creature that is known to the caster, but the
target gets a Will save to negate the effect in this case and the caster must overcome the target's
[spell resistance](ref/rule/spell-resistance). Boosting this effect word increases its level by 2.

### Locate {#locate}

::: statblock
Abbrev: Divination
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **bard 6, cleric 6, druid 6, inquisitor 6, witch 6
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The caster of a wordspell with this effect word can name any location she has visited before or any
object she has held before. For the duration of this wordspell, she always knows the direction of
the named location or object. The direction is always the swiftest path to travel, leading her
perfectly through mazes or other obstacles by the method the wordcaster is currently traveling,
irrespective of danger.

## Electricity Words {#electricity-words}

Spells using electricity words crackle with life and leap from target to target in arcs of burning
light.

### Spark {#spark}

::: statblock
Abbrev: Electricity
:::

::: paragraph statline
**School **evocation \[electricity\]
:::

::: paragraph statline
**Level **druid 0, magus 0, sorcerer/wizard 0, witch 0
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d4 points of electricity damage. If the wordspell with this effect word has
only a single target, it requires a melee or ranged touch attack and does not allow a saving throw.

### Shock Arc {#shock-arc}

::: statblock
Abbrev: Electricity
:::

::: paragraph statline
**School **evocation \[electricity\]
:::

::: paragraph statline
**Level **magus 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d4 points of electricity damage per caster level (maximum 5d4).

### Lightning Blast {#lightning-blast}

::: statblock
Abbrev: Electricity
:::

::: paragraph statline
**School **evocation \[electricity\]
:::

::: paragraph statline
**Level **druid 3, magus 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d6 points of electricity damage per caster level (maximum 10d6).

### Ball Lightning {#ball-lightning}

::: statblock
Abbrev: Electricity
:::

::: paragraph statline
**School **evocation \[electricity\]
:::

::: paragraph statline
**Level **druid 5, magus 5, sorcerer/wizard 5, witch 6
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word deals 1d8 points of electricity damage per caster level (maximum 15d8 to one
target + 1/2 that damage to any other targets included in the effect).

### Thunder Strike {#thunder-strike}

::: statblock
Abbrev: Electricity
:::

::: paragraph statline
**School **evocation \[electricity\]
:::

::: paragraph statline
**Level **druid 8, sorcerer/wizard 8, witch 9
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d8 points of electricity damage per caster level (maximum 20d8). In
addition, a target that fails its saving throw against this damage is deafened for 1 round per
caster level.

## Fear Words {#fear-words}

These words conjure a primal terror in all that hear them.

### Spook {#spook}

::: statblock
Abbrev: Fear
:::

::: paragraph statline
**School **necromancy \[fear, mind-affecting\]
:::

::: paragraph statline
**Level **bard 1, cleric 1, inquisitor 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **1d4 rounds
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **Yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word causes the target to become frightened for the duration. This word has no effect on
targets with 5 or more Hit Dice.

### Terror {#terror}

::: statblock
Abbrev: Fear
:::

::: paragraph statline
**School **necromancy \[fear, mind-affecting\]
:::

::: paragraph statline
**Level **bard 3, inquisitor 4, sorcerer/wizard 4, witch 4
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **Yes
:::

This effect word causes the targets to become frightened for the duration. A target that succeeds at
its saving throw is shaken for 1 round.

### Horror {#horror}

::: statblock
Abbrev: Fear
:::

::: paragraph statline
**School **necromancy \[fear, mind-affecting\]
:::

::: paragraph statline
**Level **sorcerer/wizard 7, witch 7
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Fortitude negates
:::

::: paragraph statline
**Spell Resistance **Yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word causes the target to take 10 points of damage per caster level. If the save
succeeds, the target instead takes 3d6 points of damage + 1 per caster level.

## Fire Words {#fire-words}

Spells using fire words burn with a hungry flame that consumes all it encounters.

### Flame Jet {#flame-jet}

::: statblock
Abbrev: Fire
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **druid 0, magus 0, sorcerer/wizard 0
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **Yes
:::

This effect word deals 1d4 points of fire damage. If the wordspell with this effect has only a
single target, it requires a melee or ranged touch attack to hit and does not allow a saving throw.

### Burning Flash {#burning-flash}

::: statblock
Abbrev: Fire
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **druid 2, inquisitor 2, magus 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d4 points of fire damage per caster level (maximum 5d4). If the wordspell
with this effect word has only a single target, it requires a ranged touch attack to hit and does
not allow a saving throw.

#### Boost {#boost-20}

::: paragraph statline
This spell does 1d6 points of fire damage per caster level, maximum 5d6. Boosting this effect word
increases its level by 1.
:::

### Fire Blast {#fire-blast}

::: statblock
Abbrev: Fire
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **magus 3, sorcerer/wizard 3
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d6 points of fire damage per caster level (maximum 10d6).

### Cinder Storm {#cinder-storm}

::: statblock
Abbrev: Fire
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **cleric 5, druid 5, inquisitor 5, magus 5, sorcerer/wizard 5, summoner 5
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d6 points of fire damage per caster level (maximum 15d6).

### Inferno {#inferno}

::: statblock
Abbrev: Fire
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **druid 8, sorcerer/wizard 8
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d8 points of fire damage per caster level (maximum 20d8).

### True Fire {#true-fire}

::: statblock
Abbrev: Fire
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **druid 9, sorcerer/wizard 9
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word deals 1d6 points of fire damage per caster level (maximum 20d6).

## Flight Words {#flight-words}

These words allow those who know them to soar through the heavens—slowing falls with weaker
wordspells, but gaining true flight with the greatest one.

### Glide {#glide}

::: statblock
Abbrev: Flight
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 1, bard 1, magus 1, sorcerer/wizard 1, summoner 1, witch 1
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word falls at a rate of 20 feet per round, and for every
5 feet fallen in this way, can move horizontally 20 feet, up to a maximum of 80 feet per round.
Regardless of the circumstances, the target can never gain elevation with this effect, and the
wordspell with this effect word immediately ends the next time the target lands on a solid surface.
If the spell ends while the subject is still gliding, the subject falls as normal.

### Float {#float}

::: statblock
Abbrev: Flight
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 2, bard 2, magus 2, sorcerer/wizard 2, summoner 2, witch 2
:::

::: paragraph statline
**Duration **1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word can float in the air, rising or falling at a rate of
30 feet per round as a move action. This effect only allows for vertical movement, but other forces
might allow the target to move horizontally as well. The caster has no control over this movement,
but can end a wordspell with this effect word prematurely as an immediate action.

### Soar {#soar}

::: statblock
Abbrev: Flight
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 3, cleric 4, magus 3, sorcerer/wizard 3, summoner 3, witch 3
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word gains a fly speed of 60 feet with average
maneuverability (40 feet if encumbered or wearing medium or heavy armor). The target also receives
an insight bonus on Fly skill checks equal to 1/2 the caster's level.

## Force Words {#force-words}

These words use raw magic to create pure force.

### Force Bolt {#force-bolt}

::: statblock
Abbrev: Force
:::

::: paragraph statline
**School **evocation \[force\]
:::

::: paragraph statline
**Level **magus 2, sorcerer/wizard 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **Yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word deals 1d4 points of force damage per caster level (maximum 5d4). This effect is
treated like a _[magic missile](ref/spell/magic-missile)_ for the purposes of spells that negate or
absorb force effects.

### Force Blast {#force-blast}

::: statblock
Abbrev: Force
:::

::: paragraph statline
**School **evocation \[force\]
:::

::: paragraph statline
**Level **magus 5, sorcerer/wizard 5
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **Yes
:::

This effect word deals 1d6 points of force damage per caster level (maximum 10d6).

## Gravity Words {#gravity-words}

Words from the gravity family use an unseen force to manipulate objects and creatures.

### Lift {#lift}

::: statblock
Abbrev: Gravity
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **bard 0, magus 0, sorcerer/wizard 0, summoner 0
:::

::: paragraph statline
**Duration **concentration
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

This effect word grants the caster the ability to lift and move nonmagical objects weighing up to 5
pounds at a distance of up to 25 feet + 5 feet per two levels of the caster. Objects moved by this
effect can be moved up to 15 feet per round and cannot be used to make attacks.

### Unfetter {#unfetter}

::: statblock
Abbrev: Gravity
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **druid 7, sorcerer/wizard 6
:::

::: paragraph statline
**Duration **1 round/level (D)
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word makes the bonds of gravity work in reverse for the targets, causing them to fall up
for the duration. They treat up as down and down as up. This can cause the creatures to take falling
damage when they hit the ceiling or another surface above them. This effect applies to the targets
and all of their gear, so long as it remains on their person. Thrown and missile weapons interact
with gravity normally, but the disorientation caused by unfetter means the target takes a –4 penalty
on such attacks. When a wordspell with this effect word ends, the targets fall to the ground unless
they have some means of staying aloft.

### Repulse {#repulse}

::: statblock
Abbrev: Gravity
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **cleric 9, druid 9, sorcerer/wizard 8, summoner 6, witch 8
:::

::: paragraph statline
**Duration **1 round/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

This effect word creates an area of impossible gravity, where all creatures and objects not securely
fastened to the ground fall away from the center of the burst, to its exterior edge. Creatures
inside the area when it forms are immediately moved toward its nearest edge. If, because of an
obstacle, they cannot reach the edge, they strike the barrier and take falling damage. While a
wordspell with this effect word persists, objects cannot enter the area unless they possess the
ability to fly. Any flying creatures that rely on wings and enter the area must immediately make a
DC 25 Fly skill check or be repelled by the area, unable to enter this turn. Missile weapons that
pass through this area automatically miss their target. The caster is immune to this effect and may
enter the area freely.

#### Boost {#boost-21}

::: paragraph statline
The caster may designate a number of creatures equal to his level that are not affected by the
wordspell.
:::

## Healing Words {#healing-words}

Healing words knit the flesh and soothe the body, repairing even the most grievous harm.

### Soothing Touch {#soothing-touch}

::: statblock
Abbrev: Healing
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **cleric 0, druid 0, inquisitor 0, paladin 1, witch 0
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

If the target of a wordspell with this effect word is dying, it is automatically stabilized.

#### Boost {#boost-22}

::: paragraph statline
The target of a wordspell with this effect word is cured of the shaken, sickened, or fatigued
condition (caster's choice). Boosting this effect word increases its level by 1.
:::

### Lesser Cure {#lesser-cure}

::: statblock
Abbrev: Healing
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **alchemist 1, bard 1, cleric 1, druid 1, inquisitor 1, paladin 1, ranger 2, witch 1
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half (harmless) or Will half
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word is cured of 1d6 points of damage + 1 point per
caster level (maximum +5). Undead are damaged by this effect word instead, but can attempt a Will
save for half damage and [spell resistance](ref/rule/spell-resistance) as normal.

#### Boost {#boost-23}

::: paragraph statline
The target is cured of 1d8 points of damage + 1 point per caster level (maximum +5).
:::

### Moderate Cure {#moderate-cure}

::: statblock
Abbrev: Healing
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **alchemist 2, bard 2, cleric 2, druid 3, inquisitor 2, paladin 3, ranger 3, witch 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half (harmless) or Will half
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word is cured of 2d6 points of damage + 1 point per
caster level (maximum +10). Undead are damaged by this effect word, but can attempt a Will save for
half damage and [spell resistance](ref/rule/spell-resistance) as normal.

#### Boost {#boost-24}

::: paragraph statline
The target is cured of 2d8 points of damage + 1 point per caster level (maximum +10).
:::

### Greater Cure {#greater-cure}

::: statblock
Abbrev: Healing
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **alchemist 3, bard 3, cleric 3, druid 4, inquisitor 3, paladin 4, ranger 4, witch 4
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half (harmless) or Will half
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word is cured of 3d6 points of damage + 1 point per
caster level (maximum +15). Undead are damaged by this effect word, but can attempt a Will save for
half damage and [spell resistance](ref/rule/spell-resistance) as normal.

#### Boost {#boost-25}

::: paragraph statline
The target is cured of 3d8 points of damage + 1 point per caster level (maximum +15).
:::

### Elder Cure {#elder-cure}

::: statblock
Abbrev: Healing
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **alchemist 4, bard 4, cleric 4, druid 5, inquisitor 4, witch 5
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half (harmless) or Will half
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

The target of a wordspell with this effect word is cured of 4d6 points of damage + 1 point per
caster level (maximum +20). Undead are damaged by this effect word, but can attempt a Will save for
half damage and [spell resistance](ref/rule/spell-resistance) as normal.

#### Boost {#boost-26}

::: paragraph statline
The target is cured of 4d8 points of damage + 1 point per caster level (maximum +20).
:::

## Illumination Words {#illumination-words}

Illumination words can either create light or siphon it away, instead creating darkness.

### Radiance {#radiance}

::: statblock
Abbrev: Illumination
:::

::: paragraph statline
**School **evocation
:::

::: paragraph statline
**Level **bard 1, cleric 1, druid 1, inquisitor 1, magus 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

The area of a wordspell with this effect word radiates light like a torch for the duration, shedding
normal light in the wordspell's area and increasing the light level for an additional 20 feet by one
step, up to normal light.

### Gloom {#gloom}

::: statblock
Abbrev: Illumination
:::

::: paragraph statline
**School **evocation
:::

::: paragraph statline
**Level **bard 2, cleric 2, magus 2, sorcerer/wizard 2, witch 2
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

The target of a wordspell with this effect word radiates darkness out to a range of 20 feet,
negating all natural light sources and all magical light sources of a level lower than the
wordspell. It reduces the natural light level by one step. A wordspell with this effect word has no
effect on an area that is already dark.

### Sunshine {#sunshine}

::: statblock
Abbrev: Illumination
:::

::: paragraph statline
**School **evocation
:::

::: paragraph statline
**Level **bard 3, cleric 3, druid 3, paladin 3, sorcerer/wizard 3
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

The target of a wordspell with this effect word radiates shining white light for the duration of the
spell, shedding bright light in the wordspell's area and increasing the light level for an
additional 30 feet by one step, up to bright light. Creatures that take penalties in bright light
take those penalties while in the wordspell's area, but it is not true sunlight and does not damage
or destroy creatures vulnerable to real sunlight.

## Illusion Words {#illusion-words}

These words deceive the senses, leaving those that witness them unsure of the world around them.

### Echo {#echo}

::: statblock
Abbrev: Illusion
:::

::: paragraph statline
**School **illusion (figment)
:::

::: paragraph statline
**Level **bard 0, sorcerer/wizard 0
:::

::: paragraph statline
**Duration **1 round/level (D)
:::

::: paragraph statline
**Saving Throw **Will disbelief
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

This effect word targets a single location, creating a sound that rises, recedes, or remains
constant for the duration. The sound's volume increases with the caster's level. The base Perception
DC to notice this sound is 0, but the DC is reduced by 1 per caster level (although it can be higher
if the caster desires). This means that the sound starts out as loud as a creature talking, but by
10th level, it is as loud as creatures engaged in a noisy battle. The sound can resemble anything
the caster desires, except it cannot replicate speech or language. Once cast, the type of sound
within the emanation cannot be changed.

### Glimmering {#glimmering}

::: statblock
Abbrev: Illusion
:::

::: paragraph statline
**School **illusion (figment)
:::

::: paragraph statline
**Level **bard 2, sorcerer/wizard 3
:::

::: paragraph statline
**Duration **1 round/level (D)
:::

::: paragraph statline
**Saving Throw **Will disbelief
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

This effect word creates a visual illusion centered on a target space within range. The illusion
must be contained within the burst radius. This illusion only contains visual elements, and while it
can move, its movements are repeated once per round. It can otherwise have any appearance the caster
desires. The caster can change the illusion's movements by concentrating, but it cannot leave its
initial area.

## Language Words {#language-words}

Words from this family deal with language and help with communication.

### Decipher {#decipher}

::: statblock
Abbrev: Language
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **alchemist 1, bard 0, cleric 0, druid 0, inquisitor 0, magus 0, paladin 1, ranger 1,
sorcerer/wizard 0, summoner 0, witch 0
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The target of a wordspell with this effect word can read text written in one particular language,
including the language of magic. The caster picks the language when the wordspell is cast. For the
duration, the target can read that language as if fluent in it. If the caster chooses magic as the
language, the target can decipher scrolls, glyphs, and other magic writing without triggering them.
A wordspell with this effect word does not impart the ability to determine what a given language is
based on its appearance; the caster must already know the language or guess what language the
writing is in to do so.

#### Boost {#boost-27}

::: paragraph statline
This effect word can use the _selected_ target word. Boosting this effect word increases its level
by 1.
:::

### Translate {#translate}

::: statblock
Abbrev: Language
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **alchemist 3, bard 2, cleric 4, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **10 minutes/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word can read, write, speak, and understand one
particular language, chosen by the caster. The language can be any that the caster is aware of, even
racial languages.

### Far Casting {#far-casting}

::: statblock
Abbrev: Language
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **bard 5, cleric 5, sorcerer/wizard 5, witch 5
:::

::: paragraph statline
**Duration **concentration
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The target of a wordspell with this effect word can reach out to another willing creature that the
target knows of and that is on the same plane of existence as the target. As long as the wordcaster
concentrates, the target can communicate verbally with the willing creature, and the willing
creature can communicate back. The target and the willing creature do not need to share a language
to communicate in this way.

#### Boost {#boost-28}

::: paragraph statline
This word can use the _selected_ target word. Boosting this effect word increases its level by 1.
:::

## Life Words {#life-words}

Spells using these words can restore life to the dead and heal the most serious of afflictions.

### Purify {#purify}

::: statblock
Abbrev: Life
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **alchemist 4, bard 4, cleric 4, druid 4, inquisitor 4, paladin 4, ranger 4
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **personal, selected
:::

When a wordspell with this effect word is cast, the wordcaster chooses one type of affliction:
curses, diseases, or poisons. The target of a wordspell with this effect word receives a new saving
throw to immediately end all such afflictions of the chosen type currently affecting the target. The
DC of this save is equal to the original DC of the affliction. The target must roll a saving throw
for each affliction individually. If the affliction does not allow a saving throw, this effect word
cannot remove that affliction.

Alternatively, a wordspell with this effect word can be used to remove 1d4 temporary negative levels
possessed by the target, or 1 permanent negative level.

### Revive {#revive}

::: statblock
Abbrev: Life
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **cleric 5, druid 5, witch 5
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word restores life to a living creature that has died within up to 1 hour per caster
level. The soul of the target receives a clear image of the caster, and can choose not to return,
causing the wordspell to fail. If the soul is willing, the target does not receive a saving throw.

The target is restored to life with 1 hit point, unless another effect word adds to this total. In
addition, the target loses 50% of any prepared spells or spell slots it had before it died
(determined randomly). Coming back from the dead in this way is an ordeal, and the target gains
three permanent negative levels from the experience (if the target does not have at least 4 Hit
Dice, a wordspell with this effect word has no effect).

While this effect word undoes any mortal wounds the target might possess, its body must otherwise be
whole for the effect word to function. Any missing parts are still missing when the creature is
restored. Normal poisons and diseases are cured as well, but magical afflictions remain. Undead
creatures are unaffected by a wordspell with this effect word, as are the dead bodies of creatures
that were undead. Constructs and outsiders cannot be restored to life by this effect word. Targets
that died as a result of old age cannot be restored to life by this effect word.

### Life Touch {#life-touch}

::: statblock
Abbrev: Life
:::

::: paragraph statline
**School **conjuration (healing)
:::

::: paragraph statline
**Level **cleric 8, witch 8
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _revive_, but it can be used on a creature that has been dead for up
to 1 day per caster level. The creature is restored with half its original hit points, and its body
does not need to be whole (just a piece of the creature is required). Any parts of the creature that
were missing before its death are not restored by this effect word. The creature gains only one
permanent negative level from being restored by this effect word, and this negative level fades
after 24 hours (although it can be removed early as normal). The creature retains all of the
prepared spells and slots it had when it died.

## Pain Words {#pain-words}

The mere sound of these words causes agony in those unfortunate enough to hear them.

### Cramp {#cramp}

::: statblock
Abbrev: Pain
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **bard 0, cleric 0, inquisitor 0, sorcerer/wizard 0, witch 0
:::

::: paragraph statline
**Duration **1 round
:::

::: paragraph statline
**Saving Throw **Fortitude negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

The targets of a wordspell with this effect word have their base speed reduced by half (minimum 10
feet).

### Wrack {#wrack}

::: statblock
Abbrev: Pain
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **bard 1, cleric 1, inquisitor 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Fortitude negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

The targets of a wordspell with this effect word are sickened.

### Torture {#torture}

::: statblock
Abbrev: Pain
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **bard 3, inquisitor 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Fortitude negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

The targets of a wordspell with this effect word are nauseated; they receive another save at the end
of their turn to end this effect.

## Power Words {#power-words}

Perhaps the most primal effect words, power words draw upon raw magic, using it to cripple and even
kill the wordcaster's foes.

### Blind {#blind}

::: statblock
Abbrev: Power
:::

::: paragraph statline
**School **enchantment (compulsion) \[mind-affecting\]
:::

::: paragraph statline
**Level **sorcerer/wizard 7
:::

::: paragraph statline
**Duration **varies, see text
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word causes a living creature to become blinded, whether or not the creature can hear
the wordspell. This effect word's duration depends on the target's current hit point total. Any
creature that currently has 201 hit points or more is unaffected.

#### Table: Blind {#table-blind}

::: statblock
Abbrev: Power
:::

::: table
caption = "Table: Blind (Power)"
head = [
  [
    { text = "Hit Points", header = true },
    { text = "Duration", header = true },
  ],
]
body = [
  [
    { text = "50 or less" },
    { text = "Permanent" },
  ],
  [
    { text = "51–100" },
    { text = "1d4+1 minutes" },
  ],
  [
    { text = "101–200" },
    { text = "1d4+1 rounds" },
  ],
]
:::

### Stun {#stun}

::: statblock
Abbrev: Power
:::

::: paragraph statline
**School **enchantment (compulsion) \[mind-affecting\]
:::

::: paragraph statline
**Level **sorcerer/wizard 8
:::

::: paragraph statline
**Duration **varies, see text
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word causes a living creature to become stunned, whether or not the creature can hear
the wordspell with this effect word. This effect word's duration depends on the target's current hit
point total. Any creature that currently has 151 hit points or more is unaffected.

#### Table: Stun {#table-stun}

::: statblock
Abbrev: Power
:::

::: table
caption = "Table: Stun (Power)"
head = [
  [
    { text = "Hit Points", header = true },
    { text = "Duration", header = true },
  ],
]
body = [
  [
    { text = "50 or less" },
    { text = "4d4 rounds" },
  ],
  [
    { text = "51–100" },
    { text = "2d4 rounds" },
  ],
  [
    { text = "101–150" },
    { text = "1d4 rounds" },
  ],
]
:::

### Kill {#kill}

::: statblock
Abbrev: Power
:::

::: paragraph statline
**School **enchantment (compulsion) \[death, mind-affecting\]
:::

::: paragraph statline
**Level **sorcerer/wizard 9
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word slays one living creature, whether or not the creature can hear the wordspell with
this effect word. Any creature that currently has 101 hit points or more is unaffected.

## Sonic Words {#sonic-words}

Sonic words utilize sound to deafen and damage those that hear them.

### Discordant Note {#discordant-note}

::: statblock
Abbrev: Sonic
:::

::: paragraph statline
**School **evocation \[sonic\]
:::

::: paragraph statline
**Level **bard 2, cleric 2, magus 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Fortitude half and partial
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d4 points of sonic damage per caster level (maximum 5d4) and causes the
targets to become staggered for 1 round. A successful Fortitude save halves the damage and negates
the staggered condition.

### Sound Blast {#sound-blast}

::: statblock
Abbrev: Sonic
:::

::: paragraph statline
**School **evocation \[sonic\]
:::

::: paragraph statline
**Level **bard 4, magus 4, sorcerer/wizard 4
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

This effect word deals 1d6 points of sonic damage per caster level (maximum 10d6).

### Destructive Vibration {#destructive-vibration}

::: statblock
Abbrev: Sonic
:::

::: paragraph statline
**School **evocation \[sonic\]
:::

::: paragraph statline
**Level **bard 6, sorcerer/wizard 7
:::

::: paragraph statline
**Duration **instantaneous, 1 round/level, see text
:::

::: paragraph statline
**Saving Throw **Fortitude half and negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **line
:::

This effect word deals 1d6 points of sonic damage per caster level (maximum 15d6) and causes the
targets to become deafened for 1 round per level. A successful Fortitude save halves the damage and
negates the deafened condition.

## Summoning Words {#summoning-words}

These words summon creatures from other planes of existence to do the caster's bidding.

### Servitor I {#servitor-i}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **bard 1, cleric 1, druid 1, ranger 1, sorcerer/wizard 1, summoner 1, witch 1
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

A wordspell with this effect word summons a creature to do your bidding. This creature attacks your
opponents to the best of its ability each turn if able. If you can communicate with the creature,
you can direct its attacks or instruct it to perform other actions. A wordspell with this effect
word summons one creature from Table 10–1 on pages 351–352 of the _Core Rulebook_ from the 1st-level
list. If a wordspell with this effect word is cast by a ranger or druid, it instead summons a
creature from Table 10–2 on page 353 of the _Core Rulebook_ from the 1st-level list.

A summoned creature cannot summon or conjure other creatures, nor can its use teleportation or
planar travel abilities. Creatures cannot be summoned into an environment that cannot support them.
Creatures summoned using a wordspell with this effect word cannot use spells or
[spell-like abilities](ref/umr/spell-like-abilities) with expensive material components.

If a wordspell with this effect word is used to summon a creature with an alignment or elemental
subtype, it is a wordspell of that type. Creatures marked with an asterisk (\*) are summoned with
the celestial template if you are good, and the fiendish template if you are evil. If you are
neutral, you may choose which template to apply. Creatures summoned using a wordspell with this
effect word that lack an alignment or elemental subtype always have an alignment that matches yours,
regardless of their usual alignment.

If you combine this word with any other effect words, the summoned creature is the only target for
these words. If the target word is boosted, a wordspell with this effect word summons 1d4+1 of the
chosen creatures.

### Servitor II {#servitor-ii}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **bard 2, cleric 2, druid 2, ranger 2, sorcerer/wizard 2, summoner 2, witch 2
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 2nd-level list. If a wordspell with this effect word is cast by a ranger or
druid, it instead summons a creature from the summon nature's ally table from the 2nd-level list. If
the target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor III {#servitor-iii}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **bard 3, cleric 3, druid 3, ranger 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 3rd-level list. If a wordspell with this effect word is cast by a ranger or
druid, it instead summons a creature from the summon nature's ally table from the 3rd-level list. If
the target word is boosted, a spell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor IV {#servitor-iv}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **bard 4, cleric 4, druid 4, ranger 4, sorcerer/wizard 4, summoner 3, witch 4
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 4th-level list. If a wordspell with this effect word is cast by a ranger or
druid, it instead summons a creature from the summon nature's ally table from the 4th-level list. If
the target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor V {#servitor-v}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **bard 5, cleric 5, druid 5, sorcerer/wizard 5, witch 5
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 5th-level list. If a wordspell with this effect word is cast by a druid, it
instead summons a creature from the summon nature's ally table from the 5th-level list. If the
target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor VI {#servitor-vi}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **bard 6, cleric 6, druid 6, sorcerer/wizard 6, summoner 4, witch 6
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 6th-level list. If a wordspell with this effect word is cast by a druid, it
instead summons a creature from the summon nature's ally table from the 6th-level list. If the
target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor VII {#servitor-vii}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **cleric 7, druid 7, sorcerer/wizard 7, summoner 5, witch 7
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 7th-level list. If a wordspell with this effect word is cast by a druid, it
instead summons a creature from the summon nature's ally table from the 7th-level list. If the
target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor VIII {#servitor-viii}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **cleric 8, druid 8, sorcerer/wizard 8, witch 8
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_, except that it summons one creature from the summon
monster table from the 8th-level list. If a wordspell with this effect spell is cast by a druid, it
instead summons a creature from the summon nature's ally table from the 8th-level list. If the
target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

### Servitor IX {#servitor-ix}

::: statblock
Abbrev: Summoning
:::

::: paragraph statline
**School **conjuration (summoning)
:::

::: paragraph statline
**Level **cleric 9, druid 9, sorcerer/wizard 9, summoner 6, witch 9
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **selected
:::

This effect word functions as _servitor I_ except that it summons one creature from the summon
monster table from the 9th-level list. If a wordspell with this effect word is cast by a druid, it
instead summons a creature from the summon nature's ally table from the 9th-level list. If the
target word is boosted, a wordspell with this effect word summons 1d4+1 of the chosen creatures.

## Teleportation Words {#teleportation-words}

Teleportation words transport the targets to other places, or even other planes of existence.

### Dimensional Hop {#dimensional-hop}

::: statblock
Abbrev: Teleportation
:::

::: paragraph statline
**School **conjuration (teleportation)
:::

::: paragraph statline
**Level **bard 3, magus 3, sorcerer/wizard 3, summoner 3, witch 3
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

A wordspell with this effect word teleports willing targets to another location within line of sight
of the wordcaster and within range of the wordspell.

### Dimensional Jump {#dimensional-jump}

::: statblock
Abbrev: Teleportation
:::

::: paragraph statline
**School **conjuration (teleportation)
:::

::: paragraph statline
**Level **magus 5, sorcerer/wizard 5, summoner 5, witch 5
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

A wordspell with this effect word teleports willing targets to another location on the same plane of
existence. The wordcaster must be one of the targets of a wordspell with this effect word and the
destination must be a place he has visited in the past.

### Dimensional Shift {#dimensional-shift}

::: statblock
Abbrev: Teleportation
:::

::: paragraph statline
**School **conjuration (teleportation)
:::

::: paragraph statline
**Level **cleric 5, sorcerer/wizard 7, witch 7
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

A wordspell with this effect word teleports willing targets to another plane of existence. The
caster must be one of the targets of a wordspell with this effect word. The wordcaster cannot
precisely control the destination, except for specifying the plane and having the targets arrive
within 5–500 miles of the intended location.

### Dimensional Gate {#dimensional-gate}

::: statblock
Abbrev: Teleportation
:::

::: paragraph statline
**School **conjuration (teleportation)
:::

::: paragraph statline
**Level **cleric 8, sorcerer/wizard 9
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

A wordspell with this effect word creates a gateway between the wordcaster's current plane and
another plane of existence. While this gate is open, creatures, spells, effects, and objects from
either plane can freely pass between the planes through the gateway, which takes the form of an
archway dividing the emanation in half. The wordcaster cannot control the destination on the other
plane and the target will arrive within 5–500 miles of the intended location.

## Time Words {#time-words}

Spells containing time words alter the flow of time, speeding it up or slowing it down.

### Fleet {#fleet}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **druid 1, ranger 1
:::

::: paragraph statline
**Duration **1 hour/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The target of a wordspell with this effect word has its base land speed increased by 10 feet for the
duration of this effect word.

### Dash {#dash}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 1, bard 1, inquisitor 1, magus 1, sorcerer/wizard 1, summoner 1
:::

::: paragraph statline
**Duration **1 minute/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The target of a wordspell with this effect word has its base land speed increased by 30 feet for the
duration of this effect word.

### Accelerate {#accelerate}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 2, bard 2, magus 2, sorcerer/wizard 2, summoner 2
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word can take one additional move action each turn. This
move action can come before, after, or between other actions, but not during a full-round action.

#### Boost {#boost-29}

::: paragraph statline
If the target takes a full-attack action, it can, instead of taking an extra move action, make one
additional attack at its highest attack bonus.
:::

### Decelerate {#decelerate}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **bard 2, magus 2, sorcerer/wizard 2, summoner 2
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word is staggered for this effect word's duration. The
target is allowed a new saving throw against this effect word at the end of each of its turns; a
successful save ends the duration of this effect word.

#### Boost {#boost-30}

::: paragraph statline
The target of a wordspell with this effect word does not receive any additional saving throws to end
the effect. If the target fails the first saving throw, it is staggered for the entire duration.
:::

### Predict {#predict}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **divination
:::

::: paragraph statline
**Level **cleric 2, witch 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

The target of a wordspell with this effect word can look into the future of one particular action
that will happen within the next hour and determine whether or not it is likely to have good or bad
results. This prediction is not guaranteed; there is only a 70% chance of receiving an accurate
prediction + 1% per caster level. If this check fails, the results are incorrect. The only
information the target receives is “weal” for a good outcome, “woe” for a bad outcome, or both for
outcomes that are both good and bad, or that are or neutral in regard to the caster. Additional
castings concerning the same course of action always reveal the same results.

### Borrow Future {#borrow-future}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **alchemist 4, bard 4, magus 4, sorcerer/wizard 4, summoner 4
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes either a standard action and a move action or
a full-round action immediately after a wordspell with this effect word is cast (maximum once per
round). The target skips its next turn, but any effects that would occur on its turn or spell
effects that would expire on its turn occur normally. The target is not helpless on its next turn,
but can take no actions.

#### Boost {#boost-31}

::: paragraph statline
Instead of losing its next turn, the target of a wordspell with this effect word is staggered on its
next turn.
:::

### Control Time {#control-time}

::: statblock
Abbrev: Time
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **sorcerer/wizard 9
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates (harmless)
:::

::: paragraph statline
**Spell Resistance **yes (harmless)
:::

::: paragraph statline
**Target Restrictions **selected
:::

Time around the target of a wordspell with this effect word comes to a halt, allowing the target to
take 1d4 standard actions before time resumes. All other creatures and objects are immune to the
target during these additional actions. Other creatures cannot even be targeted while time is
stopped in this way. The target can cast spells and use items on his person at the time of the
casting as normal.

## Wall Words {#wall-words}

Wall words create large barriers that impede and harm those who pass through them.

### Wind Wall {#wind-wall}

::: statblock
Abbrev: Wall
:::

::: paragraph statline
**School **evocation \[air\]
:::

::: paragraph statline
**Level **cleric 3, druid 3, magus 3, ranger 3, sorcerer/wizard 3, summoner 3
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **barrier
:::

This effect word creates a vertical wall of swirling wind. This wind does not obscure sight, but
missile weapons that pass through the wall automatically miss (with the exception of large missiles,
such as giant-thrown rocks and siege weapons). Creatures that pass through the wall treat it as
difficult terrain and must make a DC 10 Strength check. Failure indicates that the creature cannot
pass through the wall this round, but may try again in future rounds. Gases, gaseous breath weapons,
and creatures in _[gaseous form](ref/spell/gaseous-form)_ cannot pass through the wall.

### Fire Wall {#fire-wall}

::: statblock
Abbrev: Wall
:::

::: paragraph statline
**School **evocation \[fire\]
:::

::: paragraph statline
**Level **druid 4, magus 4, sorcerer/wizard 4, summoner 4
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **barrier
:::

This effect word creates a vertical wall of crackling flame. Creatures in the space of the wall when
it forms or that attempt to pass through the wall take 2d6 points of fire damage + 1 point of fire
damage per level of the wordcaster (maximum +20). A Reflex save halves this damage. The wall blocks
line of sight.

### Ice Wall {#ice-wall}

::: statblock
Abbrev: Wall
:::

::: paragraph statline
**School **evocation \[cold\]
:::

::: paragraph statline
**Level **druid 4, magus 4, sorcerer/wizard 4, summoner 4
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **barrier
:::

This effect word creates a vertical wall of solid ice. The wall must be a smooth, uninterrupted
surface when formed. The wall is 1 inch thick per caster level and has 3 hit points per inch of
thickness. The wall blocks line of sight.

### Stone Wall {#stone-wall}

::: statblock
Abbrev: Wall
:::

::: paragraph statline
**School **conjuration (creation)
:::

::: paragraph statline
**Level **cleric 5, druid 6, magus 5, sorcerer/wizard 5, summoner 5
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **barrier
:::

This effect word creates a vertical wall of solid stone. The wall must be a smooth, uninterrupted
surface when formed. The wall is 1 inch thick per caster level, has [hardness](ref/umr/hardness) 8,
and has 15 hit points per inch of thickness. The wall blocks line of sight.

### Blade Wall {#blade-wall}

::: statblock
Abbrev: Wall
:::

::: paragraph statline
**School **conjuration (creation)
:::

::: paragraph statline
**Level **cleric 6, summoner 5
:::

::: paragraph statline
**Duration **1 round/level
:::

::: paragraph statline
**Saving Throw **Reflex half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **barrier
:::

This effect word creates a vertical wall of whirling blades that deals 1d6 points of damage per
level to any creature that comes in contact with it. If a creature is in the area of the wall when
it forms, that creature can make a Reflex save to avoid the damage entirely. Creatures that pass
through the wall can make a Reflex save to halve the damage. Regardless of the outcome of their
roll, they still move through the wall. This wall provides cover to creatures on the other side, but
does not block line of sight.

## Weather Words {#weather-words}

Words from the weather family control the forces of nature, summoning wind, rain, and snow.

### Fog Bank {#fog-bank}

::: statblock
Abbrev: Weather
:::

::: paragraph statline
**School **conjuration (creation)
:::

::: paragraph statline
**Level **cleric 1, druid 1, sorcerer/wizard 1, witch 1
:::

::: paragraph statline
**Duration **1 minute/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **barrier, burst (emanation)
:::

This effect word creates a thick fog in its area of effect. It obscures all sight, including
[darkvision](ref/rule/darkvision), beyond 5 feet. Creatures 5 feet away have concealment, whereas
creatures farther away have total concealment. A moderate wind or fire effect removes the fog in the
affected area. The fog is stationary.

#### Boost {#boost-32}

If a wordspell with this effect word uses the _burst_ target word, it can be directed to move up to
10 feet each round by the caster as a swift action.

### Wind Blast {#wind-blast}

::: statblock
Abbrev: Weather
:::

::: paragraph statline
**School **evocation \[air\]
:::

::: paragraph statline
**Level **druid 2, sorcerer/wizard 3
:::

::: paragraph statline
**Duration **1 round
:::

::: paragraph statline
**Saving Throw **Fortitude negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **line
:::

This effect word creates a blast of air that can knock over or hinder those in its path. When a
wordspell with this effect word is cast, any Large or smaller creature within the area of the
wordspell must make a Fortitude save or be knocked prone and pushed back 10 feet. Any creature
wishing to move through the line of air must make a DC 20 Strength check. Failure means the creature
wastes 5 feet of movement, but is otherwise unhindered and can continue to move (so long as it does
not move through the line of air). The DC increases to 30 if the creature attempts to move toward
the source of the wind. Flying creatures take a –4 penalty on saves and Strength checks made against
this effect.

### Blizzard {#blizzard}

::: statblock
Abbrev: Weather
:::

::: paragraph statline
**School **conjuration (creation)
:::

::: paragraph statline
**Level **druid 3, magus 3, sorcerer/wizard 3, witch 3
:::

::: paragraph statline
**Duration **1 round/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **burst (emanation)
:::

This effect word causes heavy snow to fall in the area of effect. This provides concealment as the
_fog bank_ effect word, but it cannot be removed by wind. In addition, the ground in the area of
effect is treated as difficult terrain for the duration and as being very slippery for the purposes
of Acrobatics and Climb skill checks.

#### Boost {#boost-33}

Each creature in the area of effect takes 2d6 points of cold damage each round at the end of its
turn. Boosting this effect word increases its level by 1.

### Storm Master {#storm-master}

::: statblock
Abbrev: Weather
:::

::: paragraph statline
**School **transmutation
:::

::: paragraph statline
**Level **cleric 7, druid 7, sorcerer/wizard 7, witch 7
:::

::: paragraph statline
**Duration **1 hour/level (D)
:::

::: paragraph statline
**Saving Throw **none
:::

::: paragraph statline
**Spell Resistance **no
:::

::: paragraph statline
**Target Restrictions **personal
:::

A word spell with this effect word grants the target the ability to alter the weather around it in a
1-mile radius. The target can change the conditions by shifting the weather one step at a time up or
down a scale of weather effects. The scale is as follows: freezing cold, blizzard, snow, cold rain,
cold wind, calm, warm wind, warm rain, thunderstorm, tornado, extreme heat. Each change takes 10
minutes to fully take effect. Thus if the weather currently features warm wind and the caster wanted
to change that to cold wind, she would need to first change the weather to calm, and then to cold
wind. The target cannot control the specifics of the weather, merely what type of weather is
occurring (the target cannot, for example, make lightning strike a house, but it can cause lighting
to strike within the area).

#### Boost {#boost-34}

Each change in the weather takes only 5 minutes.

## Wounding Words {#wounding-words}

Wounding words afflict the target with cuts and bruises, causing pain and tearing at its flesh.

### Bleeding Wounds {#bleeding-wounds}

::: statblock
Abbrev: Wounding
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **cleric 0, inquisitor 0, sorcerer/wizard 0, witch 0
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will negates
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

If the target of a wordspell with this effect word is dying, it takes 1 hit point of bleed damage
each turn.

#### Boost {#boost-35}

::: paragraph statline
The target of a wordspell with this effect takes 1d3 hit points of bleed damage. Boosting this
effect word increases its level by 1.
:::

### Lesser Wound {#lesser-wound}

::: statblock
Abbrev: Wounding
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **cleric 1, inquisitor 1, witch 1
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes 1d6 points of damage + 1 point per wordcaster
level (maximum +5). Undead are instead healed by this effect and do not receive a saving throw or
[spell resistance](ref/rule/spell-resistance).

#### Boost {#boost-36}

::: paragraph statline
The target of a wordspell with this effect takes 1d8 points of damage + 1 point per wordcaster level
(maximum +5).
:::

### Moderate Wound {#moderate-wound}

::: statblock
Abbrev: Wounding
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **cleric 2, inquisitor 2, witch 2
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes 2d6 points of damage + 1 point per wordcaster
level (maximum +10). Undead are instead healed by this wordspell and do not receive a saving throw
or [spell resistance](ref/rule/spell-resistance).

#### Boost {#boost-37}

::: paragraph statline
The target takes 2d8 points of damage + 1 point per caster level (maximum +10).
:::

### Greater Wound {#greater-wound}

::: statblock
Abbrev: Wounding
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **cleric 3, inquisitor 3, witch 3
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes 3d6 points of damage + 1 point per wordcaster
level (maximum +15). Undead are instead cured by this effect and do not receive a saving throw or
[spell resistance](ref/rule/spell-resistance).

#### Boost {#boost-38}

::: paragraph statline
The target takes 3d8 points of damage + 1 point per caster level (maximum +15).
:::

### Elder Wound {#elder-wound}

::: statblock
Abbrev: Wounding
:::

::: paragraph statline
**School **necromancy
:::

::: paragraph statline
**Level **cleric 4, inquisitor 4, witch 4
:::

::: paragraph statline
**Duration **instantaneous
:::

::: paragraph statline
**Saving Throw **Will half
:::

::: paragraph statline
**Spell Resistance **yes
:::

::: paragraph statline
**Target Restrictions **selected
:::

The target of a wordspell with this effect word takes 4d6 points of damage + 1 point per wordcaster
level (maximum +20). Undead are instead healed by this effect and do not receive a saving throw or
[spell resistance](ref/rule/spell-resistance).

#### Boost {#boost-39}

::: paragraph statline
The target takes of 4d8 points of damage + 1 point per caster level (maximum +20).
:::
