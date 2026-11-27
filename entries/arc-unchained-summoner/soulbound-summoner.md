+++
id = "ref/arc-unchained-summoner/soulbound-summoner"
kind = "archetype"
title = "Soulbound Summoner"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20%28Unchained%29%20Soulbound%20Summoner"
source_ids = ["pathfinder-144-midwives-to-death"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulbound_summoner", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "pathfinder-144-midwives-to-death"
page = "82"

[fields]
kind = "archetype"
features = [
  { anchor = "pactbond-curse", level = 1 },
  { anchor = "soulbound-life-link", level = 1 },
  { anchor = "weakened-summoning", level = 1 },
  { anchor = "soulbound-evolution", level = 3 },
]
trades = [
  { alters = "Eidolon", feature = "eidolon", by = ["pactbond-curse"] },
  { alters = "Life link", feature = "life-link", by = ["soulbound-life-link"] },
  { replaces = "Summon monster spell-like ability", feature = "summon-monster-i", by = ["weakened-summoning"] },
  { replaces = "Gate spell-like ability", by = ["weakened-summoning"] },
]
+++

Not everyone who becomes a summoner is an intentional dabbler in the arcane arts. Soulbound
summoners, as a rule, never set out to bind their soul to a dangerous and enigmatic power. Rather,
they have found themselves unintentional masters of eidolons through incredible circumstances. Most
common are those who forged their pacts with an outsider out of a mutual desire for
self-preservation. Other soulbound summoners never contacted a true outsider at all, instead
manifesting an eidolon from their minds in response to mental or magical trauma. The events that
create such a summoner result in the eidolon fusing entirely to the summoner's psyche. These
accidental summoners lack the practiced skill at reaching across planes that most summoners have,
but their intense bond with their eidolon grants both summoner and outsider unusual power.

## Pactbond Curse (Ex) {#pactbond-curse}

A soulbound summoner's metaphysical connection with his eidolon has profound effects on both of
them. The eidolon's alignment always matches that of the soulbound summoner, regardless of its
subtype. In addition, at 1st level, the summoner must choose an oracle curse (_Advanced Player's
Guide_ 43), using his summoner level as his oracle level for determining the curse's effects. Once
this choice is made, it cannot be changed. A summoner that gains spells for his list of spells known
as a result of his curse must be able to cast spells of the appropriate level in order to cast the
learned spell.

The glowing rune that the soulbound summoner shares with his eidolon always appears on a place
symbolic of his pactbond curse. For example, a summoner who chooses the
[clouded vision](ref/oraclecurse/clouded-vision) curse might have his summoner's rune manifest on
one of his eyes, while a summoner who chooses the [tongues](ref/oraclecurse/tongues) curse might
have his summoner's rune appear on his lips. A soulbound summoner's eidolon is summoned from his own
psyche rather than a different plane, so spells such as _[banishment](ref/spell/banishment)_ and
_[dismissal](ref/spell/dismissal)_ do not work when cast on the eidolon.

This alters the eidolon class feature.

## Soulbound Life Link (Su) {#soulbound-life-link}

The essence of a soulbound summoner's eidolon resides within the summoner's mind and soul instead of
a home plane, and he can use this connection to restore his eidolon with his own vitality. The
summoner can use his life link ability to sacrifice any number of his hit points without using an
action. Each hit point sacrificed in this way heals the eidolon for 1 point of damage. The soulbound
summoner can use this ability even after the eidolon has been killed and sent back to its summoner's
mind; if the eidolon is healed enough that its hit point total is above 0, it can be summoned again
as normal.

This alters life link.

## Weakened Summoning {#weakened-summoning}

A soulbound summoner's eidolon is usually the result of unintended magic, trauma, or a singular
pact, instead of rigorous arcane study. Soulbound summoners do not gain the ability to cast the
_[summon monster](ref/spell/summon-monster)_ or _[gate](ref/spell/gate)_ spells as a
[spell-like ability](ref/umr/spell-like-abilities).

## Soulbound Evolution {#soulbound-evolution}

A soulbound summoner's eidolon gains power from its unusually strong bond with its summoner. At 3rd
level, and again at 5th, 7th, and 9th level, the eidolon adds 1 point to its evolution pool. At 11th
level, and again at 15th, 17th, and 19th level, the eidolon adds 2 points to its evolution pool. At
7th level, the eidolon can select evolutions even if it does not meet the subtype requirements for
that evolution.

At 13th level, the eidolon can draw from its summoner's power to cast spells. The spell must be a
spell that the summoner knows, and the summoner must expend two spell slots of the same spell level
or higher to allow the eidolon to cast the spell. Expending spell slots in this way does not take an
action. The eidolon uses the summoner's caster level, feats, and casting statistics for all
spellcasting purposes. The eidolon must be able to meet all other requirements for casting the
spell, such as being able to speak for spells requiring verbal components and providing any material
components or focuses for spells that require them. The eidolon must be able to move its body to
cast spells with somatic components, but it does not need to have the
[limbs](ref/unchevolution/limbs) (arms) evolution.
