+++
id = "ref/arc-unchained-summoner/fey-caller"
kind = "archetype"
title = "Fey Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20%28Unchained%29%20Fey%20Caller"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_caller", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "71"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-s-call" },
  { anchor = "fey-eidolon" },
]
trades = [
  { alters = "Summon monster spell-like ability", feature = "summon-monster-i", by = ["nature-s-call"] },
]
+++

The strange creatures known as fey hail from a variety of places, including the natural world and
their own domains on other planes. Fey callers are summoners whose voices reach out into those
strange faerie realms and call forth the fey who dwell there. The touch of the fey makes the fey
caller different from those summoners who call other outsiders to their sides as eidolons.

## Class Skills {#class-skills}

A fey caller adds Bluff, Diplomacy, Disguise, Knowledge (nature), Knowledge (planes), and Survival
to his list of class skills, instead of all Knowledge skills.

This alters the unchained summoner's class skills.

## Nature's Call {#nature-s-call}

Instead of summoning creatures from the _[summon monster](ref/spell/summon-monster)_ list, the fey
caller's summoning [spell-like ability](ref/umr/spell-like-abilities) summons creatures from the
list for the _[summon nature's ally](ref/spell/summon-natures-ally) spell_ of the same level. It
still follows the other rules and restrictions for the summoner's _summon monster_ spell-like
ability.

This ability alters the summoner's _summon monster_ spell-like ability.

## Fey Eidolon {#fey-eidolon}

A fey caller's eidolon is still an outsider, and its base statistics don't change, but it also
counts as a [fey](ref/type/fey). It has the following outsider type, instead of one of the types
listed in _Pathfinder RPG Pathfinder Unchained_.

### Fey Eidolons {#fey-eidolons}

Fey eidolons are whimsical and mysterious creatures, prone to flights of fancy, odd compulsions, and
alien humor. While some creatures from the faerie realms have truly unusual shapes, the ones close
enough to the human mind to serve as eidolons tend to look like idealized humanoids with unusual
features that set them apart, such as pointed ears or gossamer wings.

Fey eidolons usually choose to bond with mortals for their own mysterious reasons that vary as much
as their disparate temperaments; occasionally, their need may be immediate, such as when a
[dryad](ref/monster/dryad) whose tree is dying decides to bond with a summoner instead and become
something new. On the other hand, a [redcap](ref/monster/redcap) just looking for bloodshed might
connect with an equally sadistic summoner. Whatever their reasons, they tend to have strong bonds of
loyalty to their summoners entangled with equally strong emotional attachments, even evil fey
eidolons.

## Alignment {#alignment}

Any. Fey eidolons don't have alignment subtypes.

## Base Form {#base-form}

Biped ([limbs](ref/unchevolution/limbs) \[arms\], limbs \[legs\]).

## Base Evolutions {#base-evolutions}

Starting at 1st level, fey eidolons gain Acrobatics, Diplomacy, Disguise, Escape Artist, Knowledge
(nature), Perform, Sleight of Hand, and Use Magic Device as class skills instead of those gained by
most eidolons. They also gain the [low-light vision](ref/rule/low-light-vision) evolution, the
[skilled](ref/unchevolution/skilled) evolution (selecting one class skill), and the ability to use
either _[dancing lights](ref/spell/dancing-lights)_, _[detect magic](ref/spell/detect-magic)_,
_[ghost sound](ref/spell/ghost-sound)_, or _[prestidigitation](ref/spell/prestidigitation)_ at will
as a [spell-like ability](ref/umr/spell-like-abilities). Once the summoner selects this and any
other spell-like abilities for his fey eidolon, the selection cannot be changed.

At 4th level, fey eidolons gain [woodland stride](ref/ability/woodland-stride) (as the druid
ability).

At 8th level, fey eidolons gain the ability to use either _[charm person](ref/spell/charm-person)_,
_[entangle](ref/spell/entangle)_, _[grease](ref/spell/grease)_,
_[silent image](ref/spell/silent-image)_, _[obscuring mist](ref/spell/obscuring-mist)_, or
_[vanish](ref/spell/vanish)_ as a spell-like ability three times per day, and they can select an
additional spell-like ability from the 1st-level list.

At 12th level, fey eidolons gain DR 5/ cold iron. They also grow gossamer wings, gaining the
[flight](ref/unchevolution/flight) evolution.

At 16th level, fey eidolons gain the ability to use either
_[blindness/deafness](ref/spell/blindness-deafness)_,
_[detect thoughts](ref/spell/detect-thoughts)_, _[glitterdust](ref/spell/glitterdust)_,
_[hideous laughter](ref/spell/hideous-laughter)_, _[invisibility](ref/spell/invisibility)_ (self
only), _[minor image](ref/spell/minor-image)_, _[mirror image](ref/spell/mirror-image)_, or
_[tongues](ref/spell/tongues)_ as a spell-like ability three times per day. They also can select an
additional spell-like ability from the 1st-level list or the 8th-level list.

At 20th level, fey eidolons increase their DR to DR 10/cold iron. They gain the ability to use
either _[mass suggestion](ref/spell/suggestion-mass)_, _[mislead](ref/spell/mislead)_,
_[programmed image](ref/spell/programmed-image)_, or _[veil](ref/spell/veil)_ as a spell-like
ability once per day. They also can select an additional spell-like ability from the 1st-level list,
the 8th-level list, or the 16th-level list.
