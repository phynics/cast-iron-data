+++
id = "ref/sorcbloodline/arcane"
kind = "class_option"
title = "Arcane"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane", path = "json/class_ability_sorcerer_bloodlines.json" },
]
[[sources]]
publication = "core-rulebook"
page = "73"
[[sources]]
publication = "ultimate-magic"
page = "72"

[fields]
kind = "class_option"
group = "sorcerer-bloodline"
features = [
  { anchor = "bloodline-arcana" },
  { anchor = "arcane-bond", level = 1 },
  { anchor = "metamagic-adept", level = 3 },
  { anchor = "new-arcana", level = 9 },
  { anchor = "school-power", level = 15 },
  { anchor = "arcane-apotheosis", level = 20 },
]
+++

Your family has always been skilled in the eldritch art of magic. While many of your relatives were
accomplished wizards, your powers developed without the need for study and practice.

**Class Skill:** Knowledge (any one).

**Bonus Spells:** _identify_ (3rd), _invisibility_ (5th), _dispel magic_ (7th), _dimension door_
(9th), _overland flight_ (11th), _true seeing_ (13th), _greater teleport_ (15th), _power word stun_
(17th), _wish_ (19th).

**Bonus Feats:** [Combat Casting](ref/feat/combat-casting),
[Improved Counterspell](ref/feat/improved-counterspell),
[Improved Initiative](ref/feat/improved-initiative), [Iron Will](ref/feat/iron-will),
[Scribe Scroll](ref/feat/scribe-scroll), [Skill Focus](ref/feat/skill-focus) (Knowledge \[arcana\]),
[Spell Focus](ref/feat/spell-focus), [Still Spell](ref/feat/still-spell).

## Bloodline Arcana {#bloodline-arcana}

Whenever you apply a metamagic feat to a spell that increases the slot used by at least one level,
increase the spell's DC by +1. This bonus does not stack with itself and does not apply to spells
modified by the [Heighten Spell](ref/feat/heighten-spell) feat.

### Bloodline Powers

Magic comes naturally to you, but as you gain levels you must take care to prevent the power from
overwhelming you.

## Arcane Bond (Su) {#arcane-bond}

At 1st level, you gain an arcane bond, as a [wizard](ref/class/wizard) equal to your sorcerer level.
Your sorcerer levels stack with any wizard levels you possess when determining the powers of your
familiar or bonded object. This ability does not allow you to have both a familiar and a bonded
item. Rules for arcane bonds appear on page 78. Once per day, your bonded item allows you to cast
any one of your spells known (unlike a wizard's bonded item, which allows him to cast any one spell
in his spellbook).

## Metamagic Adept (Ex) {#metamagic-adept}

At 3rd level, you can apply any one metamagic feat you know to a spell you are about to cast without
increasing the casting time. You must still expend a higher-level spell slot to cast this spell. You
can use this ability once per day at 3rd level and one additional time per day for every four
sorcerer levels you possess beyond 3rd, up to five times per day at 19th level. At 20th level, this
ability is replaced by arcane apotheosis.

## New Arcana (Ex) {#new-arcana}

At 9th level, you can add any one spell from the sorcerer/wizard spell list to your list of spells
known. This spell must be of a level that you are capable of casting. You can also add one
additional spell at 13th level and 17th level.

## School Power (Ex) {#school-power}

At 15th level, pick one school of magic. The DC for any spells you cast from that school increases
by +2. This bonus stacks with the bonus granted by [Spell Focus](ref/feat/spell-focus).

## Arcane Apotheosis (Ex) {#arcane-apotheosis}

At 20th level, your body surges with arcane power. You can add any metamagic feats that you know to
your spells without increasing their casting time, although you must still expend higher-level spell
slots. Whenever you use magic items that require charges, you can instead expend spell slots to
power the item. For every three levels of spell slots that you expend, you consume one less charge
when using a magic item that expends charges.

## Sage {#sec-sage-wildblooded-mutation}

Scholars of the arcane are always creating new means to use magic.

**Associated Bloodline:** Arcane.

**Bloodline Arcana:** Unlike most sorcerers, whose innate magic is powered by force of personality,
you use your intellect to understand and master your mystic powers. You use your Intelligence,
rather than your Charisma, to determine all class features and effects relating to your sorcerer
class, such as bonus spells per day, the maximum spell level you can cast, the save DCs of your
spells, and the number of daily uses of your bloodline powers. You gain a +2 bonus on all Knowledge
(arcana) and Spellcraft checks.

**Bloodline Powers:** Your preferred focus is a bolt of mind-spun magic.

**Arcane Bolt (Sp):** Starting at 1st level, you can unleash a ray of magic force as a standard
action, targeting any foe within 30 feet as a ranged touch attack. This ray deals 1d4 points of
damage + 1 for every two sorcerer levels you possess. This damage is treated as a spell of a level
equal to [half](ref/misc/fractions-and-rounding) your sorcerer level, and is a force effect. You can
use this ability a number of times per day equal to 3 + your Charisma modifier. This bloodline power
replaces arcane bond.
