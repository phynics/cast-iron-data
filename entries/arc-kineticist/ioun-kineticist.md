+++
id = "ref/arc-kineticist/ioun-kineticist"
kind = "archetype"
title = "Ioun Kineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Ioun%20Kineticist"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ioun_kineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "ioun-focus", level = 1 },
  { anchor = "ioun-cloud" },
  { anchor = "basic-iounkinesis" },
  { anchor = "ioun-buffer", level = 6 },
  { anchor = "personal-resonance", level = 6 },
  { anchor = "azlanti-blast" },
]
trades = [
  { replaces = "The ability score boosts granted by elemental overflow", feature = "elemental-overflow", by = ["personal-resonance"] },
  { alters = "Elemental focus", feature = "elemental-focus", by = ["ioun-focus"] },
  { replaces = "Basic telekinesis utility wild talent granted by the aether element", feature = "elemental-focus", power = "basic utility wild talent", by = ["basic-iounkinesis"] },
  { alters = "Internal buffer", feature = "internal-buffer", by = ["ioun-buffer"] },
]
+++

Among the greatest technologies to come from Azlant are ioun stones, small crystalline minerals
imbued with magical energies that modern scholars still struggle to dissect. Some kineticists
dedicate themselves to unlocking ioun stones' cosmic secrets and seemingly limitless potential.

## Ioun Focus {#ioun-focus}

An ioun kineticist must choose aether as her [elemental focus](ref/ability/elements). She cannot
select [disintegrating infusion](ref/kinetic/disintegrating-infusion),
[foe throw](ref/kinetic/foe-throw), or [force hook](ref/kinetic/force-hook) as infusions, nor can
she select [aether puppet](ref/kinetic/aether-puppet),
[telekinetic finesse](ref/kinetic/telekinetic-finesse),
[telekinetic haul](ref/kinetic/telekinetic-haul), or
[telekinetic invisibility](ref/kinetic/telekinetic-invisibility) as wild talents. She instead treats
the following infusions and wild talents as though they were part of the aether element:
[cyclone](ref/kinetic/cyclone), [fragmentation](ref/kinetic/fragmentation),
[jagged flesh](ref/kinetic/jagged-flesh), and
[rare metal infusion](ref/kinetic/rare-metal-infusion). These infusions can be applied to the ioun
kineticist's [telekinetic blast](ref/kinetic/telekinetic-blast) and Azlanti composite blast (see
below).

An ioun kineticist's telekinetic blast always sends one or more of her _ioun stones_ to strike her
foes and immediately return, and her wild talents typically manifest as her _ioun stones_ moving or
spinning to create fields of energy.

This alters elemental focus.

## Ioun Cloud (Su) {#ioun-cloud}

An ioun kineticist forms a powerful bond with three
_[dull gray ioun stones](ref/magic-ioun/dull-gray-stone)_, referred to as her ioun cloud. She begins
play with these stones at no cost, and she gains a bond with an additional free _dull gray ioun_
stone at 6th, 12th, and 18th levels. She also increases the AC of stones in her ioun cloud by an
amount equal to her class level, and she increases the [hardness](ref/umr/hardness) of these stones
by an amount equal to half her class level (minimum +0). An ioun kineticist cannot use her gather
power, ioun buffer, kinetic blast, or personal resonance class abilities unless she has at least one
bonded _ioun stone_ orbiting her. She takes a cumulative -2 penalty on
[concentration](ref/rule/concentration) checks for each bonded _ioun stone_ less than her possible
maximum in her current ioun cloud. When she uses her gather power class ability, her ioun cloud
buzzes, glows, spins rapidly, and traces eldritch symbols in the air.

While the ioun kineticist can own additional _ioun stones_ outside of this bond, only bonded _ioun
stones_ can be a part of her ioun cloud. An ioun kineticist can spend 1 hour meditating with an
_ioun stone_ to bond with it and add it to her ioun cloud, but doing so immediately unbonds and
removes one _ioun stone_ of her choice from her ioun cloud unless she is replacing an _ioun stone_
that has been lost or destroyed.

## Basic Iounkinesis (Su or Sp) {#basic-iounkinesis}

An ioun kineticist can manipulate _ioun stones_ with ease and channel their magical fields to create
simple effects. She can activate (making the stones orbit her) or stow a number of _ioun stones_
equal to her class level in any combination as a move action, and she can activate or stow twice as
many as a standard action. She can affect only _ioun stones_ orbiting her and unattended _ioun
stones_ within 15 feet with this ability. This ability also allows her to cast
_[prestidigitation](ref/spell/prestidigitation)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities).

This replaces the basic telekinesis utility wild talent granted by the aether element.

## Ioun Buffer (Su) {#ioun-buffer}

An ioun kineticist can store excess energy in her ioun cloud. This functions as the kineticist's
internal buffer ability, except she stores each point of burn within a different _ioun stone_ in her
ioun cloud. She can access the burn stored in an _ioun stone_ only if it is orbiting her.

When expending an _ioun stone's_ stored point of burn to reduce the cost of a blast wild talent, the
ioun kineticist can expend all of that _ioun stone's_ energy, permanently transforming it into a
_dull gray ioun stone_. If the _ioun stone's_ market price was at least 4,000 gp, this effect
further reduces the burn cost of that wild talent by 2. If the _ioun stone's_ market price was at
least 10,000 gp, it instead further reduces the burn cost by 3. If the _ioun stone's_ market price
was more than 20,000 gp, it instead further reduces the burn cost by 4.

This alters internal buffer.

## Personal Resonance (Su) {#personal-resonance}

At 6th level, an ioun kineticist can harmonize her body's energies with that of her ioun cloud.
Whenever she has at least 3 points of burn, she gains the resonant powers (_Pathfinder RPG
Adventurer's Guide_ 149) of two _ioun stones_ of her choice in her ioun cloud; she is treated as
holding a _[wayfinder](ref/magic-wondrous/wayfinder)_ for the purpose of using any resonant powers
(_Adventurer's Guide_ 148). As a standard action, she can switch which two _ioun stones_ are
granting their resonance powers. At 11th level, whenever she has at least 5 points of burn, she can
gain the resonance powers of up to four _ioun stones_ in her ioun cloud. At 16th level, whenever she
has at least 7 points of burn, she gains the resonance powers of all of the _ioun stones_ in her
ioun cloud.

In place of gaining the resonant power of a _deep rose sphere_,
_[incandescent blue sphere](ref/magic-ioun/incandescent-blue-sphere)_,
_[pale blue rhomboid](ref/magic-ioun/pale-blue-rhomboid)_,
_[pink and green sphere](ref/magic-ioun/pink-and-green-sphere)_,
_[pink rhomboid](ref/magic-ioun/pink-rhomboid)_, or
_[scarlet and blue sphere](ref/magic-ioun/scarlet-and-blue-sphere)_, the ioun kineticist can instead
increase the enhancement bonus it grants to an ability score to +4. This bonus increases to +5 at
11th level when she has at least 5 points of burn and increases to +6 at 16th level when she has at
least 7 points of burn. An ioun kineticist can increase only one _ioun stone's_ enhancement bonus in
this way at a time.

This replaces the ability score boosts granted by elemental overflow.

## Azlanti Blast (Su) {#azlanti-blast}

An ioun kineticist who selects aether as her expanded element does not gain the
[force composite blast](ref/kinetic/force-blast). She instead gains the Azlanti composite blast,
which costs 2 points of burn. An Azlanti blast is a physical blast that deals bludgeoning, piercing,
or slashing damage.
