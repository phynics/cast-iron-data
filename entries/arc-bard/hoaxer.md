+++
id = "ref/arc-bard/hoaxer"
kind = "archetype"
title = "Hoaxer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Hoaxer"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hoaxer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "black-markets"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "counterfeiter", level = 1 },
  { anchor = "bad-deal", level = 1 },
  { anchor = "buyer-beware", level = 1 },
  { anchor = "personal-guarantee", level = 1 },
  { anchor = "curse-breaker", level = 12 },
  { anchor = "misery", level = 2 },
  { anchor = "versed-in-curses", level = 2 },
  { anchor = "curse-crafter", level = 5 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["counterfeiter"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["bad-deal"] },
  { replaces = "inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["bad-deal"] },
  { replaces = "and inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["bad-deal"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["buyer-beware"] },
  { replaces = "Distraction", feature = "bardic-performance", power = "distraction", by = ["personal-guarantee"] },
  { replaces = "Inspire greatness", by = ["curse-breaker"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["misery"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["versed-in-curses"] },
  { replaces = "Lore master", feature = "lore-master", by = ["curse-crafter"] },
]
+++

Hoaxers specialize in creating valuable-looking counterfeits and infusing these false treasures with
dangerous magic to make their marks more vulnerable to future swindles.

## Counterfeiter (Ex) {#counterfeiter}

A hoaxer adds [half](ref/misc/fractions-and-rounding) his bard level (minimum 1) on all Appraise,
Bluff, and Sleight of Hand checks, as well as on Craft, Knowledge, Linguistics, Perception, and
Profession checks to create or detect a counterfeit or forgery. He can attempt such skill checks
untrained. This ability replaces bardic knowledge.

## Bardic Performance (Su) {#bardic-performance}

A hoaxer dedicates his arcane energies to deceiving others rather than to entertaining them,
granting him the following unique performances.

## Bad Deal (Su) {#bad-deal}

A hoaxer can use his performance to coax a bit of luck (good or bad) into a valuable-seeming object.
As a standard action that provokes attacks of opportunity, the hoaxer can use 1 round of bardic
performance to invest a single object in his possession with a hex he knows. This object must be
light enough to hold in one hand, and cannot already have any magical properties. The object remains
hexed as long as the hoaxer continues to spend 1 round of bardic performance each round as a swift
action to maintain it, until the hoaxer drops the item, or until triggered. The hex triggers
immediately upon being willingly accepted by another creature, targeting its new owner. A bad deal
cannot be forced on a creature or slipped into its possession without its knowledge, but a hoaxer
can lie or cheat to convince his mark to accept the object, or use spells like
_[beguiling gift](ref/spell/beguiling-gift)_.

At 1st level, the hoaxer knows one [witch](ref/class/witch) hex from the following list:
[blight](ref/hex/blight), [charm](ref/hex/charm), [evil eye](ref/hex/evil-eye),
[fortune](ref/hex/fortune), [healing](ref/hex/healing), [misfortune](ref/hex/misfortune),
[slumber](ref/hex/slumber), or [unnerve beasts](ref/hex/unnerve-beasts). At 3rd level and every 3
bard levels thereafter, he can learn one additional hex. The save DC for a hoaxer's hexes is equal
to 10 + 1/2 the hoaxer's bard level + his Charisma modifier. These hexes function identically to
witch hexes, except they can only target single creatures, and the hoaxer can only use his hexes by
investing them into objects. If the hoaxer learns hexes from any other source (such as the witch
class), he cannot invoke them into an object.

Beginning at 12th level, the hoaxer adds the following major hexes to the list of hexes he can
learn: [agony](ref/hex/agony), [hoarfrost](ref/hex/hoarfrost), [ice tomb](ref/hex/ice-tomb),
[infected wounds](ref/hex/infected-wounds), [nightmares](ref/hex/nightmares),
[retribution](ref/hex/retribution), and [speak in dreams](ref/hex/speak-in-dreams). This performance
replaces inspire courage, inspire competence, and inspire greatness.

## Buyer Beware (Su) {#buyer-beware}

As a standard action, a hoaxer can convince someone to accept a gift or trade as per
_[beguiling gift](ref/spell/beguiling-gift)_ (DC = 10 + 1/2 the hoaxer's bard level + his Charisma
modifier) by spending 1 round of bardic performance on a supernatural sales pitch. The hoaxer can
use this ability to convince a creature to accept a hexed object created with his bad deal
performance. This performance replaces countersong.

## Personal Guarantee (Su) {#personal-guarantee}

A hoaxer can prevent his hexed wares from afflicting a target until he is safely out of sight. He
can spend up to 1 round of bardic performance per bard level while hexing an object. For every round
expended, the object's hex is delayed for 1 minute before triggering and hexing its current owner.
This performance replaces distraction.

## Curse Breaker (Su) {#curse-breaker}

A hoaxer of 12th level or higher can use performance to create an effect equal to
_[break enchantment](ref/spell/break-enchantment)_. This otherwise functions as
[soothing performance](ref/performance/soothing-performance). This performance replaces inspire
greatness.

## Misery (Ex) {#misery}

At 2nd level, a hoaxer learns to take joy in the misfortune of others. He gains a +1 morale bonus on
attack rolls and damage rolls against creatures suffering from a curse, hex, or harmful
mind-affecting effect, as well as a +1 morale bonus on Will saving throws against spells from such
creatures. These bonuses increase by 1 at 5th level and every 6 bard levels thereafter. This ability
replaces versatile performance.

## Versed in Curses (Ex) {#versed-in-curses}

At 2nd level, a hoaxer gains a +4 bonus on saving throws against curses, hexes, and
language-dependent effects. This ability replaces well-versed.

## Curse Crafter (Ex) {#curse-crafter}

At 5th level, a hoaxer learns how to craft cursed items. He gains one item creation feat as a bonus
feat at 5th level, plus an additional item creation feat every 6 levels thereafter. He can use these
feats only to craft cursed items. In addition, he can craft items that appear magical but have no
true magical properties—as if permanently affected by the _[magic aura](ref/spell/magic-aura)_
spell—for 50 gp. This ability replaces lore master.
