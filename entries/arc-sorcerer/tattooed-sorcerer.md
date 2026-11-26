+++
id = "ref/arc-sorcerer/tattooed-sorcerer"
kind = "archetype"
title = "Tattooed Sorcerer"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Tattooed%20Sorcerer"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tattooed_sorcerer", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "inner-sea-magic"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "familiar-tattoo", level = 1 },
  { anchor = "varisian-tattoo", level = 1 },
  { anchor = "bloodline-tattoos" },
  { anchor = "create-spell-tattoo", level = 7 },
  { anchor = "enhanced-varisian-tattoo", level = 9 },
]
trades = [
  { replaces = "1st-level bloodline power", feature = "bloodline", levels = [1], power = "bloodline power", by = ["familiar-tattoo"] },
  { replaces = "Eschew Materials bonus feat", feature = "eschew-materials", by = ["varisian-tattoo"] },
  { replaces = "Bloodline feat gained at 7th level", feature = "bloodline", levels = [7], power = "bloodline feat", by = ["create-spell-tattoo"] },
  { replaces = "9th-level bloodline power", feature = "bloodline", levels = [9], power = "bloodline power", by = ["enhanced-varisian-tattoo"] },
]
+++

The tattooed sorcerer has embraced the ancient traditions of Varisian spellcasting, and uses
colorful and intricate tattoos to enhance her magical powers. A tattooed sorcerer has the following
class features.

## Familiar Tattoo (Su) {#familiar-tattoo}

A tattooed sorcerer gains a [familiar](ref/sidekick/familiar) as an arcane bond, as a
[wizard](ref/class/wizard) equal to her sorcerer level. Her sorcerer levels stack with any wizard or
[witch](ref/class/witch) levels she possesses when determining the powers of her
[familiar](ref/ability/familiars)—this ability does not allow her to have both a familiar and a
bonded item.

Unlike most familiars, her familiar can transform itself into a tattoo that she carries in her
flesh. Transforming into a tattoo or back to normal familiar form is a move action for her familiar.
In tattoo form, the familiar looks like a stylized version of itself, but does not count as a
creature separate from the tattooed sorcerer. In tattoo form it continues to grant its special
familiar ability (_Core Rulebook_ 82), but otherwise has no abilities and can take no actions except
to transform from tattoo into creature.

A familiar tattoo cannot be erased or dispelled. This ability replaces her 1st-level bloodline
power.

## Varisian Tattoo (Ex) {#varisian-tattoo}

At 1st level, the tattooed sorcerer gains [Varisian Tattoo](ref/feat/varisian-tattoo) (see the
_Inner Sea World Guide_) as a bonus feat. If she doesn't have [Spell Focus](ref/feat/spell-focus),
she may choose which school of magic her Varisian Tattoo enhances. This ability replaces her Eschew
Materials bonus feat.

## Bloodline Tattoos (Ex) {#bloodline-tattoos}

Whenever a tattooed sorcerer gains a bloodline spell, a new tattoo manifests on her body to
represent this spell.

Her bloodline spells are always enhanced by her Varisian Tattoo feat, even if they don't match the
school to which her Varisian Tattoo belongs.

## Create Spell Tattoo (Su) {#create-spell-tattoo}

At 7th level, a tattooed sorcerer can create a _[spell tattoo](ref/magic-tattoo/spell-tattoo)_ (see
page 16) once per day with a single touch as a standard action. The recipient of the spell tattoo
must be willing to receive the spell tattoo. If she gives the _spell tattoo_ to herself, it does not
count against the regular limit of magic tattoos she can have. The _spell tattoo_ must be of a spell
that she knows that has no material or focus component. She can maintain one _spell tattoo_ created
by this ability at a time—if she uses this ability again, the previous spell tattoo she created
fades away. _Spell tattoos_ she creates with
[Inscribe Magical Tattoo](ref/feat/inscribe-magical-tattoo) do not count against this limit. She can
use this ability twice per day at 11th level, and three times per day at 15th level. This ability
replaces the bloodline feat gained at 7th level.

## Enhanced Varisian Tattoo (Su) {#enhanced-varisian-tattoo}

At 9th level, the tattooed sorcerer can pick any one spell she knows for which she has a Varisian
Tattoo feat. This spell must be one that lacks focus components and costly material components. She
can now use that spell as a [spell-like ability](ref/umr/spell-like-abilities) once per day. This
[spell-like ability](ref/umr/spell-like-abilities) is not enhanced by her Varisian Tattoo, but it
functions at +2 caster levels above her sorcerer caster level. Whenever she gains a bloodline power
at a later date, she may change this spell-like ability to another qualifying spell. This ability
replaces the 9th-level bloodline power.
