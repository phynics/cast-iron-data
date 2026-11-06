+++
id = "ref/template/mummy-lord"
kind = "rule"
title = "Mummy Lord"
source_ids = ["bestiary-5"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mummy_lord", path = "json/monster_template3.json" },
]

[fields]
kind = "none"
+++

**Mummy Lord**

**Acquired:** present

**Challenge rating:** +2

**Source:** Bestiary 5/176

Many cultures practice the sacred art of mummification, though the sinister magical techniques used
to imbue corpses with undead vitality are far less widespread. In certain ancient lands, such
blasphemous techniques have been refined through centuries of ceremony and countless deaths, giving
rise to mummies of terrible power. On rare occasions, if the deceased was of great rank and
exceeding malevolence, he might undergo such elaborate rituals, rising from his tomb as a fearful
[mummy lord](ref/monster/mummy-lord). Similarly, a ruler known for his malice or who died in a
moment of great rage might spontaneously arise as such a vengeful despot. Regardless of the exact
circumstances of his resurrection, a mummy lord retains the abilities he had in life, becoming a
creature consumed by the desire to restore his rule and dominate both the living and dead.

"Mummy lord" is an acquired template that can be added to any living corporeal creature (referred to
hereafter as the base creature) that has at least 8 Hit Dice. The process of creating a mummy lord
requires 50,000 gp worth of rare herbs, oils, and other mummification materials. The mummy lord
retains all of the base creature's statistics and special abilities, except as listed below.

**CR:** Base creature's CR + 2.

**Alignment:** Any evil alignment.

**Type:** The creature's type changes to [undead](ref/type/undead)
([augmented](ref/subtype/augmented)). Do not recalculate its base attack bonus, saves, or skill
ranks.

**Senses:** A mummy lord gains [darkvision](ref/rule/darkvision) with a range of 60 feet.

**Aura:** A mummy lord gains the following aura.

> **Great Despair Aura (Su):** All creatures within a 30-foot radius that see a mummy lord must
> succeed at a Will saving throw or be [paralyzed](ref/rule/paralyzed) with fear for 1d4 rounds,
> then [shaken](ref/misc/shaken) for the following 1d4 rounds. Whether or not the saving throw is
> successful, that creature cannot be affected again by the same mummy lord's great despair aura
> ability for 24 hours. This is a mind-affecting paralysis and fear affect. The save DC is
> Charisma-based.

**AC:** A mummy lord has either a +1 natural armor bonus for every 2 Hit Dice it possesses or the
base creature's natural armor bonus, whichever of the two leads to a higher result.

**Hit Dice:** Change the creature's racial Hit Dice to d8s. All Hit Dice derived from class levels
remain unchanged. As undead, mummy lords use their Charisma modifiers to determine bonus hit points.

**Defensive Abilities:** A mummy lord gains [channel resistance](ref/umr/channel-resistance) +4, DR
10/-, immunity to cold and electricity (in addition to the immunities granted by its undead traits),
and the following defensive ability.

> **Rejuvenation (Su):** One day after a mummy lord is destroyed, the necromantic energies that
> created the abomination begin to rebuild its body. This process takes 1d10 days. If the body is
> destroyed before that time passes, the process starts anew. After this time, the mummy lord
> awakens fully healed in its tomb. To permanently destroy a mummy lord, it must be destroyed and
> then its remains must be targeted by [consecrate](ref/spell/consecrate),
> [hallow](ref/spell/hallow), and then [dispel evil](ref/spell/dispel-evil), cast in consecutive
> rounds and in that order.

**Attacks:** The mummification process hardens the mummy lord's bones to a stone-like density,
granting it a powerful [slam attack](ref/umr/natural-attacks) if the base creature has no other
natural attacks. This slam attack deals damage based on the mummy lord's size, treating the creature
as if it were one size category larger. Those hit by a mummy lord's slam attack also run the risk of
succumbing to insidious mummy rot (see Special Attacks below).

**Special Attacks:** A mummy lord gains the following special attacks. The attacks' save DCs are
equal to 10 + 1/2 the mummy lord's Hit Dice + the mummy lord's Charisma modifier unless otherwise
noted.

> **Channel Rot (Su):** A mummy lord can deliver its insidious mummy rot through melee weapon
> attacks, its slam attack, and any natural attacks it possesses.
>
> - [Affliction: Insidious Mummy Rot (Su)](ref/affliction/mummy-lord/insidious-mummy-rot-su)
>
> Insidious mummy rot is both a curse and disease, and can be cured only by first removing the curse
> and then curing the disease. Even after the curse element of insidious mummy rot is lifted, a
> creature suffering from it cannot recover naturally over time. Anyone casting a conjuration
> (healing) spell on the afflicted creature must succeed at a caster level check (DC = 20 or 11 +
> the mummy lord's CR, whichever is higher), or the spell is wasted and the healing has no effect.
> Anyone who dies from insidious mummy rot transforms into a pile of sand and cannot be raised by
> means other than [resurrection](ref/spell/resurrection) or greater magic.

**Sandstorm Wrath (Su):** Three times per day as a standard action, a mummy lord can exhale a blast
of superheated sand in a 40-foot cone. The blast deals 2d8 points of fire and slashing damage for
every 3 Hit Dice a mummy lord possesses. A successful Reflex save halves this damage. Creatures that
fail this save are [blinded](ref/misc/blinded) for 2d4 rounds.

**Undead Mastery (Su):** As a standard action, a mummy lord can attempt to bend any undead creature
within 50 feet to its will. The targeted undead must succeed at a Will save or fall under the mummy
lord's control (the save DC is Charisma-based). An undead with an Intelligence score is allowed an
additional save every day to break free of the mummy lord's control; for undead without an
Intelligence score, the control is permanent. A creature that succeeds at its Will save cannot be
affected again by the same mummy lord's undead mastery for 24 hours. A mummy lord can control 6 Hit
Dice of undead creatures for every Hit Die it has. If the mummy lord exceeds this limit, any excess
undead from earlier uses of this ability become uncontrolled, as per
[animate dead](ref/spell/animate-dead). If another creature is currently controlling an undead that
fails its save against undead mastery, the mummy lord must roll an opposed Charisma check against
the current controller. If the mummy lord succeeds, it wrests away control of the undead. Otherwise,
the mummy lord's undead mastery attempt has no effect.

**Ability Scores:** Strength +8, Charisma +6. As an undead creature, a mummy lord has no
Constitution score.

**Skills:** A mummy lord gains a +8 racial bonus on [Intimidate](ref/skill/intimidate),
[Sense Motive](ref/skill/sense-motive), and [Stealth](ref/skill/stealth) checks. It always treats
[Climb](ref/skill/climb), [Disguise](ref/skill/disguise), [Fly](ref/skill/fly), Intimidate,
[Knowledge (arcana)](ref/skill/knowledge-arcana),
[Knowledge (religion)](ref/skill/knowledge-religion), [Perception](ref/skill/perception), Sense
Motive, [Spellcraft](ref/skill/spellcraft), and Stealth as class skills. Otherwise, its skills are
the same as those of the base creature.

**Feats:** A mummy lord gains [Toughness](ref/feat/toughness) as a bonus feat.
