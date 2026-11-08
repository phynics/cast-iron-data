+++
id = "ref/arc-barbarian/geminate-invoker"
kind = "archetype"
title = "Geminate Invoker"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geminate_invoker", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]

[fields]
kind = "archetype"
replaces = ["Trap sense", "4th", "8th", "and 12th level rage powers"]
alters = ["The barbarian's class skills", "alignment", "Rage"]
+++

**Sources:** Adventurer's Guide pg 166\
Geminate invokers are barbarians who use [Rivethun](ref/rule/aff-animists) traditions to invite
spirits into their bodies. The spirits' aid enables them to overcome the distractions of the flesh:
they can ignore pain, and even defy death. These ascetics make up much of the Rivethun martial
forces.

**Contemplative (Ex)**

**Alters:** The barbarian's class skills, alignment

**Info:** Unlike most barbarians, a geminate invoker can be lawful, but must maintain a neutral
element to his alignment. A geminate invoker who ceases to be neutral-aligned cannot activate his
trance ability.

**Passive:** A geminate invoker adds [Knowledge (history)](ref/skill/knowledge-history),
[Knowledge (religion)](ref/skill/knowledge-religion), and [Linguistics](ref/skill/linguistics) (INT)
to his list of class skills.

**Trance (Ex)**

**Alters:** Rage

**Free:** A geminate invoker can enter a self-imposed trance, ignoring the physical limits of his
body. This ability functions similarly to a barbarian's _rage,_ except where noted below, and feats,
spells, and abilities that affect a barbarian's _rage_ (such as the
[Extra Rage](ref/feat/extra-rage) feat) apply to an geminate invoker's trance. Instead of the normal
_rage_ bonuses and penalties, a geminate invoker in a trance gains a +4 morale bonus to his
Constitution; gains a +2 morale bonus on Reflex and Will saving throws; takes no penalties to AC;
can still use Dexterity-, Intelligence-, and Charisma-based skills; and gains
[Diehard](ref/feat/diehard) as a bonus feat.

**Special:** The Constitution bonus increases to +6 and the save bonus increases to +3 when he gains
_greater rage,_ and they increase to a +8 Constitution bonus and a +4 bonus on saves when he gains
_mighty rage._ A geminate invoker gains rage powers as per a normal barbarian, but he can never gain
totem rage powers via this ability.

**Haunt Channeler (Su)**

**Ability:** A geminate invoker gains the power to sense and absorb lingering spiritual energy. This
functions identically to the [medium](ref/class/medium) class ability of the same name, except the
geminate invoker deals 1d6 points of damage to haunts for every 3 barbarian levels he has.

**Gained:** At 3rd Level

**Replaces:** Trap sense

**Haunt Channeler (Su)**

**Ability:** Your touch funnels a portion of the haunt into yourself, dealing 1d6 points of damage
to the haunt per \[3 barbarian levels\] you possess as if via positive energy and allowing you to
ask the haunt a single question. The haunt can answer the question however it chooses.

**Ability2:** Additionally, you can forgo your saving throw against a haunt's effects to funnel the
haunt entirely into yourself. If you do so, you suffer the haunt's full effect, but the haunt
doesn't affect anyone else (even if it normally would). The haunt then gains control of your body
for 24 hours. Once per minute, you can attempt to end this possession early by succeeding at a Will
save (DC = 20 + 1/2 your medium level).

**Flavor:** Text from the medium class

**Passive:** You can always act on the surprise round against a haunt.

**Spirit Conduit (Su)**

**Ability:** A geminate invoker can invite a spirit into his body each time he enters a trance,
gaining a lesser totem rage power for the duration of his trance. He can select a new totem each
time he enters his trance, though the GM might rule that certain totem spirits are simply not
available in certain locations (such as channeling a celestial totem in an evil god's temple).
Invoking a totem counter to his alignment (such as a neutral good character invoking a fiend totem)
requires the geminate invoker to succeed at a DC 12 Charisma check each round to dominate the
spirit. Failure indicates the spirit escapes, immediately ending the trance.

**At 12th Level:** He now also gains the _greater totem rage power_ that uses the previously granted
powers as prerequisites.

**At 8th Level:** The geminate invoker gains a second totem rage power, though it must use the
previously granted _lesser totem rage power_ as a prerequisite.

**Gained:** At 4th Level

**Replaces:** 4th, 8th, and 12th level rage powers
