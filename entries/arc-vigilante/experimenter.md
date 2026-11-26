+++
id = "ref/arc-vigilante/experimenter"
kind = "archetype"
title = "Experimenter"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Experimenter"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "experimenter", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "horror-adventures"
page = "70"

[fields]
kind = "archetype"
features = [
  { anchor = "forbidden-science", level = 1 },
  { anchor = "mutagenic-change", level = 1 },
  { anchor = "brew-potion", level = 3 },
  { anchor = "lore-master", level = 5 },
  { anchor = "craft-construct", level = 11 },
  { anchor = "mutable-mutagen", level = 17 },
]
trades = [
  { replaces = "Vigilante specialization", feature = "vigilante-specialization", by = ["forbidden-science"] },
  { replaces = "1st-level social talent", feature = "social-talent", levels = [1], by = ["mutagenic-change"] },
  { replaces = "Unshakable", feature = "unshakable", by = ["brew-potion"] },
  { replaces = "Startling appearance", feature = "startling-appearance", by = ["lore-master"] },
  { replaces = "Frightening appearance", feature = "frightening-appearance", by = ["craft-construct"] },
  { replaces = "Stunning appearance", feature = "stunning-appearance", by = ["mutable-mutagen"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Class skills" },
]
+++

Some vigilantes adopt lives of secrecy to hide their strange experiments from public view.

## Class Skills {#class-skills}

An experimenter adds all Knowledge skills to his list of class skills.

This alters the vigilante's class skills.

## Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

Experimenters aren't proficient with martial weapons, medium armor, or shields.

This alters the vigilante's weapon and armor proficiencies.

## Forbidden Science (Ex) {#forbidden-science}

An experimenter gains a bonus equal to 1/2 his vigilante level on Craft (alchemy) checks to create
alchemical items and on Knowledge (engineering) checks (minimum +1). He also learns how to craft a
mutagen as if he were an [alchemist](ref/class/alchemist) of his class level. He can take alchemical
discoveries in place of vigilante talents, but only discoveries that affect his mutagen (including
cognatogen discoveries).

When an experimenter is [confused](ref/misc/confused), dazed, frightened, panicked, or stunned, he
must attempt a Will save (DC = 20 + his vigilante level) each round at the start of his turn. If he
fails, he transforms as if he had consumed his mutagen (determine which ability score gets the bonus
randomly). This doesn't consume his mutagen, and lasts a number of rounds equal to 3 + his vigilante
level, after which the transformation ends and he becomes [fatigued](ref/misc/fatigued). While
transformed in this way, he is confused, and he rerolls any result of "act normally." Since the
confusion is part of the mutagenic transformation, abilities that prevent or remove confusion don't
apply to this effect, though abilities that end the effect of a mutagen work normally. He forgets
everything that happened while he was involuntarily transformed.

This ability replaces vigilante specialization.

## Mutagenic Change (Ex) {#mutagenic-change}

As a full-round action, an experimenter can consume his mutagen (if he has one) and shift from his
social identity to his vigilante identity, as if he had the
[quick change](ref/soctalent/quick-change) social talent.

This ability replaces the 1st-level social talent.

## Brew Potion {#brew-potion}

At 3rd level, an experimenter gains [Brew Potion](ref/feat/brew-potion) as a bonus feat. He treats
his vigilante level as his caster level and can use Craft (alchemy) instead of Spellcraft to brew
potions. He can use another potion of the same spell as a sample to provide the necessary spell
without consuming the potion, increasing the DC by 5.

This ability replaces unshakable.

## Lore Master (Ex) {#lore-master}

At 5th level, an experimenter gains the lore master [bard](ref/class/bard) class feature.

This ability replaces startling appearance.

## Craft Construct {#craft-construct}

At 11th level, an experimenter gains [Craft Construct](ref/feat/craft-construct) as a bonus feat. He
treats his vigilante level as his caster level and can use Knowledge (engineering) instead of
Spellcraft to craft a construct.

This ability replaces frightening appearance.

## Mutable Mutagen (Su) {#mutable-mutagen}

At 17th level, the duration of an experimenter's mutagen increases to 1 hour per level.

This ability replaces stunning appearance.
