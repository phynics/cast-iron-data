+++
id = "ref/arc-warpriest/sacred-fist"
kind = "archetype"
title = "Sacred Fist"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Sacred%20Fist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_fist", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "130"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "ac-bonus" },
  { anchor = "flurry-of-blows", level = 1 },
  { anchor = "unarmed-strike", level = 1 },
  { anchor = "blessed-fortitude", level = 3 },
  { anchor = "bonus-style-feat", level = 6 },
  { anchor = "ki-pool", level = 7 },
  { anchor = "miraculous-fortitude", level = 9 },
]
trades = [
  { replaces = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Sacred weapon", feature = "sacred-weapon", by = ["flurry-of-blows"] },
  { replaces = "Focus weapon", feature = "focus-weapon", by = ["unarmed-strike"] },
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["blessed-fortitude"] },
  { replaces = "Bonus feats gained at 6th, 12th, and 18th levels", feature = "bonus-feats", levels = [6, 12, 18], by = ["bonus-style-feat"] },
  { replaces = "Sacred armor", feature = "sacred-armor", by = ["ki-pool"] },
  { replaces = "Bonus feat gained at 9th level", feature = "bonus-feats", levels = [9], by = ["miraculous-fortitude"] },
]
+++

Unlike many warpriests, sacred fists leave behind armor and shield and instead rely on their fists
and whatever protection their deity bestows on them.

**Gained class skills:** acro, ea, kh, per, stl

**Lost class skills:** ha, ke, sur

## Class Skills {#class-skills}

The sacred fist's class skills are Acrobatics (Dex), Climb (Str), Craft (Int), Diplomacy (Cha),
Escape Artist (Dex), Heal (Wis), Intimidate (Cha), Knowledge (history) (Int), Knowledge (religion)
(Int), Perception (Wis), Profession (Wis), Sense Motive (Wis), Ride (Dex), Sense Motive (Wis),
Spellcraft (Int), Stealth (Dex), and Swim (Str). These skills replace the warpriest's class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Sacred fists are proficient with the [club](ref/eq-weapon/club), crossbow (light or heavy),
[dagger](ref/eq-weapon/dagger), [handaxe](ref/eq-weapon/handaxe), [javelin](ref/eq-weapon/javelin),
[kama](ref/eq-weapon/kama), [nunchaku](ref/eq-weapon/nunchaku),
[quarterstaff](ref/eq-weapon/quarterstaff), [sai](ref/eq-weapon/sai),
[shortspear](ref/eq-weapon/shortspear), [short sword](ref/eq-weapon/short-sword),
[shuriken](ref/eq-weapon/shuriken), [siangham](ref/eq-weapon/siangham),
[sling](ref/eq-weapon/sling), and [spear](ref/eq-weapon/spear). Sacred fists are not proficient with
any armor or shields. When wearing armor, using a shield, or carrying a medium or heavy load, a
sacred fist loses his AC bonus and flurry of blows. This replaces the warpriest's weapon and armor
proficiency.

## AC Bonus (Su) {#ac-bonus}

A deity protects her sacred fist as long as he is unarmored and unencumbered. A sacred fist adds his
Wisdom modifier (minimum 0) to his AC and his CMD. In addition, a sacred fist gains a +1 dodge bonus
to AC and CMD at 4th level. This bonus increases by 1 for every 4 levels thereafter (to a maximum of
+5 at 20th level).

These bonuses to AC apply even against touch attacks or when the sacred fist is flat-footed. He
loses these bonuses when he is immobilized or helpless, when he wears any armor, when he carries a
shield, or when he carries a medium or heavy load. This counts as the [monk](ref/class/monk) ability
of the same name, and the sacred fist's warpriest levels stack with monk levels for determining the
benefits.

## Flurry of Blows (Ex) {#flurry-of-blows}

At 1st level, a sacred fist can make a flurry of blows attack as a full-attack action. This ability
works like the monk ability of the same name, except the sacred fist's attack bonus from warpriest
levels does not count as his warpriest level. This ability replaces sacred weapon.

## Unarmed Strike {#unarmed-strike}

At 1st level, a sacred fist gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a
bonus feat. He uses his warpriest levels as monk levels for determining the amount of damage dealt
with an unarmed strike. This ability replaces focus weapon.

## Blessed Fortitude (Su) {#blessed-fortitude}

At 3rd level, a sacred fist can avoid even magical and unusual attacks with help from his deity. If
he succeeds at a Fortitude saving throw against an attack that has a reduced effect on a successful
save, he instead avoids the effect entirely. A [helpless](ref/misc/helpless) sacred fist does not
gain the benefit of the blessed fortitude ability. This ability replaces the bonus feat gained at
3rd level.

## Bonus Style Feat {#bonus-style-feat}

At 6th level, the sacred fist gains a style feat as a bonus feat. The sacred fist must meet the
style feat's prerequisites. He uses his warpriest levels as monk levels for the purposes of meeting
the feat's prerequisites. At 12th and 18th levels, a sacred fist gains either another style feat or
a feat that requires a style feat as a prerequisite. This ability replaces the bonus feats gained at
6th, 12th, and 18th levels.

## Ki Pool (Su) {#ki-pool}

At 7th level, the sacred fist gains a ki pool. This functions as the monk class feature, using the
sacred fist's level - 3 as his monk level when determining the number of points in his pool and
bonuses granted to his unarmed strike. Additionally, the sacred fist can as a swift action spend 1
point from his ki pool to grant himself a +1 insight bonus to his AC for 1 minute. (This is in
addition the normal ki ability to gain a dodge bonus to AC.) This insight bonus increases by 1 for
every 3 levels above 7th (to a maximum of +5 at 19th level). This ability replaces sacred armor.

## Miraculous Fortitude (Su) {#miraculous-fortitude}

At 9th level, the sacred fist's blessed fortitude ability improves. He still takes no damage or
negative effect when he succeeds at a Fortitude save, but now when he fails a Fortitude saving throw
against a spell or effect that deals damage (including
[ability damage and drain](ref/rule/ability-damage-drain)), he takes only half the amount of damage.
A [helpless](ref/misc/helpless) sacred fist does not gain the benefit of miraculous fortitude. This
ability replaces the bonus feat gained at 9th level.
