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
features = [
  { anchor = "unassuming", level = 1 },
  { anchor = "inattention-blindness", level = 1 },
  { anchor = "null-aura", level = 4 },
  { anchor = "evasive", level = 3 },
  { anchor = "tenuous-threat", level = 5 },
  { anchor = "hide-in-plain-sight", level = 7 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["inattention-blindness"] },
  { replaces = "poison lore", feature = "poison-lore", by = ["inattention-blindness"] },
  { replaces = "poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["inattention-blindness"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["inattention-blindness"] },
  { replaces = "trap sense", feature = "trap-sense", by = ["inattention-blindness"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["null-aura"] },
  { replaces = "investigator talent gained at 9th level", feature = "investigator-talent", levels = [9], by = ["null-aura"] },
  { replaces = "Investigator talents gained at 3rd and 11th levels", feature = "investigator-talent", levels = [3, 11], by = ["evasive"] },
  { replaces = "Investigator talent gained at 7th level", feature = "investigator-talent", levels = [7], by = ["hide-in-plain-sight"] },
  { alters = "Class skills", by = ["unassuming"] },
  { alters = "inspiration", feature = "inspiration", by = ["unassuming"] },
  { alters = "Studied strike", feature = "studied-strike", by = ["tenuous-threat"] },
  { replaces = "the investigator talent gained at 5th level", feature = "investigator-talent", levels = [5], by = ["tenuous-threat"] },
]
+++

A cipher is a student of nonexistence. He trains himself to remain undetected and ignored in order
to conduct his investigations without opposition or bothersome questions. By staying unseen, a
cipher can follow and observe his quarry; being overlooked in a crowd suits him just fine.

## Unassuming (Ex) {#unassuming}

A cipher relies on subtlety, rather than skills that would draw attention to him. A cipher removes
Bluff, Diplomacy, Intimidate, and Perform from his list of class skills, and he can never use them
with inspiration, regardless of any talents or other abilities he might have. A cipher can use his
inspiration on any Disguise, Escape Artist, Knowledge (local), Sleight of Hand, and Stealth check
without expending a use of inspiration, provided he is trained in the skill, instead of the normal
investigator ability to use inspiration on any Knowledge, Linguistics, or Spellcraft check without
expending a use of inspiration.

This alters the investigator's class skills and inspiration.

## Inattention Blindness (Su) {#inattention-blindness}

At 1st level, a cipher can blind nearby creatures to his presence. A creature who would become aware
of a cipher's presence when the cipher is within 10 feet per cipher level must succeed at a
Perception check against a DC equal to 10 + the cipher's investigator level + his Intelligence
modifier or the creature ignores the investigator as though it had not become aware of his presence.
The cipher can spend a use of inspiration to raise the DC by 1d6. The affected creature continues to
ignore the cipher until he attacks, moves out of range, directly interacts with the creature,
interacts with another creature or object in a way the affected creature notices, or otherwise
specifically draws attention to himself. If the cipher does none of these things, the affected
creature can attempt another Perception check at the same DC for each minute the cipher remains in
range.

A creature that was aware of the cipher's presence prior to being in range of his inattention
blinding ability is unaffected. This is a mind-affecting compulsion effect.

A cipher can affect only one creature with inattention blindness at any given time, plus one
additional creature at 5th level and every 3 investigator levels thereafter, to a maximum of seven
creatures at 19th level. Once a cipher reaches that maximum, he can't affect an additional creature
until he ends the effect for an already affected creature. If multiple creatures enter the range of
inattention blindness simultaneously, they all must attempt Perception checks; the inattention
blindness effect affects the creatures with the lowest Perception check results, in order, until it
reaches the maximum number of creatures it can affect.

The cipher can suppress or activate inattention blindness as a free action, and dismiss its effects
on any affected creature within range as a move action.

This ability replaces trapfinding, poison lore, poison resistance, poison immunity, and trap sense.

## Null Aura (Su, Sp) {#null-aura}

At 4th level, a cipher becomes much harder to notice with divinations. He gains a +4 bonus on saving
throws against divination spells, [spell-like abilities](ref/umr/spell-like-abilities), and effects.

Attempts to locate the cipher with _[scrying](ref/spell/scrying)_ and other spells that share the
knowledge and connection rules with _[scrying](ref/spell/scrying)_ function only if the caster has
firsthand or familiar knowledge of the cipher, or has one of his body parts (not from secondhand
knowledge, possession, or a likeness of the cipher).

If the caster does not meet these conditions, or if the cipher succeeds at a saving throw to negate
such an effect, the spell or effect reveals nothing but darkness as if the target was invalid or did
not exist; unlike normal, even if she is using a spell with a single target, the caster of the
divination effect does not discover that her target succeeded at a saving throw.

At 9th level, a cipher benefits from constant _[nondetection](ref/spell/nondetection)_, requiring
those who wish to use divinations on him to succeed at a caster level check (DC = 15 + his
investigator level).

This ability replaces swift alchemy and the investigator talent gained at 9th level.

## Evasive (Ex) {#evasive}

At 3rd level, a cipher can avoid unusual attacks. He gains the [evasion](ref/ability/evasion)
ability, and at 11th level, he gains the [improved evasion](ref/ability/improved-evasion) ability.

This ability replaces the investigator talents gained at 3rd and 11th levels.

## Tenuous Threat (Su) {#tenuous-threat}

At 5th level, a cipher's opponents tend to forget that he is a threat. The first time each day that
he successfully hits an opponent who is not the target of his studied combat with a melee attack,
the opponent must succeed at a Will save (DC = 10 + 1/2 the cipher's investigator level + his
Intelligence modifier) or be affected by the cipher's studied strike. This is a mind-affecting
effect.

This ability alters studied strike, and replaces the investigator talent gained at 5th level.

## Hide in Plain Sight (Su) {#hide-in-plain-sight}

At 7th level, a cipher can use the Stealth skill to hide even while being observed; as long as his
observer is within range of his inattention blindness ability (even if it is not affected by
inattention blindness), he can hide without anything to actually hide behind.

This ability replaces the investigator talent gained at 7th level.
