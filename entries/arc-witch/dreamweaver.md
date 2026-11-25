+++
id = "ref/arc-witch/dreamweaver"
kind = "archetype"
title = "Dreamweaver"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Dreamweaver"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dreamweaver", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "advanced-race-guide"
page = "185"

[fields]
kind = "archetype"
features = [
  { anchor = "patron" },
  { anchor = "spells" },
  { anchor = "dream-spinner", level = 2 },
  { anchor = "dream-thief", level = 6 },
  { anchor = "dream-possession", level = 10 },
]
trades = [
  { replaces = "Witch's hex gained at 2nd level", feature = "hex", levels = [2], by = ["dream-spinner"] },
  { replaces = "Witch's hex gained at 6th level", feature = "hex", levels = [6], by = ["dream-thief"] },
  { replaces = "Witch's hex gained at 10th level", feature = "hex", levels = [10], by = ["dream-possession"] },
]
+++

A changeling dreamweaver draws upon her hag heritage to ply the dream realms in order to touch
mortal minds and souls, for good or ill. A dreamweaver witch has the following class features.

## Class Skills {#class-skills}

The dreamweaver adds Sense Motive to her list of class skills and removes Healing from her list of
class skills.

## Patron {#patron}

A dreamweaver's patron is normally [portents](ref/patron/portents) or [stars](ref/patron/stars).

## Spells {#spells}

A dreamweaver replaces some of her patron's spells with the following: 2nd—_sow thoughts_ (see
below), 4th—_dust of twilight_ (_Pathfinder RPG Advanced Player's Guide_), 6th—_deep slumber_,
8th—_modify memory_, 10th—_dream_, 12th— _cloak of dreams_ (_Advanced Player's Guide_),
14th—_ethereal jaunt_, 16th—_moment of prescience_, 18th—_astral projection_.

## Dream Spinner (Su) {#dream-spinner}

At 2nd level, when a dreamweaver casts a mind-affecting spell on a target that is sleeping because
of her [slumber](ref/hex/slumber) hex or a spell she cast, she adds +1 to the mind-affecting spell's
DC. If the target succeeds at the saving throw against the spell, it does not wake up, nor does it
have any recollection of having resisted a spell. If appropriate, the dreamweaver may incorporate
elements of a mind-affecting spell (i.e., _[sow thought](ref/spell/sow-thought)_,
_[suggestion](ref/spell/suggestion)_, and so on) into the target's subconscious so it believes the
spell's effects originated in its dreams (the details of how these elements fit into the dream is up
to the GM). This ability replaces the witch's hex gained at 2nd level.

## Dream Thief (Su) {#dream-thief}

At 6th level, a dreamweaver can alter the sleeping mind of any creature that is sleeping because of
her slumber hex or a spell she cast. She can reshape one of the target's memories as if using
_[modify memory](ref/spell/modify-memory)_. Alternatively, she may insert herself into the dreaming
memories of the target, prompting the target's mind to show her some specific information; the
dreamer's subconscious may resist, or try to deceive her with out-of-context memories, similar to
the way a corpse can resist when questioned with _[speak with dead](ref/spell/speak-with-dead)_. A
Will save negates either effect (DC equal to that of the witch's hex). Whether or not the save is
successful, a creature cannot be the target of this hex again for 1 day. This ability replaces the
witch's hex gained at 6th level.

## Dream Possession (Su) {#dream-possession}

At 10th level, a dreamweaver can take control of any creature that is sleeping because of her
slumber hex or a spell she cast. This effect functions as _[magic jar](ref/spell/magic-jar)_, using
the witch's familiar acting as the soul receptacle. A Will save negates either effect (DC equal to
that of the witch's hex). Whether or not the save is successful, a creature cannot be the target of
this hex again for 1 day. This ability replaces the witch's hex gained at 10th level.

## Hexes {#hexes}

The following hexes complement the dreamweaver archetype: charm, slumber (_Advanced Player's
Guide_); beast of ill-omen (_Ultimate Magic_).

## Major Hexes {#major-hexes}

The following major hexes complement the dreamweaver archetype: nightmare, vision (_Advanced
Player's Guide_).

## Grand Hexes {#grand-hexes}

The following grand hexes complement the dreamweaver archetype: eternal slumber (_Advanced Player's
Guide_); dire prophecy (_Ultimate Magic_).
