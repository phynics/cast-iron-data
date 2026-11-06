+++
id = "ref/skill/perception"
kind = "rule"
title = "Perception"
source_ids = ["core-rulebook", "aquatic-adventures", "occult-adventures", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "perception", path = "json/skills.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 102

**Associated Skill**

**Details:** Wisdom

**Trained Only**

**Details:** No

**Armor Check Penalty**

**Details:** No

**Optional Unchained Skill**

**Details:** No

**Optional Background Skill**

**Details:** No

### Check

Perception has a number of uses, the most common of which is an opposed check versus an opponent's
[Stealth](ref/skill/stealth) check to notice the opponent and avoid being surprised. If you are
successful, you notice the opponent and can react accordingly. If you fail, your opponent can take a
variety of actions, including sneaking past you and attacking you.

Perception is also used to notice fine details in the environment. The DC to notice such details
varies depending upon distance, the environment, and how noticeable the detail is. The following
table gives a number of guidelines.

### Details Table

|Detail|Perception DC|
| --- | --- |
|Hear the sound of battle|-10|
|Notice the stench of rotting garbage|-10|
|Detect the smell of smoke|0|
|Hear the details of a conversation|0|
|Notice a visible creature|0|
|Determine if food is spoiled|5|
|Hear the sound of a creature walking|10|
|Hear the details of a whispered conversation|15|
|Find the average concealed door|15|
|Hear the sound of a key being turned in a lock|20|
|Find the average secret door|20|
|Hear a bow being drawn|25|
|Sense a burrowing creature underneath you|25|
|Notice a pickpocket|Opposed by Sleight of Hand|
|Notice a creature using Stealth|Opposed by Stealth|
|Find a hidden trap|Varies by trap|
|Identify the powers of a potion through taste|15 + the potion's caster level|

### Modifiers Table

|Perception Modifiers|DC Modifier|
| --- | --- |
|Distance to the source, object, or creature|+1/10 feet|
|Through a closed door|+5|
|Through a wall|+10/foot of thickness|
|Favorable conditions|-2|
|Unfavorable conditions|+2|
|Terrible conditions|+5|
|Creature making the check is distracted|+5|
|Creature making the check is asleep|+10|
|Creature or object is invisible|+20|

Favorable and unfavorable conditions depend upon the sense being used to make the check. For
example, bright light might decrease the DC of checks involving sight, while torchlight or moonlight
might increase the DC. Background noise might increase a DC involving hearing, while competing odors
might increase the DC of a check involving scent.

Terrible conditions are unfavorable conditions, but more extreme. For example, candlelight for DCs
involving sight, a roaring dragon for DCs involving hearing, and an overpowering stench covering the
area for DCs involving scent.

### Action

Most Perception checks are reactive, made in response to observable stimulus. Intentionally
searching for stimulus is a **move action**.

### Try Again

Yes. You can try to sense something you missed the first time, so long as the stimulus is still
present.

### Special

Elves, half-elves, gnomes, and halflings receive a +2 racial bonus on Perception checks. Creatures
with the [scent](ref/umr/scent) special quality have a +8 bonus on Perception checks made to detect
a scent. Creatures with the [tremorsense](ref/umr/tremorsense) special quality have a +8 bonus on
Perception checks against creatures touching the ground and automatically make any such checks
within their range. For more on special qualities, see
[Special Abilities](ref/rule/special-abilities-2).

A spellcaster with a [hawk](ref/monster/familiar-hawk) or [owl](ref/monster/familiar-owl)
[familiar](ref/ability/familiars) gains a +3 bonus on Perception checks. If you have the
[Alertness](ref/feat/alertness) feat, you get a bonus on Perception checks.

### Underwater Perception

**Sources:** Aquatic Adventures pg 46\
Even in clear water, the way light travels underwater makes it harder to see underwater than on
land, and water sometimes contains particulates that further obscure vision. Perception checks to
see something are always made at a minimum -2 penalty underwater, and often a greater penalty when
the water is murky (flowing water, such as in a current or river, is always at least somewhat
murky). The maximum distance most creatures can see underwater varies from 40 to 320 feet in clear
water (4d8 × 10) and from 10 to 80 feet in murky water (1d8 × 10). Generally the only way to gain
the [concealment](ref/rule/concealment) necessary to use Stealth in open water is to swim at least
that distance away from an opponent.

Most naturally aquatic creatures either have eyes that are evolved to be exposed to water or have
protective transparent eyelids, as do beavers. Surface creatures can use goggles to protect their
eyes from water and its particulates; otherwise, they take a -4 penalty on Perception checks to see
underwater and risk eye damage or blinding, depending on the water source.

Many undersea denizens, particularly those in deep areas, use scent or
[tremorsense](ref/umr/tremorsense) instead of sight. Scent usually works normally underwater for
aquatic creatures (though terrestrial creatures that rely on scent can't follow a trail in the
water), but water is more conducive to carrying scents from afar, allowing creatures like
[sharks](ref/monster/shark) to detect blood up to a mile away with their
[keen scent](ref/umr/keen-scent) ability. Aquatic tremorsense detects disturbances in the water
nearby, even without touching the same solid surface.

Sound travels farther and faster underwater, but that benefit is usually mitigated by the ambient
noise of moving water. In situations with particularly little ambient noise (for instance, an area
where all wildlife has been killed by a necromantic blight, or a flooded chamber or tank),
Perception checks to hear something underwater are made with a +2 bonus.

### Occult Skill Unlocks

[Occult skill unlocks](ref/rule/occult-skill-unlocks) are available to those using the occult rules
and meet certain requirements.

#### Read Aura

**Sources:** Occult Adventures pg 197

Your psychic sensitivity allows you to read the psychic and magical auras of creatures and objects.

##### Check

Once per day, you can examine the natural aura of a creature or object to discern the subject's
alignment, emotions, health, or magic. This requires 10 minutes of concentration, after which you
attempt a Perception check. Each time, you must pick one of four auras to read: alignment, emotion,
health, or magic. The result of the check applies only to the selected aura. You must be within 30
feet of the subject at all times during the reading. Objects typically have only magic auras, though
some also have alignment auras (and intelligent items have emotion auras). You can still attempt to
detect a type of aura an object doesn't have, but you get no results. The DC varies depending on the
aura, as shown on the table.

###### Read Alignment Aura

You attempt to read the alignment aura, learning the alignment and its strength. An alignment aura's
strength depends on the creature's Hit Dice or item's caster level, as noted in the description of
the [detect evil](ref/spell/detect-evil) spell.

###### Read Emotion Aura

The colors within the target's aura reveal its emotional state. If successful, you learn the
target's disposition and its attitude toward any creatures within 30 feet of it. For a number of
rounds equal to the amount by which you exceeded the skill check's DC, you gain a +2 circumstance
bonus on Bluff, Diplomacy, Intimidate, and Sense Motive checks against the target.

###### Read Health Aura

Viewing the flow of vital force, you assess a creature's physical condition. You learn if the
creature is unharmed or wounded, if it is poisoned or diseased, and whether it is affected by any of
the following conditions: confused, disabled, dying, nauseated, panicked, staggered, stunned, and
unconscious. You also learn the total number of points available in its ki pool, grit pool, or
similar resource.

###### Read Magic Aura

You attempt to determine the number and power of all magical auras on a target creature or object
(see [detect magic](ref/spell/detect-magic) to determine a magic aura's power). If the check is
successful, you can attempt Knowledge (arcana) or Spellcraft checks to determine the school or
identify properties of a magic item, as normal. If the item is affected by
[magic aura](ref/spell/magic-aura) or a similar spell, you can realize this and determine the actual
properties of the item if your check result exceeds the DC by 5 or more. If the spell is of a higher
level (such as [aura alteration](ref/spell/aura-alteration)), increase this threshold DC by 2 for
every spell level beyond 1st.

|Task|DC|
| --- | --- |
|Read alignment aura|15 + creature's HD or item's caster level|
|Read emotion aura|20 + creature's HD or item's caster level (intellignt items only)|
|Read health aura|15 + creature's HD|
|Read magic aura|20 + creature's HD or item's caster level|

### Action

Reading an aura requires 10 minutes of study.

##### Try Again

Yes. You can read a creature or object's aura more than once, whether you read the same aura or a
different one. You can still attempt only one skill check to read an aura per day.

### Unchained Rogue Skill Unlocks

**Sources:** Pathfinder Unchained pg 85\
If using [skill unlocks](ref/rule/skill-unlocks), with sufficient ranks in Perception, you earn the
following.

**5 Ranks**

**Details:** You remain alert to sounds even in your sleep, and the normal DC increase to Perception
checks when you are sleeping is halved. The distance modifier on the DC of Perception checks you
attempt is reduced to +1 per 20 feet.

**10 Ranks**

**Details:** The distance modifier on the DC of Perception checks you attempt is reduced to +1 per
30 feet. In addition, you gain a +5 bonus on Perception checks to notice or locate an invisible
creature or object.

**15 Ranks**

**Details:** You remain alert to sounds even in your sleep, and the normal DC increase to Perception
checks when you are sleeping doesn't apply to you. The distance modifier on the DC of your
Perception checks is reduced to +1 per 40 feet.

**20 Ranks**

**Details:** You gain a +10 bonus on Perception checks to notice invisible creatures or objects. The
distance modifier on the DC of Perception checks you attempt is reduced to +1 per 60 feet.
