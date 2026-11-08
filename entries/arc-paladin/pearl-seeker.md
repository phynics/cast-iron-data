+++
id = "ref/arc-paladin/pearl-seeker"
kind = "archetype"
title = "Pearl Seeker"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pearl_seeker", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "archetype"
replaces = ["Detect evil", "Aura of courage", "aura of resolve", "Channel positive energy"]
alters = ["Armor proficiency", "Spells", "Divine bond"]
+++

**Sources:** Aquatic Adventures pg 54\
Some paladins are called to their faith by strange empathic visions and dreams that beckon them to
the oceans and beyond, to right aquatic injustice and search for a glorious gasping and whispering
pearl they don't understand. Their contact with the strange but benevolent entity sending the dreams
grants them unusual powers compared to other paladins.

**Armor Proficiency**

**Alters:** Armor proficiency

**Info:** A pearl seeker is proficient with light and medium armor but not with shields.

**Gained class skills:** swim

**Seek Impressions (Ex, Sp)**

**Ability:** A pearl seeker gains [Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus
feat and can use [detect psychic significance](ref/spell/detect-psychic-significance) at will as a
[spell-like ability](ref/umr/spell-like-abilities).

**Flavor:** Pearl seekers gain their power from a rare resonant sensitivity to the vision-granting
entity.

**Replaces:** Detect evil

**Aquatic Domain (Su)**

**Ability:** A pearl seeker gains the 1st-level domain power (Sealord) of the
[Aquatic](ref/druiddomain/aquatic) terrain domain, using her paladin level as her effective druid
level.

**At 8th Level:** She gains the 6th-level domain power (Seastrike) of the Aquatic terrain domain.

**Gained:** At 3rd Level

**Replaces:** Aura of courage, aura of resolve

**Sealord (Su)**

**Flavor:** From the Aquatic domain

**At 1st Level:** You can [channel energy](ref/ability/channel-energy) (as a cleric of your druid
level) a number of times per day equal to 3 + your Charisma modifier, but only to heal creatures
with the aquatic or water subtype or to command them (similar to using the
[Command Undead](ref/feat/command-undead) feat against undead). You can take other feats to add to
this ability, such as [Extra Channel](ref/feat/extra-channel) and
[Improved Channel](ref/feat/improved-channel), but not feats that alter this ability, such as
[Elemental Channel](ref/feat/elemental-channel) and [Alignment Channel](ref/feat/alignment-channel).
The DC to save against this ability is equal to 10 + 1/2 your druid level + your Charisma modifier.

**Seastrike (Su)**

**Flavor:** From the Aquatic domain

**At 8th Level:** As a **free action**, you may use natural and manufactured weapons in water as if
you had continuous _[freedom of movement](ref/spell/freedom-of-movement)._ As a **standard action**,
you can throw a weapon underwater without the normal penalties for throwing weapons; if your target
is in or under the water, the weapon also acts as a [returning](ref/magic-enh/returning) weapon for
that attack.

**Vision Magic**

**Ability:** A pearl seeker casts divine spells spontaneously, using the spells known and spells per
day from the [bloodrager](ref/class/bloodrager) progression table.

**Alters:** Spells

**At 10th Level:** She gains [ride the waves](ref/spell/ride-the-waves) as a bonus 2nd-level spell
known

**At 13th Level:** She gains [fluid form](ref/spell/fluid-form) as a bonus 3rd-level spell known

**At 16th Level:** She gains [seamantle](ref/spell/seamantle) as a bonus 4th-level spell known.

**At 7th Level:** She she gains [slipstream](ref/spell/slipstream) as a bonus 1st-level spell known.

**Special:** She also adds [hydraulic push](ref/spell/hydraulic-push) and
[hydraulic torrent](ref/spell/hydraulic-torrent) (as a 1st and 3rd level spells, respectively) to
her paladin spell list (but must learn these spells as normal).

**Divine Hippocampus**

**Action:** Info

**Alters:** Divine bond

**Gained:** At 5th Level

**Replaces:** Channel positive energy

A pearl seeker must choose a mount as her _divine bond,_ gaining a hippocampus mount with the
following companion statistics. (These statistics are equal to the regular
[hippocampus](ref/companion/hippocampus) companion with the 7th-level _Monstrous Mount Mastery_
benefits.)

> **Size** Large\
> **Speed** 5 ft., swim 80 ft.\
> **AC** +4 natural armor\
> **Attack** bite (1d6), tail slap (1d4; secondary attack)\
> **Ability Scores** Str 18, Dex 13, Con 15, Int 2, Wis 12, Cha 11\
> **Special Qualities** [darkvision](ref/rule/darkvision) 60 ft.,
> [low-light vision](ref/rule/low-light-vision), [scent](ref/umr/scent),
> [water dependency](ref/umr/water-dependency)
