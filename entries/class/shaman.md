+++
id = "ref/class/shaman"
kind = "class"
title = "Shaman"
aon = "ClassDisplay.aspx?ItemName=Shaman"
source_ids = ["advanced-class-guide", "chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shaman", path = "json/classes6.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "35"
[[sources]]
publication = "chronicle-of-legends"
page = "28, 30"

[fields]
kind = "class"
class_type = "hybrid"
hit_die = "d8"
skill_ranks = "4 + Int modifier"
features = [
  { anchor = "spells" },
  { anchor = "orisons", level = 1 },
  { anchor = "spirit", level = 1 },
  { anchor = "spirit-animal", level = 1 },
  { anchor = "spirit-magic", level = 1 },
  { anchor = "hex", level = 2 },
  { anchor = "wandering-spirit", level = 4 },
  { anchor = "wandering-hex", level = 6 },
  { anchor = "manifestation", level = 20 },
]
+++

While some heroes speak to gods or consort with otherworldly muses, shamans commune with the spirits
of the world and the energies that exist in every living thing. These divine adventurers draw upon
their power to shape the world and expand the influence of their spiritual patrons. Shamans have
strong ties to natural spirits. They form powerful bonds with particular spirits, and as their power
grows they learn to call upon other spirits in times of need.

**Role:** Shamans make for potent divine spellcasters, capable of using divine spells and the power
of their spirits to aid their allies and destroy their foes. While they aren't the healers that
clerics are, they can still fill that role when needed.

**Alignment:** Any

**Hit Die:** d8

**Parent Class(es):** [Oracle](ref/class/oracle) and [witch](ref/class/witch).

**Starting Wealth:** 3d6 × 10 gp (average 105 gp)

**Skill Points per Level:** 4 + Int modifier

**Class Skills (Dex):** Fly, Ride

**Class Skills (Int):** Craft (any), Knowledge (nature), Knowledge (planes), Knowledge (religion),
Spellcraft

**Class Skills (Wis):** Heal, Profession (any), Survival

**Class Skills (Cha):** Diplomacy, Handle Animal

### Class Features and Spells Per Day

|Level|Base Attack Bonus|Fort Save|Ref Save|Will Save|Special|0|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1st|+0|+0|+0|+2|Orisons, spirit, spirit animal, spirit magic|3|1|-|-|-|-|-|-|-|-|
|2nd|+1|+0|+0|+3|Hex|4|2|-|-|-|-|-|-|-|-|
|3rd|+2|+1|+1|+3|-|4|2|1|-|-|-|-|-|-|-|
|4th|+3|+1|+1|+4|Hex, wandering spirit|4|3|2|-|-|-|-|-|-|-|
|5th|+3|+1|+1|+4|-|4|3|2|1|-|-|-|-|-|-|
|6th|+4|+2|+2|+5|Wandering hex|4|3|3|2|-|-|-|-|-|-|
|7th|+5|+2|+2|+5|-|4|4|3|2|1|-|-|-|-|-|
|8th|+6/+1|+2|+2|+6|Hex, spirit (greater)|4|4|3|3|2|-|-|-|-|-|
|9th|+6/+1|+3|+3|+6|-|4|4|4|3|2|1|-|-|-|-|
|10th|+7/+2|+3|+3|+7|Hex|4|4|4|3|3|2|-|-|-|-|
|11th|+8/+3|+3|+3|+7|-|4|4|4|4|3|2|1|-|-|-|
|12th|+9/+4|+4|+4|+8|Hex, wandering spirit (greater)|4|4|4|4|3|3|2|-|-|-|
|13th|+9/+4|+4|+4|+8|-|4|4|4|4|4|3|2|1|-|-|
|14th|+10/+5|+4|+4|+9|Wandering hex (2 hexes)|4|4|4|4|4|3|3|2|-|-|
|15th|+11/+6/+1|+5|+5|+9|-|4|4|4|4|4|4|3|2|1|-|
|16th|+12/+7/+2|+5|+5|+10|Hex, spirit (true)|4|4|4|4|4|4|3|3|2|-|
|17th|+12/+7/+2|+5|+5|+10|-|4|4|4|4|4|4|4|3|2|1|
|18th|+13/+8/+3|+6|+6|+11|Hex|4|4|4|4|4|4|4|3|3|2|
|19th|+14/+9/+4|+6|+6|+11|-|4|4|4|4|4|4|4|4|3|3|
|20th|+15/+10/+5|+6|+6|+12|Hex, manifestation, wandering spirit (true)|4|4|4|4|4|4|4|4|4|4|

### Class Features {#class-features}

The following are the class features of the shaman.

#### Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

A shaman is proficient with all simple weapons, and with light and medium armor.

#### Spells {#spells}

A shaman casts divine spells drawn from the shaman spell list (see page 48). A shaman must choose
and prepare her spells in advance.

To prepare or cast a spell, a shaman must have a Wisdom score equal to at least 10 + the spell's
level. The saving throw DC against a shaman's spell is 10 + the spell's level + the shaman's Wisdom
modifier.

Like other spellcasters, a shaman can cast only a certain number of spells of each spell level per
day. Her base daily spell allotment is given on Table 1–9. In addition, she receives bonus spells
per day if she has a high Wisdom score (see Table 1–3 in the _Pathfinder RPG Core Rulebook_).

Shamans commune with their spirit animals to prepare their spells. Each shaman must choose a time
when she must spend 1 hour each day in quiet contemplation with her spirit animal to regain her
daily allotment of spells. A shaman can prepare and cast any spell on the shaman spell list,
provided that she can cast spells of that level, but she must choose which spells to prepare during
her daily communion.

#### Orisons {#orisons}

Shamans can prepare a number of orisons, or 0-level spells, each day as noted on Table 1–9. These
spells are cast like any other spell, but they are not expended when cast and may be used again.

#### Spirit (Su) {#spirit}

A shaman forms a mystical bond with the spirits of the world. She forms a lasting bond with a single
[spirit](ref/ability/shaman-spirits) (see Spirits on page 37), which grants a number of abilities
and defines many of her other class features.

At 1st level, a shaman gains the spirit ability granted by her chosen spirit. She adds the spells
granted by that spirit to the list of spells that she can cast using spirit magic. She also adds the
hexes possessed by that spirit to the list of hexes that she can use with the hex and wandering hex
class features.

At 8th level, the shaman gains the abilities listed in the greater version of her selected spirit.
At 16th level, the shaman gains the abilities listed for the true version of her selected spirit.

If the shaman takes levels in another class that grants a mystery (such as the oracle), the spirit
and mystery must match, even if that means one of them must change. Subject to GM discretion, the
shaman can change her former mystery or spirit to make them conform.

#### Spirit Animal (Ex) {#spirit-animal}

At 1st level, a shaman forms a close bond with a spirit animal tied to her chosen spirit. This
animal is her conduit to the spirit world, guiding her along the path to enlightenment. The animal
also aids a shaman by granting her a special ability. See the Spirit Animal section on page 47.

A shaman must commune with her spirit animal each day to prepare her spells. While the spirit animal
does not store the spells like a witch's [familiar](ref/sidekick/familiar) does, the spirit animal
serves as her conduit to divine power. If a shaman's spirit animal is slain, she cannot prepare new
spells or use her spirit magic class feature until the spirit animal is replaced.

#### Spirit Magic {#spirit-magic}

A shaman can spontaneously cast a limited number of spells per day beyond those she prepared ahead
of time. She has one spell slot per day of each shaman spell level she can cast, not including
orisons. She can choose these spells from the list of spells granted by her spirits (see the spirit
class feature and the wandering spirit class feature) at the time she casts them. She can enhance
these spells using any metamagic feat that she knows, using up a higher-level spell slot as required
by the feat and increasing the time to cast the spell (see Spontaneous Casting and Metamagic Feats
on page 113 of the _Core Rulebook_).

#### Hex {#hex}

A shaman learns a number of magical tricks, called hexes, which grant her powers or weaken foes. At
2nd level, a shaman learns one hex. At 4th, 8th, 10th, 12th, 16th, 18th, and 20th level, the shaman
learns new hexes. A shaman can select from any of the following hexes or from any of the hexes
listed in the description of her chosen spirit. A shaman cannot select a hex more than once unless
noted otherwise.

Using a hex is a standard action that doesn't provoke an attack of opportunity unless otherwise
noted. The saving throw DC to resist a hex is equal to 10 + 1/2 the shaman's level + the shaman's
Wisdom modifier.

- [Chant (Ex)](ref/shamanhex/chant)
- [Charm (Su)](ref/shamanhex/charm)
- [Evil Eye (Su)](ref/shamanhex/evil-eye)
- [Fetish (Ex)](ref/shamanhex/fetish)
- [Fortune (Su)](ref/shamanhex/fortune)
- [Fury (Su)](ref/shamanhex/fury)
- [Healing (Su)](ref/shamanhex/healing)
- [Misfortune (Su)](ref/shamanhex/misfortune)
- [Secret (Ex)](ref/shamanhex/secret)
- [Shapeshift (Su)](ref/shamanhex/shapeshift)
- [Tongues (Su)](ref/shamanhex/tongues)
- [Ward (Su)](ref/shamanhex/ward)
- [Witch Hex](ref/shamanhex/witch-hex)

#### Wandering Spirit (Su) {#wandering-spirit}

At 4th level, a shaman can form a temporary bond with a spirit other than the one selected using her
spirit class feature. She must make this selection each day when preparing her spells. While this
feature is active, she gains the spirit ability granted by the spirit. She also adds the spells
granted by that spirit to her list of spells that she can cast using spirit magic. She does not add
the hexes from her wandering spirit to her list of hexes that she can choose from with the hex class
feature. At 12th level, she gains the abilities listed in the greater version of her wandering
spirit. At 20th level, she gains the ability listed in the true version of her wandering spirit.

#### Wandering Hex {#wandering-hex}

At 6th level, a shaman can temporarily gain the use of one of the hexes possessed by either one of
her spirits. She must make this selection each day when she prepares her spells. For the purposes of
this ability, she can select any hex possessed by her spirit or wandering spirit. If she selects it
from her wandering spirit, she loses the hex immediately if she bonds with another spirit, although
she can then select a different hex to gain using this ability, from either her spirit or her new
wandering spirit. At 14th level, a shaman can select two wandering hexes each day instead of one.
This ability otherwise functions as the hex class feature.

#### Manifestation (Su) {#manifestation}

Upon reaching 20th level, a shaman undergoes a transformation as she manifests as a pinnacle of her
main spirit. The nature of this manifestation depends on the shaman's spirit, and is described in
its entry.

### Spirit Animal {#spirit-animal-rules}

By communing with the incredible powers of her spirit, the shaman forges a cherished bond with one
specific servant of that spirit—known as a spirit animal. A spirit animal is a creature chosen by a
shaman to serve as a conduit, allowing her to more fully access the magic of her spirit on a daily
basis. The shaman's spirit animal also grants her special powers. This ability uses the same rules
as the wizard's arcane bond class feature and is treated as a familiar (see pages 78 and 82 of the
_Core Rulebook_), except as noted below.

A shaman uses her level as her effective wizard level when determining the abilities of her spirit
animal. A shaman can select any familiar available to wizards to serve as her spirit animal,
although her spirit animal is augmented by the power of her chosen spirit. Once selected, the spirit
animal cannot be changed. Although a shaman's spirit animal uses the statistics of a specific
animal, it is treated as an outsider with the native subtype for the purposes of spells and
abilities that affect it.

Levels of different classes that are entitled to familiars stack with shaman levels for the purpose
of determining any spirit animal abilities that depend on the shaman's level. If a shaman possesses
such levels in other classes, her spirit animal always uses the shaman rules for spirit animals, not
those used by familiars of other classes (such as witches, wizards, or sorcerers with the arcane
bloodline). If the shaman has witch levels, her spirit animal also serves as the conduit to her
patron and stores her witch spells. The shaman's spirit animal is treated as a familiar for the
purposes of all spells, effects, and abilities that affect familiars.

If a spirit animal is lost or dies, it can be replaced after 24 hours through a special ritual that
consumes material components worth 500 gp per shaman level. The ritual takes 8 hours to complete.
The new spirit animal must be of the same sort of creature as the previous one.

_Spirit Animal (Ex)_: At 1st level, a shaman's spirit animal gains specific abilities, depending
upon the type of spirit selected by the shaman using her spirit class feature. These abilities
affect the animal's appearance and grant it special abilities that can aid it in serving the shaman
and the spirit it represents and is connected to. These abilities are described in the spirit animal
section of each individual spirit description.

_Deliver Touch Spells (Su)_: If a shaman is 3rd level or higher, her spirit animal can deliver touch
spells or hexes for her. If the shaman and the spirit animal are in contact at the time the shaman
casts a touch spell, she can designate her animal as the "toucher." The spirit animal can then
deliver the touch spell just as the shaman would. If the shaman casts another spell before the touch
is delivered, the touch spell dissipates. If the shaman activates a hex, her spirit animal can be
used to make the touch; she doesn't have to be in contact with the animal to use this ability with
hexes.

### Shaman Spells {#shaman-spells}

Shamans gain access to the following spells. While most of these spells are found in the _Core
Rulebook_, those with superscripts are drawn from other sources. Those marked with an asterisk (\*)
appear in Chapter 4 of this book.

### Alternate Capstones

When a character reaches the 20th level of a class, she gains a powerful class feature or ability,
sometimes referred to as a capstone. The following section provides new capstones for characters to
select at 20th level. A character can select one of the following capstones in place of the capstone
provided by her class. Some capstones are for specific classes, while others are for a range of
classes that qualify for them. In some cases, a capstone specifies what ability it replaces. A
character can't select a new capstone if she has previously traded away her class capstone via an
archetype. Clerics and wizards can receive a capstone at 20th level, despite not having one to begin
with. A character that gains certain abilities may be eligible for capstones other than those listed
below.

**Hex Mastery (Su)**

At 20th level, the shaman has learned ever more terrible hexes. She can select one grand hex from
the list available to witches.

**Also available:** Arch-Familiar

### Archetypes

From the noble paladin to the skillful rogue, each class draws upon a central archetype. Yet, beyond
that basic concept exists the potential for innumerable interpretations, details, and refinements;
and some archetypes prove pervasive and exciting enough to see use in play time and time again.

To help players interested in creating iconic fantasy characters, **archetypes** were introduced.
These optional features represent a unique view of what a class deliberately designed to capture a
specific character archetype might become. While the types of options presented for each class
differ, each subsystem is customized to best serve that class, emulate the abilities and talents of
classic fantasy archetypes, and expand players' freedom to design exactly the characters they
desire.

**Animist**

**Class:** shaman

**Modifies or Replaces:** Spirit Magic Spells; 2nd, 8th, 10th, 12th, and 18th-level Hexes;
Manifestation

**Description:** Even among mystical practitioners, the animist has a strange perspective and even
stranger magic. The animist perceives that all things have a spirit, including objects, constructs,
illnesses, buildings, and the environment.

**Benefactor**

**Class:** shaman

**Modifies or Replaces:** Spellcasting; Hexes

**Description:** A benefactor seeks to improve the lives of others by primarily offering powerful
supportive abilities and magic to her allies and others she deems worthy.

**Crystal Tender**

**Class:** shaman

**Modifies or Replaces:** Spirit Animal; Wandering Spirit; 8th-level Shaman Hex; Manifestation

**Description:** A crystal tender focuses on the spirits of metal and stone, using crystals as a
means to focus the power of the spirits she venerates.

**Deep Shaman**

**Class:** shaman

**Modifies or Replaces:** Spirit; Spirit Animal; Class Skills; Spirit Abilities

**Description:** Deep shamans are tied to spirits from the depths.

**Draconic Shaman**

**Class:** shaman

**Modifies or Replaces:** Spirit; Spirit Animal; 4th, 10th-level Hexes; Spirit Magic

**Description:** Some shamans draw their powers from the might of dragons. These shamans each gain a
powerful drake as an ally, and view caring for that drake as a sacred duty

**Grasping Vine**

**Class:** shaman

**Modifies or Replaces:** Spirit Animal; Spirit Magic; 2nd, 8th-level Hex

**Description:** Grasping vine shamans are typically adherents of one of several scattered sects
dedicated to the Green Mother. They revere plant life in all its forms, with a special fondness for
poisonous or carnivorous plants.

**Name-Keeper**

**Class:** shaman

**Modifies or Replaces:** Class Skills; Spirit Animal; Spirit Magic; Wandering Spirit; Wandering Hex

**Description:** Name-keepers have delved into the storied histories etched into the Wall of Names
and communed with the departed spirits of those whose names are memorialized on the monument.

**Overseer**

**Class:** shaman

**Modifies or Replaces:** Spirit Magic; Deliver Touch Spells

**Description:** While all shamans use their connection to the spirits of the world to draw upon
otherworldly magic powers, the shamans of the Lands of the Linnorm Kings have a unique tradition in
which they use the power of patron spirits to directly control their enemies.

**Possessed Shaman**

**Class:** shaman

**Modifies or Replaces:** Spirit Magic; 2nd and 6th-level Hexes

**Description:** For a possessed shaman, merely communing with the spirit world is insufficient.
Instead, she invites the spirits to share her body, granting them the chance to experience corporeal
existence.

**Primal Warden**

**Class:** shaman

**Modifies or Replaces:** Spirit Animal; Spirit Magic; 4th, 8th, 12th-level Hex

**Description:** A shaman who communes with spirits that linger in areas where primal magic reigns,
learning to stabilize these erratic energies and draw upon them to her benefit.

**Serendipity Shaman**

**Class:** shaman

**Modifies or Replaces:** Spirit Magic spells

**Description:** The serendipitous, shamanistic rites associated with the traditional catfolk
worship of the so-called "spirits of creation" focus upon attracting good fortune and banishing ill
fortune in the name of these spirits.

**Speaker for the Past**

**Class:** shaman

**Modifies or Replaces:** Spirit Animal; Wandering Spirit; Wandering Hex

**Description:** A speaker for the past is a shaman who specifically serves as the voice for spirits
from her people's history.

**Spirit Warden**

**Class:** shaman

**Modifies or Replaces:** Class Skills; Spirit Magic Spells; 2nd and 10th-level Hexes

**Description:** Not all spirits deserve reverence and respect. Some are twisted and despicable.
It's a spirit warden's duty to end these spirits' existence.

**True Silvered Throne**

**Class:** shaman

**Modifies or Replaces:** Class Skills; Spirit Animal; Wandering Spirit; Wandering Hex; 8th-level
Hex

**Description:** Members in good standing who have risen to a prestigious rank within the Esoteric
Order of the Palatine Eye, true silvered thrones have managed to discover rituals and occult secrets
within the lore of their order.

**Unsworn Shaman**

**Class:** shaman

**Modifies or Replaces:** Spirit; Hex; Spirit Animal; Wandering Spirit; Wandering Hex; Spirit Magic

**Description:** An unsworn shaman never binds herself to one specific spirit, always making new
deals as she deems necessary for the circumstances that she finds herself in.

**Visionary**

**Class:** shaman

**Modifies or Replaces:** Wandering Spirit; Spirit Magic Spells; Wandering Hex; Greater Wandering
Spirit; True Wandering Spirit

**Description:** The visionary is a master at divination, drawing upon her intimate relationship
with the spirit world to ferret out all manner of secrets and insights about the world around her
and beyond.

**Witch Doctor**

**Class:** shaman

**Modifies or Replaces:** Alignment; 4th, 8th, 10th, and 12th-level Hexes

**Description:** The witch doctor is a healer who specializes in afflictions of the soul.

### Archetypes by Feature

|Archetype|Alignment|Class Skills|Deliver Touch Spells|Hexes|2nd-level Hex|4th-level Hex|6th-level Hex|8th-level Hex|10th-level Hex|12th-level Hex|18th-level Hex|Manifestation|Spellcasting|Spirit|Greater Spirit|Spirit Animal|Spirit Magic|Wandering Hex|Wandering Spirit|Greater Wandering Spirit|True Wandering Spirit|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|[Animist](ref/arc-shaman/animist)|||||X|||X|X|X|X|X|||||X|||||
|[Benefactor](ref/arc-shaman/benefactor)||||X|||||||||X|||||||||
|[Crystal Tender](ref/arc-shaman/crystal-tender)||||||||X||||X||||X|||X|||
|[Deep Shaman](ref/arc-shaman/deep-shaman)||X||||||||||||X|X|X||||||
|[Draconic Shaman](ref/arc-shaman/draconic-shaman)||||||X|||X|||||X||X|X|||||
|[Grasping Vine](ref/arc-shaman/grasping-vine)|||||X|||X||||||||X|X|||||
|[Name-Keeper](ref/arc-shaman/name-keeper)||X||||||||||||||X|X|X|X|||
|[Overseer](ref/arc-shaman/overseer)|||X||||||||||||||X|||||
|[Possessed Shaman](ref/arc-shaman/possessed-shaman)|||||X||X||||||||||X|||||
|[Primal Warden](ref/arc-shaman/primal-warden)||||||X||X||X||||||X|X|||||
|[Serendipity Shaman](ref/arc-shaman/serendipity-shaman)|||||||||||||||||X|||||
|[Speaker for the Past](ref/arc-shaman/speaker-for-the-past)||||||||||||||||X||X|X|||
|[Spirit Warden](ref/arc-shaman/spirit-warden)||X|||X||||X||||||||X|||||
|[True Silvered Throne](ref/arc-shaman/true-silvered-throne)||X||||||X||||||||X||X|X|||
|[Unsworn Shaman](ref/arc-shaman/unsworn-shaman)||||X||||||||||X||X|X|X|X|||
|[Visionary](ref/arc-shaman/visionary)|||||||||||||||||X|X|X|X|X|
|[Witch Doctor](ref/arc-shaman/witch-doctor)|X|||||X||X|X|X||||||||||||

### Favored Class Bonuses

_The favored class options for shaman are listed on the
[separate class options page](ref/carried/advanced-race-guide/rules/core-races/alternate-racial-rules#favored-class-options)._
