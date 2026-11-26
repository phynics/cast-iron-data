+++
id = "ref/arc-investigator/guardian-of-immortality"
kind = "archetype"
title = "Guardian of Immortality"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Guardian%20of%20Immortality"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guardian_of_immortality", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "41"

[fields]
kind = "archetype"
features = [
  { anchor = "guardian-s-gaze", level = 2 },
  { anchor = "desert-survivor", level = 2 },
  { anchor = "liar-s-familiarity", level = 7 },
  { anchor = "orchid-s-drop", level = 11 },
  { anchor = "teleportation-warden", level = 13 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["guardian-s-gaze"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["desert-survivor"] },
  { replaces = "Investigator talent gained at 7th level", feature = "investigator-talent", levels = [7], by = ["liar-s-familiarity"] },
  { replaces = "Immunity to poison", feature = "poison-resistance", levels = [11], by = ["orchid-s-drop"] },
  { replaces = "Investigator talent gained at 13th level", feature = "investigator-talent", levels = [13], by = ["teleportation-warden"] },
]
+++

Guardians of immortality are Thuvian investigators charged with hunting down those who would attempt
to steal or learn for themselves the secret to creating the
[sun orchid elixir](ref/magic-artifact/sun-orchid-elixir).

## Guardian's Gaze (Ex) {#guardian-s-gaze}

At 2nd level, a guardian of immortality adds 1/2 his investigator level as a bonus on Sense Motive
checks.

This ability replaces poison lore.

## Desert Survivor (Ex) {#desert-survivor}

At 2nd level, a guardian of immortality is trained by the druids of Duwwor to survive the hazards of
the desert. He gains [Endurance](ref/feat/endurance) as a bonus feat and does not treat sand as
[difficult terrain](ref/rule/terrain-and-obstacles). At 5th level, he gains
[resist](ref/umr/resistance) fire 10. At 8th level, he can see twice as far in sandstorms, clouds,
and fog, and whenever he gains an advantage in a desert tile during a [pursuit](ref/rule/pursuit),
he gains an additional advantage.

This ability replaces poison resistance.

## Liar's Familiarity (Ex) {#liar-s-familiarity}

At 7th level, a guardian of immortality learns Lamasaran decoy and forgery techniques to better
defeat them. His inspiration applies automatically without using an action or a use of inspiration
on saving throws to disbelieve illusions, Disguise skill checks, Perception checks to see through
disguises, and Linguistics checks to create or detect forgeries.

This replaces the investigator talent gained at 7th level.

## Orchid's Drop (Ex) {#orchid-s-drop}

At 11th level, a guardian of immortality is entrusted with a secret solution designed by Thuvian
alchemists to emulate certain aspects of the _sun orchid elixir_, granting him a +1 alchemical bonus
on all saving throws.

This ability replaces immunity to poison.

## Teleportation Warden (Su) {#teleportation-warden}

At 13th level, a guardian of immortality is trained by the mages of Pashow to sense the impending
arrival or departure of creatures using teleportation. This ability constantly functions like
_[trace teleport](ref/spell/trace-teleport)_. In addition, the guardian of immortality can use
_[conjuration foil](ref/spell/conjuration-foil)_ once per day as an immediate action.

This replaces the investigator talent gained at 13th level.

## Investigator Talents {#investigator-talents}

The following investigator talents complement the guardian of immortality archetype:
[alchemist discovery](ref/invtalent/alchemist-discovery),
[combat inspiration](ref/invtalent/combat-inspiration),
[greater combat inspiration](ref/invtalent/greater-combat-inspiration),
[inspired alertness](ref/invtalent/inspired-alertness),
[stealing strike](ref/invtalent/stealing-strike), and
[toppling strike](ref/invtalent/toppling-strike).
