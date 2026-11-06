+++
id = "ref/arc-kineticist/ioun-kineticist"
kind = "archetype"
title = "Ioun Kineticist"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ioun_kineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]

[fields]
kind = "none"
+++

**Sources:** Blood of the Ancients pg 12\
Among the greatest technologies to come from Azlant are ioun stones, small crystalline minerals
imbued with magical energies that modern scholars still struggle to dissect. Some kineticists
dedicate themselves to unlocking ioun stones' cosmic secrets and seemingly limitless potential.

**Ioun Focus**

**Alters:** Elemental focus

**Info:** An ioun kineticist must choose aether as her [elemental focus](ref/ability/elements). She
cannot select [disintegrating infusion](ref/kinetic/disintegrating-infusion),
[foe throw](ref/kinetic/foe-throw), or [force hook](ref/kinetic/force-hook) as infusions, nor can
she select [aether puppet](ref/kinetic/aether-puppet),
[telekinetic finesse](ref/kinetic/telekinetic-finesse),
[telekinetic haul](ref/kinetic/telekinetic-haul), or
[telekinetic invisibility](ref/kinetic/telekinetic-invisibility) as wild talents. She instead treats
the following infusions and wild talents as though they were part of the aether element:
[cyclone](ref/kinetic/cyclone), [fragmentation](ref/kinetic/fragmentation),
[jagged flesh](ref/kinetic/jagged-flesh), and
[rare-metal infusion](ref/kinetic/rare-metal-infusion). These infusions can be applied to the ioun
kineticist's [telekinetic blast](ref/kinetic/telekinetic-blast) and _Azlanti composite blast_ (see
below).

**Special:** An ioun kineticist's telekinetic blast always sends one or more of her ioun stones to
strike her foes and immediately return, and her wild talents typically manifest as her ioun stones
moving or spinning to create fields of energy.

**Ioun Cloud (Su)**

**Ability:** An ioun kineticist forms a powerful bond with three
[dull gray ioun stones](ref/magic-ioun/dull-gray-stone), referred to as her _ioun cloud._ She begins
play with these stones at no cost. She also increases the AC of stones in her _ioun cloud_ by an
amount equal to her class level, and she increases the [hardness](ref/umr/hardness) of these stones
by an amount equal to half her class level (minimum +0). An ioun kineticist cannot use her _gather
power, ioun buffer, kinetic blast,_ or _personal resonance_ class abilities unless she has at least
one bonded ioun stone orbiting her. She takes a cumulative -2 penalty on
[concentration](ref/rule/concentration) checks for each bonded ioun stone less than her possible
maximum in her current _ioun cloud._ When she uses her _gather power_ class ability, her _ioun
cloud_ buzzes, glows, spins rapidly, and traces eldritch symbols in the air.

**Special:** While the ioun kineticist can own additional ioun stones outside of this bond, only
bonded ioun stones can be a part of her _ioun cloud._ An ioun kineticist can spend 1 hour meditating
with an ioun stone to bond with it and add it to her _ioun cloud,_ but doing so immediately unbonds
and removes one ioun stone of her choice from her _ioun cloud_ unless she is replacing an ioun stone
that has been lost or destroyed.

At 6th level: She gains a bond with a 4th free dull gray ioun.

At 12th level: She gains a bond with a 5th free dull gray ioun.

At 18th level: She gains a bond with a 6th free dull gray ioun.

**Basic Iounkinesis (Su or Sp)**

**Ability:** She can activate (making the stones orbit her) or stow a number of ioun stones equal to
her class level in any combination as a **move action**, and she can activate or stow twice as many
as a **standard action**. She can affect only ioun stones orbiting her and unattended ioun stones
within 15 feet with this ability. This ability also allows her to cast
[prestidigitation](ref/spell/prestidigitation) at will as a
[spell-like ability](ref/umr/spell-like-abilities).

**Alters:** Basic telekinesis utility wild talent granted by the aether element

**Flavor:** An ioun kineticist can manipulate ioun stones with ease and channel their magical fields
to create simple effects.

**Ioun Buffer (Su)**

**Ability:** An ioun kineticist can store excess energy in her _ioun cloud._ This functions as the
kineticist's _internal buffer_ ability, except she stores each point of burn within a different ioun
stone in her _ioun cloud._ She can access the burn stored in an ioun stone only if it is orbiting
her. When expending an ioun stone's stored point of burn to reduce the cost of a blast wild talent,
the ioun kineticist can expend all of that ioun stone's energy, permanently transforming it into a
dull gray ioun stone. If the ioun stone's market price was at least 4,000 gp, this effect further
reduces the burn cost of that wild talent by 2. If the ioun stone's market price was at least 10,000
gp, it instead further reduces the burn cost by 3. If the ioun stone's market price was more than
20,000 gp, it instead further reduces the burn cost by 4.

**Alters:** Internal buffer

**Personal Resonance (Su)**

**Ability:** Whenever she has at least 3 points of burn, she gains the resonant powers of two ioun
stones of her choice in her _ioun cloud;_ she is treated as holding a
[wayfinder](ref/magic-wondrous/wayfinder) for the purpose of using any resonant powers. As a
**standard action**, she can switch which two ioun stones are granting their resonance powers.

**Choice:** In place of gaining the resonant power of a
[deep red sphere](ref/magic-ioun/deep-red-sphere),
[incandescent blue sphere](ref/magic-ioun/incandescent-blue-sphere),
[pale blue rhomboid](ref/magic-ioun/pale-blue-rhomboid),
[pink and green sphere](ref/magic-ioun/pink-and-green-sphere),
[pink rhomboid](ref/magic-ioun/pink-rhomboid), or
[scarlet and blue sphere](ref/magic-ioun/scarlet-and-blue-sphere), the ioun kineticist can instead
increase the enhancement bonus it grants to an ability score to +4. An ioun kineticist can increase
only one ioun stone's enhancement bonus in this way at a time.

**Flavor:** An ioun kineticist can harmonize her body's energies with that of her ioun cloud.

**At 11th Level:** Whenever she has at least 5 points of burn, she can gain the resonance powers of
up to four ioun stones in her _ioun cloud,_ and the bonus she can get from certain ioun stones
becomes +5.

**At 16th Level:** Whenever she has at least 7 points of burn, she gains the resonance powers of all
of the ioun stones in her _ioun cloud,_ and the bonus she can get from certain ioun stones becomes
+6.

**Gained:** At 6th Level

**Replaces:** The ability score boosts granted by _elemental overflow_

**Azlanti Blast (Su)**

**Ability:** An ioun kineticist who selects aether as her _expanded element_ does not gain the
[force composite blast](ref/kinetic/force-blast). She instead gains the _Azlanti composite blast,_
which costs 2 points of burn. An _Azlanti blast_ is a physical blast that deals bludgeoning,
piercing, or slashing damage.
