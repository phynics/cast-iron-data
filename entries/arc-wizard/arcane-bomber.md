+++
id = "ref/arc-wizard/arcane-bomber"
kind = "archetype"
title = "Arcane Bomber"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Arcane%20Bomber"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_bomber", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "ultimate-combat"
page = "75"

[fields]
kind = "archetype"
replaces = ["Arcane bond", "Cantrips", "Arcane school"]
+++

To many wizards, the experimentation of the alchemist seems quaint, if not dangerous or frightening.
A few wizards take up the secrets of the bomb, however, fusing alchemy with their already
considerable magical power.

**Bomb (Su)**

**Ability:** The arcane bomber gains an ability nearly identical to the
[alchemist's](ref/class/alchemist) _bomb_ ability. Unlike the alchemist, at 1st level, the arcane
bomber chooses one type of energy from the following list: acid, cold, fire, and electricity. He can
throw bombs of that type, but cannot modify them with discoveries. This ability stacks with the
alchemist _bomb_ ability to determine the level of bomb damage, but an arcane bomber that becomes an
alchemist does not gain that class's _bomb_ ability, nor does an alchemist that becomes an arcane
bomber gain this _bomb_ ability.

**Gained:** At 1st Level

**Replaces:** Arcane bond

**Bomb (Su)**

**Action:** Info

**Flavor:** Relevant text from the alchemist class ability.

**At 11th Level:** The base bomb damage becomes 6d6.

**At 13th Level:** The base bomb damage becomes 7d6.

**At 15th Level:** The base bomb damage becomes 8d6.

**At 17th Level:** The base bomb damage becomes 9d6.

**At 19th Level:** The base bomb damage becomes 10d6.

**At 3rd Level:** The base bomb damage becomes 2d6.

**At 5th Level:** The base bomb damage becomes 3d6.

**At 7th Level:** The base bomb damage becomes 4d6.

**At 9th Level:** The base bomb damage becomes 5d6.

**Gained:** At 1st Level

**Provokes attack of opportunity:** Yes

**Special:** Splash damage from your bomb is always equal to the bomb's minimum damage (so if the
bomb would deal 1d6+4 points of fire damage on a direct hit, its splash damage would be 5 points of
fire damage). Those caught in the splash damage can attempt a Reflex save for half damage, with a DC
equal to 10 + [half](ref/misc/fractions-and-rounding) your alchemist level + your Intelligence
modifier.

**Standard:** You can make and throw bombs. Drawing the components of, creating, and throwing a bomb
is a single action. Thrown bombs have a range of 20 feet and use the
[Throw Splash Weapon special attack](ref/rule/throw-splash-weapon). On a direct hit, your bomb
inflicts 1d6 points of fire damage + additional damage equal to your Intelligence modifier (this
bonus damage is not multiplied on a critical hit or by using feats such as
[Vital Strike](ref/feat/vital-strike)).

**Usage:** You can use a number of bombs each day equal to your class level + your Intelligence
modifier.

**Usage:** You can use a number of bombs each day equal to your class level + your Intelligence
modifier.

In addition to magical extracts, alchemists are adept at swiftly mixing various volatile chemicals
and infusing them with their magical reserves to create powerful bombs that they can hurl at their
enemies. Bombs are unstable, and if not used in the round they are created, they degrade and become
inert - their method of creation prevents large volumes of explosive material from being created and
stored. In order to create a bomb, you must use a small vial containing an ounce of liquid
catalyst - you can create this liquid catalyst from small amounts of chemicals from an alchemy lab,
and these supplies can be readily refilled in the same manner as a spellcaster's component pouch.
Most alchemists create a number of catalyst vials at the start of the day equal to the total number
of bombs they can create in that day - once created, a catalyst vial remains usable by you for
years.

Bombs are considered weapons and can be selected using feats such as
[Point-Blank Shot](ref/feat/point-blank-shot) and [Weapon Focus](ref/feat/weapon-focus). Your bombs
become inert if used or carried by anyone else.

**Spellblast Bombs (Su)**

**Ability:** The arcana bomber gains the [detect magic](ref/spell/detect-magic) and
[read magic](ref/spell/read-magic) cantrips and places them in his spellbook. He can cast either of
these as 1st-level spells.

**Gained:** At 1st Level

**Replaces:** Cantrips

**Swift:** An arcane bomber can sacrifice one of his spells to empower the next bomb he throws
during his turn. When he does, he gains a bonus to hit with the next bomb he throws before the end
of his turn equal to the level of the spell he sacrificed, and a bonus to damage equal to twice the
level of the spell.

**School of the Bomb**

**Info:** The creation and use of bombs is often so engrossing or intellectually taxing that an
arcane bomber forsakes four schools of magic. These opposition schools are chosen at 1st level and
cannot be changed later. An arcane bomber who prepares spells from his opposition school must use
two spell slots of that level to prepare the spell.

**Passive:** In addition, the arcane bomber takes a -4 penalty on any skill checks made when
crafting a magic item that has a spell from one of his opposition schools.

**Replaces:** Arcane school
