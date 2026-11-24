+++
id = "ref/arc-warpriest/disenchanter"
kind = "archetype"
title = "Disenchanter"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Disenchanter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disenchanter", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "129"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feats" },
  { anchor = "mystic-interference", level = 4 },
  { anchor = "banish-enchantment", level = 6 },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["mystic-interference"] },
  { replaces = "Bonus feat gained at 6th level", feature = "bonus-feats", levels = [6], by = ["banish-enchantment"] },
  { alters = "Bonus feats", feature = "bonus-feats", by = ["bonus-feats"] },
]
+++

While many warpriests focus on threats to the body, the disenchanter focuses on dangers to the mind
and the soul. Using the power of his patron, the disenchanter seeks to keep the powers of magic in
check.

## Bonus Feats (Ex) {#bonus-feats}

Whenever a disenchanter gains a bonus feat, he must choose from the following list:
[Great Fortitude](ref/feat/great-fortitude),
[Improved Counterspell](ref/feat/improved-counterspell), [Iron Will](ref/feat/iron-will),
[Lightning Reflexes](ref/feat/lightning-reflexes), [Skill Focus](ref/feat/skill-focus) (Spellcraft),
or [Spell Focus](ref/feat/spell-focus) (abjuration). At 6th level, he adds the following feats to
this list: [Dispel Synergy](ref/feat/dispel-synergy),
[Improved Great Fortitude](ref/feat/improved-great-fortitude),
[Improved Iron Will](ref/feat/improved-iron-will), and
[Improved Lightning Reflexes](ref/feat/improved-lightning-reflexes). At 12th level, he adds the
following feats to this list: [Destructive Dispel](ref/feat/destructive-dispel),
[Dispelling Critical](ref/feat/dispelling-critical), [Parry Spell](ref/feat/parry-spell), and
[Ray Shield](ref/feat/ray-shield). He need not meet the prerequisites for these feats. This ability
alters bonus feats.

## Mystic Interference (Su) {#mystic-interference}

At 4th level, a disenchanter can channel a [burst](ref/misc/burst) of pure abjuration magic to grant
protection to himself and all allies with 30 feet. Affected creatures receive a +1 bonus on saving
throws against spells and [spell-like abilities](ref/umr/spell-like-abilities) for a number of
rounds equal to his warpriest level. This is a sacred bonus if the warpriest is good-aligned or able
to spontaneously cast cure spells, and a profane bonus if the warpriest is evil-aligned or able to
spontaneously cast inflict spells. Using this ability consumes two uses of his fervor ability. At
8th level and every 4 levels thereafter, the bonus granted by mystic interference increases by 1 (to
a maximum of +5 at 20th level). This ability replaces channel energy.

## Banish Enchantment (Su) {#banish-enchantment}

At 6th level, a disenchanter learns to focus his mystic interference. As a standard action, he can
consume two uses of his fervor ability to target a single creature within 30 feet with a targeted
_[dispel magic](ref/spell/dispel-magic)_. This ability replaces the bonus feat gained at 6th level.
