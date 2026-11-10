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
replaces = ["Bardic knowledge", "Inspire courage", "inspire competence", "and inspire greatness", "Countersong", "Distraction", "Inspire greatness", "Versatile performance", "Well-versed", "Lore master"]
+++

Hoaxers specialize in creating valuable-looking counterfeits and infusing these false treasures with
dangerous magic to make their marks more vulnerable to future swindles.

**Counterfeiter (Ex)**

**Ability:** A hoaxer adds [half](ref/misc/fractions-and-rounding) his bard level (minimum 1) on all
Appraise, Bluff, and Sleight of Hand checks, as well as on Craft, Knowledge, Linguistics,
Perception, and Profession checks to create or detect a counterfeit or forgery. He can attempt such
skill checks untrained.

**Replaces:** Bardic knowledge

**Bardic Performance (Su)**

**Info:** A hoaxer dedicates his arcane energies to deceiving others rather than to entertaining
them, granting him the following unique performances.

**Bad Deal (Su)**

**Flavor:** A hoaxer can use his performance to coax a bit of luck (good or bad) into a
valuable-seeming object.

**At 1st Level:** The hoaxer knows one witch hex from the following list: [blight](ref/hex/blight),
[charm](ref/hex/charm), [evil eye](ref/hex/evil-eye), [fortune](ref/hex/fortune),
[healing](ref/hex/healing), [misfortune](ref/hex/misfortune), [slumber](ref/hex/slumber), or
[unnerve beasts](ref/hex/unnerve-beasts).

**At 12th Level:** He can learn one additional hex, and the list of hexes grows to include
[agony](ref/hex/agony), [hoarfrost](ref/hex/hoarfrost), [ice tomb](ref/hex/ice-tomb),
[infected wounds](ref/hex/infected-wounds), [nightmares](ref/hex/nightmares),
[retribution](ref/hex/retribution), and [speak in dreams](ref/hex/speak-in-dreams).

**Provokes attack of opportunity:** Yes

**Repeat At:** He can learn one additional hex., 3, 6, 9, 15, 18

**Replaces:** Inspire courage, inspire competence, and inspire greatness

**Special:** A bad deal cannot be forced on a creature or slipped into its possession without its
knowledge, but a hoaxer can lie or cheat to convince his mark to accept the object, or use spells
like _[beguiling gift](ref/spell/beguiling-gift)._ The save DC for a hoaxer's hexes is equal to 10 +
1/2 the hoaxer's bard level + his Charisma modifier. These hexes function identically to witch
hexes, except they can only target single creatures, and the hoaxer can only use his hexes by
investing them into objects. If the hoaxer learns hexes from any other source (such as the
[witch](ref/class/witch) class), he cannot invoke them into an object.

**Standard:** The hoaxer can use 1 round of bardic performance to invest a single object in his
possession with a hex he knows. This object must be light enough to hold in one hand, and cannot
already have any magical properties. The object remains hexed as long as the hoaxer continues to
spend 1 round of bardic performance each round as a **swift action** to maintain it, until the
hoaxer drops the item, or until triggered. The hex triggers immediately upon being willingly
accepted by another creature, targeting its new owner.

**Buyer Beware (Su)**

**Replaces:** Countersong

**Standard:** A hoaxer can convince someone to accept a gift or trade as per
[beguiling gift](ref/spell/beguiling-gift) (DC = 10 + 1/2 the hoaxer's bard level + his Charisma
modifier) by spending 1 round of bardic performance on a supernatural sales pitch. The hoaxer can
use this ability to convince a creature to accept a hexed object created with his bad deal
performance.

**Personal Guarantee (Su)**

**Ability:** A hoaxer can prevent his hexed wares from afflicting a target until he is safely out of
sight. He can spend up to 1 round of bardic performance per bard level while hexing an object. For
every round expended, the object's hex is delayed for 1 minute before triggering and hexing its
current owner.

**Replaces:** Distraction

**Curse Breaker (Su)**

**At 12th Level:** A hoaxer can use performance to create an effect equal to
[break enchantment](ref/spell/break-enchantment). This otherwise functions as
[soothing performance](ref/performance/soothing-performance).

**Replaces:** Inspire greatness

**Misery (Ex)**

**Ability:** He gains a +1 morale bonus on attack rolls and damage rolls against creatures suffering
from a curse, hex, or harmful mind-affecting effect, as well as a +1 morale bonus on Will saving
throws against spells from such creatures.

**Flavor:** A hoaxer learns to take joy in the misfortune of others.

**Gained:** At 2nd Level

**Replaces:** Versatile performance

At 7th level: p!These bonuses +2.

At 13th level: p!These bonuses +3.

At 19th level: p!These bonuses +4.

**Versed in Curses (Ex)**

**Gained:** At 2nd Level

**Passive:** A hoaxer gains a +4 bonus on saving throws against curses, hexes, and
language-dependent effects.

**Replaces:** Well-versed

**Curse Crafter (Ex)**

**Ability:** A hoaxer learns how to craft cursed items. He gains one item creation feat as a bonus
feat.

**Gained:** At 5th Level

**Repeat:** He gains another bonus item creation feat., 11, 6

**Replaces:** Lore master

**Special:** He can use these feats only to craft cursed items. In addition, he can craft items that
appear magical but have no true magical properties - as if permanently affected by the
[magic aura](ref/spell/magic-aura) spell - for 50 gp.
