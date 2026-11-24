+++
id = "ref/arc-cavalier/luring-cavalier"
kind = "archetype"
title = "Luring Cavalier"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Luring%20Cavalier"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "luring_cavalier", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-combat"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "far-challenge" },
  { anchor = "careful-aim", level = 3 },
  { anchor = "infuriating-aim", level = 11 },
  { anchor = "versatile-challenge", level = 12 },
  { anchor = "supreme-aim", level = 20 },
]
trades = [
  { replaces = "Challenge", feature = "challenge", by = ["far-challenge"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["careful-aim"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["infuriating-aim"] },
  { replaces = "Demanding challenge", feature = "demanding-challenge", by = ["versatile-challenge"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["supreme-aim"] },
]
+++

Those who study the perfection of strategy and tactics know that picking the battlefield can grant
advantages that only overwhelming numbers of allies can eclipse. The luring cavalier is a special
type of cavalier that helps accomplish that goal. Typically, he uses a bow or other ranged weapon to
lure opponents toward him, and then makes strategic retreats to position his enemies exactly where
he wants them.

## Far Challenge (Ex) {#far-challenge}

Once per day, a luring cavalier can use his far challenge ability as a swift action. When he does,
the luring cavalier chooses one target within sight to challenge. The luring cavalier's ranged
attacks deal extra damage whenever the attacks are made against the target of his challenge. This
extra damage is equal to the luring cavalier's level. The luring cavalier can use this ability once
per day at 1st level, plus one additional time per day for every three levels beyond 1st, to a
maximum of seven times per day at 19th level. Furthermore, once per day, the luring cavalier may
spend a use of his far challenge ability to double the potential extra damage of his ranged attack.
Before making the attack roll, he can choose to spend a use of his challenge to deal twice his
cavalier level in extra damage on a successful hit instead of just his cavalier level in extra
damage. If the attack misses, the use of the challenge is wasted.

Challenging a foe requires subtle deceits and strategies. The cavalier must make it look like he is
a soft target. The subject of the far challenge gains a +4 bonus on attack rolls made against him.

This challenge remains in effect until the target is dead or unconscious, until the target hits the
luring cavalier with a melee attack, or until the combat ends. If this challenge ends because the
target hits the luring cavalier with a melee attack, this challenge changes to the effects of the
normal cavalier challenge, and gains any order benefit the luring cavalier has. Far challenge
replaces the challenge ability.

## Careful Aim (Ex) {#careful-aim}

At 3rd level, when a luring cavalier makes a ranged attack with his highest base attack bonus, he
can ignore the penalties for firing up to three range increments away. If he is using a firearm, he
can target touch AC up to two range increments away. This effect stacks with effects that allow the
cavalier to make ranged attacks farther without penalty or that allow him to target touch AC with a
firearm beyond the first range increment. This ability replaces cavalier's charge.

## Infuriating Aim (Ex) {#infuriating-aim}

At 11th level, when a luring cavalier confirms a critical hit with a ranged attack made at his
highest base attack bonus against the target of a far challenge, the target becomes infuriated for 1
round. While infuriated, the target must spend its turn moving closer to the cavalier, making move,
[run](ref/rule/run), or [charge](ref/rule/charge) actions only (challenged creature's choice). This
is a mind-affecting effect. This ability replaces mighty charge.

## Versatile Challenge (Ex) {#versatile-challenge}

At 12th level, a luring cavalier can expend a use of his challenge to gain the benefit of far
challenge or the normal cavalier challenge. He can even change the type of challenge an opponent is
under the effects of as a swift action, as long as the target of the challenge is within line of
sight. This ability replaces demanding challenge.

## Supreme Aim (Ex) {#supreme-aim}

At 20th level, the luring cavalier gains the careful aim bonus and the effect of infuriating aim on
all ranged attacks. This ability replaces supreme charge.
