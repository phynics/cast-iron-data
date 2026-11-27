+++
id = "ref/arc-magus/armored-battlemage"
kind = "archetype"
title = "Armored Battlemage"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Armored%20Battlemage"
source_ids = ["armor-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "armored_battlemage", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "armor-masters-handbook"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "medium-armor", level = 1 },
  { anchor = "arcane-pool", level = 1 },
  { anchor = "armor-training", level = 3 },
  { anchor = "heavy-armor", level = 7 },
  { anchor = "expanded-arcane-pool", level = 14 },
]
trades = [
  { replaces = "Spell combat", feature = "spell-combat", by = ["medium-armor"] },
  { replaces = "Magus arcana gained at 3rd and 18th levels", feature = "magus-arcana", levels = [3, 18], by = ["armor-training"] },
  { replaces = "improved spell combat", feature = "improved-spell-combat", by = ["armor-training"] },
  { replaces = "Greater spell combat", feature = "greater-spell-combat", by = ["expanded-arcane-pool"] },
  { alters = "Medium armor", feature = "medium-armor", by = ["medium-armor"] },
  { alters = "Arcane pool", feature = "arcane-pool", by = ["arcane-pool"] },
  { alters = "Heavy armor", feature = "heavy-armor", by = ["heavy-armor"] },
]
+++

Though it hasn't been at war with its southern neighbor for centuries, Nex continues to train
battlemages at its arcane schools in Ecanus. Many battlemages focus purely on destructive
evocations, but some extend their tactical studies to include use of the tried-and-true protection
of steel. These armored battlemages learn to move and cast spells in even the most restrictive
armors, and have developed new methods to magically enhance their armor. Most armored battlemages
strongly support the Arclords of Nex. Many travel beyond their homelands seeking some method of
contacting the archmage Nex, and hope for some excuse to convince the Council of Three and Nine to
renew hostilities with the nation of Geb.

## Medium Armor (Ex) {#medium-armor}

An armored battlemage gains this ability at 1st level instead of 7th. When wearing medium or heavy
armor, the armored battlemage gains a +4 bonus on [concentration](ref/rule/concentration) checks to
cast defensively. This stacks with the bonus from the [Combat Casting](ref/feat/combat-casting)
feat.

This ability replaces spell combat and alters the medium armor ability.

## Arcane Pool (Su) {#arcane-pool}

An armored battlemage cannot spend points from his arcane pool to enhance weapons. Instead, he can
expend 1 point from his arcane pool as a swift action to grant armor he is wearing a +1 enhancement
bonus for 1 minute. For every 4 magus levels he has beyond 1st, the armor gains another +1
enhancement bonus, to a maximum of +5 at 17th level. These bonuses stack with existing armor
enhancement bonuses to a maximum of +5. Multiple uses of this ability do not stack with themselves.

At 5th level, these bonuses can be used to add any of the following armor special abilities:
_[balanced](ref/magic-enh/balanced)_, _[bitter](ref/magic-enh/bitter)_, _fortification_ (heavy,
light, or medium), _[ghost touch](ref/magic-enh/ghost-touch-armor)_,
_[invulnerability](ref/magic-enh/invulnerability)_, _spell resistance_ (13, 15, 17, or 19), or
_[spell storing](ref/magic-enh/spell-storing-armor)_. Adding these special abilities consumes an
amount of bonus equal to the ability's base price modifier. In addition, the armored battlemage can
grant his armor the _[energy resistance](ref/magic-enh/energy-resistance)_ special ability at the
cost of a +3 bonus or the _[improved energy resistance](ref/magic-enh/energy-resistance-improved)_
special ability at the cost of a +5 bonus. These special abilities are added to any the armor
already has, but duplicates do not stack. If the armor is not magical, at least a +1 enhancement
bonus must be added before any other special abilities can be added. These bonuses and special
abilities are decided when the arcane pool point is spent and cannot be changed until the next time
the armored battlemage uses this ability. These bonuses do not function if the armor is worn by
anyone other than the magus.

An armored battlemage can enhance only one suit of armor in this way at one time. If he uses this
ability again, the first use immediately ends.

This ability alters arcane pool.

## Armor Training (Ex) {#armor-training}

At 3rd level, an armored battlemage gains armor training, as per the [fighter](ref/class/fighter)
ability. At 8th level, he gains armor training 2. At 13th level, he gains armor training 3. At 18th
level, he gains armor training 4.

This ability replaces the magus arcana gained at 3rd and 18th levels, and improved spell combat.

## Heavy Armor (Ex) {#heavy-armor}

An armored battlemage gains this ability at 7th level instead of 13th.

This ability alters heavy armor.

## Expanded Arcane Pool (Su) {#expanded-arcane-pool}

At 14th level, the armored battlemage can grant his armor the _[glamered](ref/magic-enh/glamered)_
special ability at the cost of a +2 bonus, the _[slick](ref/magic-enh/slick)_ or
_[shadow](ref/magic-enh/shadow)_ special ability at the cost of a +3 bonus, and the
_[greater slick](ref/magic-enh/slick-greater)_ or _[greater shadow](ref/magic-enh/shadow-greater)_
special ability at the cost of a +5 bonus when using his arcane pool.

This ability replaces greater spell combat.
