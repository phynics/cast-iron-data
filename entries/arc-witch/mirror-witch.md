+++
id = "ref/arc-witch/mirror-witch"
kind = "archetype"
title = "Mirror Witch"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirror_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "villain-codex"
page = "152"

[fields]
kind = "archetype"
replaces = ["Familiar"]
+++

After being locked away and denied her former familiar, the queen learned to talk to her patron via
mirror magic.

**Patron Mirror (Su)**

**Action:** Ability

**Replaces:** Familiar

A mirror witch creates a direct link to the power of her patron. She chooses a patron as normal, but
instead of gaining a familiar that serves as the conduit to her patron, she uses a
[mirror](ref/eq-misc/mirror) (worth at least 10 gp) to speak to a fragment of her patron's power.
This fragment teaches her magic and acts as a counselor.

The mirror is essentially an immobile familiar. The mirror witch can activate it with a minute-long
ritual that calls the patron fragment to manifest itself through the mirror. While this connection
is open, she can prepare spells, add new spells to the mirror, and use the mirror's special
abilities. In place of the boost granted by an ordinary familiar, the mirror grants the mirror witch
a +2 bonus on Diplomacy checks regardless of whether the mirror is nearby. The mirror can't be used
for abilities that require the presence of a familiar, such as the [blight](ref/hex/blight) hex.

If the patron mirror is destroyed, the mirror witch can replace it 1 day later through a special
ritual, attuning a new mirror to a different fragment of her patron. The mirror witch must purchase
or procure a new, suitable mirror and spend 500 gp per witch level she has. The ritual takes 8 hours
to complete, and when it is finished, the mirror witch establishes a connection with a new fragment
of her patron and loses access to spells stored in the previous mirror, as normal for a lost witch's
familiar.

As the mirror witch progresses in level, the mirror's defenses increase, and the connection between
it and the mirror witch becomes stronger, allowing the patron to manifest more of its personality.
Instead of using the normal familiar abilities table, use the table below to determine the strength
of a mirror witch's patron mirror.

|Witch Class Level|Hardness|Hit Points|Int|Special|
| --- | --- | --- | --- | --- |
|1st-2nd|5|2|12 (+1)|Cryptic omens, seek guidence|
|3rd-4th|10|5|13 (+1)|Greater omens|
|5th-6th|15|5|14 (+2)|Specialized knowledge|
|7th-8th|20|5|15 (+2)|Clairvoyance/clairaudience|
|9th-10th|20|5|16 (+3)|-|
|11th-12th|25|10|17 (+3)|Scrying|
|13th-14th|25|10|18 (+4)|Mirror casting|
|15th-16th|25|10|19 (+4)|-|
|17th-18th|30|10|20 (+5)|-|
|19th-20th|30|15|21 (+5)|-|

**Hardness**

**Passive:** As the connection between the witch and her patron mirror becomes more powerful, so
does the [hardness](ref/umr/hardness) of the mirror, making it more difficult to damage. This value
is the hardness of the patron mirror.

**Hit Points**

**Info:** The base hit points of a mirror witch's patron mirror are based on what kind of mirror she
chooses. A steel mirror has 4 hit points and a glass mirror has 1 hit point. The patron mirror gains
the listed hit points in addition to the mirror's normal hit points, and the hit points increase as
the link between the witch and her patron mirror strengthens.

**Intelligence**

**Passive:** A patron is a powerful and unknowable entity, able to see great distances and offer
sage council, but the power of the fragment it manifests through a patron mirror is proportional to
the link the fragment has with the mirror witch. This column indicates the effective Intelligence
score of the patron mirror as the witch progresses in level. The patron mirror is not a creature,
and nothing can increase its Intelligence above the listed value.

**Cryptic Omens (Ex)**

**Ability:** Once per day, after the witch receives this advice, she can gain one of the following
benefits without taking an action: gain a +2 insight bonus on a saving throw she is about to
attempt; gain a +2 insight bonus on a Bluff, Diplomacy, or Sense Motive check she is about to
attempt; or instead of rolling initiative, treat her initiative as if she rolled a 12 on the die.
She can't use this last option if she can't act during a surprise round. She doesn't choose which
benefit she gains while consulting the mirror; instead, she does so when she would be about to roll
a saving throw, initiative check, or appropriate skill check.

**Info:** Each day, when a mirror witch consults with her patron mirror, the patron fragment can
speak a few words of cryptic advice about the witch's future. While the words are often obscure when
the fragment utters them, they nearly always make sense to the witch at just the right moment aid
her in dealing with the threats of the day.

**Gained:** At 1st Level

**Seek Guidance (Ex)**

**Ability:** Whenever the mirror witch consults with her patron fragment, she can spend 10 minutes
instead of the usual 1 minute and attempt a single Knowledge check. She gains a +2 insight bonus on
any Knowledge check she attempts during such a consultation.

**Gained:** At 1st Level

**Greater Omens (Ex)**

**Ability:** After consulting with her patron for 1 minute, she can expend a use of _cryptic omens_
to gain the effects of [augury](ref/spell/augury) instead of one of the usual three benefits.

**Gained:** At 3rd Level

**Passive:** The number of times per day that the mirror witch can use _cryptic omens_ increases by
an amount equal to the Intelligence modifier of the patron mirror.

**Specialized Knowledge (Ex)**

**Choice:** The mirror witch chooses a number of Knowledge skills equal to the patron mirror's
Intelligence modifier (and chooses more as the mirror's Intelligence modifier increases).

**Gained:** At 5th Level

**Passive:** When the witch consults her patron fragment with seek guidance for a Knowledge skill of
one of the chosen types, the insight bonus increases by an amount equal to the mirror's Intelligence
modifier. For example, at 5th and 6th levels, she gains a +4 insight bonus on a chosen Knowledge
skill instead of the normal +2.

**Clairvoyance/Clairaudience (Sp)**

**Ability:** By consulting her patron fragment for 10 minutes, the mirror witch can expend a single
use of _cryptic omens_ to cast [clairvoyance/clairaudience](ref/spell/clairaudience-clairvoyance) as
a [spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her witch level.

**Gained:** At 7th Level

**Scrying (Sp)**

**Ability:** By consulting with her patron fragment for 1 hour, the mirror witch can expend a single
use of _cryptic omens_ to use [scrying](ref/spell/scrying) as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to her witch level,
using the patron mirror as the focus.

**Gained:** At 11th Level

**Mirror Casting (Su)**

**Ability:** When using the mirror's _[scrying](ref/spell/scrying)_ ability,
[detect chaos, detect evil, detect good, detect law](ref/spell/detect-evil),
[detect magic](ref/spell/detect-magic), [message](ref/spell/message),
[read magic](ref/spell/read-magic), and [tongues](ref/spell/tongues) all function reliably through
the sensor.

**Ability2:** Also, if the mirror witch is at least 15th level, there is a 5% chance each of the
following spells operates successfully through the sensor: cause fear,
[charm person](ref/spell/charm-person), [command](ref/spell/command),
[crushing despair](ref/spell/crushing-despair), [deep slumber](ref/spell/deep-slumber),
[enthrall](ref/spell/enthrall), [fear](ref/spell/fear), [hold person](ref/spell/hold-person),
[moonstruck](ref/spell/moonstruck), [seek thoughts](ref/spell/seek-thoughts), and
[sleep](ref/spell/sleep); a creature that succeeds at its saving throw against one of these linked
spells is forever immune to that particular mirror witch's attempts to cast that spell on that
creature through her mirror.

**Gained:** At 13th Level
