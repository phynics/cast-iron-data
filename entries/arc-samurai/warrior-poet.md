+++
id = "ref/arc-samurai/warrior-poet"
kind = "archetype"
title = "Warrior Poet"
aon = "ArchetypeDisplay.aspx?FixedName=Samurai%20Warrior%20Poet"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warrior_poet", path = "json/archetypes_samurai.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/samurai" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "dancer-s-grace" },
  { anchor = "flourish", level = 1 },
  { anchor = "graceful-warrior" },
  { anchor = "skirmisher-s-challenge", level = 1 },
  { anchor = "graceful-strike", level = 4 },
  { anchor = "battle-dance", level = 6 },
]
trades = [
  { replaces = "Proficiency with medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["dancer-s-grace"] },
  { replaces = "heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor", by = ["dancer-s-grace"] },
  { replaces = "and shields", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["dancer-s-grace"] },
  { replaces = "Mount", feature = "mount", by = ["flourish"] },
  { replaces = "weapon expertise", feature = "weapon-expertise", by = ["flourish"] },
  { replaces = "banner", feature = "banner", by = ["flourish"] },
  { replaces = "greater banner", feature = "greater-banner", by = ["flourish"] },
  { replaces = "Mounted archer", feature = "mounted-archer", by = ["graceful-strike"] },
  { replaces = "demanding challenge", feature = "demanding-challenge", by = ["graceful-strike"] },
  { replaces = "Bonus combat feats", feature = "bonus-feat", by = ["battle-dance"] },
  { alters = "Challenge", feature = "challenge", by = ["skirmisher-s-challenge"] },
]
+++

Warrior poets often study calligraphy, flower arrangement, poetry, and other courtly arts, but when
called to battle, they treat combat as its own art form, fighting with beauty and grace. While these
traditions first arose among the Jininese elves and are still extremely common in Jinin, the warrior
poet's art has spread to different nations and peoples in Tian Xia over centuries.

## Dancer's Grace (Ex) {#dancer-s-grace}

When wearing no armor and not using a shield, the warrior poet gains a bonus to Armor Class equal to
her Charisma bonus (to a maximum of her samurai level). A warrior poet loses this bonus while
[flat-footed](ref/rule/flat-footed) or otherwise denied her Dexterity bonus.

This replaces the samurai's proficiency with medium armor, heavy armor, and shields.

## Flourish (Ex) {#flourish}

The warrior poet is skilled at performing elegant moves in battle. At 1st level, the warrior poet
gains a flourish of her choice from the list below. She gains another flourish at 3rd, 5th, 9th,
13th, 17th, and 20th levels.

### Chrysanthemum's Blooming {#chrysanthemum-s-blooming}

The warrior poet gains [Vital Strike](ref/feat/vital-strike) as a bonus feat and can apply its
benefit when using [Spring Attack](ref/feat/spring-attack). If the warrior poet is at least 16th
level and has [Improved Vital Strike](ref/feat/improved-vital-strike), she can apply that feat's
benefit instead. The warrior poet must be at least 11th level to select this flourish.

### Exodus of Jinin {#exodus-of-jinin}

As long as the warrior poet is wearing light or no armor and carrying no more than a light load, her
land speed increases by 10 feet. A warrior poet can select this flourish up to three times.

### Harmony of the Tranquil Garden {#harmony-of-the-tranquil-garden}

The warrior poet can focus her senses as a move action to gain [blindsense](ref/umr/blindsense) out
to 5 feet for 1 round. For every 5 samurai levels she has, the range of this
[blindsense](ref/rule/blindsight-and-blindsense) increases by 5 feet.

### Jininsiel's Guidance {#jininsiel-s-guidance}

The warrior poet gains the rogue's [uncanny dodge](ref/ability/uncanny-dodge) class feature. This
flourish can be selected up to twice; selecting it a second time grants the warrior poet the rogue's
[improved uncanny dodge](ref/ability/improved-uncanny-dodge) class feature. The warrior poet must be
at least 4th level to select this flourish the first time and at least 8th level to select this
flourish the second time.

### Kitsune's Mystique {#kitsune-s-mystique}

The warrior poet gains [Improved Feint](ref/feat/improved-feint) as a bonus feat, ignoring its
prerequisites. When the warrior poet uses Spring Attack or takes a move action to move, she can
attempt to feint against one creature she threatens during her movement as part of her movement.

### Petals on the Wind {#petals-on-the-wind}

Whenever a foe provokes an attack of opportunity from the warrior poet, she can move 5 feet before
making the attack of opportunity. This movement does not provoke attacks of opportunity. If the
warrior poet takes an action to move during her next turn, she subtracts 5 feet from her total
movement for each time she has used this ability since her last turn.

### Wrath of the Heavens {#wrath-of-the-heavens}

The warrior poet gains [Shot on the Run](ref/feat/shot-on-the-run) as a bonus feat, ignoring its
prerequisites.

This replaces mount, weapon expertise, banner, and greater banner.

## Graceful Warrior (Ex) {#graceful-warrior}

The warrior poet gains [Weapon Finesse](ref/feat/weapon-finesse) as a bonus feat and can apply its
benefits to [glaives](ref/eq-weapon/glaive), [katanas](ref/eq-weapon/katana), and
[naginatas](ref/eq-weapon/naginata) as if they were light weapons. This does not alter the weapons'
properties for the purposes of any other effects.

## Skirmisher's Challenge (Ex) {#skirmisher-s-challenge}

The warrior poet adds her samurai level to her damage rolls only on her first successful attack
against a challenged target each round.

This modifies challenge.

## Graceful Strike (Ex) {#graceful-strike}

At 4th level, when the warrior poet uses Weapon Finesse to make a melee attack that adds her
Dexterity bonus to attack rolls and her Strength bonus to damage rolls, she also adds half her
samurai level to damage rolls.

This replaces mounted archer and demanding challenge.

## Battle Dance (Ex) {#battle-dance}

At 6th level, the warrior poet gains Spring Attack as a bonus feat. At 12th level, she gains
[Improved Spring Attack](ref/feat/improved-spring-attack) as a bonus feat, and at 18th level, she
gains [Greater Spring Attack](ref/feat/greater-spring-attack) as a bonus feat. The warrior poet does
not need to meet the prerequisites for these feats.

This replaces the samurai's bonus combat feats.
