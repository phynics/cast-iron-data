+++
id = "ref/arc-arcanist/twilight-sage"
kind = "archetype"
title = "Twilight Sage"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twilight_sage", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-origins"
page = "6"

[fields]
kind = "archetype"
replaces = ["Consume spells", "The arcanist exploit gained at 11th level", "Magical supremacy"]
alters = ["The arcanist exploit gained at 1st level"]
+++

The twilight sages of Geb carry out experiments to solve the ultimate puzzle and unlock the secrets
of life and death. While the twilight sages generally aren't actively malicious, most are willing to
perform human experimentation in pursuit of knowledge with little regard for the casualties.

**Consume Life (Su)**

**Flavor:** By wresting a soul from life to death, a twilight sage gains a slightly deeper
understanding of mortality, fueling her curiosity and eldritch power.

**Fullround:** She can consume the life energy of a helpless living creature, killing it. This
creature must have 2 or more Hit Dice and be below 0 hit points. The twilight sage adds 2 points to
her _arcane reservoir_ if the creature's Hit Dice equaled or exceeded the sage's character level, or
1 point if the creature's Hit Dice equaled at least [half](ref/misc/fractions-and-rounding) her
character level. This ability is a death effect.

**Replaces:** Consume spells

**Necromantic Focus (Ex)**

**Info:** Twilight sages consider their research into life and death to be paramount, beyond all
other concerns. Each day, a twilight sage must prepare at least one necromancy spell of each spell
level she can cast.

**Twilight Barrier (Ex)**

**Ability:** A twilight sage must choose the [arcane barrier](ref/exploit/arcane-barrier) exploit as
her first arcanist exploit. Whenever an attack removes the last temporary hit point from the
twilight sage's arcane barrier, the barrier's negative energy lashes back at the attacker, dealing
an amount of negative energy damage equal to the barrier's maximum temporary hit point capacity.

**Alters:** The arcanist exploit gained at 1st level

**Flavor:** A twilight sage's arcane barrier differs from those of other arcanists, as it draws upon
both negative and positive energy to protect the sage.

**Gained:** At 1st Level

**Twilight Transfer (Su)**

**Ability:** Once per day, she can expend 1 point from her arcane reservoir while touching a
creature that died within the past round to affect that creature as if it had received a
[breath of life](ref/spell/breath-of-life) spell, using her arcanist level as the caster level. At
the same time, a willing or unconscious living creature within 300 feet that has a number of Hit
Dice equal to or greater than the recipient's instantly dies. This ability is a death effect, and if
the victim doesn't actually die (such as if it was summoned or is immune to death effects), the
recipient doesn't receive the _[breath of life](ref/spell/breath-of-life)_ effect.

**Flavor:** A twilight sage's mastery over life and death allows her to transfer life energy into a
fading vessel.

**Gained:** At 11th Level

**Replaces:** The arcanist exploit gained at 11th level

**Death's Release (Su)**

**Flavor:** A twilight sage has mastered the relationship between death and arcane power, and has
gained a limited ability to surpass her own mortality.

**Gained:** At 20th Level

**Passive:** Whenever she dies (but not if she becomes undead), if she still has points in her
arcane reservoir she appears as an ephemeral spirit in the air above her corpse. She can still cast
spells in this form, using her corpse as the origin point and determining whether she can see or
target any creature or area as though she were alive in that square. To cast a spell, she must
expend a number of points from her arcane reservoir equal to 1 + the spell's level.

**Replaces:** Magical supremacy

**Special:** The spirit disappears if she has no points remaining in her arcane reservoir or she
spends a round without casting a spell. The spirit can't move, deliver touch or ranged touch spells,
or do anything that isn't part of casting a spell. Her spirit completes the verbal and somatic
components of her spells, any material components are consumed from the supply on the corpse, and
any focus components must be on the corpse.
