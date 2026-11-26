+++
id = "ref/arc-hunter/feral-hunter"
kind = "archetype"
title = "Feral Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Feral%20Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feral_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "advanced-class-guide"
page = "95"

[fields]
kind = "archetype"
features = [
  { anchor = "solitary" },
  { anchor = "feral-focus", level = 1 },
  { anchor = "precise-summoned-animal", level = 2 },
  { anchor = "wild-shape", level = 4 },
  { anchor = "summon-pack", level = 6 },
]
trades = [
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["feral-focus"] },
  { replaces = "speak with master", feature = "speak-with-master", by = ["feral-focus"] },
  { replaces = "Bonus tricks", feature = "bonus-tricks", by = ["wild-shape"] },
  { replaces = "improved empathic link", feature = "improved-empathic-link", by = ["wild-shape"] },
  { replaces = "greater empathic link", feature = "greater-empathic-link", by = ["wild-shape"] },
  { replaces = "master of the wild", by = ["wild-shape"] },
  { replaces = "raise animal companion", feature = "raise-animal-companion", by = ["wild-shape"] },
  { replaces = "Teamwork feats gained at 6th, 9th, 12th, 15th, and 18th levels", feature = "teamwork-feat", levels = [6, 9, 12, 15, 18], by = ["summon-pack"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["feral-focus"] },
  { alters = "Precise companion", feature = "precise-companion", by = ["precise-summoned-animal"] },
]
+++

A feral hunter has forged a bond with nature that's so strong that she doesn't merely channel the
aspects of animals—she actually becomes an animal herself. Though she lacks an animal companion, a
feral hunter is in tune with the beast lurking within her flesh and spirit, and lives in a near-wild
state of being. A feral hunter often resembles a lycanthrope, but her power comes from her own
nature and is not influenced by moonlight or silver.

## Solitary {#solitary}

Unlike most hunters, a feral hunter does not gain an animal companion.

## Feral Focus (Su) {#feral-focus}

At 1st level, a feral hunter gains a limited ability to change her shape into hybrid animal forms.
This functions as the animal focus class feature, except that the hunter always applies the animal
aspect to herself, and there is no limit to this ability's duration. She can end this ability as a
free action.

When a feral hunter uses this ability, her body takes on cosmetic aspects of an animal, such as
furry skin, longer nails, elongated teeth, and oddly colored eyes; these changes do not grant her
any abilities other than what is stated in the animal focus, and end when she takes on a different
aspect or ends the ability. This physical change is a [polymorph](ref/spelldef/polymorph) effect,
though the effects of the animal focus are not.

This ability alters animal focus and replaces the hunter tactics and speak with master class
abilities.

## Precise Summoned Animal (Ex) {#precise-summoned-animal}

This functions like the precise companion class ability, except the hunter grants all her teamwork
feats to all animals she summons with _[summon nature's ally](ref/spell/summon-natures-ally)_. This
ability alters precise companion.

## Wild Shape (Su) {#wild-shape}

At 4th level, a feral hunter gains the ability to change shape. This ability functions like the
[druid](ref/class/druid) wild shape ability, except the hunter can take only animal forms (not
elemental or plant forms). The hunter's effective druid level is equal to her class level. This
ability replaces the bonus tricks, improved empathic link, greater empathic link, master of the
wild, and raise animal companion class abilities.

## Summon Pack (Sp) {#summon-pack}

Starting at 6th level, whenever a feral hunter casts a
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell to summon one or more animals, she
summons one additional animal of the same type. The summoned creature or creatures must be animals
and must be of the same type as the hunter's current aspect or of a similar type (bears for bear
aspect, dogs or wolves for wolf aspect, great cats for the tiger aspect, and so on). The additional
creature immediately vanishes if the hunter chooses a different aspect or ends his feral focus
ability. She can increase the duration of any one
[summon nature's ally](ref/spell/summon-natures-ally) spell affected by this ability to 1 minute per
level. She can have only one spell with a duration increased by this ability active at a time. This
ability replaces the teamwork feats gained at 6th, 9th, 12th, 15th, and 18th levels.
