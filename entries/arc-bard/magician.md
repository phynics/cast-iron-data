+++
id = "ref/arc-bard/magician"
kind = "archetype"
title = "Magician"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Magician"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magician", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "82"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "dweomercraft", level = 1 },
  { anchor = "spell-suppression", level = 8 },
  { anchor = "metamagic-mastery", level = 14 },
  { anchor = "magical-talent", level = 1 },
  { anchor = "improved-counterspell", level = 1 },
  { anchor = "extended-performance", level = 2 },
  { anchor = "expanded-repertoire", level = 2 },
  { anchor = "arcane-bond", level = 5 },
  { anchor = "wand-mastery", level = 10 },
]
trades = [
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["dweomercraft"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["spell-suppression"] },
  { replaces = "Frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["metamagic-mastery"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["magical-talent"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["improved-counterspell"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["extended-performance"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["expanded-repertoire"] },
  { replaces = "Lore master", feature = "lore-master", by = ["arcane-bond"] },
  { replaces = "Jack of all trades", feature = "jack-of-all-trades", by = ["wand-mastery"] },
]
+++

A magician dabbles in performance, but sees it as a means to tap into universal energies and channel
them.

## Bardic Performance {#bardic-performance}

A magician gains the following types of bardic performance.

## Dweomercraft (Su) {#dweomercraft}

A magician can use performance to manipulate magical energies. Allies of the magician gain a +1
bonus on caster level checks, [concentration](ref/rule/concentration) checks, and attack rolls with
spells and [spell-like abilities](ref/umr/spell-like-abilities). This bonus increases by +1 at 5th
level and every six levels thereafter. This ability relies on visual and audible components. It
replaces inspire courage.

## Spell Suppression (Su) {#spell-suppression}

At 8th level, a magician can use performance to counter the spells of his foes. Once the bard begins
using this performance, he tracks the number of rounds it has been in use. While performing, as an
immediate action, he can attempt to counter any spell that he can identify using Spellcraft, so long
as that spell's level is equal or less than the total number of rounds he has been performing spell
suppression. The attempt to counter the spell is made as if using
_[dispel magic](ref/spell/dispel-magic)_, using the bard's level as the caster level. If successful,
the bardic performance immediately ends. This ability requires audible components. This performance
replaces dirge of doom.

## Metamagic Mastery (Ex) {#metamagic-mastery}

At 14th level, a magician can use performance to apply a metamagic feat to a spell he is about to
cast without increasing the casting time. The bard must still expend a higher-level slot to cast
this spell. This causes the performance to immediately end. This ability requires audible
components. This performance replaces frightening tune.

## Magical Talent (Ex) {#magical-talent}

A magician gains a bonus equal to [half](ref/misc/fractions-and-rounding) his level on Knowledge
(arcana), Spellcraft, and Use Magic Device checks. This ability replaces bardic knowledge.

## Improved Counterspell {#improved-counterspell}

A magician gains [Improved Counterspell](ref/feat/improved-counterspell) as a bonus feat. This
ability replaces countersong.

## Extended Performance (Su) {#extended-performance}

At 2nd level, a magician can extend the duration of bardic performance after he stops concentrating
by sacrificing a spell slot as a swift action. The performance effect lingers for 1 extra round per
level of the spell. Only one spell may be sacrificed per performance, and performance types that
take affect after a specific number of rounds cannot be extended. This ability replaces well-versed.

## Expanded Repertoire (Ex) {#expanded-repertoire}

At 2nd level and every four levels thereafter, a magician can add one spell to his spells known from
the spell list of any arcane spellcasting class. The spell must be of a level he can cast. This
ability replaces versatile performance.

## Arcane Bond (Ex) {#arcane-bond}

At 5th level, a magician gains the arcane bond ability as a [wizard](ref/class/wizard). He may not
choose a familiar or a weapon as a bonded item. This ability replaces lore master.

## Wand Mastery (Ex) {#wand-mastery}

At 10th level, when a magician uses a wand containing a spell on his spell list, he uses his
Charisma bonus to set the wand's save DC. At 16th level, when using such a wand, he uses his caster
level in place of the wand's caster level. This ability replaces jack of all trades.
