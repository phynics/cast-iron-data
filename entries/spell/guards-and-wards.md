+++
id = "ref/spell/guards-and-wards"
kind = "spell"
title = "Guards and Wards"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guards_and_wards", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "292"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "30 minutes"
components = "V, S, M (burning incense, a small measure of brimstone and oil, a knotted string, and a small amount of blood), F (a small silver rod)"
range = "anywhere within the area to be warded"
effects = [
  { label = "Area", value = "up to 200 sq. ft./level (S)" },
]
duration = "2 hours/level (D)"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 30 minutes
Components: V, S, M (burning incense, a small measure of brimstone and oil, a knotted string, and a small amount of blood), F (a small silver rod)
Range: anywhere within the area to be warded
Duration: 2 hours/level (D)
Saving throw: see text
Spell resistance: see text
Area: up to 200 sq. ft./level (S)
:::

This powerful spell is primarily used to defend a stronghold or fortress by creating a number of
magical wards and effects. The ward protects 200 square feet per caster level. The warded area can
be as much as 20 feet high, and shaped as you desire. You can ward several stories of a stronghold
by dividing the area among them; you must be somewhere within the area to be warded to cast the
spell. The spell creates the following magical effects within the warded area.

_Fog:_ Fog fills all corridors, obscuring all sight, including [darkvision](ref/rule/darkvision),
beyond 5 feet. A creature within 5 feet has concealment (attacks have a 20% miss chance). Creatures
farther away have total concealment (50% miss chance, and the attacker cannot use sight to locate
the target). _Saving Throw:_ none. _Spell Resistance:_ no.

_Arcane Locks:_ All doors in the warded area are arcane locked. _Saving Throw:_ none. _Spell
Resistance:_ no.

_Webs:_ Webs fill all stairs from top to bottom. These strands are identical with those created by
the web spell, except that they regrow in 10 minutes if they are burned or torn away while the
guards and wards spell lasts. _Saving Throw:_ Reflex negates; see text for web. _Spell Resistance:_
no.

_Confusion:_ Where there are choices in direction - such as a corridor intersection or side
passage - a minor confusion-type effect functions so as to make it 50% probable that intruders
believe they are going in the opposite direction from the one they actually chose. This is a
mind-affecting effect. _Saving Throw:_ none. _Spell Resistance:_ yes.

_Lost Doors:_ One door per caster level is covered by a silent image to appear as if it were a plain
wall. _Saving Throw:_ Will disbelief (if interacted with). _Spell Resistance:_ no.

In addition, you can place your choice of one of the following five magical effects.

1. [Dancing lights](ref/spell/dancing-lights) in four corridors. You can designate a simple program
  that causes the lights to repeat as long as the guards and wards spell lasts. _Saving Throw:_
  none. _Spell Resistance:_ no.
1. A [magic mouth](ref/spell/magic-mouth) in two places. _Saving Throw:_ none. _Spell Resistance:_
  no.
1. A [stinking cloud](ref/spell/stinking-cloud) in two places. The vapors appear in the places you
  designate; they return within 10 minutes if dispersed by wind while the guards and wards spell
  lasts. _Saving Throw:_ Fortitude negates; see text for stinking cloud. _Spell Resistance:_ no.
1. A [gust of wind](ref/spell/gust-of-wind) in one corridor or room. _Saving Throw:_ Fortitude
  negates. _Spell Resistance:_ yes.
1. A [suggestion](ref/spell/suggestion) in one place. You select an area of up to 5 feet square, and
  any creature who enters or passes through the area receives the suggestion mentally. _Saving
  Throw:_ Will negates. _Spell Resistance:_ yes.

The whole warded area radiates strong magic of the abjuration school. A
[dispel magic](ref/spell/dispel-magic) cast on a specific effect, if successful, removes only that
effect. A successful mage's disjunction destroys the entire guards and wards effect.
