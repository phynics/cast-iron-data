+++
id = "ref/rule/psychometabolic"
kind = "rule"
title = "Psychometabolic"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychometabolic", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Psychic Anthology pg. 31-32\
Strange powers exist on Golarion and beyond. Those who survive a brush with cosmic phenomena, occult
mysteries, or horrors from beyond the veil occasionally find psychic abilities awakening in their
minds. Although potent, such power corrupts the body, subconscious mind, and emotions - often with
disastrous results.

The following corruption can be contracted by those who delve into occult lore better left
forgotten.

### Catalyst

A psychometabolic corruption is contracted as a result of experiencing extreme psychic trauma. When
you contract this corruption, you gain a pool of psychometabolic power with a number of points equal
to 1 + your manifestation level. These points are used to fuel the gifts of your manifestations. The
pool replenishes at the start of each week or whenever you gain a new manifestation level.

### Progression

The corruption is tied to your exposure to psychic power: the more you experience, the faster your
progression advances. Whenever the total number of points in your psychometabolic pool reaches 0,
you become afflicted with a random [madness](ref/rule/madness) from the following list within the
next 24 hours: [delirium](ref/madness/delirium), [delusion](ref/madness/delusion),
[hallucination](ref/madness/hallucination), [mania](ref/madness/mania),
[night terrors](ref/madness/night-terrors), [paranoia](ref/madness/paranoid), or
[phobia](ref/madness/phobia). This affliction lasts 8 hours, after which you must succeed at a Will
save (DC = 15 + your manifestation level) or become twisted by your powers. You must also attempt
this save when you are reduced to 10% or fewer of your maximum hit points by a psychic effect or
when you fail a save against psychic effect by 5 or more. If you are unconscious or under the
effects of [calm emotions](ref/spell/calm-emotions) for at least 6 of the hours that you spend
afflicted with the madness, your corruption doesn't progress. However, the DC of checks to prevent
your corruption from progressing increases by 2. These increases stack each time this occurs, and
they last until your corruption reaches the next corruption stage.

**Corruption Stage 1**

**Details:** The first time you fail a Will save (as described above), your powers twist your mind.
You are constantly afflicted with one madness of the GM's choice from among those listed above. This
madness can't be cured or removed while you have this corruption.

**Corruption Stage 2**

**Details:** The second time you fail a Will save (as described above), your powers erode your
values and morals and replace them with megalomaniacal thoughts. You gain the
[moral insanity](ref/madness/moral-insanity) madness. This madness can't be cured or removed while
you have this corruption.

**Corruption Stage 3**

**Details:** The third time you fail a Will save (as described above), your body is twisted into a
writhing mass of flesh that imprisons your mind. You become a
[hungry flesh](ref/monster/hungry-flesh) under the GM's control, retaining all class levels and
abilities that do not rely upon your original form.

### Removing the Corruption

To remove the psychometabolic corruption, a psychic spellcaster whose caster level is at least
double your manifestation level must eliminate your memories of gaining the corruption and your
corruption stage advancing, such as by [modify memory](ref/spell/modify-memory), and then must cast
[psychic surgery](ref/spell/psychic-surgery) on you.

### Manifestations

The following are manifestations of the psychometabolic corruption.

**Ameliorate Damage**

**Flavor:** You can repair damage to your body.

**Gift:** You can use any of the following spells as a
[spell-like ability](ref/umr/spell-like-abilities) by spending a number of points from your
psychometabolic pool equal to the spell's cleric spell level:
[lesser restoration](ref/spell/restoration-lesser), [regenerate](ref/spell/regenerate),
[restoration](ref/spell/restoration), or any cure spell (a spell with the word &quot&cure&quot in
its name). You can target only yourself with these spells, and you can use this manifestation to
cast only a spell whose spell level on the cleric spell list is equal to or less than your
manifestation level. You are always treated as a living creature for the purpose of these spells'
effects.

**Stain:** Your body becomes twisted and alien. When an effect other than this manifestation's
[spell-like abilities](ref/umr/spell-like-abilities) heals your ability damage or hit point damage,
roll the amount of healing twice and use the lower result.

**Defy Gravity**

**Flavor:** You can lift creatures and objects with your mind.

**Prereq:** Manifestation level 2nd

**Gift:** By spending 2 points of psychometabolic power, you can use [levitate](ref/spell/levitate)
as a [spell-like ability](ref/umr/spell-like-abilities).

At manifestation level 4th, you can spend 3 points of psychometabolic power to use
[hostile levitation](ref/spell/hostile-levitation).

**Stain:** Your body weakens. You take a -4 penalty on all Strength- and Dexterity-based checks and
skill checks.

**Endless Echoes**

**Flavor:** You hear voices in your head.

**Gift:** You gain telepathy with a range of 10 feet + 10 feet per manifestation level that you
have. You can use [detect thoughts](ref/spell/detect-thoughts) as a
[spell-like ability](ref/umr/spell-like-abilities) by spending 1 point of psychometabolic power.

**Stain:** Garbled thoughts ring in your ears. You take a -2 penalty on all
[concentration](ref/rule/concentration) checks.

At manifestation level 4th, the penalty changes to -4.

**Eschew Gravity**

**Flavor:** You lift yourself with your mind.

**Prereq:** Defy gravity, manifestation level 5th

**Gift:** By spending 3 points of psychometabolic power as a **swift action**, you can use
[fly](ref/spell/fly) as a [spell-like ability](ref/umr/spell-like-abilities).

**Stain:** Your limbs slow as they weaken. Your speed for all nonmagical movement types is reduced
by 10 feet.

**Mind Blast**

**Flavor:** You can rend your foes' minds with psychic power.

**Prereq:** Endless echoes, psychometabolic blast

**Gift:** When you use the telekinetic blast gained from the _psychometabolic blast_ manifestation,
you can spend 2 points of psychometabolic power to use the telekinetic force to wreck the mind of
each creature targeted.

Instead of you rolling to hit targets with your blast, each target can attempt a Will save (DC =
10 + half your manifestation level + your Constitution modifier) to try to negate the damage and any
infusions or metakinesis abilities applied to it. When using this ability, your telekinetic blast is
a mind-affecting effect.

**Stain:** Using your powers causes blood to ooze from your nose and eyes. Whenever you spend a
psychometabolic point, you take nonlethal damage equal to your manifestation level per point spent.

**Psychometabolic Blast**

**Flavor:** You can attack your enemies with your mind.

**Gift:** You gain the [kineticist's](ref/class/kineticist) kinetic blast class feature, as well as
the [telekinetic blast](ref/kinetic/telekinetic-blast) wild talent. Use your manifestation level as
your effective kineticist level to determine the effects of these abilities.

If you have the _elemental focus (aether)_ or _expanded element (aether)_ class ability, you instead
gain a bonus on damage rolls with your telekinetic blast equal to half your manifestation level
(minimum +1).

**Stain:** Your cranium swells massively. You take a -2 penalty on all Wisdom- and Charisma-based
checks and skill checks.

**Psychometabolic Jaunt**

**Flavor:** You can travel with a thought.

**Prereq:** Defy gravity, manifestation level 6th

**Gift:** You can spend 4 psychometabolic points to use [dimension door](ref/spell/dimension-door)
as a [spell-like ability](ref/umr/spell-like-abilities).

At manifestation level 9th, you can spend 6 psychometabolic points to instead use
[teleport](ref/spell/teleport) as a [spell-like ability](ref/umr/spell-like-abilities).

**Stain:** Your body deteriorates. You take a -2 penalty to your Constitution score.

**Psychometabolic Shield**

**Flavor:** You can project a shield with your mind.

**Prereq:** Manifestation level 2nd

**Gift:** You gain the [force ward](ref/kinetic/force-ward) defense wild talent. Use your kineticist
level or your manifestation level (whichever is higher) as your effective kineticist level to
determine the effects of these abilities. You can spend 1 point of psychometabolic power to enhance
your _force ward_ as if you had accepted a point of burn. If you already have the _force ward_
defense wild talent, this gift has no effect.

**Stain:** You reflexes become sluggish. You take a -1 penalty on your AC and on Reflex saving
throws.
