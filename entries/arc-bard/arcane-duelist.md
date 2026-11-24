+++
id = "ref/arc-bard/arcane-duelist"
kind = "archetype"
title = "Arcane Duelist"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Arcane%20Duelist"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_duelist", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "80"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-strike" },
  { anchor = "bardic-performance" },
  { anchor = "rallying-cry", level = 1 },
  { anchor = "bladethirst" },
  { anchor = "mass-bladethirst" },
  { anchor = "arcane-bond", level = 5 },
  { anchor = "arcane-armor", level = 10 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["arcane-strike"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["rallying-cry"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["bladethirst"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["mass-bladethirst"] },
  { replaces = "Versatile performance", feature = "versatile-performance" },
  { replaces = "well-versed", feature = "well-versed" },
  { replaces = "Lore master", feature = "lore-master", by = ["arcane-bond"] },
  { replaces = "Jack of all trades", feature = "jack-of-all-trades", by = ["arcane-armor"] },
]
+++

A master of the martial applications of steel and spell, the arcane duelist blends both into a
lethal combination.

## Arcane Strike {#arcane-strike}

Arcane duelists gain [Arcane Strike](ref/feat/arcane-strike) as a bonus feat at 1st level. This
ability replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

An arcane duelist gains the following types of bardic performance.

## Rallying Cry (Su) {#rallying-cry}

At 1st level, an arcane duelist can use performance to rally dispirited allies. Each round he makes
an Intimidate check. Any ally (including the bard) within 30 feet may use this check in place of his
own saving throw against fear and despair effects. Those already under a fear or despair effect can
attempt a new save each round using the bard's Intimidate check. Rallying cry does not work on
effects that don't allow saves. This is a mind-affecting ability that uses audible components. This
performance replaces countersong.

## Bladethirst (Su) {#bladethirst}

An arcane duelist of 6th level or higher may use performance to grant one weapon, one natural
weapon, one end of a double weapon, or 50 items of ammunition of the same type within 30 feet a +1
enhancement bonus. This enhancement bonus increases by +1 for every three levels after 6th (maximum
+5 at 18th level). These bonuses stack with existing bonuses and may be used to increase the item's
enhancement bonus up to +5 or to add any of the following weapon properties:
_[defending](ref/magic-enh/defending)_, _[distance](ref/magic-enh/distance)_,
_[ghost touch](ref/magic-enh/ghost-touch-weapon)_, _[keen](ref/magic-enh/keen)_,
_[mighty cleaving](ref/magic-enh/mighty-cleaving)_, _[returning](ref/magic-enh/returning)_,
_[shock](ref/magic-enh/shock)_, _[shocking burst](ref/magic-enh/shocking-burst)_,
_[seeking](ref/magic-enh/seeking)_, _[speed](ref/magic-enh/speed)_, or
_[wounding](ref/magic-enh/wounding)_. If the weapon is not magical, at least a +1 enhancement bonus
must be added before adding special abilities. This performance replaces suggestion.

## Mass Bladethirst (Su) {#mass-bladethirst}

An arcane duelist of 18th level or higher can use his bladethirst performance to enhance the weapons
of as many allies as desired within 30 feet. The bonus provided by this power is +4 if conferred on
two allies, +3 for three allies, +2 for four allies, and +1 for five or more allies. The power
granted to each weapon must be identical. This ability replaces mass suggestion.

## Bonus Feats {#bonus-feats}

An arcane duelist weaves might and magic in his combat style, gaining the following bonus feats at
2nd level and every four levels thereafter: 2nd level—[Combat Casting](ref/feat/combat-casting), 6th
level—[Disruptive](ref/feat/disruptive), 10th level—[Spellbreaker](ref/feat/spellbreaker), 14th
level—[Penetrating Strike](ref/feat/penetrating-strike), 18th
level—[Greater Penetrating Strike](ref/feat/greater-penetrating-strike). This ability replaces
versatile performance and well-versed.

## Arcane Bond (Ex) {#arcane-bond}

At 5th level, an arcane duelist gains the arcane bond ability as a [wizard](ref/class/wizard), using
a weapon as his bonded item, allowing him to cast any one additional spell that he knows once per
day. He may not choose a familiar or other type of bonded item. He may use the hand holding his
bonded weapon for somatic components. This ability replaces lore master.

## Arcane Armor (Ex) {#arcane-armor}

At 10th level, an arcane duelist gains Medium Armor Proficiency and can cast bard spells in medium
armor with no chance of arcane spell failure. At 16th level, he gains Heavy Armor Proficiency and
can cast bard spells in heavy armor with no arcane spell failure. This ability replaces jack of all
trades.
