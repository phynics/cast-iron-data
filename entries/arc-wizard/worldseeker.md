+++
id = "ref/arc-wizard/worldseeker"
kind = "archetype"
title = "Worldseeker"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Worldseeker"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "worldseeker", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "planar-adventures"
page = "21"

[fields]
kind = "archetype"
replaces = ["Scribe Scroll", "The school ability normally gained at 6th or 8th level", "5th-level bonus feat", "15th-level bonus feat"]
alters = ["Arcane bond"]
+++

Worldseekers are wizards who travel to all corners of the Great Beyond. While neophytes must content
themselves with study and practice, the most powerful worldseekers are movers and shakers throughout
the Great Beyond, power players of whom even demigods take note. Worldseekers are rare sights on
Golarion, but among those few, more are trained in Kyonin and Nex than any other nation; those in
Kyonin explore the potential of using elf gates to travel beyond this realm, while those in Nex
emulate some of the dimensional exploits of Nex's legendary founder.

Most worldseekers prefer not to specialize in a school of magic, for having a diverse array of
available spells is a boon when exploring the countless wonders of the Great Beyond. Those who do
specialize usually do so as [conjurers](ref/arcaneschool/conjuration). Conjuration is a poor choice
of oppositional school for a worldseeker.

**Walk the Planes (Sp, Su)**

**Flavor:** A worldseeker learns every plane's place in the Great Beyond and trains to survive even
on the harshest of them.

**Passive:** She gains a +2 bonus on Knowledge (planes) checks and is constantly under the effects
of [endure elements](ref/spell/endure-elements).

**Replaces:** Scribe Scroll

**Planar Adaptation (Su)**

**At 15th Level:** She can extend that benefit to all allies within 30 feet of her.

**At 8th Level:** A worldseeker is continually protected from planar environments as by
[planar adaptation](ref/spell/planar-adaptation).

**Replaces:** The school ability normally gained at 6th or 8th level

**Planar Associates (Ex)**

**Alters:** Arcane bond

**At 11th Level:** She automatically learns [planar ally](ref/spell/planar-ally) as a 6th-level
wizard spell.

**At 15th Level:** She automatically learns [greater planar ally](ref/spell/planar-ally-greater) as
an 8th-level wizard spell.

**At 5th Level:** She gains [Improved Familiar](ref/feat/improved-familiar) as a bonus feat and must
choose an outsider familiar that matches her alignment exactly; she can choose an outsider in this
way even if it normally requires a 7th-level spellcaster as its master.

**At 7th Level:** A worldseeker automatically learns
[lesser planar ally](ref/spell/planar-ally-lesser) as a 4th-level wizard spell.

**Info:** A worldseeker's travels and dealings across the planes allow her to make connections she
can call upon when necessary to gain assistance without needing to resort to
[planar binding](ref/spell/planar-binding). A worldseeker must choose a
[familiar](ref/ability/familiars) for her _arcane bond._

**Replaces:** 5th-level bonus feat

**Special:** She can swap out a prepared spell of an equal spell level to spontaneously cast any of
the three bonus spells (one 4th-level spell for
_[lesser planar ally](ref/spell/planar-ally-lesser),_ a 6th-level spell for
_[planar ally](ref/spell/planar-ally),_ and a 8th level spell for
_[greater planar ally](ref/spell/planar-ally-greater)_).

The first time each day she casts one of these three spells, the worldseeker reduces the gp value of
the material component cost by an amount equal to her caster level &times& 100 (to a minimum cost of
0 gp).

**Planar Redoubt (Sp)**

**Ability:** A worldseeker creates a _planar redoubt,_ a personal demiplane to which she can retreat
to rest and plan. This functions like [lesser create demiplane](ref/spell/create-demiplane-lesser),
except the demiplane is up to a single 50-foot cube in size and is permanent.

**Gained:** At 15th Level

**Replaces:** 15th-level bonus feat
