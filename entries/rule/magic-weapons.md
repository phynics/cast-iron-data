+++
id = "ref/rule/magic-weapons"
kind = "rule"
title = "Magic Weapons"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_weapons", path = "json/rules_basics02.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 468

A magic weapon is enhanced to strike more truly and deliver more damage. Magic weapons have
enhancement bonuses ranging from +1 to +5. They apply these bonuses to both attack and damage rolls
when used in combat. All magic weapons are also masterwork weapons, but their masterwork bonuses on
attack rolls do not stack with their enhancement bonuses on attack rolls.

Weapons come in two basic categories: **melee** and **ranged**. Some of the weapons listed as melee
weapons can also be used as ranged weapons. In this case, their enhancement bonuses apply to both
melee and ranged attacks.

Some magic weapons have special abilities. Special abilities count as additional bonuses for
determining the market value of the item, but do not modify attack or damage bonuses except where
specifically noted). A single weapon cannot have a modified bonus (enhancement bonus plus special
ability bonus equivalents, including from character abilities and spells) higher than +10. A weapon
with a special ability must also have at least a +1 enhancement bonus. Weapons cannot possess the
same special ability more than once.

Weapons or ammunition can be made of an unusual material. Roll d%: 01-95 indicates that the item is
of a standard sort, and 96-100 indicates that it is made of a special material.

**Caster Level for Weapons:** The caster level of a weapon with a special ability is given in the
item description. For an item with only an enhancement bonus and no other abilities, the caster
level is three times the enhancement bonus. If an item has both an enhancement bonus and a special
ability, the higher of the two caster level requirements must be met.

**Additional Damage Dice:** Some magic weapons deal additional dice of damage. Unlike other
modifiers to damage, additional dice of damage are not multiplied when the attacker scores a
critical hit.

**Ranged Weapons and Ammunition:** The enhancement bonus from a ranged weapon does not stack with
the enhancement bonus from ammunition. Only the higher of the two enhancement bonuses applies.

Ammunition fired from a projectile weapon with an enhancement bonus of +1 or higher is treated as a
magic weapon for the purpose of overcoming [damage reduction](ref/rule/damage-reduction). Similarly,
ammunition fired from a projectile weapon with an alignment gains the alignment of that projectile
weapon.

**Magic Ammunition and Breakage:** When a magic arrow, crossbow bolt, or sling bullet misses its
target, there is a 50% chance it breaks or is otherwise rendered useless. A magic arrow, bolt, or
bullet that successfully hits a target is automatically destroyed after it delivers its damage.

**Light Generation:** Fully 30% of magic weapons shed light equivalent to a light spell. These
glowing weapons are quite obviously magical. Such a weapon can't be concealed when drawn, nor can
its light be shut off. Some of the specific weapons detailed below always or never glow, as defined
in their descriptions.

**Hardness and Hit Points:** Each +1 of a magic weapon's enhancement bonus adds +2 to its
[hardness](ref/umr/hardness) and +10 to its hit points. See also
[Table 7-12](ref/rule/breaking-things).

**Activation:** Usually a character benefits from a magic weapon in the same way a character
benefits from a mundane weapon: by wielding (attacking with) it. If a weapon has a special ability
that the user needs to activate, then the user usually needs to utter a command word (a standard
action). A character can activate the special abilities of 50 pieces of ammunition at the same time,
assuming each piece has identical abilities.

**Magic Weapons and Critical Hits:** Some weapon special abilities and some specific weapons have an
extra effect on a critical hit. This special effect also functions against creatures not normally
subject to critical hits. On a successful critical roll, apply the special effect, but do not
multiply the weapon's regular damage.

**Weapons for Unusually Sized Creatures:** The cost of weapons for creatures who are neither Small
nor Medium varies. The cost of the masterwork quality and any magical enhancement remains the same.

**Special Qualities:** Roll d%. A 01-30 result indicates that the item sheds light, 31-45 indicates
that something (a design, inscription, or the like) provides a clue to the weapon's function, and
46-100 indicates no special qualities.

### Table 15-8: Weapons

|Minor|Medium|Major|Weapon Bonus|Base Price^[1](ref/rule/magic-weapons#footnote-1)^|
| --- | --- | --- | --- | --- |
|01-70|01-10|-|+1|2,000 gp|
|71-85|11-29|-|+2|8,000 gp|
|-|30-58|01-20|+3|18,000 gp|
|-|59-62|21-38|+4|32,000 gp|
|-|-|39-49|+5|50,000 gp|
|-|-|-|+6^[2](ref/rule/magic-weapons#footnote-2)^|72,000 gp|
|-|-|-|+7^[2](ref/rule/magic-weapons#footnote-2)^|98,000 gp|
|-|-|-|+8^[2](ref/rule/magic-weapons#footnote-2)^|128,000 gp|
|-|-|-|+9^[2](ref/rule/magic-weapons#footnote-2)^|162,000 gp|
|-|-|-|+10^[2](ref/rule/magic-weapons#footnote-2)^|200,000 gp|
|86-90|63-68|50-63|Specific weapon (below)|-|
|92-100|69-100|64-100|Special ability (below) and roll again|-|

_Also see: [Random Weapons (Gamemastery)](ref/rule/random-weapons)_

### Table 15-9: Melee Weapon Special Abilities

|Minor|Medium|Major|Special Ability|\*|Base Price Modifier^[1](ref/rule/magic-weapons#footnote-1)^|
| --- | --- | --- | --- | --- | --- |
|01-10|01-06|01-03|[Bane](ref/magic-enh/bane)||+1 bonus|
|11-17|07-12|-|[Defending](ref/magic-enh/defending)||+1 bonus|
|18-27|13-19|04-06|[Flaming](ref/magic-enh/flaming)||+1 bonus|
|28-37|20-26|07-09|[Frost](ref/magic-enh/frost)||+1 bonus|
|38-47|27-33|10-12|[Shock](ref/magic-enh/shock)||+1 bonus|
|48-56|34-38|13-15|[Ghost touch (weapon)](ref/magic-enh/ghost-touch-weapon)||+1 bonus|
|57-67|39-44|-|[Keen](ref/magic-enh/keen)|^[3](ref/rule/magic-weapons#footnote-4)^|+1 bonus|
|68-71|45-48|16-19|[Ki focus](ref/magic-enh/ki-focus)||+1 bonus|
|72-75|49-50|-|[Merciful](ref/magic-enh/merciful)||+1 bonus|
|76-82|51-54|20-21|[Mighty cleaving](ref/magic-enh/mighty-cleaving)||+1 bonus|
|83-87|55-59|22-24|[Spell storing (weapon)](ref/magic-enh/spell-storing)||+1 bonus|
|88-91|60-63|25-28|[Throwing](ref/magic-enh/throwing)||+1 bonus|
|92-95|64-65|29-32|[Thundering](ref/magic-enh/thundering)||+1 bonus|
|96-99|66-69|33-36|[Vicious](ref/magic-enh/vicious)||+1 bonus|
|-|70-72|37-41|[Anarchic](ref/magic-enh/anarchic)||+2 bonus|
|-|73-75|42-46|[Axiomatic](ref/magic-enh/axiomatic)||+2 bonus|
|-|76-78|47-49|[Disruption](ref/magic-enh/disruption)|^[4](ref/rule/magic-weapons#footnote-5)^|+2 bonus|
|-|79-81|50-54|[Flaming burst](ref/magic-enh/flaming-burst)||+2 bonus|
|-|82-84|55-59|[Icy burst](ref/magic-enh/icy-burst)||+2 bonus|
|-|85-87|60-64|[Holy](ref/magic-enh/holy)||+2 bonus|
|-|88-90|65-69|[Shocking burst](ref/magic-enh/shocking-burst)||+2 bonus|
|-|91-93|70-74|[Unholy](ref/magic-enh/unholy)||+2 bonus|
|-|94-95|75-78|[Wounding](ref/magic-enh/wounding)||+2 bonus|
|-|-|79-83|[Speed](ref/magic-enh/speed)||+3 bonus|
|-|-|84-86|[Brilliant energy](ref/magic-enh/brilliant-energy)||+4 bonus|
|-|-|87-88|[Dancing](ref/magic-enh/dancing)||+4 bonus|
|-|-|89-90|[Vorpal](ref/magic-enh/vorpal)|^[3](ref/rule/magic-weapons#footnote-4)^|+5 bonus|
|100|96-100|91-100|Roll again twice|^[5](ref/rule/magic-weapons#footnote-6)^|-|

### Table 15-10: Ranged Weapon Special Abilities

|Minor|Medium|Major|Special Ability|\*|Base Price Modifier^[6](ref/rule/magic-weapons#footnote-3)^|
| --- | --- | --- | --- | --- | --- |
|01-12|01-08|01-04|[Bane](ref/magic-enh/bane)|^[7](ref/rule/magic-weapons#footnote-7)^|+1 bonus|
|13-25|09-16|05-08|[Distance](ref/magic-enh/distance)||+1 bonus|
|26-40|17-28|09-12|[Flaming](ref/magic-enh/flaming)|^[7](ref/rule/magic-weapons#footnote-7)^|+1 bonus|
|41-55|29-40|13-16|[Frost](ref/magic-enh/frost)|^[7](ref/rule/magic-weapons#footnote-7)^|+1 bonus|
|56-60|41-42|-|[Merciful](ref/magic-enh/merciful)|^[7](ref/rule/magic-weapons#footnote-7)^|+1 bonus|
|61-68|43-47|17-21|[Returning](ref/magic-enh/returning)||+1 bonus|
|69-83|48-59|22-25|[Shock](ref/magic-enh/shock)|^[7](ref/rule/magic-weapons#footnote-7)^|+1 bonus|
|84-93|60-64|26-27|[Seeking](ref/magic-enh/seeking)||+1 bonus|
|94-99|65-68|28-29|[Thundering](ref/magic-enh/thundering)|^[7](ref/rule/magic-weapons#footnote-7)^|+1 bonus|
|-|69-71|30-34|[Anarchic](ref/magic-enh/anarchic)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|72-74|35-39|[Axiomatic](ref/magic-enh/axiomatic)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|75-79|40-49|[Flaming burst](ref/magic-enh/flaming-burst)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|80-82|50-54|[Holy](ref/magic-enh/holy)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|83-87|55-64|[Icy burst](ref/magic-enh/icy-burst)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|88-92|65-74|[Shocking burst](ref/magic-enh/shocking-burst)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|93-95|75-79|[Unholy](ref/magic-enh/unholy)|^[7](ref/rule/magic-weapons#footnote-7)^|+2 bonus|
|-|-|80-84|[Speed](ref/magic-enh/speed)||+3 bonus|
|-|-|85-90|[Brilliant energy](ref/magic-enh/brilliant-energy)||+4 bonus|
|100|96-100|91-100|Roll again twice|^[5](ref/rule/magic-weapons#footnote-6)^|-|

### Table 15–11: Specific Weapons

|Minor|Medium|Major|Specific Weapon|Market Price|
| --- | --- | --- | --- | --- |
|01–15|-|-|[Sleep arrow](ref/magic-weapon/sleep-arrow)|132 gp|
|16–25|-|-|[Screaming bolt](ref/magic-weapon/screaming-bolt)|267 gp|
|26–45|-|-|[Masterwork silver dagger](ref/eq-weapon/masterwork-silver-dagger)|322 gp|
|46–65|-|-|[Cold iron masterwork longsword](ref/eq-weapon/cold-iron-masterwork-longsword)|330 gp|
|66–75|01–09|-|[Javelin of lightning](ref/magic-weapon/javelin-of-lightning)|1,500 gp|
|76–80|10–15|-|[Slaying arrow](ref/magic-weapon/slaying-arrow-normal)|2,282 gp|
|81–90|16–24|-|[Adamantine dagger](ref/eq-weapon/adamantine-dagger)|3,002 gp|
|91–100|25–33|-|[Adamantine battleaxe](ref/eq-weapon/adamantine-battleaxe)|3,010 gp|
|-|34–37|-|[Slaying arrow (greater)](ref/magic-weapon/slaying-arrow-greater)|4,057 gp|
|-|38–40|-|[Shatterspike](ref/magic-weapon/shatterspike)|4,315 gp|
|-|41–46|-|[Dagger of venom](ref/magic-weapon/dagger-of-venom)|8,302 gp|
|-|47–51|-|[Trident of warning](ref/magic-weapon/trident-of-warning)|10,115 gp|
|-|52–57|01–04|[Assassin's dagger](ref/magic-weapon/assassins-dagger)|10,302 gp|
|-|58–62|05–07|[Shifter's sorrow](ref/magic-weapon/shifters-sorrow)|12,780 gp|
|-|63–66|08–09|[Trident of fish command](ref/magic-weapon/trident-of-fish-command)|18,650 gp|
|-|67–74|10–13|[Flame tongue](ref/magic-weapon/flame-tongue)|20,715 gp|
|-|75–79|14–17|[Luck blade (0 wishes)](ref/magic-weapon/luck-blade-0-wishes)|22,060 gp|
|-|80–86|18–24|[Sword of subtlety](ref/magic-weapon/sword-of-subtlety)|22,310 gp|
|-|87–91|25–31|[Sword of the planes](ref/magic-weapon/sword-of-the-planes)|22,315 gp|
|-|92–95|32–37|[Nine lives stealer](ref/magic-weapon/nine-lives-stealer)|23,057 gp|
|-|96–98|38–42|[Oathbow](ref/magic-weapon/oathbow)|25,600 gp|
|-|99–100|43–46|[Sword of life stealing](ref/magic-weapon/sword-of-life-stealing)|25,715 gp|
|-|-|47–51|[Mace of terror](ref/magic-weapon/mace-of-terror)|38,552 gp|
|-|-|52–57|[Life-drinker](ref/magic-weapon/life-drinker)|40,320 gp|
|-|-|58–62|[Sylvan scimitar](ref/magic-weapon/sylvan-scimitar)|47,315 gp|
|-|-|63–67|[Rapier of puncturing](ref/magic-weapon/rapier-of-puncturing)|50,320 gp|
|-|-|68–73|[Sun blade](ref/magic-weapon/sun-blade)|50,335 gp|
|-|-|74–79|[Frost brand](ref/magic-weapon/frost-brand)|54,475 gp|
|-|-|80–84|[Dwarven thrower](ref/magic-weapon/dwarven-thrower)|60,312 gp|
|-|-|85–91|[Luck blade (1 wish)](ref/magic-weapon/luck-blade-1-wish)|62,360 gp|
|-|-|92–95|[Mace of smiting](ref/magic-weapon/mace-of-smiting-normal)|75,312 gp|
|-|-|96–97|[Luck blade (2 wishes)](ref/magic-weapon/luck-blade-2-wishes)|102,660 gp|
|-|-|98–99|[Holy avenger](ref/magic-weapon/holy-avenger)|120,630 gp|
|-|-|100|[Luck blade (3 wishes)](ref/magic-weapon/luck-blade-3-wishes)|142,960 gp|

###### ^1^ {#footnote-1}

For ammunition, this price is for 50 arrows, bolts, or bullets.

###### ^2^ {#footnote-2}

A weapon can't have an enhancement bonus higher than +5. Use these lines to determine price when
special abilities are added in.

###### ^6^ {#footnote-3}

Add to enhancement bonus on Table 15-8 to determine total market price.

###### ^3^ {#footnote-4}

Piercing or slashing weapons only (slashing only for vorpal). Reroll if randomly generated for a
bludgeoning weapon.

###### ^4^ {#footnote-5}

Bludgeoning weapons only. Reroll if randomly generated for a piercing or slashing weapon.

###### ^5^ {#footnote-6}

Reroll if you get a duplicate special ability, an ability incompatible with an ability that you've
already rolled, or if the extra ability puts you over the +10 limit. A weapon's enhancement bonus
and special ability bonus equivalents can't total more than +10.

###### ^7^ {#footnote-7}

Bows, crossbows, and slings crafted with this ability bestow this power upon their ammunition.
