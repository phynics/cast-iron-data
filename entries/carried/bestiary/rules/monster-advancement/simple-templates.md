+++
id = "ref/carried/bestiary/rules/monster-advancement/simple-templates"
kind = "rule"
title = "Simple Templates"
source_ids = ["bestiary"]
section = ["Rules", "Monster Advancement"]
parent = "ref/rule/monster-advancement"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Rules/Monster Advancement/Simple Templates", path = "bestiary/rules/monster_advancement.json" },
]

[fields]
kind = "none"
+++

Simple templates can be applied during the game with minimal effort. This makes it easy, for
example, to deal with celestial and fiendish creatures conjured in the heat of battle by
_[summon monster](ref/spell/summon-monster)_ spells.

All simple templates have two categories of changes. The “quick rules” present a fast way to modify
die rolls made in play to simulate the template's effects without actually rebuilding the stat
block—this method works well for summoned creatures. The “rebuild rules” list the exact changes you
make to the base stat block if you have the time to completely rebuild it—this method works best
when you have time during game preparation to build full stat blocks. The two methods result in
creatures of similar, if not identical, abilities. In some cases, a complete rebuild does unusual
things to a creature. For example, the advanced creature template gives and animal too much
Intelligence, and a young incorporeal creature is tougher than a normal one.

## Advanced Creature {#advanced-creature}

::: statblock
Abbrev: CR +1
:::

Creatures with the advanced template are fiercer and more powerful than their ordinary cousins.

### Challenge Rating {#challenge-rating}

As base creature +1

### Quick Rules {#quick-rules}

+2 on all rolls (including damage rolls) and special ability DCs; +4 to AC and CMD; +2 hp/HD.

### Rebuild Rules {#rebuild-rules}

**AC** increase natural armor by +2; **Ability Scores** +4 to all ability scores (except Int scores
of 2 or less).

## Celestial Creature {#celestial-creature}

::: statblock
Abbrev: CR +0 or +1
:::

Celestial creatures dwell in the higher planes, but can be summoned using spells such as
_[summon monster](ref/spell/summon-monster)_ and _[planar ally](ref/spell/planar-ally)_. A celestial
creature's quick and rebuild rules are the same.

### Challenge Rating {#challenge-rating-2}

A celestial creature's CR increases by +1 only if the base creature has 5 or more HD.

### Rebuild Rules {#rebuild-rules-2}

**Senses** gains [darkvision](ref/rule/darkvision) 60 ft.; **Defensive Abilities** gains DR and
energy resistance as noted on the table; **SR** gains SR equal to new CR +5; **Special Attacks**
smite evil 1/day as a swift action (adds Cha bonus on attack rolls and damage bonus equal to HD
against evil foes; smite persists until the target is dead or the celestial creature rests).

#### Celestial Creature Defenses {#celestial-creature-defenses}

::: table
caption = "Celestial Creature Defenses"
head = [
  [
    { text = "Hit Dice", header = true },
    { text = "Resist Cold, Acid, and Electricity", header = true },
    { text = "DR", header = true },
  ],
]
body = [
  [
    { text = "1–4" },
    { text = "5" },
    { text = "—" },
  ],
  [
    { text = "5–10" },
    { text = "10" },
    { text = "5/evil" },
  ],
  [
    { text = "11+" },
    { text = "15" },
    { text = "10/evil" },
  ],
]
:::

## Entropic Creature {#entropic-creature}

::: statblock
Abbrev: CR +0 or +1
:::

Creatures with the entropic template live in planes where chaos is paramount. They can be summoned
using spells such as _[summon monster](ref/spell/summon-monster)_ and
_[planar ally](ref/spell/planar-ally)_. An entropic creature's quick and rebuild rules are the same.

### Challenge Rating {#challenge-rating-3}

An entropic creature's CR increases by +1 only if the base creature has 5 or more HD.

### Rebuild Rules {#rebuild-rules-3}

**Senses** gains [darkvision](ref/rule/darkvision) 60 ft.; **Defensive Abilities** gains DR and
energy resistance as noted on the table; **SR** gains SR equal to new CR +5; **Special Attacks**
smite law 1/day as a swift action (adds Cha bonus on attack rolls and damage bonus equal to HD
against lawful foes; smite persists until the target is dead or the entropic creature rests).

#### Entropic Creature Defenses {#entropic-creature-defenses}

::: table
caption = "Entropic Creature Defenses"
head = [
  [
    { text = "Hit Dice", header = true },
    { text = "Resist Acid and Fire", header = true },
    { text = "DR", header = true },
  ],
]
body = [
  [
    { text = "1–4" },
    { text = "5" },
    { text = "—" },
  ],
  [
    { text = "5–10" },
    { text = "10" },
    { text = "5/lawful" },
  ],
  [
    { text = "11+" },
    { text = "15" },
    { text = "10/lawful" },
  ],
]
:::

## Fiendish Creature {#fiendish-creature}

::: statblock
Abbrev: CR +0 or +1
:::

Creatures with the fiendish template live in the Lower Planes, such as the Abyss and Hell, but can
be summoned using spells such as _[summon monster](ref/spell/summon-monster)_ and
_[planar ally](ref/spell/planar-ally)_. A fiendish creature's quick and rebuild rules are the same.

### Challenge Rating {#challenge-rating-4}

A fiendish creature's CR increases by +1 only if the base creature has 5 or more HD.

### Rebuild Rules {#rebuild-rules-4}

**Senses** gains [darkvision](ref/rule/darkvision) 60 ft.; **Defensive Abilities** gains DR and
energy resistance as noted on the table; **SR** gains SR equal to new CR +5; **Special Attacks**
smite good 1/day as a swift action (adds Cha bonus on attack rolls and damage bonus equal to HD
against good foes; smite persists until target is dead or the fiendish creature rests).

#### Fiendish Creature Defenses {#fiendish-creature-defenses}

::: table
caption = "Fiendish Creature Defenses"
head = [
  [
    { text = "Hit Dice", header = true },
    { text = "Resist Cold and Fire", header = true },
    { text = "DR", header = true },
  ],
]
body = [
  [
    { text = "1–4" },
    { text = "5" },
    { text = "—" },
  ],
  [
    { text = "5–10" },
    { text = "10" },
    { text = "5/good" },
  ],
  [
    { text = "11+" },
    { text = "15" },
    { text = "10/good" },
  ],
]
:::

## Giant Creature {#giant-creature}

::: statblock
Abbrev: CR +1
:::

Creatures with the giant template are larger and stronger than their normal-sized kin. This template
cannot be applied to creatures that are Colossal.

### Challenge Rating {#challenge-rating-5}

As base creature +1

### Quick Rules {#quick-rules-2}

+2 on all rolls based on Str or Con, +2 hp/HD, –1 penalty on all rolls based on Dex.

### Rebuild Rules {#rebuild-rules-5}

**Size** increase by one category; **AC** increase natural armor by +3; **Attacks** increase dice
rolled by 1 step; **Ability Scores** +4 size bonus to Str and Con, –2 Dex.

## Resolute Creature {#resolute-creature}

::: statblock
Abbrev: CR +0 or +1
:::

Creatures with the resolute template live in planes where law is paramount. They can be summoned
using spells such as _[summon monster](ref/spell/summon-monster)_ and
_[planar ally](ref/spell/planar-ally)_. A resolute creature's quick and rebuild rules are the same.

### Challenge Rating {#challenge-rating-6}

A resolute creature's CR increases by +1 only if the base creature has 5 or more HD.

### Rebuild Rules {#rebuild-rules-6}

**Senses** gains [darkvision](ref/rule/darkvision) 60 ft.; **Defensive Abilities** gains DR and
energy resistance as noted on the table; **SR** gains SR equal to new CR +5; **Special Attacks**
smite chaos 1/day as a swift action (adds Cha bonus on attack rolls and damage bonus equal to HD
against chaotic foes; smite persists until target is dead or the resolute creature rests).

#### Resolute Creature Defenses {#resolute-creature-defenses}

::: table
caption = "Resolute Creature Defenses"
head = [
  [
    { text = "Hit Dice", header = true },
    { text = "Resist Acid, Cold and Fire", header = true },
    { text = "DR", header = true },
  ],
]
body = [
  [
    { text = "1–4" },
    { text = "5" },
    { text = "—" },
  ],
  [
    { text = "5–10" },
    { text = "10" },
    { text = "5/chaotic" },
  ],
  [
    { text = "11+" },
    { text = "15" },
    { text = "10/chaotic" },
  ],
]
:::

## Young Creature {#young-creature}

::: statblock
Abbrev: CR -1
:::

Creatures with the young template are immature specimens of the base creature. You can also use this
simple template to easily create a smaller variant of a monster. This template cannot be applied to
creatures that increase in power through aging or feeding (such as dragons or barghests) or
creatures that are Fine-sized.

### Challenge Rating {#challenge-rating-7}

As base creature -1

### Quick Rules {#quick-rules-3}

+2 on all Dex-based rolls, –2 on all other rolls, –2 hp/HD.

### Rebuild Rules {#rebuild-rules-7}

**Size** decrease by one category; **AC** reduce natural armor by –2 (minimum +0); **Attacks**
decrease damage dice by 1 step; **Ability Scores** –4 Strength, –4 Con, +4 size bonus to Dex.
