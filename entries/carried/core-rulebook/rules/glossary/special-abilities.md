+++
id = "ref/carried/core-rulebook/rules/glossary/special-abilities"
kind = "rule"
title = "Special Abilities"
source_ids = ["core-rulebook"]
section = ["Rules", "Glossary"]
parent = "ref/carried/core-rulebook/rules/glossary"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Glossary/Special Abilities", path = "core_rulebook/rules/glossary.json" },
]

[fields]
kind = "none"
+++

The following special abilities include rules commonly used by a number of creatures, spells, and
traps.

## Extraordinary Abilities {#extraordinary-abilities}

::: statblock
Abbrev: Ex
:::

Extraordinary abilities are nonmagical. They are, however, not something that just anyone can do or
even learn to do without extensive training. Effects or areas that suppress or negate magic have no
effect on extraordinary abilities.

## Spell-Like Abilities {#spell-like-abilities}

::: statblock
Abbrev: Sp
:::

[Spell-like abilities](ref/umr/spell-like-abilities), as the name implies, are magical abilities
that are very much like spells. Spell-like abilities are subject to
[spell resistance](ref/rule/spell-resistance) and _[dispel magic](ref/spell/dispel-magic)_. They do
not function in areas where magic is suppressed or negated (such as an
_[antimagic field](ref/spell/antimagic-field)_). Spell-like abilities can be dispelled but they
cannot be counterspelled or used to counterspell.

## Supernatural Abilities {#supernatural-abilities}

::: statblock
Abbrev: Su
:::

Supernatural abilities are magical but not spell-like. Supernatural abilities are not subject to
[spell resistance](ref/rule/spell-resistance) and do not function in areas where magic is suppressed
or negated (such as an _[antimagic field](ref/spell/antimagic-field)_). A supernatural ability's
effect cannot be dispelled and is not subject to counterspells. See Table: Special Ability Types for
a summary of the types of special abilities.

### Table: Special Ability Types {#table-special-ability-types}

::: table
caption = "Table: Special Ability Types"
head = [
  [
    { text = "", header = true },
    { text = "Extraordinary", header = true },
    { text = "Spell-Like", header = true },
    { text = "Supernatural", header = true },
  ],
]
body = [
  [
    { text = "Dispel" },
    { text = "No" },
    { text = "Yes" },
    { text = "No" },
  ],
  [
    { text = "[Spell resistance](ref/rule/spell-resistance)" },
    { text = "No" },
    { text = "Yes" },
    { text = "No" },
  ],
  [
    { text = "Antimagic field" },
    { text = "No" },
    { text = "Yes" },
    { text = "Yes" },
  ],
  [
    { text = "Attack of opportunity" },
    { text = "No" },
    { text = "Yes" },
    { text = "No" },
  ],
]
foot = [
  [
    { text = "_Dispel_: Can _[dispel magic](ref/spell/dispel-magic)_ and similar spells dispel the effects of abilities of that type?", colspan = 4 },
  ],
  [
    { text = "_Spell Resistance_: Does [spell resistance](ref/rule/spell-resistance) protect a creature from these abilities?", colspan = 4 },
  ],
  [
    { text = "_Antimagic Field_: Does an _[antimagic field](ref/spell/antimagic-field)_ or similar magic suppress the ability?", colspan = 4 },
  ],
  [
    { text = "_Attack of Opportunity_: Does using the ability provoke attacks of opportunity the way that casting a spell does?", colspan = 4 },
  ],
]
:::

## Ability Score Bonuses {#ability-score-bonuses}

Some spells and abilities increase your ability scores. Ability score increases with a duration of 1
day or less give only temporary bonuses. For every two points of increase to a single ability, apply
a +1 bonus to the skills and statistics listed with the relevant ability.

### Strength {#strength}

Temporary increases to your Strength score give you a bonus on Strength-based skill checks, melee
attack rolls, and weapon damage rolls (if they rely on Strength). The bonus also applies to your
Combat Maneuver Bonus (if you are Small or larger) and to your Combat Maneuver Defense.

### Dexterity {#dexterity}

Temporary increases to your Dexterity score give you a bonus on Dexterity-based skill checks, ranged
attack rolls, initiative checks, and Reflex saving throws. The bonus also applies to your Armor
Class, your Combat Maneuver Bonus (if you are Tiny or smaller), and your Combat Maneuver Defense.

### Constitution {#constitution}

Temporary increases to your Constitution score give you a bonus on your Fortitude saving throws. In
addition, multiply your total Hit Dice by this bonus and add that amount to your current and total
hit points. When the bonus ends, remove this total from your current and total hit points.

### Intelligence {#intelligence}

Temporary increases to your Intelligence score give you a bonus on Intelligence-based skill checks.
This bonus also applies to any spell DCs based on Intelligence.

### Wisdom {#wisdom}

Temporary increases to your Wisdom score give you a bonus on Wisdom-based skill checks and Will
saving throws. This bonus also applies to any spell DCs based on Wisdom.

### Charisma {#charisma}

Temporary increases to your Charisma score give you a bonus on Charisma-based skill checks. This
bonus also applies to any spell DCs based on Charisma and the DC to resist your channeled energy.

### Permanent Bonuses {#permanent-bonuses}

Ability bonuses with a duration greater than 1 day actually increase the relevant ability score
after 24 hours. Modify all skills and statistics related to that ability. This might cause you to
gain skill points, hit points, and other bonuses. These bonuses should be noted separately in case
they are removed.

## Ability Score Damage, Penalty, and Drain {#ability-score-damage-penalty-and-drain}

Diseases, poisons, spells, and other abilities can all deal damage directly to your ability scores.
This damage does not actually reduce an ability, but it does apply a penalty to the skills and
statistics that are based on that ability.

For every 2 points of damage you take to a single ability, apply a –1 penalty to skills and
statistics listed with the relevant ability. If the amount of ability damage you have taken equals
or exceeds your ability score, you immediately fall unconscious until the damage is less than your
ability score. The only exception to this is your Constitution score. If the damage to your
Constitution is equal to or greater than your Constitution score, you die. Unless otherwise noted,
damage to your ability scores is healed at the rate of 1 per day to each ability score that has been
damaged. Ability damage can be healed through the use of spells, such as
_[lesser restoration](ref/spell/restoration-lesser)_.

Some spells and abilities cause you to take an ability penalty for a limited amount of time. While
in effect, these penalties function just like ability damage, but they cannot cause you to fall
unconscious or die. In essence, penalties cannot decrease your ability score to less than 1.

### Strength {#strength-2}

Damage to your Strength score causes you to take penalties on Strength-based skill checks, melee
attack rolls, and weapon damage rolls (if they rely on Strength). The penalty also applies to your
Combat Maneuver Bonus (if you are Small or larger) and your Combat Maneuver Defense.

### Dexterity {#dexterity-2}

Damage to your Dexterity score causes you to take penalties on Dexterity-based skill checks, ranged
attack rolls, initiative checks, and Reflex saving throws. The penalty also applies to your Armor
Class, your Combat Maneuver Bonus (if you are Tiny or smaller), and to your Combat Maneuver Defense.

### Constitution {#constitution-2}

Damage to your Constitution score causes you to take penalties on your Fortitude saving throws. In
addition, multiply your total Hit Dice by this penalty and subtract that amount from your current
and total hit points. Lost hit points are restored when the damage to your Constitution is healed.

### Intelligence {#intelligence-2}

Damage to your Intelligence score causes you to take penalties on Intelligence-based skill checks.
This penalty also applies to any spell DCs based on Intelligence.

### Wisdom {#wisdom-2}

Damage to your Wisdom score causes you to take penalties on Wisdom-based skill checks and Will
saving throws. This penalty also applies to any spell DCs based on Wisdom.

### Charisma {#charisma-2}

Damage to your Charisma score causes you to take penalties on Charisma-based skill checks. This
penalty also applies to any spell DCs based off Charisma and the DC to resist your channeled energy.

### Ability Drain {#ability-drain}

Ability drain actually reduces the relevant ability score. Modify all skills and statistics related
to that ability. This might cause you to lose skill points, hit points, and other bonuses. Ability
drain can be healed through the use of spells such as _[restoration](ref/spell/restoration)_.

## Afflictions {#afflictions}

From curses to poisons to diseases, there are a number of afflictions that can affect a creature.
While each of these afflictions has a different effect, they all function using the same basic
system. All afflictions grant a saving throw when they are contracted. If successful, the creature
does not suffer from the affliction and does not need to make any further rolls. If the saving throw
is a failure, the creature falls victim to the affliction and must deal with its effects.

Afflictions require a creature to make a saving throw after a period of time to avoid taking certain
penalties. With most afflictions, if a number of saving throws are made consecutively, the
affliction is removed and no further saves are necessary. Some afflictions, usually supernatural
ones, cannot be cured through saving throws alone and require the aid of powerful magic to remove.
Each affliction is presented as a short block of information to help you better adjudicate its
results.

### Name {#name}

This is the name of the affliction.

### Type {#type}

This is the type of the affliction, such as curse, disease, or poison. It might also include the
means by which it is contracted, such as contact, ingestion, inhalation, injury, spell, or trap.

### Save {#save}

This gives the type of save necessary to avoid contracting the affliction, as well as the DC of that
save. Unless otherwise noted, this is also the save to avoid the affliction's effects once it is
contracted, as well as the DC of any caster level checks needed to end the affliction through magic,
such as _[remove curse](ref/spell/remove-curse)_ or
_[neutralize poison](ref/spell/neutralize-poison)_.

### Onset {#onset}

Some afflictions have a variable amount of time before they set in. Creatures that come in contact
with an affliction with an onset time must make a saving throw immediately. Success means that the
affliction is avoided and no further saving throws must be made. Failure means that the creature has
contracted the affliction and must begin making additional saves after the onset period has elapsed.
The affliction's effect does not occur until after the onset period has elapsed and then only if
further saving throws are failed.

### Frequency {#frequency}

This is how often the periodic saving throw must be attempted after the affliction has been
contracted (after the onset time, if the affliction has any). While some afflictions last until they
are cured, others end prematurely, even if the character is not cured through other means. If an
affliction ends after a set amount of time, it will be noted in the frequency. For example, a
disease with a frequency of “1/day” lasts until cured, but a poison with a frequency of “1/round for
6 rounds” ends after 6 rounds have passed.

Afflictions without a frequency occur only once, immediately upon contraction (or after the onset
time if one is listed).

### Effect {#effect}

This is the effect that the character suffers each time if he fails his saving throw against the
affliction. Most afflictions cause ability damage or hit point damage. These effects are cumulative,
but they can be cured normally. Other afflictions cause the creature to take penalties or other
effects. These effects are sometimes cumulative, with the rest only affecting the creature if it
failed its most recent save. Some afflictions have different effects after the first save is failed.
These afflictions have an initial effect, which occurs when the first save is failed, and a
secondary effect, when additional saves are failed, as noted in the text. Hit point and ability
score damage caused by an affliction cannot be healed naturally while the affliction persists.

### Cure {#cure}

This tells you how the affliction is cured. Commonly, this is a number of saving throws that must be
made consecutively. Even if the affliction has a limited frequency, it might be cured prematurely if
enough saving throws are made. Hit point damage and ability score damage is not removed when an
affliction is cured. Such damage must be healed normally. Afflictions without a cure entry can only
be cured through powerful spells, such as _[neutralize poison](ref/spell/neutralize-poison)_ and
_[remove curse](ref/spell/remove-curse)_. No matter how many saving throws are made, these
afflictions continue to affect the target.

He failed a DC 15 Fortitude save to avoid contracting it, so after the onset period of 1d3 days has
passed, he must make another DC 15 Fortitude save to avoid taking 1d6 points of Strength damage.
From this point onward, he must make a DC 15 Fortitude save each day (according to the disease's
frequency) to avoid further Strength damage. If, on two consecutive days, he makes his Fortitude
saves, he is cured of the disease and any damage it caused begins to heal as normal.

## Curses {#curses}

Careless rogues plundering a tomb, drunken heroes insulting a powerful wizard, and foolhardy
adventurers who pick up ancient swords all might suffer from curses. These magic afflictions can
have a wide variety of effects, from a simple penalty to certain checks to transforming the victim
into a toad. Some even cause the afflicted to slowly rot away, leaving nothing behind but dust.
Unlike other afflictions, most curses cannot be cured through a number of successful saving throws.
Curses can be cured through magic, however, usually via spells such as
_[remove curse](ref/spell/remove-curse)_ and _[break enchantment](ref/spell/break-enchantment)_.
While some curses cause a progressive deterioration, others inflict a static penalty from the moment
they are contracted, neither fading over time nor growing worse. In addition, there are a number of
magic items that act like curses. See Magic Items for a description of these cursed items.

The following samples present just some of the possibilities when creating curses.

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/curses/baleful-polymorph-spell"
title = "Baleful Polymorph Spell"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/curses/bestow-curse-trap"
title = "Bestow Curse Trap"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/curses/curse-of-the-ages"
title = "Curse of the Ages"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/curses/mummy-rot"
title = "Mummy Rot"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/curses/unluck"
title = "Unluck"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/curses/werewolf-lycanthropy"
title = "Werewolf Lycanthropy"
:::

## Diseases {#diseases}

From a widespread plague to the bite of a dire rat, disease is a serious threat to common folk and
adventurers alike. Diseases rarely have a limited frequency, but most have a lengthy onset time.
This onset time can also be variable. Most diseases can be cured by a number of consecutive saving
throws or by spells such as _[remove disease](ref/spell/remove-disease)_.

The following samples represent just some of the possibilities when creating diseases.

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/blinding-sickness"
title = "Blinding Sickness"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/bubonic-plague"
title = "Bubonic Plague"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/cackle-fever"
title = "Cackle Fever"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/demon-fever"
title = "Demon Fever"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/devil-chills"
title = "Devil Chills"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/filth-fever"
title = "Filth Fever"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/leprosy"
title = "Leprosy"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/mindfire"
title = "Mindfire"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/red-ache"
title = "Red Ache"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/shakes"
title = "Shakes"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/diseases/slimy-doom"
title = "Slimy Doom"
:::

## Poison {#poison}

No other affliction is so prevalent as poison. From the fangs of a viper to the ichor-stained
assassin's blade, poison is a constant threat. Poisons can be cured by successful saving throws and
spells such as _[neutralize poison](ref/spell/neutralize-poison)_.

Contact poisons are contracted the moment someone touches the poison with his bare skin. Such
poisons can be used as injury poisons. Contact poisons usually have an onset time of 1 minute and a
frequency of 1 minute. Ingested poisons are contracted when a creature eats or drinks the poison.
Ingested poisons usually have an onset time of 10 minutes and a frequency of 1 minute. Injury
poisons are primarily contracted through the attacks of certain creatures and through weapons coated
in the toxin. Injury poisons do not usually have an onset time and have a frequency of 1 round.
Inhaled poisons are contracted the moment a creature enters an area containing such poisons. Most
inhaled poisons fill a volume equal to a 10-foot cube per dose. Creatures can attempt to hold their
breaths while inside to avoid inhaling the toxin. Creatures holding their breaths receive a 50%
chance of not having to make a Fortitude save each round. See the rules for holding your breath and
suffocation in Environment. Note that a character that would normally suffocate while attempting to
hold its breath instead begins to breathe normally again.

Unlike other afflictions, multiple doses of the same poison stack. Poisons delivered by injury and
contact cannot inflict more than one dose of poison at a time, but inhaled and ingested poisons can
inflict multiple doses at once. Each additional dose extends the total duration of the poison (as
noted under frequency) by half its total duration. In addition, each dose of poison increases the DC
to resist the poison by +2. This increase is cumulative. Multiple doses do not alter the cure
conditions of the poison, and meeting these conditions ends the affliction for all the doses. For
example, a character is bit three times in the same round by a trio of Medium monstrous spiders,
injecting him with three doses of Medium spider venom. The unfortunate character must make a DC 18
Fortitude save for the next 8 rounds. Fortunately, just one successful save cures the character of
all three doses of the poison.

Applying poison to a weapon or single piece of ammunition is a standard action. Whenever a character
applies or readies a poison for use there is a 5% chance that he exposes himself to the poison and
must save against the poison as normal. This does not consume the dose of poison. Whenever a
character attacks with a poisoned weapon, if the attack roll results in a natural 1, he exposes
himself to the poison. This poison is consumed when the weapon strikes a creature or is touched by
the wielder. Characters with the poison use class feature do not risk accidentally poisoning
themselves.

Poisons can be made using Craft (alchemy). The DC to make a poison is equal to its Fortitude save
DC. Rolling a natural 1 on a Craft skill check while making a poison exposes the crafter to the
poison. Crafters with the poison use class feature do not risk poisoning themselves when using Craft
to make poison.

The following samples represent just some of the possibilities when creating poisons.

### Table: Sample Poisons {#table-sample-poisons}

::: table
caption = "Table: Sample Poisons"
head = [
  [
    { text = "Name", header = true },
    { text = "Type", header = true },
    { text = "Fort DC", header = true },
    { text = "Onset", header = true },
    { text = "Frequency", header = true },
    { text = "Effect", header = true },
    { text = "Cure", header = true },
    { text = "Cost", header = true },
  ],
]
body = [
  [
    { text = "Arsenic" },
    { text = "ingested" },
    { text = "13" },
    { text = "10 min." },
    { text = "1/min. for 4 min." },
    { text = "1d2 Con" },
    { text = "1 save" },
    { text = "120 gp" },
  ],
  [
    { text = "Belladonna" },
    { text = "ingested" },
    { text = "14" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d2 Str, see text" },
    { text = "1 save" },
    { text = "100 gp" },
  ],
  [
    { text = "Black adder venom" },
    { text = "injury" },
    { text = "11" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d2 Con" },
    { text = "1 save" },
    { text = "120 gp" },
  ],
  [
    { text = "Black lotus extract" },
    { text = "contact" },
    { text = "20" },
    { text = "1 min." },
    { text = "1/rd. for 6 rds." },
    { text = "1d6 Con" },
    { text = "2 saves" },
    { text = "4,500 gp" },
  ],
  [
    { text = "Bloodroot" },
    { text = "injury" },
    { text = "12" },
    { text = "1 rd." },
    { text = "1/rd. for 4 rds." },
    { text = "1 Con and 1 Wis" },
    { text = "1 save" },
    { text = "100 gp" },
  ],
  [
    { text = "Blue whinnis" },
    { text = "injury" },
    { text = "14" },
    { text = "—" },
    { text = "1/rd. for 2 rds" },
    { text = "1 Con/unconscious 1d3 hours" },
    { text = "1 save" },
    { text = "120 gp" },
  ],
  [
    { text = "Burnt othur fumes" },
    { text = "inhaled" },
    { text = "18" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1 Con drain/1d3 Con" },
    { text = "2 saves" },
    { text = "2,100 gp" },
  ],
  [
    { text = "Dark reaver powder" },
    { text = "ingested" },
    { text = "18" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Con and 1 Str" },
    { text = "2 saves" },
    { text = "800 gp" },
  ],
  [
    { text = "Deathblade" },
    { text = "injury" },
    { text = "20" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Con" },
    { text = "2 saves" },
    { text = "1,800 gp" },
  ],
  [
    { text = "Dragon bile" },
    { text = "contact" },
    { text = "26" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Str" },
    { text = "—" },
    { text = "1,500 gp" },
  ],
  [
    { text = "Drow poison" },
    { text = "injury" },
    { text = "13" },
    { text = "—" },
    { text = "1/min. for 2 min." },
    { text = "unconscious 1 min./2d4 hours" },
    { text = "1 save" },
    { text = "75 gp" },
  ],
  [
    { text = "Giant wasp poison" },
    { text = "injury" },
    { text = "18" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d2 Dex" },
    { text = "1 save" },
    { text = "210 gp" },
  ],
  [
    { text = "Greenblood oil" },
    { text = "injury" },
    { text = "13" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1 Con" },
    { text = "1 save" },
    { text = "100 gp" },
  ],
  [
    { text = "Green prismatic poison" },
    { text = "spell" },
    { text = "varies" },
    { text = "—" },
    { text = "1/rd." },
    { text = "for 6 rds. Death/1 Con" },
    { text = "2 saves" },
    { text = "—" },
  ],
  [
    { text = "Hemlock" },
    { text = "ingested" },
    { text = "18" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d6 Dex, see text" },
    { text = "2 saves" },
    { text = "2,500 gp" },
  ],
  [
    { text = "Id moss" },
    { text = "ingested" },
    { text = "14" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Int" },
    { text = "1 save" },
    { text = "125 gp" },
  ],
  [
    { text = "Insanity mist" },
    { text = "inhaled" },
    { text = "15" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Wis" },
    { text = "1 save" },
    { text = "1,500 gp" },
  ],
  [
    { text = "King's sleep" },
    { text = "ingested" },
    { text = "19" },
    { text = "1 day" },
    { text = "1/day" },
    { text = "1 Con drain" },
    { text = "2 saves" },
    { text = "5,000 gp" },
  ],
  [
    { text = "Large scorpion venom" },
    { text = "injury" },
    { text = "17" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d2 Str" },
    { text = "1 save" },
    { text = "200 gp" },
  ],
  [
    { text = "Lich dust" },
    { text = "ingested" },
    { text = "17" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Str" },
    { text = "2 saves" },
    { text = "400 gp" },
  ],
  [
    { text = "Malyass root paste" },
    { text = "contact" },
    { text = "16" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d2 Dex" },
    { text = "1 save" },
    { text = "250 gp" },
  ],
  [
    { text = "Medium spider venom" },
    { text = "injury" },
    { text = "14" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1d2 Str" },
    { text = "1 save" },
    { text = "150 gp" },
  ],
  [
    { text = "Nightmare vapor" },
    { text = "inhaled" },
    { text = "20" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1 Wis and confused 1 round" },
    { text = "2 saves" },
    { text = "1,800 gp" },
  ],
  [
    { text = "Nitharit" },
    { text = "contact" },
    { text = "13" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Con" },
    { text = "1 save" },
    { text = "650 gp" },
  ],
  [
    { text = "Oil of taggit" },
    { text = "ingested" },
    { text = "15" },
    { text = "min." },
    { text = "—" },
    { text = "unconscious 1d3 hours" },
    { text = "1 save" },
    { text = "90 gp" },
  ],
  [
    { text = "Purple worm poison" },
    { text = "injury" },
    { text = "24" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d3 Str" },
    { text = "2 saves" },
    { text = "700 gp" },
  ],
  [
    { text = "Sassone leaf residue" },
    { text = "contact" },
    { text = "16" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "2d12 hp/1 Con" },
    { text = "1 save" },
    { text = "300 gp" },
  ],
  [
    { text = "Shadow essence" },
    { text = "injury" },
    { text = "17" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1 Str drain/1d2 Str" },
    { text = "1 save" },
    { text = "250 gp" },
  ],
  [
    { text = "Small centipede poison" },
    { text = "injury" },
    { text = "11" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1 Dex" },
    { text = "save" },
    { text = "90 gp" },
  ],
  [
    { text = "Striped toadstool" },
    { text = "ingested" },
    { text = "11" },
    { text = "10 min." },
    { text = "1/min. for 4 min." },
    { text = "1d3 Wis and 1 Int" },
    { text = "1 save" },
    { text = "180 gp" },
  ],
  [
    { text = "Tears of death" },
    { text = "contact" },
    { text = "22" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d6 Con and paralyzed 1 min." },
    { text = "—" },
    { text = "6,500 gp" },
  ],
  [
    { text = "Terinav root" },
    { text = "contact" },
    { text = "16" },
    { text = "1 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Dex" },
    { text = "1 save" },
    { text = "400 gp" },
  ],
  [
    { text = "Ungol dust" },
    { text = "inhaled" },
    { text = "15" },
    { text = "—" },
    { text = "1/rd. for 4 rds." },
    { text = "1 Cha drain/1d2 Cha" },
    { text = "1 save" },
    { text = "1,000 gp" },
  ],
  [
    { text = "Wolfsbane" },
    { text = "ingested" },
    { text = "16" },
    { text = "10 min." },
    { text = "1/min. for 6 min." },
    { text = "1d3 Con" },
    { text = "1 save" },
    { text = "500 gp" },
  ],
  [
    { text = "Wyvern poison" },
    { text = "injury" },
    { text = "17" },
    { text = "—" },
    { text = "1/rd. for 6 rds." },
    { text = "1d4 Con" },
    { text = "2 saves" },
    { text = "3,000 gp" },
  ],
]
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/arsenic"
title = "Arsenic"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/belladonna"
title = "Belladonna"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/black-adder-venom"
title = "Black Adder Venom"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/black-lotus-extract"
title = "Black Lotus Extract"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/bloodroot"
title = "Bloodroot"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/blue-whinnis"
title = "Blue Whinnis"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/burnt-othur-fumes"
title = "Burnt Othur Fumes"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/dark-reaver-powder"
title = "Dark Reaver Powder"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/deathblade"
title = "Deathblade"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/dragon-bile"
title = "Dragon Bile"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/drow-poison"
title = "Drow Poison"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/giant-wasp-poison"
title = "Giant Wasp Poison"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/greenblood-oil"
title = "Greenblood Oil"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/green-prismatic-poison"
title = "Green Prismatic Poison"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/hemlock"
title = "Hemlock"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/id-moss"
title = "Id Moss"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/insanity-mist"
title = "Insanity Mist"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/kings-sleep"
title = "King's Sleep"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/large-scorpion-venom"
title = "Large Scorpion Venom"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/lich-dust"
title = "Lich Dust"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/malyass-root-paste"
title = "Malyass Root Paste"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/medium-spider-venom"
title = "Medium Spider Venom"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/nightmare-vapor"
title = "Nightmare Vapor"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/nitharit"
title = "Nitharit"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/oil-of-taggit"
title = "Oil of Taggit"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/purple-worm-poison"
title = "Purple Worm Poison"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/sassone-leaf-residue"
title = "Sassone Leaf Residue"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/shadow-essence"
title = "Shadow Essence"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/small-centipede-poison"
title = "Small Centipede Poison"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/striped-toadstool"
title = "Striped Toadstool"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/tears-of-death"
title = "Tears of Death"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/terinav-root"
title = "Terinav Root"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/ungol-dust"
title = "Ungol Dust"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/wolfsbane"
title = "Wolfsbane"
:::

::: entry-link
target = "ref/carried/core-rulebook/rules/glossary/special-abilities/poison/wyvern-poison"
title = "Wyvern Poison"
:::

## Blindsight and Blindsense {#blindsight-and-blindsense}

Some creatures possess [blindsight](ref/rule/blindsight-and-blindsense), the extraordinary ability
to use a nonvisual sense (or a combination senses) to operate effectively without vision. Such
senses may include sensitivity to vibrations, acute scent, keen hearing, or echolocation. This makes
invisibility and concealment (even magical darkness) irrelevant to the creature (though it still
can't see ethereal creatures). This ability operates out to a range specified in the creature
description.

- [Blindsight](ref/rule/blindsight-and-blindsense) never allows a creature to distinguish color or
  visual contrast. A creature cannot read with blindsight.
- [Blindsight](ref/rule/blindsight-and-blindsense) does not subject a creature to gaze attacks (even
  though [darkvision](ref/rule/darkvision) does).
- Blinding attacks do not penalize creatures that use
  [blindsight](ref/rule/blindsight-and-blindsense).
- Deafening attacks thwart [blindsight](ref/rule/blindsight-and-blindsense) if it relies on hearing.
- [Blindsight](ref/rule/blindsight-and-blindsense) works underwater but not in a vacuum.
- [Blindsight](ref/rule/blindsight-and-blindsense) negates displacement and blur effects.

### Blindsense {#blindsense}

Other creatures have [blindsense](ref/rule/blindsight-and-blindsense), a lesser ability that lets
the creature notice things it cannot see, but without the precision of blindsight. The creature with
blindsense usually does not need to make Perception checks to notice and locate creatures within
range of its blindsense ability, provided that it has line of effect to that creature. Any opponent
that cannot be seen has total concealment (50% miss chance) against a creature with blindsense, and
the blindsensing creature still has the normal miss chance when attacking foes that have
concealment. Visibility still affects the movement of a creature with blindsense. A creature with
blindsense is still denied its Dexterity bonus to Armor Class against attacks from creatures it
cannot see.

## Channel Resistance {#channel-resistance}

Creatures with [channel resistance](ref/rule/channel-resistance) gain a bonus on Will saves made
against channeled energy. They add their bonus to any Will saves made to halve the damage and resist
the effect.

## Charm and Compulsion {#charm-and-compulsion}

Many abilities and spells can cloud the minds of characters and monsters, leaving them unable to
tell friend from foe—or worse yet, deceiving them into thinking that their former friends are now
their worst enemies. Two general types of enchantments affect characters and creatures: charms and
compulsions.

Charming another creature gives the charming character the ability to befriend and suggest courses
of action to his minion, but the servitude is not absolute or mindless. Charms of this type include
the various _charm_ spells and some monster abilities. Essentially, a _charmed_ character retains
free will but makes choices according to a skewed view of the world.

- A charmed creature doesn't gain any magical ability to understand his new friend's language.
- A charmed character retains his original alignment and allegiances, generally with the exception
  that he now regards the charming creature as a dear friend and will give great weight to his
  suggestions and directions.
- A charmed character fights his former allies only if they threaten his new friend, and even then
  he uses the least lethal means at his disposal as long as these tactics show any possibility of
  success (just as he would in a fight with an actual friend).
- A charmed character is entitled to an opposed Charisma check against his master in order to resist
  instructions or commands that would make him do something he wouldn't normally do even for a close
  friend. If he succeeds, he decides not to go along with that order but remains charmed.
- A charmed character never obeys a command that is obviously suicidal or grievously harmful to him.
- If the charming creature commands his minion to do something that the influenced character would
  be violently opposed to, the subject may attempt a new saving throw to break free of the influence
  altogether.
- A charmed character who is openly attacked by the creature who charmed him or by that creature's
  apparent allies is automatically freed of the spell or effect.

Compulsion is a different matter altogether. A compulsion overrides the subject's free will in some
way or simply changes the way the subject's mind works. A charm makes the subject a friend of the
caster; a compulsion makes the subject obey the caster.

Regardless of whether a character is charmed or compelled, he does not volunteer information or
tactics that his master doesn't ask for.

## Damage Reduction {#damage-reduction}

Some magic creatures have the supernatural ability to instantly heal damage from weapons or ignore
blows altogether as though they were invulnerable.

The numerical part of a creature's [damage reduction](ref/rule/damage-reduction) (or DR) is the
amount of damage the creature ignores from normal attacks. Usually, a certain type of weapon can
overcome this reduction (see Overcoming DR). This information is separated from the damage reduction
number by a slash. For example, DR 5/magic means that a creature takes 5 less points of damage from
all weapons that are not magic. If a dash follows the slash, then the damage reduction is effective
against any attack that does not ignore damage reduction.

Whenever [damage reduction](ref/rule/damage-reduction) completely negates the damage from an attack,
it also negates most special effects that accompany the attack, such as injury poison, a monk's
stunning, and injury-based disease. Damage reduction does not negate touch attacks, energy damage
dealt along with an attack, or energy drains. Nor does it affect poisons or diseases delivered by
inhalation, ingestion, or contact.

Attacks that deal no damage because of the target's [damage reduction](ref/rule/damage-reduction) do
not disrupt spells.

Spells, [spell-like abilities](ref/umr/spell-like-abilities), and energy attacks (even nonmagical
fire) ignore [damage reduction](ref/rule/damage-reduction).

Sometimes [damage reduction](ref/rule/damage-reduction) represents instant healing. Sometimes it
represents the creature's tough hide or body. In either case, other characters can see that
conventional attacks won't work.

If a creature has [damage reduction](ref/rule/damage-reduction) from more than one source, the two
forms of damage reduction do not stack. Instead, the creature gets the benefit of the best damage
reduction in a given situation.

### Overcoming DR {#overcoming-dr}

[Damage reduction](ref/rule/damage-reduction) may be overcome by special materials, magic weapons
(any weapon with a +1 or higher enhancement bonus, not counting the enhancement from masterwork
quality), certain types of weapons (such as slashing or bludgeoning), and weapons imbued with an
alignment.

Ammunition fired from a projectile weapon with an enhancement bonus of +1 or higher is treated as a
magic weapon for the purpose of overcoming [damage reduction](ref/rule/damage-reduction). Similarly,
ammunition fired from a projectile weapon with an alignment gains the alignment of that projectile
weapon (in addition to any alignment it may already have).

Weapons with an enhancement bonus of +3 or greater can ignore some types of
[damage reduction](ref/rule/damage-reduction), regardless of their actual material or alignment. The
following table shows what type of enhancement bonus is needed to overcome some common types of
damage reduction.

#### DR Type {#dr-type}

::: table
head = [
  [
    { text = "DR Type", header = true },
    { text = "Weapon Enhancement Bonus Equivalent", header = true },
  ],
]
body = [
  [
    { text = "cold iron/silver" },
    { text = "+3" },
  ],
  [
    { text = "adamantine\\*" },
    { text = "+4" },
  ],
  [
    { text = "alignment-based" },
    { text = "+5" },
  ],
]
foot = [
  [
    { text = "\\* Note that this does not give the ability to ignore [hardness](ref/umr/hardness), like an actual adamantine weapon does", colspan = 2 },
  ],
]
:::

## Darkvision {#darkvision}

[Darkvision](ref/rule/darkvision) is the extraordinary ability to see with no light source at all,
out to a range specified for the creature. Darkvision is black-and-white only (colors cannot be
discerned). It does not allow characters to see anything that they could not see otherwise—invisible
objects are still invisible, and illusions are still visible as what they seem to be. Likewise,
darkvision subjects a creature to gaze attacks normally. The presence of light does not spoil
darkvision.

## Death Attacks {#death-attacks}

In most cases, a death attack allows the victim a Fortitude save to avoid the effect, but if the
save fails, the creature takes a large amount of damage, which might cause it to die instantly.

- _[Raise dead](ref/spell/raise-dead) _doesn't work on someone killed by a death attack or effect.
- Death attacks slay instantly. A victim cannot be made stable and thereby kept alive.
- In case it matters, a dead character, no matter how he died, has hit points equal to or less than
  his negative Constitution score.
- The spell _[death ward](ref/spell/death-ward)_ protects against these attacks.

## Energy Drain and Negative Levels {#energy-drain-and-negative-levels}

Some spells and a number of undead creatures have the ability to drain away life and energy; this
dreadful attack results in “negative levels.” These cause a character to take a number of penalties.

For each negative level a creature has, it takes a cumulative –1 penalty on all ability checks,
attack rolls, combat maneuver checks, Combat Maneuver Defense, saving throws, and skill checks. In
addition, the creature reduces its current and total hit points by 5 for each negative level it
possesses. The creature is also treated as one level lower for the purpose of level-dependent
variables (such as spellcasting) for each negative level possessed. Spellcasters do not lose any
prepared spells or slots as a result of negative levels. If a creature's negative levels equal or
exceed its total Hit Dice, it dies.

A creature with temporary negative levels receives a new saving throw to remove the negative level
each day. The DC of this save is the same as the effect that caused the negative levels.

Some abilities and spells (such as _[raise dead](ref/spell/raise-dead)_) bestow permanent level
drain on a creature. These are treated just like temporary negative levels, but they do not allow a
new save each day to remove them. Level drain can be removed through spells like
_[restoration](ref/spell/restoration)_. Permanent negative levels remain after a dead creature is
restored to life. A creature whose permanent negative levels equal its Hit Dice cannot be brought
back to life through spells like _[raise dead](ref/spell/raise-dead)_ and
_[resurrection](ref/spell/resurrection)_ without also receiving a
_[restoration](ref/spell/restoration)_ spell, cast the round after it is restored to life.

## Energy Immunity and Vulnerability {#energy-immunity-and-vulnerability}

A creature with energy immunity never takes damage from that energy type. Vulnerability means the
creature takes half again as much (+50%) damage as normal from that energy type, regardless of
whether a saving throw is allowed or if the save is a success or failure.

## Energy Resistance {#energy-resistance}

A creature with resistance to energy has the ability (usually extraordinary) to ignore some damage
of a certain type per attack, but it does not have total immunity.

Each resistance ability is defined by what energy type it resists and how many points of damage are
resisted. It doesn't matter whether the damage has a mundane or magical source.

When resistance completely negates the damage from an energy attack, the attack does not disrupt a
spell. This resistance does not stack with the resistance that a spell might provide.

## Fear {#fear}

Spells, magic items, and certain monsters can affect characters with fear. In most cases, the
character makes a Will saving throw to resist this effect, and a failed roll means that the
character is shaken, frightened, or panicked.

### Shaken {#shaken}

Characters who are shaken take a –2 penalty on attack rolls, saving throws, skill checks, and
ability checks.

### Frightened {#frightened}

Characters who are frightened are shaken, and in addition they flee from the source of their fear as
quickly as they can. They can choose the paths of their flight. Other than that stipulation, once
they are out of sight (or hearing) of the source of their fear, they can act as they want. If the
duration of their fear continues, however, characters can be forced to flee if the source of their
fear presents itself again. Characters unable to flee can fight (though they are still shaken).

### Panicked {#panicked}

Characters who are panicked are shaken, and they run away from the source of their fear as quickly
as they can, dropping whatever they are holding. Other than running away from the source, their
paths are random. They flee from all other dangers that confront them rather than facing those
dangers. Once they are out of sight (or hearing) of any source of danger, they can act as they want.
Panicked characters cower if they are prevented from fleeing.

### Becoming Even More Fearful {#becoming-even-more-fearful}

Fear effects are cumulative. A shaken character who is made shaken again becomes frightened, and a
shaken character who is made frightened becomes panicked instead. A frightened character who is made
shaken or frightened becomes panicked instead.

## Invisibility {#invisibility}

The ability to move about unseen is not foolproof. While they can't be seen, invisible creatures can
be heard, smelled, or felt.

Invisibility makes a creature undetectable by vision, including [darkvision](ref/rule/darkvision).

Invisibility does not, by itself, make a creature immune to critical hits, but it does make the
creature immune to extra damage from being a ranger's favored enemy and from sneak attacks.

A creature can generally notice the presence of an active invisible creature within 30 feet with a
DC 20 Perception check. The observer gains a hunch that “something's there” but can't see it or
target it accurately with an attack. It's practically impossible (+20 DC) to pinpoint an invisible
creature's location with a Perception check. Even once a character has pinpointed the square that
contains an invisible creature, the creature still benefits from total concealment (50% miss
chance). There are a number of modifiers that can be applied to this DC if the invisible creature is
moving or engaged in a noisy activity.

### Invisible creature is... {#invisible-creature-is}

|Invisible creature is...|Perception|
| --- | --- |
|In combat or speaking|–20|
|Moving at half speed|–5|
|Moving at full speed|–10|
|Running or charging|–20|
|Not moving|+20|
|Using Stealth|Stealth check +20|
|Some distance away|+1 per 10 feet|
|Behind an obstacle (door)|+5|
|Behind an obstacle (stone wall)|+15|

A creature can grope about to find an invisible creature. A character can make a touch attack with
his hands or a weapon into two adjacent 5-foot squares using a standard action. If an invisible
target is in the designated area, there is a 50% miss chance on the touch attack. If successful, the
groping character deals no damage but has successfully pinpointed the invisible creature's current
location. If the invisible creature moves, its location, obviously, is once again unknown.

If an invisible creature strikes a character, the character struck knows the location of the
creature that struck him (until, of course, the invisible creature moves). The only exception is if
the invisible creature has a reach greater than 5 feet. In this case, the struck character knows the
general location of the creature but has not pinpointed the exact location.

If a character tries to attack an invisible creature whose location he has pinpointed, he attacks
normally, but the invisible creature still benefits from full concealment (and thus a 50% miss
chance). A particularly large and slow invisible creature might get a smaller miss chance.

If a character tries to attack an invisible creature whose location he has not pinpointed, have the
player choose the space where the character will direct the attack. If the invisible creature is
there, conduct the attack normally. If the enemy's not there, roll the miss chance as if it were
there and tell him that the character has missed, regardless of the result. That way the player
doesn't know whether the attack missed because the enemy's not there or because you successfully
rolled the miss chance.

If an invisible character picks up a visible object, the object remains visible. An invisible
creature can pick up a small visible item and hide it on his person (tucked in a pocket or behind a
cloak) and render it effectively invisible. One could coat an invisible object with flour to at
least keep track of its position (until the flour falls off or blows away).

Invisible creatures leave tracks. They can be tracked normally. Footprints in sand, mud, or other
soft surfaces can give enemies clues to an invisible creature's location.

An invisible creature in the water displaces water, revealing its location. The invisible creature,
however, is still hard to see and benefits from concealment.

A creature with the scent ability can detect an invisible creature as it would a visible one.

A creature with the Blind-Fight feat has a better chance to hit an invisible creature. Roll the miss
chance twice, and he misses only if both rolls indicate a miss. (Alternatively, make one 25% miss
chance roll rather than two 50% miss chance rolls.)

A creature with [blindsight](ref/rule/blindsight-and-blindsense) can attack (and otherwise interact
with) creatures regardless of invisibility.

An invisible burning torch still gives off light, as does an invisible object with a
_[light](ref/spell/light)_ or similar spell cast upon it.

Ethereal creatures are invisible. Since ethereal creatures are not materially present, Perception
checks, scent, Blind-Fight, and [blindsight](ref/rule/blindsight-and-blindsense) don't help locate
them. Incorporeal creatures are often invisible. Scent, Blind-Fight, and blindsight don't help
creatures find or attack invisible, incorporeal creatures, but Perception checks can help.

Invisible creatures cannot use gaze attacks.

Invisibility does not thwart divination spells.

Since some creatures can detect or even see invisible creatures, it is helpful to be able to hide
even when invisible.

## Low-Light Vision {#low-light-vision}

Characters with [low-light vision](ref/rule/low-light-vision) have eyes that are so sensitive to
light that they can see twice as far as normal in dim light. Low-light vision is color vision. A
spellcaster with low-light vision can read a scroll as long as even the tiniest candle flame is next
to him as a source of light.

Characters with [low-light vision](ref/rule/low-light-vision) can see outdoors on a moonlit night as
well as they can during the day.

## Paralysis {#paralysis}

Some monsters and spells have the supernatural or [spell-like ability](ref/umr/spell-like-abilities)
to paralyze their victims, immobilizing them through magical means. Paralysis from poison is
discussed in the Afflictions section.

A paralyzed character cannot move, speak, or take any physical action. He is rooted to the spot,
frozen and helpless. Not even friends can move his limbs. He may take purely mental actions, such as
casting a spell with no components.

A winged creature flying in the air at the time that it becomes paralyzed cannot flap its wings and
falls. A swimmer can't swim and may drown.

## Scent {#scent}

This extraordinary ability lets a creature detect approaching enemies, sniff out hidden foes, and
track by sense of smell.

A creature with the scent ability can detect opponents by sense of smell, generally within 30 feet.
If the opponent is upwind, the range is 60 feet. If it is downwind, the range is 15 feet. Strong
scents, such as smoke or rotting garbage, can be detected at twice the ranges noted above.
Overpowering scents, such as skunk musk or troglodyte stench, can be detected at three times these
ranges.

The creature detects another creature's presence but not its specific location. Noting the direction
of the scent is a move action. If the creature moves within 5 feet (1 square) of the scent's source,
the creature can pinpoint the area that the source occupies, even if it cannot be seen.

A creature with the Survival skill and the scent ability can follow tracks by smell, making a
Survival check to find or follow a track. A creature with the scent ability can attempt to follow
tracks using Survival untrained. The typical DC for a fresh trail is 10. The DC increases or
decreases depending on how strong the quarry's odor is, the number of creatures, and the age of the
trail. For each hour that the trail is cold, the DC increases by 2. The ability otherwise follows
the rules for the Survival skill in regards to tracking. Creatures tracking by scent ignore the
effects of surface conditions and poor visibility.

Creatures with the scent ability can identify familiar odors just as humans do familiar sights.

Water, particularly running water, ruins a trail for air-breathing creatures. Water-breathing
creatures that have the scent ability, however, can use it in the water easily.

False, powerful odors can easily mask other scents. The presence of such an odor completely spoils
the ability to properly detect or identify creatures, and the base Survival DC to track becomes 20
rather than 10.

## Spell Resistance {#spell-resistance}

[Spell resistance](ref/rule/spell-resistance) is the extraordinary ability to avoid being affected
by spells. Some spells also grant spell resistance.

To affect a creature that has [spell resistance](ref/rule/spell-resistance), a spellcaster must make
a caster level check (1d20 + caster level) at least equal to the creature's spell resistance. The
defender's spell resistance is like an Armor Class against magical attacks. If the caster fails the
check, the spell doesn't affect the creature. The possessor does not have to do anything special to
use spell resistance. The creature need not even be aware of the threat for its spell resistance to
operate.

Only spells and [spell-like abilities](ref/umr/spell-like-abilities) are subject to
[spell resistance](ref/rule/spell-resistance). Extraordinary and supernatural abilities (including
enhancement bonuses on magic weapons) are not. A creature can have some abilities that are subject
to spell resistance and some that are not. Even some spells ignore spell resistance; see When Spell
Resistance Applies, below.

A creature can voluntarily lower its [spell resistance](ref/rule/spell-resistance). Doing so is a
standard action that does not provoke an attack of opportunity. Once a creature lowers its
resistance, it remains down until the creature's next turn. At the beginning of the creature's next
turn, the creature's spell resistance automatically returns unless the creature intentionally keeps
it down (also a standard action that does not provoke an attack of opportunity).

A creature's [spell resistance](ref/rule/spell-resistance) never interferes with its own spells,
items, or abilities.

A creature with [spell resistance](ref/rule/spell-resistance) cannot impart this power to others by
touching them or standing in their midst. Only the rarest of creatures and a few magic items have
the ability to bestow spell resistance upon another.

[Spell resistance](ref/rule/spell-resistance) does not stack, but rather overlaps.

## When Spell Resistance Applies {#when-spell-resistance-applies}

Each spell includes an entry that indicates whether [spell resistance](ref/rule/spell-resistance)
applies to the spell. In general, whether spell resistance applies depends on what the spell does.

### Targeted Spells {#targeted-spells}

[Spell resistance](ref/rule/spell-resistance) applies if the spell is targeted at the creature. Some
individually targeted spells can be directed at several creatures simultaneously. In such cases, a
creature's spell resistance applies only to the portion of the spell actually targeted at that
creature. If several different resistant creatures are subjected to such a spell, each checks its
spell resistance separately.

### Area Spells {#area-spells}

[Spell resistance](ref/rule/spell-resistance) applies if the resistant creature is within the
spell's area. It protects the resistant creature without affecting the spell itself.

### Effect Spells {#effect-spells}

Most effect spells summon or create something and are not subject to
[spell resistance](ref/rule/spell-resistance). Sometimes, however, spell resistance applies to
effect spells, usually to those that act upon a creature more or less directly, such as _web_.

[Spell resistance](ref/rule/spell-resistance) can protect a creature from a spell that's already
been cast. Check spell resistance when the creature is first affected by the spell.

Check [spell resistance](ref/rule/spell-resistance) only once for any particular casting of a spell
or use of a [spell-like ability](ref/umr/spell-like-abilities). If spell resistance fails the first
time, it fails each time the creature encounters that same casting of the spell. Likewise, if the
spell resistance succeeds the first time, it always succeeds. If the creature has voluntarily
lowered its spell resistance and is then subjected to a spell, the creature still has a single
chance to resist that spell later, when its spell resistance is back up.

[Spell resistance](ref/rule/spell-resistance) has no effect unless the energy created or released by
the spell actually goes to work on the resistant creature's mind or body. If the spell acts on
anything else and the creature is affected as a consequence, no roll is required. Spell-resistant
creatures can be harmed by a spell when they are not being directly affected.

[Spell resistance](ref/rule/spell-resistance) does not apply if an effect fools the creature's
senses or reveals something about the creature.

Magic actually has to be working for [spell resistance](ref/rule/spell-resistance) to apply. Spells
that have instantaneous durations but lasting results aren't subject to spell resistance unless the
resistant creature is exposed to the spell the instant it is cast.

## Successful Spell Resistance {#successful-spell-resistance}

[Spell resistance](ref/rule/spell-resistance) prevents a spell or a
[spell-like ability](ref/umr/spell-like-abilities) from affecting or harming the resistant creature,
but it never removes a magical effect from another creature or negates a spell's effect on another
creature. Spell resistance prevents a spell from disrupting another spell.

Against an ongoing spell that has already been cast, a failed check against
[spell resistance](ref/rule/spell-resistance) allows the resistant creature to ignore any effect the
spell might have. The magic continues to affect others normally.
