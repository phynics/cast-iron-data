+++
id = "ref/monster/clockwork-clockwork-overseer"
kind = "creature"
title = "Clockwork Overseer"
aon = "MonsterDisplay.aspx?ItemName=Clockwork%20Overseer"
source_ids = ["pathfinder-123-the-flooded-cathedral"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "clockwork_clockwork_overseer", path = "json/monsters05.json" },
]
[[sources]]
publication = "pathfinder-123-the-flooded-cathedral"
page = "86"

[fields]
kind = "creature"
cr = "7"
creature_type = "construct"
subtypes = ["clockwork"]
size = "medium"
alignment = "neutral"
ac = "21/14/17"
hp = "75~10d10+20"
fortitude = "+4"
reflex = "+8"
will = "+5"
melee = "lash +15 (1d4+5 plus trip), slam +15 (1d6+5 plus push)"
special_attacks = "overclock"
special_qualities = "swift reactions, tactical calculus, winding"
abilities = ["19", "14", "-", "-", "13", "1"]
+++

_One arm of this six-limbed clockwork construct ends in a broad fist, and the other extends into an
articulated metal lash._

**Clockwork Overseer**

**Challenge rating:** 7

**aura:** aura of command (30 ft.)

**Type:** construct

**Initiative:** +6

**Size:** medium

**Alignment:** Neutral

**Perception:** +1

**Senses:** All-around vision, Darkvision 60 ft., Low-light vision

**Subtype:** Clockwork

**Experience points:** 3,200

**Armor class:** 21/14/17

**Dr:** 5/adamantine

**Fort:** +4

**Hit points:** 75 (10d10+20)

**Immune:** [construct traits](ref/umr/construct-traits)

**Mod:** +2 Dex, +2 dodge, +7 natural

**Ref:** +8

**Vulner:** electricity

**Will:** +5

**Offense**

**Speed:** 30 ft., climb 30 ft.

**Melee:** lash +15 (1d4+5 plus [trip](ref/umr/trip)), slam +15 (1d6+5 plus push)

**Push:** slam, 10 ft.

**Reach:** 5

**Reach P:** 10 ft. with lash

**Space:** 5

**Spec Att:** overclock

**Statistics**

**Ability scores:** Str 19, Dex 14, Con -, Int -, Wis 13, Cha 1

**Base attack bonus:** +10

**Combat maneuver bonus:** +15

**Combat maneuver defense:** 29

**Feats:** Improved Initiative^B^, Lightning Reflexes^B^

**Skills:** Climb +12

**Special qualities:** swift reactions, tactical calculus, winding

###### B {#footnote-b}

Bonus feat.

**Ecology**

**Environment:** any land

**Organization:** solitary, crew (1 plus 2-5
[clockwork servants](ref/monster/clockwork-clockwork-servant)), or deployment (1-2 plus 2-5
[clockwork soldiers](ref/monster/clockwork-clockwork-soldier))

**Treasure:** None

### Special Abilities

**Aura of Command (Ex)** A clockwork overseer broadcasts subtle commands in a 30-foot radius,
granting heightened combat abilities to all clockwork creatures in the area. Affected clockwork
creatures, including the clockwork overseer, gain a +1 competence bonus on saving throws, attack
rolls, and weapon damage rolls; these bonuses are already calculated into the clockwork overseer's
statistics. As a standard action, a clockwork overseer can intensify the aura until the beginning of
its next turn, increasing the competence bonus to +2.

**Lash (Ex)** A clockwork overseer's lash is a primary natural attack that deals bludgeoning damage.

**Overclock (Ex)** In place of making a lash attack on its turn, a clockwork overseer can overclock
another clockwork creature within its reach, impelling it to exceed its performance limitations. At
the beginning of its turn, an overclocked creature takes an amount of damage equal to half its Hit
Dice (minimum 1), expends 1 full day of activity stored by its winding ability, and gains one of the
following benefits, selected by the clockwork overseer.

- The overclocked creature gains the benefits of [haste](ref/spell/haste).
- The overclocked creature's natural attacks and attacks with metal melee weapons deal an additional
  1d6 points of fire damage. If the creature already deals fire damage, including with a
  [breath weapon](ref/umr/breath-weapon) or the [swallow whole](ref/umr/swallow-whole) ability, that
  special attack's fire damage increases by 2d6.
- The overclocked creature gains [Combat Reflexes](ref/feat/combat-reflexes) as a bonus feat and
  gains a +2 bonus on attack rolls when making attacks of opportunity.

A clockwork overseer can end this effect on a clockwork creature affected by its aura of command as
a free action. The overclocked condition otherwise continues until the clockwork creature expends
its stored days of activity or is destroyed.

**Tactical Calculus (Ex)** A clockwork overseer can store hundreds of commands and scripts, allowing
it to perform modest feats of problem-solving and strategic command as though it had an Intelligence
score of 10. In practice, this enables a clockwork overseer to make tactical decisions, such as
exploiting terrain or flanking targets, as well as convey simple tactical commands to other
clockwork creatures in its aura of command. If the clockwork overseer takes electricity damage, it
must succeed at a Fortitude save (DC = the electricity damage dealt) or lose both its aura of
command and tactical calculus abilities for 1d4 rounds.

### Description

What clockwork creatures boast in both strength and resilience, they often lack in nuance and
strategy. Most machinists are content to command their constructs directly when seeking tactical
precision, but only a few artificers have the technical expertise needed to create a mechanical
lieutenant capable of reasoning and adapting in its master's absence. Known as clockwork overseers,
these constructs boast extraordinarily complex programming that far exceeds the basic command
vocabulary of other clockwork creatures. This allows clockwork overseers to store hundreds or even
thousands of commands, which they can parse and sort quickly enough to simulate an intelligent
creature's adaptive thinking - at least regarding combat strategy and moderately complex tasks of
coordinating construct laborers. These functions fall short of true thought, and clockwork overseers
are incapable of language, emotion, higher thinking, or symbolic reasoning beyond specific sounds
and statements they might parrot on command.

**Family:** [Clockwork](ref/family/clockwork)

### Ecology

Like most clockwork creatures, clockwork overseers are finely tuned creations of metal, gears, and
magic, but they differ in two major regards: their mechanical "brains" and their kinetic generators.
The complex inner workings of a clockwork overseer's programming core are an order of magnitude more
complicated that those of its counterparts, composed of delicate arrays of counters, springs,
toggles, and other perfectly fitted components that collectively store and compute data.

Clockwork overseers can compel even greater feats from their subordinates, though doing so requires
direct contact between the constructs via the overseer's lash to convey an electrical charge. This
electricity builds over time, accumulated by static energy discharges created by the movement of
limbs and gears. Most clockwork creatures respond readily to this electrical goading, overriding
their standard operating specifications based on the exact combination of current and voltage the
overseer conveys. Clockwork overseers harness and exploit electricity in small amounts, but they're
as vulnerable as other clockwork creatures to massive discharges - arguably more so, since such
attacks can scramble an overseer's decision-making hardware and temporarily reduce it to a truly
mindless state.

Numerous cultures and machine schools have built clockwork overseers over the ages, emphasizing
different martial techniques in the process. These variant clockwork overseers can grant a different
combat feat - typically one for which they qualify - to their minions. What's more, these overseers
sometimes represent the last record of otherwise extinct fighting styles; a creature with the
[Craft Construct](ref/feat/craft-construct) feat or that succeeds at a DC 21 Craft (clockwork) or
Knowledge (engineering) check can spend 8 hours deciphering an overseer's mechanical "brain" in
order to decode the stored combat feat, using this new knowledge as the basis to learn the feat or
teach it to others.

### Habitat

Since they are artificial constructs, clockwork overseers almost always exist because either a
skilled artificer or a machinist created them. The creator typically already owns several other
clockwork creatures and needs a capable, tireless entity to direct them. As a result, a clockwork
overseer is only rarely encountered alone, unless attrition, misfortune, or time have destroyed its
entourage.

Under rare circumstances - especially involving areas of sustained magical energy - an overseer can
independently learn new tricks or even develop self-awareness. These creatures often commandeer
other clockwork creatures, creating tiny fiefdoms dedicated to building new wonders or helping the
overseer attain true sentience. The faithful of [Brigh](ref/faith/brigh) seek out such awakened
constructs, considering it their duty to protect and guide these mechanical "children."

### Construction

The creator of a clockwork overseer must start with crafted clockwork pieces worth 2,000 gp.

**CL** 12th; **Price** 42,000 gp\
**Requirements** Craft Construct, [geas/quest](ref/spell/geas-quest) and _[haste](ref/spell/haste),_
creator must be at least caster level 12th; **Skill** Craft (clockwork) DC 20; **Cost** 22,000 gp
