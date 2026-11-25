+++
id = "ref/arc-summoner/synthesist"
kind = "archetype"
title = "Synthesist"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Synthesist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "synthesist", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "ultimate-magic"
page = "81"

[fields]
kind = "archetype"
features = [
  { anchor = "fused-eidolon", level = 1 },
  { anchor = "fused-link", level = 1 },
  { anchor = "shielded-meld", level = 4 },
  { anchor = "maker-s-jump", level = 6 },
  { anchor = "greater-shielded-meld", level = 12 },
  { anchor = "split-forms", level = 16 },
]
trades = [
  { replaces = "Eidolon", feature = "eidolon", by = ["fused-eidolon"] },
  { replaces = "bond senses", feature = "bond-senses", by = ["fused-eidolon"] },
  { replaces = "life bond", feature = "life-bond", by = ["fused-eidolon"] },
  { replaces = "Life link", feature = "life-link", by = ["fused-link"] },
  { replaces = "Shield ally", feature = "shield-ally", by = ["shielded-meld"] },
  { replaces = "Maker's call", feature = "maker-s-call", by = ["maker-s-jump"] },
  { replaces = "transposition", feature = "transposition", by = ["maker-s-jump"] },
  { replaces = "Greater shield ally", feature = "greater-shield-ally", by = ["greater-shielded-meld"] },
  { replaces = "Merge forms", feature = "merge-forms", by = ["split-forms"] },
]
+++

Rather than summon an eidolon to serve by his side, the synthesist fuses his eidolon's essence to
his own. Instead of two creatures, the synthesist is a fusion of the summoner and eidolon into a
single being.

## Fused Eidolon {#fused-eidolon}

A synthesist summons the essence of a powerful outsider to meld with his own being. The synthesist
wears the eidolon like translucent, living armor. The eidolon mimics all of the synthesist's
movements, and the synthesist perceives through the eidolon's senses and speaks through its voice,
as the two are now one creature. The synthesist directs all of the eidolon's actions while fused,
perceives through its senses, and speaks through its voice, as the two are now one creature.

While fused with his eidolon, the synthesist uses the eidolon's Strength, Dexterity, and
Constitution, but retains his own Intelligence, Wisdom, and Charisma. The synthesist gains the
eidolon's hit points as [temporary hit points](ref/rule/temporary-hit-points). When these hit points
reach 0, the eidolon is killed and sent back to its home plane. The synthesist uses the eidolon's
base attack bonus, and gains the eidolon's armor and natural armor bonuses and modifiers to ability
scores. The synthesist also gains access to the eidolon's special abilities and the eidolon's
evolutions. The synthesist is still limited to the eidolon's maximum number of natural attacks. The
eidolon has no skills or feats of its own. The eidolon must be at least the same size as the
synthesist. The eidolon must have [limbs](ref/evolution/limbs) for the synthesist to cast spells
with somatic components. The eidolon's temporary hit points can be restored with the
_[rejuvenate eidolon](ref/spell/rejuvenate-eidolon)_ spell.

While fused, the synthesist loses the benefits of his armor. He counts both as his original type and
as an outsider for any effect related to type, whichever is worse for the synthesist. Spells such as
_[banishment](ref/spell/banishment)_ or _[dismissal](ref/spell/dismissal)_ work normally on the
eidolon, but the synthesist is unaffected. Neither the synthesist nor his eidolon can be targeted
separately, as they are fused into one creature. The synthesist and eidolon cannot take separate
actions. While fused with his eidolon, the synthesist can use all of his own abilities and gear,
except for his armor. In all other cases, this ability functions as the summoner's normal eidolon
ability (for example, the synthesist cannot use his _[summon monster](ref/spell/summon-monster)_
ability while the eidolon is present). This ability replaces the class's eidolon ability, bond
senses, and life bond.

The following class abilities function differently for synthesist summoners.

## Fused Link (Su) {#fused-link}

Starting at 1st level, the synthesist forms a close bond with his eidolon. Whenever the temporary
hit points from his eidolon would be reduced to 0, the summoner can, as a free action, sacrifice any
number of his own hit points. Each hit point sacrificed this way prevents 1 point of damage done to
the eidolon (thus preventing the loss of the summoner's temporary hit points), preventing the
eidolon from being killed and sent back to its home plane. This ability replaces life link.

## Shielded Meld (Ex) {#shielded-meld}

At 4th level, whenever the synthesist is fused with his eidolon, he gains a +2 shield bonus to his
Armor Class and a +2 circumstance bonus on his saving throws. This ability replaces shield ally.

## Maker's Jump (Sp) {#maker-s-jump}

At 6th level, whenever the synthesist is fused with his eidolon, the synthesist can cast
_[dimension door](ref/spell/dimension-door)_ as a [spell-like ability](ref/umr/spell-like-abilities)
using his caster level. This ability only affects the fused synthesist and eidolon. The synthesist
can use this ability once per day at 6th level, plus one additional time per day for every six
levels beyond 6th. This ability replaces maker's call and transposition.

## Greater Shielded Meld (Ex) {#greater-shielded-meld}

At 12th level, whenever the synthesist is fused with his eidolon, he gains a +4 shield bonus to his
Armor Class and a +4 circumstance bonus on his saving throws. This ability replaces greater shield
ally.

## Split Forms (Su) {#split-forms}

At 16th level, as a swift action, the synthesist and his fused eidolon can split into two creatures:
the synthesist and the eidolon. Both have the same evolutions. The synthesist emerges in a square
adjacent to the eidolon if possible. All effects and spells currently targeting the fused
synthesist-eidolon affect both the synthesist and the eidolon.

The synthesist can use this ability for a number of rounds per day equal to his summoner level. He
can end this effect at any time as a full-round action. For the duration of this effect, the eidolon
functions as a normal eidolon of the summoner's class level. This ability replaces merge forms.
