+++
id = "ref/arc-investigator/malice-binder"
kind = "archetype"
title = "Malice Binder"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "malice_binder", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]

[fields]
kind = "archetype"
replaces = ["Trapfinding", "trap sense", "Alchemy", "Poison resistance", "Poison immunity"]
alters = ["Inspiration"]
+++

**Sources:** Blood of the Coven pg 28\
A lock of hair, a bit of blood, even a footprint is enough to grant a wily witch hunter an edge.
Malice binders often rise from the ranks of the common folk rather than from wealthy nobles or the
church. Their magic is old and crude, but devastatingly effective against those they hunt.

**Witch Lore (Ex)**

**Ability:** A malice binder can use _inspiration_ on Knowledge (arcana), Spellcraft, Sleight of
Hand, and Survival checks without expending a use of _inspiration,_ provided he is trained in the
skill, rather than on any Knowledge and Linguistics checks.

**Alters:** Inspiration

**Flavor:** Malice binders hunt and kill those who would plague the world with supernatural power.

**Special:** He can later spend an **investigator talent** to gain the ability to use _inspiration_
on any Knowledge and Linguistics checks.

**Take a Bit (Ex)**

**At 1st Level:** The malice binder gains [Improved Steal](ref/feat/improved-steal) as a bonus feat.

**At 3rd Level:** He can use _inspiration_ to improve a steal combat maneuver check by spending one
use of _inspiration_ rather than two.

**Replaces:** Trapfinding, trap sense

**Fettering (Su)**

**Action:** Ability

**At 7th Level:** The malice binder can prepare a token as a **swift action**.

**Replaces:** Alchemy

A malice binder forgoes alchemy for the study of sympathetic magic that allows him to hinder foes.
Fetters rely on the magical resonance of creatures capable of casting spells (spellcasters and
creatures with [spell-like abilities](ref/umr/spell-like-abilities)) which saturates even their hair
and clothing. Fetters cannot target a creature with no magical ability.

Every fetter requires a token taken from his desired target: a few hairs, a lost tooth, nail
clippings, a scrap of clothing, or a small treasured possession with some significance. An
investigator can obtain a single token in any of the following ways: a successful Sleight of Hand
check against an unsuspecting target, a successful [steal](ref/rule/steal) combat maneuver, or a
successful Perception check (DC = 15 + the creature's CR) to search an area his target occupied for
at least 2 hours. Malice binders can search such a location for additional tokens, but each
subsequent Perception check increases the DC by 5, regardless of success or failure. Tokens rely on
the magic that clings to spellcasters and creatures with
[spell-like abilities](ref/umr/spell-like-abilities); they must be carefully preserved as soon as
they are recovered and before they can be used. Preparing a token requires a **move action**, and a
malice binder can maintain one prepared token per class level. Each token can be used only to power
a fetter targeting the creature it came from, and it is consumed in the process.

The DC to resist a fetter is equal to 10 + half the investigator's class level + the investigator's
Charisma bonus. Activating a fetter is a **standard action** that provokes attacks of opportunity,
and unless otherwise stated the target must be within 30 feet, plus 5 feet per 2 levels. Once a
creature has been the target of a specific fetter, it is immune to that effect for 24 hours.

The malice binder knows one fetter at 1st level and gains another at 4th level and every 2 levels
thereafter.

**Divine Dread (Su)**

**Ability:** Binding a token to a holy symbol anathema to the target fills the creature with
supernatural dread, imposing the [shaken](ref/misc/shaken) condition for 1 round per class level.

**At 11th Level:** The target becomes [panicked](ref/misc/panicked) instead.

**At 6th Level:** The target is [frightened](ref/misc/frightened) instead.

**Special:** On a successful Will saving throw, the target is instead shaken for a single round.

**Hexing Shield (Su)**

**Ability:** By placing a token between two shiny copper coins and then putting them in a creature's
mouth, the malice binder can ward himself or others. This fetter grants whoever holds it in his
mouth a +2 resistance bonus on Will saving throws against the target's spells, supernatural
abilities, and [spell-like abilities](ref/umr/spell-like-abilities). The fetter lasts 10 minutes per
class level, but whoever holds it in his mouth cannot eat, drink, speak, or cast spells with verbal
components without ending the effect early.

**Special:** The malice binder can have only one hexing shield active at a time.

At 4th level: The bonus +2.

At 7th level: The bonus +3.

At 10th level: The bonus +4.

At 13th level: The bonus +5.

At 16th level: The bonus +6.

At 19th level: The bonus +7.

**Incapacitate (Su)**

**Ability:** By rubbing soot into a token, the malice binder clouds his target's senses or stifles
the target's tongue. This fetter [deafens](ref/misc/deafened) or silences the target for 1 round per
2 class levels (minimum 1 round). Silenced creatures cannot speak or cast spells with verbal
components, but they are otherwise unrestricted from making sounds.

**At 6th Level:** A malice binder can either [blind](ref/misc/blinded) his target or both silence
and deafen it.

**Special:** On a successful Will saving throw, the target is instead [dazzled](ref/misc/dazzled)
for a single round.

**Repulse (Su)**

**Ability:** By binding a token to a bit of rancid meat, the malice binder can impede his target's
approach. Once activated, this fetter forces its target to spend twice the normal amount of movement
to approach the fetter while within range of its effect; it does not affect the target's ability to
move away.

**At 11th Level:** The fetter's target cannot physically approach within 10 feet of the fetter, as
if affected by a [repulsion](ref/spell/repulsion) spell.

**Special:** This fetter remains active for 1 minute per class level and can be handed to another
creature or left somewhere to ward against a witch's entry. A target can overcome this effect with a
successful Will saving throw when the fetter is first activated.

**Salting Wounds (Su)**

**Ability:** The malice binder can rub salt into a wound - his own or that of an adjacent ally -
treating the wound as a token to protect the injured creature from the danger that threatens it.
This fetter grants a deflection bonus to AC against attacks from the creature that caused the
original wound, which is treated as the fetter's target for the purposes of how often it can be
used. The deflection bonus is equal to 2 + [one-fifth](ref/misc/fractions-and-rounding) of his
investigator level.

**Special:** This fetter is painful to whom it protects, [sickening](ref/misc/sickened) the
protected creature while the fetter remains in effect.

**Shackle (Su)**

**Ability:** Binding a token to manacles or a length of rope causes the restraints to fly out and
entangle the target. A target can avoid this fetter with a successful Reflex save. An
[entangled](ref/rule/entangled) target can attempt to escape as a **standard action** with either an
Escape Artist check or a combat maneuver check using the same DC as the initial saving throw.

**Special:** Using [masterwork manacles](ref/eq-misc/manacles-masterwork) in this fetter increases
the escape DC by 2.

**Temptation (Su)**

**Ability:** Anointing a token with incense or scented oils creates a supernaturally appealing
object to attract a target's attention. Once activated, this fetter lasts for 1 minute per class
level. If the target approaches within the fetter's area of effect, it is compelled to approach the
fetter and pick it up; the compulsion can be negated with a successful Will save. This effect ends
immediately if the target picks up the fetter or the fetter moves more than 30 feet plus 5 feet per
2 levels away from the target.

**At 11th Level:** The fetter [fascinates](ref/misc/fascinated) its target once picked up, affecting
it as if by the spell [hypnotism](ref/spell/hypnotism) for 1 round per class level; this fetter is
not limited by the target's Hit Dice.

**Witch Compass (Su)**

**Ability:** Placing a token on top of a compass causes the needle to point toward the malice
binder's target for 1 hour per class level, granting a +10 circumstance bonus on Survival checks to
track that creature. The target must be within 1 mile per class level, or else the needle spins
aimlessly.

**Wrack (Su)**

**Ability:** The binder can drive an iron nail through a token to leave his target sickened with
pain until the end of the malice binder's next turn.

**At 6th Level:** The target is instead [staggered](ref/misc/staggered) until the end of the malice
binder's next turn. The target can negate this fetter with a successful Fortitude save.

**Special:** For this fetter, a binder can use a clear footprint as a token; finding an appropriate
footprint requires a successful Survival skill check to track the target.

**Take a Bit More (Ex)**

**Ability:** He gains [Quick Steal](ref/feat/quick-steal) as a bonus feat. When attempting to steal
a token, he gains a +2 competence bonus on combat maneuver checks.

**Flavor:** Taking a bit of clothing or hair to use as a token becomes second nature for the malice
binder.

**Gained:** At 8th Level

**Replaces:** Poison resistance

**Witch Trapper (Ex)**

**Ability:** Whenever the malice binder would gain a fetter, he can instead select a ranger trap,
treating his investigator level as his ranger level for the purpose of determining the trap's
effect.

**Gained:** At 11th Level

**Replaces:** Poison immunity
