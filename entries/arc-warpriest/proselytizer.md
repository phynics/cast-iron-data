+++
id = "ref/arc-warpriest/proselytizer"
kind = "archetype"
title = "Proselytizer"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Proselytizer"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "proselytizer", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "emotional-appeal", level = 3 },
  { anchor = "sacred-subdual", level = 1 },
  { anchor = "blessing-of-conversion", level = 1 },
  { anchor = "voice-of-the-faithful", level = 1 },
]
trades = [
  { replaces = "Sacred armor", feature = "sacred-armor", by = ["emotional-appeal"] },
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["emotional-appeal"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Sacred weapon", feature = "sacred-weapon", by = ["sacred-subdual"] },
  { alters = "Blessings", feature = "blessings", by = ["blessing-of-conversion"] },
  { alters = "Blessings (major)", feature = "blessings", power = "major", by = ["voice-of-the-faithful"] },
]
+++

The proselytizer is the perfect militant missionary. He seeks to win the hearts and lay claim to the
souls of those he meets, and—failing that—spreads the word of his deity at the edge of the sword.

## Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

A proselytizer does not gain proficiency with heavy armor or with all martial weapons, though he
does gain proficiency in his deity's favored weapon. If his deity's favored weapon is unarmed
strike, he gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat. This
ability alters the warpriest's weapon and armor proficiencies.

## Emotional Appeal {#emotional-appeal}

A proselytizer has great power over the emotions of others, wielding his voice like a weapon to
pierce the heart of listeners and bring them closer to communion with his deity's power. The
warpriest adds the following spells to his warpriest spell list at the indicated levels. He casts
these as divine warpriest spells: 1st—_charm person_, _rally point_, _wrath_; 2nd—_castigate_,
_heroism_, _suggestion_; 3rd—_charm monster_, _geas (lesser)_; 4th—_forced repentance_, _serenity_;
5th—_castigate (mass)_, _suggestion (mass)_; 6th—_antipathy_, _sympathy_.

This ability replaces sacred armor and the bonus feat gained at 3rd level.

## Sacred Subdual (Su) {#sacred-subdual}

When a proselytizer uses his sacred weapon damage in place of his normal weapon damage, all damage
he deals with that weapon is nonlethal damage.

This ability modifies sacred weapon.

## Blessing of Conversion {#blessing-of-conversion}

The proselytizer always gains the conversion bonus upon converting an NPC, rather than only the
first time he does so each level. The bonuses overlap their durations, and do not stack. The
proselytizer does not gain access to the minor blessings granted by his blessing class feature until
3rd level. This ability modifies blessings.

## Voice of the Faithful (Ex) {#voice-of-the-faithful}

A proselytizer of 10th level or higher can expend a use of his major blessing to be able to speak to
and understand any creature with a language for 1 hour.

This ability modifies blessings (major).
