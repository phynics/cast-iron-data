+++
id = "ref/implement/necromancy"
kind = "rule"
title = "Necromancy"
source_ids = ["occult-adventures", "occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necromancy", path = "json/class_ability_implements.json" },
]

[fields]
kind = "none"
+++

**Sources:** Occult Adventures pg 56\
Implements that draw power from necromancy can control undead and harm the living.

**Implements**

**Details:** Bone, coin, doll, drum, robe, skull.

### Resonant Power

**Necromantic Focus (Su)**

**Ability:** Whoever possesses the implement can control an additional 2 Hit Dice of undead for
every point of mental focus invested in the item (to a maximum number of Hit Dice equal to 4 &times&
your occultist level). Any spellcaster who bears the implement can add it as an additional focus
component for a necromancy spell he casts to create undead. If he does so, he can create an
additional number of HD of undead equal to the additional HD the implement allows him to control
(apply this effect after doubling the HD of undead for [desecrate](ref/spell/desecrate), if
applicable).

Undead creatures take a -1 penalty on saving throws against spells cast by the bearer of this
implement for every 4 points of mental focus invested in this implement.

**Flavor:** The implement grants its possessor greater power over the undead.

### Base Focus Power

**Mind Fear (Sp)**

**Special:** This is a mind-affecting fear effect.

**Standard:** You can expend 1 point of mental focus to cause a living creature to succumb to fear.
The target must be within 30 feet of you, and it can attempt a Will saving throw to negate the
effect. If the target fails the save and has a number of Hit Dice less than or equal to yours, it is
[frightened](ref/misc/frightened) for 1d4 rounds. If the target fails the saving throw and has a
number of Hit Dice greater than yours, it is instead [shaken](ref/misc/shaken) for 1d4 rounds.

### Focus Powers

**Flesh Rot (Sp)**

**Prereq:** 3rd-level occultist

**Standard:** You can make a melee touch attack and expend 1 point of mental focus to cause the
flesh of a living creature to rot and wither. If the attack hits, the target takes 1d8 points of
damage + 1 point per occultist level you possess. If you miss with the melee touch attack, this
power is wasted with no effect.

At 7th level: The damage 2d8 + your occultist level.

At 11th level: The damage 3d8 + your occultist level.

At 15th level: The damage 4d8 + your occultist level.

At 19th level: The damage 5d8 + your occultist level.

**Necromantic Servant (Sp)**

**At 13th Level:** When you take an immediate action to restore your servant, it splits into two
servants. You can have a maximum number of servants in existence equal to
[half](ref/misc/fractions-and-rounding) of your occultist level.

**At 17th Level:** The servant gains a teamwork feat of your choice.

**At 5th Level:** Whenever the necromantic servant would be destroyed, if you are within medium
range (100 feet + 10 feet per level) of the servant, you can expend 1 point of mental focus as an
**immediate action** to cause the servant to return to full hit points.

**At 9th Level:** You can choose to give the servant the _bloody_ or _burning_ simple template (if
it's a skeleton) or the _fast_ simple template (if it's a zombie).

**Standard:** You can expend 1 point of mental focus to raise a single human
[skeleton](ref/template/skeleton) or human [zombie](ref/template/zombie) from the ground to serve
you for 10 minutes per occultist level you possess or until it is destroyed, whichever comes first.
This servant has a number of hit points equal to [half](ref/misc/fractions-and-rounding) your
maximum hit point total (not adjusted for temporary hit points or other temporary increases). It
also uses your base attack bonus and gains a bonus on damage rolls equal to 1/2 your occultist
level.

**Pain Wave (Sp)**

**Prereq:** 7th-level occultist

**Special:** This is a mind-affecting pain effect.

**Standard:** You can expend 1 point of mental focus to unleash a wave of pain. This wave hits all
creatures other than you in a 20-foot-radius [burst](ref/misc/burst) centered on a point that you
designate within 100 feet. All living creatures in this area are wracked with pain, gaining the
[sickened](ref/misc/sickened) condition for 1 round per occultist level you possess. Affected
creatures can attempt a Will save to reduce the duration to just 1 round.

**Psychic Curse (Sp)**

**Prereq:** 5th-level occultist

**Special:** A creature can't be under the effects of more than one _psychic curse_ at a time. This
is a mind-affecting curse effect.

**Standard:** You can expend 1 point of mental focus to curse a living creature within 30 feet with
your psychic magic. You can choose one of the following effects: **memory lapse, mental block,** or
**pain confusion.**

If you choose **[memory lapse](ref/spell/memory-lapse),** the target loses its memory of the past 1
hour per occultist level you possess.

If you choose **[mental block](ref/spell/mental-block),** you can proscribe one specific action,
such as attacking with a type of weapon, casting a specific spell, or something else suitably
specific (subject to the GM's discretion). The target can't take that action without first
succeeding at a Will save. If it fails, it can take other actions instead. If it attempts the
prohibited action again on subsequent rounds, it gains a cumulative +2 bonus on the save until it
succeeds.

If you select **pain confusion,** the creature is [confused](ref/misc/confused) for 1d4 rounds
whenever it is damaged by a critical hit. The target can attempt a Will save to negate this effect.
This effect lasts for 1 day per occultist level you possess.

**Soulbound Puppet (Su)**

**Fullround:** You can expend 1 point of mental focus to create a _soulbound puppet_ from a bone,
doll, or skull. If you use a bone or a skull, your power builds a Tiny or Small flesh puppet around
it that vaguely resembles the original creature from which the bones were taken. If the implement is
a doll, the doll comes to life.

Treat this as a [familiar](ref/sidekick/familiar), using your occultist level as your wizard level
to determine its powers and abilities. By using a bone or skull from the appropriate creature or a
doll shaped like that creature, you can select any of the [familiar](ref/ability/familiars) choices
available to a wizard. You can instead use a humanoid bone, doll, or skull, to give the _puppet_ the
base statistics of a [homunculus](ref/monster/homunculus), but without a fly speed or the poison
bite or telepathic link abilities.

No matter the form, this creature is a construct with an alignment matching your own. You can have
no more than one _soulbound puppet_ active at any given time. The _soulbound puppet_ remains
animated for 10 minutes per occultist level you possess.

**Spirit Shroud (Su)**

**At 4th Level:** As long as the _shroud_ remains, you also gain a resistance bonus on all saving
throws against death effects, fear effects, and any spells or effects that bestow
[negative levels](ref/rule/energy-drain-and-negative-levels) or deal negative energy damage (if the
spells or effects allow a save). This bonus is equal to one-fourth of your occultist level.

**Prereq:** 3rd-level occultist

**Standard:** You can expend 1 point of mental focus to surround yourself with a shroud of spirit
energy. You gain a number of [temporary hit points](ref/rule/temporary-hit-points) equal to 1d6 +
your occultist level. This _shroud_ lasts for 1 minute per occultist level or until the temporary
hit points are expended, whichever comes first. These temporary hit points stack with those from
other sources, but not with those gained through multiple uses of this ability.

### Sacred Implement

**Sources:** Occult Origins pg 15

**Deity**

**Details:** [Urgathoa](ref/faith/urgathoa)

**Implement**

**Details:** coin

**Opposition School**

**Details:** evocation

**Wake (Su)**

**Standard:** You can expend 1 point of mental focus to inspire fits of grief in a single creature
within 30 feet that can see and hear you. You fill the target with haunting visions of the deaths of
loved ones and the brevity of life, and for 1 minute, the target's emotional vulnerability grants
you a circumstance bonus equal to your occultist level on [Diplomacy](ref/skill/diplomacy) and
[Intimidate](ref/skill/intimidate) checks attempted against the target. If this implement is used in
combat, these emotions instead distract your target, leaving it [dazzled](ref/misc/dazzled) for 1
round per occultist level you have.
