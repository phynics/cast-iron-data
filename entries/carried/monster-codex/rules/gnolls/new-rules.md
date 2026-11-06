+++
id = "ref/carried/monster-codex/rules/gnolls/new-rules"
kind = "rule"
title = "New Rules"
source_ids = ["monster-codex"]
section = ["Rules", "Gnolls"]
parent = "ref/carried/monster-codex/rules/gnolls"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Monster Codex/Rules/Gnolls/New Rules", path = "monster_codex/rules/gnolls.json" },
]

[fields]
kind = "none"
+++

The methods, materials, and magic of the gnolls focus on their pack mentality and their brutal,
savage nature.

## Gnoll Archetypes {#gnoll-archetypes}

The following archetypes are common among gnolls.

### Bouda {#bouda}

::: statblock
Abbrev: Witch
:::

These strange and often solitary witches have a strong connection to curses, the evil eye, and
hyenas.

#### Alignment {#alignment}

Because of the dark nature of her magic, a bouda must be of an evil alignment. If a character with
the bouda archetype ceases to be evil, she loses the ability to use all alternate class features
granted by this archetype (but still retains all other witch class features), though she's still
considered to be a bouda when taking further levels in the witch class. A bouda regains use of all
archetype alternate class features if she atones for her violations (see the
_[atonement](ref/spell/atonement)_ spell).

#### Fetish {#fetish}

A bouda keeps a small fetish: sometimes a carved idol, other times a necklace adorned with teeth or
bones. A bouda's spells come from the will of evil spirits residing in the fetish, and its ability
to hold spells functions in a manner identical to the way a witch's spells are granted by her
familiar. The bouda must commune with her fetish each day to prepare her spells and can only prepare
spells stored in the fetish.

At 3rd level, a bouda can use her fetish to deliver touch spells a number of times per day equal to
1/4 her witch level (minimum 1). When casting a touch spell, as a free action she can use this
ability. When she does, she can deliver her spell as a ranged touch spell within a range of 30 feet.
At 10th level, she can deliver these spells within a range of 60 feet. At 15th level and higher, she
can deliver these spells within a range of 90 feet.

This ability replaces the familiar class feature.

#### Bouda's Eye {#boudas-eye}

::: statblock
Ability Type: Supernatural
:::

A bouda's gaze can bestow ill fortune on her enemies. This hex can affect a creature within 30 feet
that the bouda can see. The target takes a –2 penalty on one of the following (bouda's choice): AC,
ability checks, attack rolls, saving throws, or skill checks. The hex lasts for a number of rounds
equal to 3 + the bouda's Intelligence modifier. A successful Will saving throw reduces the duration
of the hex to 1 round. Once per day when the bouda uses this hex, she can impose two different
penalties on the target instead of just one. If the bouda takes the evil eye hex, it increases the
number of different penalties she can impose on the hex's target by 1. At 8th level, the penalties
imposed by this hex increase to –4. This is a mind-affecting effect.

This hex must be taken as a bouda's 1st-level hex, and only a bouda can take this hex.

#### Hyena Shape {#hyena-shape}

::: statblock
Ability Type: Supernatural
:::

At 10th level, a bouda gains the ability to turn into a hyena or dire hyena and back again a number
of times per day equal to her Intelligence modifier. This ability functions as
_[beast shape II](ref/spell/beast-shape-2)_, except for the following. The effect lasts for 1 hour
per witch level, or until the bouda changes back. Changing form (to animal or back) is a standard
action that does not provoke attacks of opportunity. At 20th level, a bouda can change her form at
will. If a bouda dies while in hyena shape, she does not revert back to her true form.

The bouda does not lose the ability to speak while in animal form, and can communicate with hyenas
and dire hyenas as if under the effects of _[speak with animals](ref/spell/speak-with-animals)_ .
Furthermore, while in this form, the bouda gains the benefit of the Natural Spell feat, even if she
does not meet the prerequisites.

This ability replaces the major hex granted at 10th level.

### Pack Rager {#pack-rager}

::: statblock
Abbrev: Barbarian
:::

Barbarian rages can be a thing of savage beauty, exhibiting a lethal grace. While such uncontrolled
displays of carnage often disregard group tactics, there are those barbarians whose rages inspire
and spur on their allies during the ferocious dance of death.

#### Bonus Feat {#bonus-feat}

At 2nd level and every 4 levels thereafter, the pack rager can take a bonus teamwork feat. This
teamwork feat must also be a combat feat. This ability replaces the rage powers gained at 2nd, 6th,
10th, 14th, and 18th level.

#### Raging Tactician {#raging-tactician}

At 7th level, while a pack rager is raging, she grants a single teamwork feat she knows to all
allies within 30 feet who can see and hear her. She chooses the feat at the start of the rage, and
cannot change it during the rage. An ally who moves more than 30 feet away from the raging pack
rager loses access to the feat, but regains it again each time he moves back within 30 feet of the
raging pack rager. Allies do not need to meet the prerequisites of these teamwork feats.

At 13th level, the pack rager chooses two teamwork feats when she enters a rage, and grants her
allies the use of both of those feats when they are within 30 feet of her.

At 16th level, the pack rager grants these teamwork feats as long as her allies are within 60 feet
of her.

At 19th level, the pack rager chooses three teamwork feats when she enters a rage, and grants her
allies the use of all three feats when they are within 60 feet of her.

This ability replaces the [damage reduction](ref/rule/damage-reduction) class feature.

## Gnoll Feats {#gnoll-feats}

Gnolls have access to the following feats, some of which enhance the tactics of gnoll packs.

### Coordinated Reposition {#coordinated-reposition}

::: statblock
Abbrev: Teamwork
:::

You are skilled in coordinating combat positioning with your allies.

#### Prerequisite {#prerequisite}

::: paragraph statline
Step-Up.
:::

#### Benefit {#benefit}

::: paragraph statline
Whenever an ally with this feat who is threatening a creature you are threatening takes a 5-foot
step, you can move 5 feet as an immediate action. This movement does not provoke attacks of
opportunity.
:::

### Disarm Partner {#disarm-partner}

::: statblock
Abbrev: Combat, Teamwork
:::

When your ally fails to disarm an opponent within your reach, you can try to disarm that same foe.

#### Prerequisite {#prerequisite-2}

::: paragraph statline
Base attack bonus +1.
:::

#### Benefit {#benefit-2}

::: paragraph statline
When an ally with this feat fails a disarm combat maneuver check made on his turn against an
opponent within your melee reach, as an immediate action you can attempt a disarm combat maneuver
check against that foe.
:::

### Improved Disarm Partner {#improved-disarm-partner}

::: statblock
Abbrev: Combat, Teamwork
:::

You are ever the opportunist.

#### Prerequisites {#prerequisites}

::: paragraph statline
Disarm Partner, base attack bonus +5.
:::

#### Benefit {#benefit-3}

::: paragraph statline
When an ally with this feat fails a disarm combat maneuver check made on his turn against a foe
that's within your melee reach, you can make an attack of opportunity against that foe. If that
attack of opportunity hits the foe, you can also attempt a disarm combat maneuver check against that
opponent as part of that attack of opportunity.
:::

### Snapping Flank {#snapping-flank}

::: statblock
Abbrev: Combat, Teamwork
:::

You can make a swift bite attack against a flanked foe.

#### Prerequisites {#prerequisites-2}

::: paragraph statline
Base attack bonus +9, bite attack.
:::

#### Benefit {#benefit-4}

::: paragraph statline
Whenever you are flanking with an ally who also has this feat, as a swift action you can make a bite
attack against the opponent you and your ally are flanking.
:::

### Snapping Jaws {#snapping-jaws}

::: statblock
Abbrev: Combat
:::

When enemies get too close, your jaws tear flesh and bone.

#### Prerequisites {#prerequisites-3}

::: paragraph statline
Base attack bonus +1, gnoll.
:::

#### Benefits {#benefits}

::: paragraph statline
You can use your bite as a natural weapon. This is a primary attack that deals 1d6 points of damage.
:::

## Gnoll Equipment {#gnoll-equipment}

The following weapon is a favorite of flinds, but is sometimes used by other gnolls who master its
use.

::: entry-link
target = "ref/eq-weapon/flindbar"
title = "Flindbar"
:::

## Gnoll Magic Items {#gnoll-magic-items}

The following magic items are favored by gnolls and flinds.

::: entry-link
target = "ref/magic-wondrous/hunters-nose-ring"
title = "Hunter's Nose Ring"
:::

::: entry-link
target = "ref/magic-wondrous/hyena-shawl"
title = "Hyena Shawl"
:::

::: entry-link
target = "ref/magic-wondrous/pugwampi-braid"
title = "Pugwampi Braid"
:::
