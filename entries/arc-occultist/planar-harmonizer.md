+++
id = "ref/arc-occultist/planar-harmonizer"
kind = "archetype"
title = "Planar Harmonizer"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Planar%20Harmonizer"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_harmonizer", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "7"

[fields]
kind = "archetype"
replaces = ["Magic item skill", "Shift focus, 7th-level focus power", "Aura sight, 5th-level focus power"]
alters = ["Implements", "implement mastery", "Magic circles"]
+++

Tuning forks resonate with the music of the planes, guiding travelers between worlds. Planar
harmonizers are masters of this symphony, forging bonds with tuning forks to unlock the true
potential of these instruments. Planar harmonizers typically select their tuning forks carefully,
choosing planes that resonate best with particular schools of magic.

**Conductor (Su)**

**Ability:** Each time she gains an occultist level, a planar harmonizer can add one conjuration
spell from the wizard spell list to her occultist spell list and her list of spells known. The
planar harmonizer can't choose a spell of a higher level than she is able to cast, and she adds the
spell at the same spell level it appears on the wizard spell list.

**Alters:** Implements, implement mastery

**At 10th Level:** She adds [plane shift](ref/spell/plane-shift) to her list as a 5th-level
occultist spell.

**At 14th Level:** She doesn't gain an additional school of implements. Instead, the DCs of saving
throws to resist a planar harmonizer's conjuration spells and conjuration focus powers increase
by 2.

**Info:** A planar harmonizer gains access to only the [conjuration](ref/implement/conjuration)
school of implements, gaining a [common tuning fork](ref/rule/common-tuning-fork) as her implement.
She must select conjuration for her _implement mastery._

**Special:** All future implements that a planar harmonizer gains are common tuning forks.

**Planar Scholar (Su)**

**Flavor:** A planar harmonizer deepens her knowledge about other worlds.

**Gained:** At 2nd Level

**Passive:** She gains a bonus on Knowledge (planes) checks equal to half her occultist level.

**Replaces:** Magic item skill

**Harmonic Shield (Su)**

**Flavor:** A planar harmonizer learns to cloak herself in the essence of her home plane.

**At 11th Level:** The duration of this protection extends to 1 hour per occultist level.

**At 4th Level:** She doesn't take penalties on Intelligence-, Wisdom-, or Charisma-based checks for
being on a plane whose alignment traits clash with her own alignment.

**At 7th Level:** She can expend 1 point of mental focus to gain the benefits of
[planar adaptation](ref/spell/planar-adaptation) for 1 minute per occultist level.

**Replaces:** Shift focus, 7th-level focus power

**Outside Messenger (Su)**

**Ability:** A planar harmonizer gains the _magic circles_ class feature. Whenever she creates a
_[magic circle](ref/spell/magic-circle),_ she can expend 1 additional point of mental focus (either
generic focus or focus from any one of her implements) to focus the circle inward and lure that
outsider to the circle (similar to using [lesser planar binding](ref/spell/planar-binding-lesser)).
This functions as the _outside contact_ occultist ability, except the information gained can be
anything that might be learned through an [augury](ref/spell/augury) spell.

**Alters:** Magic circles

**Gained:** At 5th Level

**Replaces:** Aura sight, 5th-level focus power
