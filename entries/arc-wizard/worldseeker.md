+++
id = "ref/arc-wizard/worldseeker"
kind = "archetype"
title = "Worldseeker"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Worldseeker"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "worldseeker", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "planar-adventures"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "walk-the-planes", level = 1 },
  { anchor = "planar-adaptation", level = 8 },
  { anchor = "planar-associates", level = 1 },
  { anchor = "planar-redoubt", level = 15 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["walk-the-planes"] },
  { replaces = "The school ability normally gained at 6th or 8th level", feature = "arcane-school", levels = [6, 8], power = "school powers", by = ["planar-adaptation"] },
  { replaces = "Bonus feat gained at 5th level", feature = "bonus-feats", levels = [5], by = ["planar-associates"] },
  { replaces = "Bonus feat gained at 15th level", feature = "bonus-feats", levels = [15], by = ["planar-redoubt"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["planar-associates"] },
]
+++

Worldseekers are wizards who travel to all corners of the Great Beyond. While neophytes must content
themselves with study and practice, the most powerful worldseekers are movers and shakers throughout
the Great Beyond, power players of whom even demigods take note. Worldseekers are rare sights on
Golarion, but among those few, more are trained in Kyonin and Nex than any other nation; those in
Kyonin explore the potential of using elf gates to travel beyond this realm, while those in Nex
emulate some of the dimensional exploits of Nex's legendary founder.

Most worldseekers prefer not to specialize in a school of magic, for having a diverse array of
available spells is a boon when exploring the countless wonders of the Great Beyond. Those who do
specialize usually do so as [conjurers](ref/arcaneschool/conjuration). Conjuration is a poor choice
of oppositional school for a worldseeker.

## Walk the Planes (Sp, Su) {#walk-the-planes}

A worldseeker learns every plane's place in the Great Beyond and trains to survive even on the
harshest of them. She gains a +2 bonus on Knowledge (planes) checks and is constantly under the
effects of _[endure elements](ref/spell/endure-elements)_.

This replaces Scribe Scroll.

## Planar Adaptation (Su) {#planar-adaptation}

At 8th level, a worldseeker is continually protected from planar environments as by
_[planar adaptation](ref/spell/planar-adaptation)_. At 15th level, she can extend that benefit to
all allies within 30 feet of her.

This replaces the school ability normally gained at 6th or 8th level.

## Planar Associates (Ex) {#planar-associates}

A worldseeker's travels and dealings across the planes allow her to make connections she can call
upon when necessary to gain assistance without needing to resort to
_[planar binding](ref/spell/planar-binding)_. A worldseeker must choose a
[familiar](ref/ability/familiars) for her arcane bond. At 5th level, she gains
[Improved Familiar](ref/feat/improved-familiar) as a bonus feat and must choose an outsider familiar
that matches her alignment exactly; she can choose an outsider in this way even if it normally
requires a 7th-level spellcaster as its master.

At 7th level, a worldseeker automatically learns
_[lesser planar ally](ref/spell/planar-ally-lesser)_ as a 4th-level wizard spell. She automatically
learns _[planar ally](ref/spell/planar-ally)_ as a 6th-level wizard spell at 11th level, and
_[greater planar ally](ref/spell/planar-ally-greater)_ as an 8th-level wizard spell at 15th level.
She can swap out a prepared spell of an equal spell level to spontaneously cast any of these three
spells (one 4th-level spell for _[lesser planar ally](ref/spell/planar-ally-lesser)_, a 6th-level
spell for _[planar ally](ref/spell/planar-ally)_, and a 8th level spell for
_[greater planar ally](ref/spell/planar-ally-greater)_).

The first time each day she casts one of these three spells, the worldseeker reduces the gp value of
the material component cost by an amount equal to her caster level � 100 (to a minimum cost of 0
gp).

This alters arcane bond and replaces the bonus feat gained at 5th level.

## Planar Redoubt (Sp) {#planar-redoubt}

At 15th level, a worldseeker creates a planar redoubt, a personal demiplane to which she can retreat
to rest and plan. This functions like
_[lesser create demiplane](ref/spell/create-demiplane-lesser)_, except the demiplane is up to a
single 50-foot cube in size and is permanent.

This replaces the bonus feat gained at 15th level.
