+++
id = "ref/implement/performers-accoutrements"
kind = "class_option"
title = "Performer's Accoutrements (Panoply)"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "performers_accoutrements", path = "json/class_ability_implements.json" },
]

[fields]
kind = "class_option"
group = "occultist-implement"
+++

## Performer's Accoutrements

**Sources:** Psychic Anthology pg 27\
This panoply is associated with those who deceive as well as those who entertain.

**Implements**

**Details:** Mask ([illusion](ref/implement/illusion)) and musical instrument
([enchantment](ref/implement/enchantment)).

### Resonant Power

**Actor's Skill (Su)**

**Passive:** The panoply grants a bonus on [Bluff](ref/skill/bluff), [Disguise](ref/skill/disguise),
and [Perform](ref/skill/perform-any) checks equal to [one-third](ref/misc/fractions-and-rounding) of
the total amount of points of mental focus invested in all of the associated implements, to a
maximum bonus equal to half the occultist's level. The panoply also grants an equal bonus on saving
throws against divination effects.

### Base Focus Power

**False Persona (Su)**

**Ability:** By spending 1 minute in meditation and expending 2 points of mental focus, you can
create a psychic mask that obscures your identity. When you create this _false persona,_ you choose
the nature of the persona's alignment and magical auras, and can create a simple background of up to
four basic facts about the persona.

All divination spells that reveal information about you instead reveal information based on the
_false persona's_ background and aura information. Additionally, attempts to scry or magically
locate you work only if the creature making such attempts knows that you and your current _false
persona_ are the same individual. Otherwise, the spell has no effect, revealing nothing but
darkness, as if you did not exist.

This effect lasts up to 24 hours or until you next refresh your mental focus (whichever occurs
first), though you can dismiss this _false persona_ at any time before then as a **full-round
action**.

**Special:** This effect fools only magical attempts to discern your identity or background, and has
no effect on mundane means of gathering information about you.

### Focus Powers

**False Confidence (Sp)**

**Move:** You can shatter the feeling of confidence, leaving the target feeling hopeless and
distraught. If you do, the target can immediately attempt a Will save to negate the effect, with a
cumulative -1 penalty for every 2 minutes the creature benefited from the morale bonus. If the
target fails this save, it takes a -2 penalty on ability checks, attack rolls, saving throws, and
skill checks for the remainder of the effect's duration. If the creature then fails an ability
check, attack roll, saving throw, or skill check by 10 or more while subject to this penalty, the
penalty changes to -4.

**Standard:** By expending 1 point of mental focus, you can instill incredible, boundless confidence
in a single living creature with an Intelligence score of 3 or higher within 60 feet, granting that
creature a +2 morale bonus on ability checks, attack rolls, saving throws, and skill checks for 10
minutes.

**Hypnotic Gaze (Sp)**

**Standard:** By expending 1 point of mental focus, you can hypnotize a single creature within 60
feet that can see you. The target must succeed at a Will save or become
[fascinated](ref/misc/fascinated) for as long as you maintain the effect (a move action), plus 1
additional round. Fascinated creatures take a -1 penalty on Will saving throws. For every 3 rounds
that you maintain the effect, this penalty increases by 1 to a maximum penalty of -4. Anything that
ends the fascination effect also ends the penalty.

A creature that succeeds at its saving throw to resist this effect is immune to that occultist's
_hypnotic gaze_ for 24 hours.

**Puppet Master (Sp)**

**Standard:** By expending 2 points of mental focus, you can implant a hypnotic suggestion in a
creature. This functions as per [suggestion](ref/spell/suggestion) (using your occultist level as
the caster level), except that the saving throw DC is equal to 10 +
[half](ref/misc/fractions-and-rounding) your occultist level + your Intelligence modifier, and if
the target fails its saving throw, you can choose to have it forget everything that occurs while it
is under the spell's effects, as well as any recollection of you using this ability on it. Memories
forgotten in this way can be recovered with restoration or spells or effects that can restore lost
memories (such as [modify memory](ref/spell/modify-memory)).
