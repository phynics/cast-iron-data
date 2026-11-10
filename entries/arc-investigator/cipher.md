+++
id = "ref/arc-investigator/cipher"
kind = "archetype"
title = "Cipher"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Cipher"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cipher", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "32"

[fields]
kind = "archetype"
replaces = ["Trapfinding", "poison lore", "poison resistance", "poison immunity", "trap sense", "Swift alchemy", "investigator talent gained at 9th level", "Investigator talents gained at 3rd and 11th levels", "Investigator talent gained at 7th level"]
alters = ["Class skills", "inspiration", "Studied strike", "the investigator talent gained at 5th level"]
replaces_features = ["trapfinding", "poison-lore", "poison-resistance", "trap-sense", "swift-alchemy"]
alters_features = ["inspiration", "studied-strike"]
+++

A cipher is a student of nonexistence. He trains himself to remain undetected and ignored in order
to conduct his investigations without opposition or bothersome questions. By staying unseen, a
cipher can follow and observe his quarry; being overlooked in a crowd suits him just fine.

**Unassuming (Ex)**

**Ability:** A cipher can use his _inspiration_ on any Disguise, Escape Artist, Knowledge (local),
Sleight of Hand, and Stealth check without expending a use of _inspiration,_ provided he is trained
in the skill, instead of the normal investigator ability to use _inspiration_ on any Knowledge,
Linguistics, or Spellcraft check without expending a use of _inspiration._

**Alters:** Class skills, inspiration

**Flavor:** A cipher relies on subtlety, rather than skills that would draw attention to him.

**Passive:** A cipher removes Bluff, Diplomacy, Intimidate, and Perform from his list of class
skills, and he can never use them with _inspiration,_ regardless of any talents or other abilities
he might have.

**Inattention Blindness (Su)**

**Action:** Ability

**Flavor:** A cipher can blind nearby creatures to his presence.

**Gained:** At 1st Level

**Replaces:** Trapfinding, poison lore, poison resistance, poison immunity, trap sense

At 5th level: The cipher can now affect 2 creatures at the same time.

At 8th level: The cipher can now &quot&blind&quot& 3 creatures at the same time.

At 11th level: The cipher can now affect 4 creatures at the same time.

At 14th level: The cipher can now &quot&blind&quot& 5 creatures at the same time.

At 17th level: The cipher can now affect 6 creatures at the same time.

At 20th level: The cipher can now &quot&blind&quot& 7 creatures at the same time.

A creature who would become aware of a cipher's presence when the cipher is within 10 feet per
cipher level must succeed at a Perception check against a DC equal to 10 + the cipher's investigator
level + his Intelligence modifier or the creature ignores the investigator as though it had not
become aware of his presence. The cipher can spend a use of _inspiration_ to raise the DC by 1d6.
The affected creature continues to ignore the cipher until he attacks, moves out of range, directly
interacts with the creature, interacts with another creature or object in a way the affected
creature notices, or otherwise specifically draws attention to himself. If the cipher does none of
these things, the affected creature can attempt another Perception check at the same DC for each
minute the cipher remains in range.

A creature that was aware of the cipher's presence prior to being in range of his _inattention
blinding_ ability is unaffected. This is a mind-affecting compulsion effect.

A cipher can affect only one creature with _inattention blindness_ at any given time. Once a cipher
reaches that maximum, he can't affect an additional creature until he ends the effect for an already
affected creature. If multiple creatures enter the range of _inattention blindness_ simultaneously,
they all must attempt Perception checks; the _inattention blindness_ effect affects the creatures
with the lowest Perception check results, in order, until it reaches the maximum number of creatures
it can affect.

The cipher can suppress or activate _inattention blindness_ as a **free action**, and dismiss its
effects on any affected creature within range as a **move action**.

**Null Aura (Su, Sp)**

**Action:** Passive Ability

**At 9th Level:** A cipher benefits from constant [nondetection](ref/spell/nondetection), requiring
those who wish to use divinations on him to succeed at a caster level check (DC = 15 + his
investigator level).

**Gained:** At 4th Level

**Replaces:** Swift alchemy, investigator talent gained at 9th level

A cipher becomes much harder to notice with divinations. He gains a +4 bonus on saving throws
against divination spells, [spell-like abilities](ref/umr/spell-like-abilities), and effects.

Attempts to locate the cipher with [scrying](ref/spell/scrying) and other spells that share the
knowledge and connection rules with _[scrying](ref/spell/scrying)_ function only if the caster has
firsthand or familiar knowledge of the cipher, or has one of his body parts (not from secondhand
knowledge, possession, or a likeness of the cipher).

If the caster does not meet these conditions, or if the cipher succeeds at a saving throw to negate
such an effect, the spell or effect reveals nothing but darkness as if the target was invalid or did
not exist; unlike normal, even if she is using a spell with a single target, the caster of the
divination effect does not discover that her target succeeded at a saving throw.

**Evasive (Ex)**

**At 11th Level:** He gains the [improved evasion](ref/ability/improved-evasion) ability.

**At 3rd Level:** A cipher can avoid unusual attacks. He gains the [evasion](ref/ability/evasion)
ability.

**Replaces:** Investigator talents gained at 3rd and 11th levels

**Tenuous Threat (Su)**

**Ability:** A cipher's opponents tend to forget that he is a threat. The first time each day that
he successfully hits an opponent who is not the target of his _studied combat_ with a melee attack,
the opponent must succeed at a Will save (DC = 10 + 1/2 the cipher's investigator level + his
Intelligence modifier) or be affected by the cipher's _studied strike._ This is a mind-affecting
effect.

**Alters:** Studied strike, the investigator talent gained at 5th level

**Gained:** At 5th Level

**Hide in Plain Sight (Su)**

**Ability:** A cipher can use the Stealth skill to hide even while being observed; as long as his
observer is within range of his _inattention blindness_ ability (even if it is not affected by
_inattention blindness_), he can hide without anything to actually hide behind.

**Gained:** At 7th Level

**Replaces:** Investigator talent gained at 7th level
