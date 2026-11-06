+++
id = "ref/rule/lich"
kind = "rule"
title = "Lich"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lich", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Adventures pg. 26-27\
Your attempt to transition into unlife has gone horribly awry and your soul is trapped. Lich
corruption also works for becoming another sort of corporeal undead (except ghouls and vampires,
which have their own corruptions).

### Catalyst

This corruption originates from an unsuccessful attempt at lichdom. You might have lacked sufficient
power or used a flawed phylactery. If you're not a spellcaster, you could have been an innocent
bystander or become corrupted upon destroying a particularly powerful lich's phylactery.

### Progression

Lich corruptions are rarely stable, and cause incredible mental and physical strain. Whenever you
fail a saving throw against a necromancy effect, learn how to cast a new spell or spells, or are
exposed to 25 points of negative energy damage or more from a single source (whether it heals or
harms you), you must succeed at a Fortitude save (DC = 15 + your manifestation level) or become
spiritually disjoined. You also need to make a saving throw whenever anyone successfully casts the
[death ward](ref/spell/death-ward) spell on you. After a failed save, your spirit and body
disconnect, leaving your corporeal form helpless and your mind trapped within the Negative Energy
Plane. This state lasts for 1 hour per manifestation level; if you are killed during this time, you
rise 24 hours later as a [wraith](ref/monster/wraith) under the GM's control.

**Corruption Stage 1**

**Details:** The first time you recover from this disconnected state, you return diminished, taking
a permanent -2 penalty to your Charisma score, and your alignment shifts one step toward evil.

**Corruption Stage 2**

**Details:** The second time this happens, your alignment shifts another step toward evil and you
take an additional -2 penalty to your Charisma score.

**Corruption Stage 3**

**Details:** The third time this happens, you die and your soul is consumed by the Negative Energy
Plane. You can't be raised or resurrected except by powerful magic such as
[miracle](ref/spell/miracle) or [wish](ref/spell/wish). Even if you do get brought back, you are an
evil lich NPC under the GM's control.

### Removing the Corruption

Curing lich corruption requires great acts of purification, such as being exorcised by a powerful
cleric, bathing in sacred springs, or creating a phylactery of your own into which to expel the lich
corruption.

### Manifestations

The following are manifestations of the lich corruption.

**Agonizing Touch**

**Flavor:** Your touch racks the living with pain.

**Prereq:** Manifestation level 4th, death's caress

**Gift:** Once per day per manifestation level, you can make an _agonizing touch_ as a **standard
action**. A living creature hit by this touch attack must succeed at a Fortitude save or be
[staggered](ref/misc/staggered) for a number of rounds equal to 1/2 your manifestation level.

**Stain:** Both of your hands wither to nearly skeletal appendages, and your emotions dim towards
the coldness of undeath. You take a -2 penalty on attacks with manufactured weapons. Your spells
with somatic or emotion components have a 5% failure chance. This stacks with any spell failure
chances you incur from other sources.

**Bleak Aura**

**Flavor:** Entropy seeps from your body.

**Prereq:** Manifestation level 4th, deathless

**Gift:** Any living creature that ends its turn adjacent to you takes 1 point of negative energy
damage for every 2 manifestation levels you have.

**Stain:** Animals are startled by your presence, worsening their starting attitudes toward you by
one step. Any animal companion you have abandons you when you acquire this stain. Whispering voices
fill the air around you, begging for release or cursing your existence. Any creature that succeeds
at a DC 20 [Perception](ref/skill/perception) check can hear these whispers, which might alert it to
your presence if you're using [Stealth](ref/skill/stealth).

**Cadaver's Countenance**

**Flavor:** Your body takes on a deathly likeness.

**Gift:** You gain a +1 natural armor bonus to your AC and a +2 bonus on saves against
mind-affecting effects.

**Stain:** Your flesh tightens, turning corpse-like and gray as your body rots. You take a -2
penalty to your Constitution.

**Death's Caress**

**Flavor:** Your touch drains the warmth of life from others.

**Gift:** You can make a touch attack as a **standard action** that deals cold damage equal to 1d4 +
your manifestation level.

**Stain:** The flesh from one of your hands rots away, leaving it a blackened, skeletal claw. Spells
that detect undead sense you, though the peculiar result they return informs the caster that you're
still a living creature. Other spells and effects don't treat you as undead.

**Deathless**

**Flavor:** You are inured to negative energy.

**Gift:** You gain a +2 bonus on saving throws against spells and effects that work only on living
creatures.

**Stain:** You are healed by negative energy and harmed by positive energy as if you were an undead
creature.

**Greater Cadaver's Countenance**

**Flavor:** You become emaciated and nearly skeletal.

**Prereq:** Manifestation level 4th, cadaver's countenance

**Gift:** You gain cold resistance 5 and DR equal to 1/2 your manifestation level that is overcome
by bludgeoning damage.

**Stain:** You take an additional -2 penalty to your Constitution score and are affected by spells
and abilities (including [bane](ref/magic-enh/bane) and [favored enemy](ref/ability/favored-enemy))
as if your creature type were undead. This doesn't grant you the immunities of undead creatures, nor
does it make you immune to effects that target living creatures or change how negative and positive
energy affect you.

**Malevolence**

**Flavor:** You can wrench your soul from your body to possess another.

**Prereq:** Manifestation level 7th, bleak aura, deathless

**Gift:** You can touch a living creature as a **standard action** and force your soul into its
body. If hit by this touch attack, the target must succeed at a Will save (DC = 15 + your
manifestation level) or be affected by [possession](ref/spell/possession). You can possess creatures
for a number of minutes per day equal to your manifestation level. These minutes don't need to be
used consecutively, but must be spent in 1-minute increments. A failed attempt costs 1 minute of use
and renders your target immune to your _malevolence_ for 24 hours.

Your body is helpless while you possess another creature, and if it is destroyed you die when the
duration of _malevolence_ ends. You can use _malevolence_ while in another creature's body to
transfer your soul again (following the same rules for casting _[possession](ref/spell/possession)_
while in a body that's not your own).

**Stain:** Your spirit is untethered from your body. You roll twice and take the lowest result on
saves against spells that imprison or target your soul, such as [magic jar](ref/spell/magic-jar) and
[trap the soul](ref/spell/trap-the-soul), as well as against positive energy effects. If you drop
below 0 hit points, your soul leaves your body and you instantly die.

**Master of the Dead**

**Flavor:** You can animate the dead with your necromantic power.

**Prereq:** Manifestation level 6th, agonizing touch, death's caress

**Gift:** You can cast [animate dead](ref/spell/animate-dead) at will as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to your character
level. You must provide the material components, and you take 2 points of
[Charisma drain](ref/rule/ability-damage-drain) for every creature you animate. If the drain is
removed or you avoid taking it, the animated creature is immediately destroyed (you choose which
creatures are destroyed if some but not all drain is removed). Conversely, the Charisma drain from
animating a creature is instantly removed when that creature is destroyed. You still must abide by
the usual Hit Die limits of _[animate dead](ref/spell/animate-dead)._

**Stain:** Your emotions are nearly a thing of the past. You can't benefit from morale bonuses or
bardic performances.

**Necromantic Knowledge**

**Flavor:** You have gained unusual insights into necromancy.

**Prereq:** Manifestation level 2nd, ability to cast spells

**Special:** You can gain this manifestation multiple times. Each time you gain the _gift,_ you gain
a different necromancy spell, and each time you gain the _stain,_ the penalties stack.

**Gift:** You can add one necromancy spell from the sorcerer/wizard spell list to your spellbook,
familiar, or list of spells you can prepare or to your spells known. This spell must be of a level
you can cast. A spell learned in this fashion is treated as though it were on your class spell list.

If you normally cast your spells from the sorcerer/wizard spells list, you can add a necromancy
spell from the cleric or witch spell list instead.

**Stain:** You cast any spell from a school other than necromancy as though your caster level were 1
lower, which might prevent you from casting the spell altogether.
