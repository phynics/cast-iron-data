+++
id = "ref/arc-brawler/winding-path-renegade"
kind = "archetype"
title = "Winding Path Renegade"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Winding%20Path%20Renegade"
source_ids = ["adventurers-guide", "advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "winding_path_renegade", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "adventurers-guide"
page = "105"
[[sources]]
publication = "advanced-class-origins"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "school-focus", level = 2 },
  { anchor = "monk-moves", level = 4 },
]
trades = [
  { replaces = "Bonus feats gained at 2nd, 8th, and 14th levels", feature = "bonus-combat-feats", levels = [2, 8, 14], by = ["school-focus"] },
  { replaces = "AC bonus", feature = "ac-bonus", by = ["monk-moves"] },
]
+++

In the sacred text _Unbinding the Fetters_, Irori teaches that the path to transcendence can be
straight or twisted. Those who follow the straight path adhere to the traditions and techniques
perfected by others who have traveled before them, while those who seek the twisted path abandon
tradition and follow their own unique routes to self-perfection. Both paths can lead to the same
place, but those who follow the twisted path must take care to not lose their way.

Winding path renegades epitomize those who have chosen the twisted path. These brawlers initially
studied at the [Houses of Perfection](ref/rule/aff-monasteries) in Jalmeray, but while they grasped
the mechanical aspects of the forms, they lacked the mental discipline required by the masters of
the school. Thus, they have withdrawn from their monasteries—some peacefully, some not—to find their
own paths.

## School Focus (Ex) {#school-focus}

At 2nd level, a winding path renegade continues the training she left behind, gaining the benefits
of the mystery taught at her old monastery. As the winding path renegade progresses in her
self-guided training, she gains a deeper understanding of her chosen monastery's mystery, which
grants her new powers.

### Mystery of Unblinking Flame (Su) {#mystery-of-unblinking-flame}

At 2nd level, the winding path renegade increases her speed by 10 feet (this is treated as an
enhancement bonus). If she uses her monk moves class ability to gain fast movement, the abilities
stack with each other. At 8th level, if the winding path renegade begins her turn with the
[grappled](ref/rule/grapple-conditions) condition, she can deal 2d6 points of fire damage to all
other creatures in the grapple as a free action. At 14th level, the winding path renegade becomes as
difficult to contain as a flame. Once per day as a full-round action, she can transform into liquid
flame, instantly escaping all bonds as if under the effect of
_[freedom of movement](ref/spell/freedom-of-movement)_ and moving up to her speed. When moving as
part of this ability, she can move through creatures' squares freely and doesn't provoke attacks of
opportunity. She deals 10d6 points of fire damage to any creature whose square she enters during
this movement. A successful Reflex saving throw (DC = 10 + [half](ref/misc/fractions-and-rounding)
her brawler level + her Dexterity bonus) halves this damage.

### Mystery of Unfolding Wind (Su) {#mystery-of-unfolding-wind}

At 2nd level, the winding path renegade adds 10 to the range increments of ranged weapons she wields
and gains [Deflect Arrows](ref/feat/deflect-arrows) as a bonus feat. At 8th level, she can harness
the power of the wind to make enormous leaps. As a move action, she can leap without attempting an
Acrobatics check, jumping any distance up to her speed (upward movement counts as double, as when
flying). She can leap in this way a number of times per day equal to her class level. At 14th level,
when using the Deflect Arrows feat, the winding path renegade can send one projectile back at her
attacker, using the same attack roll and damage roll the attacker rolled against her. Even if the
deflected attack had more than one projectile (as with [Manyshot](ref/feat/manyshot)), the winding
path renegade sends only one projectile back at the attacker. The others are deflected as normal.

### Mystery of Untwisting Iron (Su) {#mystery-of-untwisting-iron}

At 2nd level, metal weapons and armor in the winding path renegade's possession are treated as
[masterwork](ref/rule/masterwork-weapons) unless they have the [broken](ref/misc/broken) condition.
At 8th level, the winding path renegade gains a bonus equal to half her level on Craft checks
involving metal, and she gains the benefits of the [Master Craftsman](ref/feat/master-craftsman) and
Craft Arms and Armor feats when crafting items made of metal. At 14th level, any weapon the winding
path renegade wields is treated as [adamantine](ref/eq-material/adamantine).

This ability replaces the bonus feats gained at 2nd, 8th, and 14th levels.

## Monk Moves (Ex) {#monk-moves}

At 4th level, a winding path renegade can use her martial flexibility ability to gain the benefits
of certain monk abilities as well as combat feats. Each ability counts as one combat feat for this
purpose, and the winding path renegade is treated as a monk of a level equal to her brawler level
for the purpose of determining the effects of these abilities. The winding path renegade gains
access to these abilities at the levels listed on the Monk Moves table above. She does not gain a ki
pool, and she can't use powers that require ki. The winding path renegade must be wearing light or
no armor to benefit from this ability.

This ability replaces AC bonus.

### Monk Moves {#monk-moves-table}

|Monk Ability|Level Gained|
| --- | --- |
|[Evasion](ref/ability/evasion)|4th|
|Fast movement|4th|
|Slow fall|4th|
|High jump|5th|
|[Improved evasion](ref/ability/improved-evasion)|9th|
