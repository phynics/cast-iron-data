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
features = [
  { anchor = "conductor", level = 1 },
  { anchor = "planar-scholar", level = 2 },
  { anchor = "harmonic-shield", level = 4 },
  { anchor = "outside-messenger", level = 5 },
]
trades = [
  { replaces = "Magic item skill", feature = "magic-item-skill", by = ["planar-scholar"] },
  { replaces = "Shift focus", feature = "shift-focus", by = ["harmonic-shield"] },
  { replaces = "Focus power gained at 7th level", feature = "focus-powers", levels = [7], by = ["harmonic-shield"] },
  { replaces = "Aura sight", feature = "aura-sight", by = ["outside-messenger"] },
  { replaces = "Focus power gained at 5th level", feature = "focus-powers", levels = [5], by = ["outside-messenger"] },
  { alters = "Implements", feature = "implements", by = ["conductor"] },
  { alters = "implement mastery", feature = "implement-mastery", by = ["conductor"] },
  { alters = "Magic circles", feature = "magic-circles", by = ["outside-messenger"] },
]
+++

Tuning forks resonate with the music of the planes, guiding travelers between worlds. Planar
harmonizers are masters of this symphony, forging bonds with tuning forks to unlock the true
potential of these instruments. Planar harmonizers typically select their tuning forks carefully,
choosing planes that resonate best with particular schools of magic.

## Conductor (Su) {#conductor}

A planar harmonizer gains access to only the [conjuration](ref/implement/conjuration) school of
implements, gaining a [common tuning fork](ref/rule/common-tuning-fork) as her implement. She must
select conjuration for her implement mastery. Each time she gains an occultist level, a planar
harmonizer can add one conjuration spell from the wizard spell list to her occultist spell list and
her list of spells known. The planar harmonizer can't choose a spell of a higher level than she is
able to cast, and she adds the spell at the same spell level it appears on the wizard spell list.
Additionally, she adds _[plane shift](ref/spell/plane-shift)_ to her list as a 5th-level occultist
spell. At 14th level, she doesn't gain an additional school of implements. Instead, at 14th level,
the DCs of saving throws to resist a planar harmonizer's conjuration spells and conjuration focus
powers increase by 2. All future implements that a planar harmonizer gains are common tuning forks.

This alters implements and implement mastery.

## Planar Scholar (Su) {#planar-scholar}

At 2nd level, a planar harmonizer deepens her knowledge about other worlds. She gains a bonus on
Knowledge (planes) checks equal to half her occultist level.

This replaces magic item skill.

## Harmonic Shield (Su) {#harmonic-shield}

At 4th level, a planar harmonizer learns to cloak herself in the essence of her home plane. She
doesn't take penalties on Intelligence-, Wisdom-, or Charisma-based checks for being on a plane
whose alignment traits clash with her own alignment. At 7th level, she can expend 1 point of mental
focus to gain the benefits of _[planar adaptation](ref/spell/planar-adaptation)_ for 1 minute per
occultist level. At 11th level, the duration of this protection extends to 1 hour per occultist
level.

This replaces shift focus and the focus power gained at 7th level.

## Outside Messenger (Su) {#outside-messenger}

At 5th level, a planar harmonizer gains the magic circles class feature. Whenever she creates a
[magic circle](ref/spell/magic-circle), she can expend 1 additional point of mental focus (either
generic focus or focus from any one of her implements) to focus the circle inward and lure that
outsider to the circle (similar to using
_[lesser planar binding](ref/spell/planar-binding-lesser)_). This functions as the outside contact
occultist ability, except the information gained can be anything that might be learned through an
_[augury](ref/spell/augury)_ spell.

This alters magic circles and replaces aura sight and the focus power gained at 5th level.
