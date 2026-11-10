+++
id = "ref/arc-spiritualist/shadow-caller"
kind = "archetype"
title = "Shadow Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Shadow%20Caller"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_caller", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "50"

[fields]
kind = "archetype"
replaces = ["Shared consciousness", "Etheric tether", "Phantom recall", "See invisibility", "Fused consciousness", "Empowered consciousness"]
alters = ["Spellcasting", "Phantom"]
+++

While most spiritualists form a bond with the remnants of a creature's soul, some explore ways to
bind ephemeral shadows to their own souls in exchange for power.

**Prerequisites:** Creatures that don't normally cast shadows (such as vampires) cannot be shadow
callers

**Shadowcaster**

**Alters:** Spellcasting

**Info:** A shadow caller adds [darkness](ref/spell/darkness) and
[deeper darkness](ref/spell/deeper-darkness) to their class spell list as 2nd- and 3rd-level spells,
respectively.

**Passive:** When her shade (see below) inhabits her shadow, the shadow caller's effective caster
level is one higher when she casts all spells with the shadow or darkness descriptor.

**Shade**

**Ability:** A shadow caller gains a special kind of phantom known as a shade. A shade functions as
a phantom, except as noted below. A shade is from the Shadow Plane instead of the Ethereal Plane. A
shade is not confined to the shadow caller's consciousness, but instead inhabits her shadow.

**Alters:** Phantom

**Emotionless (Su)**

**Ability:** The shade gains a number of ranks in Intimidate and Stealth equal to its Hit Dice. The
shadow caller gains [Skill Focus](ref/feat/skill-focus) in each of these skills while the shade
inhabits her shadow.

**Flavor:** A shadow caller's shade lacks an emotional focus; it is cold and devoid of all emotions.

**Info:** The shade has good Reflex and Will saves, gains
[Lightning Reflexes](ref/feat/lightning-reflexes) as a bonus feat, and gains the following
abilities.

**Weakening Touch (Su)**

**Ability:** A shade's slam attack causes its victim to take a -2 penalty to Strength for 1 round.

**Special:** This penalty does not stack with itself. This is a negative energy effect.

**Standard:** A shade in incorporeal form can deliver the penalty as a touch attack.

**Umbral Shroud (Su)**

**At 7th Level:** The the shadow caller's shade can emit a 10-foot aura of swirling shadows that
grants all allies 20% [concealment](ref/rule/concealment) against creatures without
[darkvision](ref/rule/darkvision) or the [see in darkness](ref/umr/see-in-darkness) ability, and a
+4 bonus on Stealth checks.

**Shadow Caster (Sp)**

**At 18th Level:** The maximum spell level improves to 6th level and effects are 60% real.

**At 12th Level:** Her shade gains the ability to cast either
[shadow conjuration](ref/spell/shadow-conjuration) or [shadow evocation](ref/spell/shadow-evocation)
once per day. It uses its Hit Dice as its caster level, and the DC for these spells equals 10 + 1/2
the shade's Hit Dice + its Charisma modifier. Instead of the normal spell level and percentage of
reality for the two spells, the maximum spell level of the duplicated spell is 4th level, and the
effects are 40% real.

**Midnight Shroud (Su)**

**At 17th Level:** Her shade's _umbral shroud_ also lowers the
[light level](ref/rule/vision-and-light) in its range to darkness, regardless of the prevailing
conditions; this counts as a 7th-level _[darkness](ref/spell/darkness)_ spell for the purpose of
adjudicating light and darkness effects.

**Inhabit Shadow (Su)**

**At 12th Level:** This bonus increases to +8.

**Info:** A shade resides within a shadow caller's own shadow. When the shade is summoned, the
shadow caller does not cast a shadow under any circumstances.

**Passive:** While the shade inhabits its master's shadow, the shadow caller gains
[darkvision](ref/rule/darkvision) 60 feet. If the shadow caller already has darkvision, its range
increases by 30 feet. Additionally, the shadow caller gains a +4 circumstance bonus on Stealth
checks against creatures without darkvision or the
_[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness)_ ability.

**Replaces:** Shared consciousness

**Shadow Bound (Su)**

**Ability:** A shadow caller's shade remains stable while adjacent to the shadow caller, or while up
to 5 feet away from the shadow caller for every 5 levels the shadow caller possesses. If the shade
moves beyond this distance, it is automatically dismissed back to the Shadow Plane (preventing the
shade from being summoned back for 24 hours) unless the shadow caller concentrates as per the
_etheric tether_ ability. However, if both the shadow caller and shade are in areas of total
darkness, the shade can move any distance from the shadow caller.

**Replaces:** Etheric tether

**Special:** If the shade is beyond its maximum distance and enters an area of dim or brighter
illumination, it immediately returns to the Shadow Plane and cannot be summoned for 24 hours.

**Shadow Jump (Su)**

**Ability:** When a shadow caller's shade inhabits her shadow, she can travel between shadows as per
the [shadowdancer's](ref/pclass/shadowdancer) _shadow jump_ ability. Each day, she can travel a
total of 40 feet per spiritualist level in this way and, as with a shadowdancer, the distance is
rounded to the nearest 10-foot increment.

**Gained:** At 6th Level

**Replaces:** Phantom recall

**Shadow Jump (Su)**

**Ability:** A shadowdancer gains the ability to travel between shadows as if by means of a
[dimension door](ref/spell/dimension-door) spell. The limitation is that the magical transport must
begin and end in an area with at least some dim light.

**Flavor:** Relevant text from the shadowdancer class ability.

**Usage:** A shadowdancer can jump up to a total of 40 feet each day in this way. This amount can be
split among many jumps, but each one, no matter how small, counts as a 10-foot increment.

**Usage:** A shadowdancer can jump up to a total of 40 feet each day in this way. This amount can be
split among many jumps, but each one, no matter how small, counts as a 10-foot increment.

**See in Darkness (Su)**

**Gained:** At 9th Level

**Replaces:** See invisibility

**Standard:** A shadow caller can gain the [see in darkness](ref/umr/see-in-darkness) universal
monster ability.

**Usage:** 1 time/day per spiritualist level

**Umbral Aura (Su, Sp)**

**Ability:** While her shade inhabits her shadow, the shadow caller can _hide in plain sight_ (the
ability to use [Stealth](ref/skill/stealth) to hide, even while being observed), even if an
observing creature has [darkvision](ref/rule/darkvision) or
_[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness)._

**Gained:** At 10th Level

**Passive:** A shadow caller is wreathed in an aura of darkness while her shade inhabits her shadow,
gaining 50% [concealment](ref/rule/concealment) against creatures without
[darkvision](ref/rule/darkvision) or the
_[see in darkness](ref/carried/bestiary/rules/universal-monster-rules/see-in-darkness)_ ability.
Additionally, the shadow caller's square and all adjacent squares are treated as areas of dim
illumination while she benefits from this ability; this second effect counts as a 4th-level
_[darkness](ref/spell/darkness)_ spell for the purpose of adjudicating light and darkness effects.

**Replaces:** Fused consciousness

**Living Darkness (Su)**

**Flavor:** A shadow caller becomes a creature of absolute darkness.

**Gained:** At 20th Level

**Passive:** When using her incorporeal bonded manifestation, she is immune to cold and
mind-affecting effects.

**Replaces:** Empowered consciousness

**Standard:** She can use an incorporeal touch attack to deal 20d6 points of negative energy damage.
When the shadow caller damages a creature with this ability, she gains 5d6
[temporary hit points](ref/rule/temporary-hit-points) (Fortitude half; DC = 20 + her Wisdom
modifier), so long as she doesn't already have any temporary hit points gained via this ability).
Temporary hit points gained this way disappear after 1 hour.
