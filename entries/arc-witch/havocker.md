+++
id = "ref/arc-witch/havocker"
kind = "archetype"
title = "Havocker"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Havocker"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "havocker", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "11"

[fields]
kind = "archetype"
replaces = ["1st-level hex", "All 2nd-level and higher hexes", "major hex", "grand hex"]
alters = ["Familiar"]
+++

Although most witches are guided to subtle curses and debilitating hexes by their mysterious
patrons, some are instead taught the secrets of harnessing raw, destructive elemental power.

**Patron Element**

**Ability:** The havocker gains the _elemental focus_ and _kinetic blast_ class features with the
associated element, using her witch level as her effective kineticist level.

**Alters:** Familiar

**Choice:** At 1st level, rather than selecting a standard patron and gaining patron spells, the
witch selects a specific [kineticist](ref/class/kineticist) [element](ref/ability/elements), which
represents the shadowy forces from which she gains her familiar and class powers.

**Flavor:** A havocker's patron grants her the ability to devastate her foes with a specific
element.

**Replaces:** 1st-level hex

**Special:** If the havocker takes levels in another class that grants an _elemental focus,_ the
_elemental focuses_ must be the same type, even if that means that the _elemental focus_ of one of
the classes must change. Subject to GM discretion, the havocker can change her former _elemental
focus_ to make them conform.

**Elemental Focus (Su)**

**Ability:** You gain your selected element's basic utility wild talent as a bonus wild talent.

**Flavor:** Relevant text from the kineticist class ability.

**Passive:** You choose one primary element on which to focus.

**Kinetic Blast (Sp)**

**Ability:** You gain a [kinetic blast wild talent](ref/ability/simple-kinetic-blasts) of your
choice. This kinetic blast must be a simple blast that matches your element.

**Action:** Special

**Flavor:** Relevant text from the kineticist class ability.

**Standard:** You can unleash a kinetic blast at a single target up to a range of 30 feet. You must
have at least one hand free to aim the blast (or one prehensile appendage, if you lack hands).

All damage from a kinetic blast is treated as magic for the purpose of bypassing
[damage reduction](ref/rule/damage-reduction).

Kinetic blasts count as a type of weapon for the purpose of feats such as
[Weapon Focus](ref/feat/weapon-focus). You are never considered to be wielding or gripping the
kinetic blast (regardless of effects from _form infusions_), and you can't use
[Vital Strike](ref/feat/vital-strike) feats with kinetic blasts.

Even the weakest kinetic blast involves a sizable mass of elemental matter or energy, so kinetic
blasts always deal full damage to swarms of any size (though only area blasts deal extra damage to
swarms).

A readied kinetic blast can be used to [counterspell](ref/rule/counterspells) any spell of equal or
lower level that shares its descriptor.

A kinetic blast that deals energy damage of any type (including force) has the corresponding
descriptor.

**Infusion**

**Ability:** The havocker gains an [infusion wild talent](ref/ability/infusion-wild-talents) from
the list of options available based on her elemental focus, functioning as the kineticist ability of
the same name. A havocker must meet the prerequisites of the infusion wild talent and can't accept
burn (but see the _spellburn_ ability below).

**Gained:** At 2nd Level

**Repeat:** She gains another infusion wild talent., 6, 4

**Replaces:** All 2nd-level and higher hexes, major hex, grand hex

**Infusion (Su)**

**Action:** Ability

**Flavor:** Relevant text from the kineticist class ability.

**Special:** When you modify a kinetic blast with a form infusion and a substance infusion that both
require saving throws, each target first attempts a saving throw against the form infusion. If a
target succeeds and a successful save negates the infusion's effects, the entire kinetic blast is
negated; otherwise, the target then attempts a saving throw against the substance infusion. If your
form and substance infusions both alter the kinetic blast's damage, apply the substance infusion's
alteration first.

You gain an [infusion wild talent](ref/ability/infusion-wild-talents) from the list of options
available based on your elemental focus.

By using infusions along with your kinetic blasts, you can alter your kinetic blasts to suit your
needs. Infusions come in two types, each of which changes a kinetic blast differently: a
**substance** infusion causes an additional effect, while a **form** infusion causes the kinetic
blast to manifest in a different way. Each infusion can alter only certain kinds of kinetic blasts,
which are listed in its Associated Blasts entry.

Each time you use one of your kinetic blast wild talents, you can apply up to one associated form
infusion and up to one associated substance infusion. Some infusions change the action required to
activate a kinetic blast or entirely transform the kinetic blast's normal effects. The burn cost
listed in each infusion's Burn entry is added to the burn cost of the kinetic blast the infusion
modifies.

The DC for a save against an infusion is based on the associated kinetic blast's effective spell
level, not the level of the infusion. The DCs for form infusions are calculated using your Dexterity
modifier instead of your Constitution modifier.

**Spellburn**

**Ability:** A havocker can channel stored spell energy into her kinetic blast to increase the
blast's overall utility and power. To use her infusions, the havocker must lose a prepared witch
spell to apply the infusion to her kinetic blast. Any spell sacrificed is required to have a spell
level equal to or greater than the infusion's effective spell level.

**Gained:** At 2nd Level

**Special:** The havocker cannot accept additional burn if the infusion would allow her to do so.
