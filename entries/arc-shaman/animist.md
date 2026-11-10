+++
id = "ref/arc-shaman/animist"
kind = "archetype"
title = "Animist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animist", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "advanced-class-guide"
page = "110"

[fields]
kind = "archetype"
replaces = ["Spirit magic spells gained from the shaman's spirit", "2nd-level hex", "Hex gained at 8th level", "Hex gained at 10th level", "Hex gained at 12th level", "Hex gained at 18th level", "Manifestation"]
replaces_features = ["manifestation"]
+++

Even among mystical practitioners, the animist has a strange perspective and even stranger magic.
The animist perceives that all things have a spirit, including objects, constructs, illnesses,
buildings, and the environment.

**Animist Spirit Magic**

**Info:** The animist adds the following spells to the list of spells he can cast using _spirit
magic_ at the given spell levels:

**Replaces:** Spirit magic spells gained from the shaman's spirit

**Spells:** Speak with animals

**Spells:** Skinsend

**Spells:** Speak with plants

**Spells:** Malfunction

**Spells:** Dream

**Spells:** Stone tell

**Spells:** Control construct

**Spells:** Trap the soul

**Spells:** Soul bind

**Wrangle Condition**

**Action:** Ability

**At 13th Level:** He can remove severe conditions without rolling.

**At 17th Level:** He can dispatch dire conditions automatically.

**At 5th Level:** The animist can use this ability to exorcise minor conditions without needing to
attempt a Diplomacy check.

**At 9th Level:** He can dispatch major conditions without a roll.

**Gained:** At 2nd Level

**Replaces:** 2nd-level hex

**Special:** Even if he doesn't need to roll, removing a condition still requires one use of this
ability per condition.

The animist interacts directly with unwholesome spirits of the ills that trouble him or his people.
To the animist, negative conditions manifest as anthropomorphic spirits or are caused by such
spirits (visited upon the creature by bad magic). Either way, the animist can attempt to persuade
the spirit to leave its victim alone, thus performing a miraculous healing. As the animist grows in
power, he can simply inform these spirits that they are unwelcome and command them to depart.

The animist can attempt a Diplomacy check to persuade the condition's spirit to leave. Conditions
the animist can affect are ranked from minor to dire, with each category having an accompanying
Diplomacy DC (see below). The animist cannot take 10 or 20 on the check or receive aid from any
creature except another shaman. Failure by 5 or less means the condition spirit is willing to leave
the target and transfer to the animist for the rest of the duration or until cured; this happens
only if the animist is willing. Failure by 10 or more means that not only is the target inflicted
with the condition, but the animist is as well (whether or not he is willing) for the remaining
duration or until cured.

- **Minor Conditions (DC 15):** Fatigued, shaken, and sickened.
- **Major Conditions (DC 20):** Dazed and staggered.
- **Severe Conditions (DC 25):** Exhausted, frightened, and nauseated.
- **Dire Conditions (DC 30):** Blinded, deafened, paralyzed, and stunned.

The animist can use this ability a number of times per day equal to half his shaman level + his
Wisdom modifier. Using this ability is a **standard action** that requires no contact or shared
language with the target, but it relies on audible components and the target must be within 30 feet.
If a target is afflicted with multiple conditions, the animist targets one condition at a time (of
her choosing). The animist cannot use this ability on himself.

**Exorcism (Su)**

**Fullround:** The animist can attempt to end effects that control a creature or object, such as
[magic jar](ref/spell/magic-jar), [possess object](ref/spell/possess-object),
[dominate person](ref/spell/dominate-person), and [dominate monster](ref/spell/dominate-monster), or
possessing entities such as [ghosts](ref/template/ghost). This requires the animist to touch the
target. The possessing or dominating creature must attempt a Will save with a DC equal to 10 + 1/2
the shaman level + her Wisdom modifier. Failure means that the controlling effect ends or the entity
is immediately cast out of the target, as appropriate.

**Gained:** At 8th Level

**Replaces:** Hex gained at 8th level

**Special:** If the possessing entity is exorcised, it cannot attempt to dominate or possess that
target again for 24 hours. The animist can exorcise the same entity out of different targets, but
once the entity successfully saves against the animist's exorcism, it cannot be affected by this
ability again for 24 hours.

**Dominate Spirit (Sp)**

**Ability:** The animist can attempt to possess creatures or objects as
_[magic jar](ref/spell/magic-jar)_ or _[possess object](ref/spell/possess-object)._ When the animist
is attempting to possess the creature, his familiar acts as the jar and must be within 10 feet when
the animist attempts to possess a creature. The animist's soul can perceive his surroundings through
the familiar's senses, clearly evaluate potential targets for possession, and communicate with his
familiar telepathically. The familiar retains its autonomy while acting as the jar, and is not
harmed by being used as a vessel for the animist's soul.

**Gained:** At 10th Level

**Replaces:** Hex gained at 10th level

**Usage:** 1 time/day + 1 per 4 shaman levels beyond 10th

**Contact with the Spirit World (Su)**

**Ability:** The shaman can interact with incorporeal entities as if his unarmed strikes and melee
weapons had the [ghost touch](ref/magic-enh/ghost-touch-weapon) weapon special ability. While using
this ability, he can also see nearby ethereal entities and likewise strike at them as if they were
incorporeal.

**Gained:** At 12th Level

**Replaces:** Hex gained at 12th level

**Usage:** 1 time/day per shaman level

**Etherealness (Sp)**

**Ability:** The animist can cast [etherealness](ref/spell/etherealness) once per day as a
[spell-like ability](ref/umr/spell-like-abilities).

**Gained:** At 18th Level

**Replaces:** Hex gained at 18th level

**Spirit Shaman (Sp)**

**Ability:** The animist can use [ethereal jaunt](ref/spell/ethereal-jaunt) as at will as a
[spell-like ability](ref/umr/spell-like-abilities), and cast
[astral projection](ref/spell/astral-projection) once per day as a spell-like ability.

**Gained:** At 20th Level

**Replaces:** Manifestation
