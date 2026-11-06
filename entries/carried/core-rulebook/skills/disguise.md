+++
id = "ref/carried/core-rulebook/skills/disguise"
kind = "skill"
title = "Disguise"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Disguise", path = "core_rulebook/skill/disguise.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Cha
Trained Only: Yes
Armor Check Penalty: Yes
:::

_You are skilled at changing your appearance._

## Check {#check}

Your Disguise check result determines how good the disguise is, and it is opposed by others'
Perception check results. If you don't draw any attention to yourself, others do not get to make
Perception checks. If you come to the attention of people who are suspicious (such as a guard who is
watching commoners walking through a city gate), it can be assumed that such observers are taking 10
on their Perception checks.

You get only one Disguise check per use of the skill, even if several people make Perception checks
against it. The Disguise check is made secretly, so that you can't be sure how good the result is.

The effectiveness of your disguise depends on how much you're changing your appearance. Disguise can
be used to make yourself appear like a creature that is one size category larger or smaller than
your actual size. This does not change your actual size or reach, should you enter combat while
wearing such a disguise.

### Disguise {#disguise}

::: table
head = [
  [
    { text = "Disguise", header = true },
    { text = "Check Modifier", header = true },
  ],
]
body = [
  [
    { text = "Minor details only" },
    { text = "+5" },
  ],
  [
    { text = "Disguised as different gender^1^" },
    { text = "–2" },
  ],
  [
    { text = "Disguised as different race^1^" },
    { text = "–2" },
  ],
  [
    { text = "Disguised as different age category^1^" },
    { text = "–2^2^" },
  ],
  [
    { text = "Disguised as different size category^1^" },
    { text = "–10" },
  ],
]
foot = [
  [
    { text = "1 These modifiers are cumulative; use all that apply.", colspan = 2 },
  ],
  [
    { text = "2 Per step of difference between your actual age category and your disguised age category. The steps are: young (younger than adulthood), adulthood, middle age, old, and venerable.", colspan = 2 },
  ],
]
:::

### Familiarity {#familiarity}

|Familiarity|Viewer's Perception Check Bonus|
| --- | --- |
|Recognizes on sight|+4|
|Friends or associates|+6|
|Close friends|+8|
|Intimate|+10|

If you are impersonating a particular individual, those who know what that person looks like get a
bonus on their Perception checks according to the table below. Furthermore, they are automatically
considered to be suspicious of you, so opposed checks are always called for.

An individual makes a Perception check to see through your disguise immediately upon meeting you and
again every hour thereafter. If you casually meet a large number of different creatures, each for a
short time, check once per day or hour, using an average Perception modifier for the group.

## Action {#action}

Creating a disguise requires 1d3 × 10 minutes of work. Using magic (such as the
_[disguise self](ref/spell/disguise-self)_ spell) reduces this action to the time required to cast
the spell or trigger the effect.

## Try Again {#try-again}

Yes. You may try to redo a failed disguise, but once others know that a disguise was attempted,
they'll be more suspicious.

## Special {#special}

Magic that alters your form, such as _alter self, disguise self, polymorph_, or
_[shapechange](ref/spell/shapechange)_, grants you a +10 bonus on Disguise checks (see the
individual spell descriptions). Divination magic that allows people to see through illusions (such
as _[true seeing](ref/spell/true-seeing)_) does not penetrate a mundane disguise, but it can negate
the magical component of a magically enhanced one.

You must make a Disguise check when you cast a _[simulacrum](ref/spell/simulacrum)_ spell to
determine how good the likeness is.

If you have the Deceitful feat, you gain a bonus on Disguise checks (see Feats).
