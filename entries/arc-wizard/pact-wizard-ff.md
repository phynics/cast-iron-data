+++
id = "ref/arc-wizard/pact-wizard-ff"
kind = "archetype"
title = "Pact Wizard (FF)"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Pact%20Wizard%20%28FF%29"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pact_wizard_ff", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "familiar-folio"
page = "8"

[fields]
kind = "archetype"
alters = ["Arcane bond", "Arcane school"]
alters_features = ["arcane-bond", "arcane-school"]
+++

Some wizards make bargains with beings from other realms in order to gain arcane power. These pact
wizards have unparalleled access to extraplanar allies, but these bonds never come without strings
attached.

**Familiar (Ex)**

**Alters:** Arcane bond

**Info:** A pact wizard must select a [familiar](ref/ability/familiars) for his _arcane bond._ The
familiar's loyalty ultimately lies with the pact wizard's patron, and it reports back to the patron
on the wizard's activities.

**Pact Focus (Ex)**

**Alters:** Arcane school

**Info:** A pact wizard must choose one additional opposition school, even if he is a universalist.
A pact wizard can't pick [conjuration](ref/arcaneschool/conjuration) as an opposition school.

**Gained:** At 1st Level

**Pact (Ex)**

**Flavor:** A pact wizard enters into a bargain with an extraplanar being in order to gain increased
wizardly powers.

**At 1st Level:** The wizard selects a patron belonging to one specific subtype of outsider for
which there exists an [improved familiar](ref/feat/improved-familiar) option (such as devil or
azata). The pact wizard can select a subtype of outsider even with a diametrically opposed
alignment; in this case, the patron being offers the pact in an attempt to tempt or redeem the pact
wizard.

**Special:** A pact wizard whose alignment shifts away from the chosen outsider subtype, who grossly
abuses his familiar or any outsider of the chosen subtype, or who commits egregious acts against the
alignment of the patron loses all the benefits of this archetype (but keeps the additional
opposition school) until he receives an [atonement](ref/spell/atonement).

**Aura (Ex)**

**Passive:** A pact wizard has an aura corresponding to the alignment of his chosen subtype as a
cleric of his wizard level.

**Aura (Ex)**

**Flavor:** Text from the cleric class ability.

**Passive:** If you are a cleric of a chaotic, evil, good, or lawful deity, you have a particularly
powerful aura corresponding to your deity's alignment (see [detect evil](ref/spell/detect-evil)).

**Pact Summons (Ex)**

**Ability:** A pact wizard can select [Sacred Summons](ref/feat/sacred-summons) as a wizard bonus
feat. He can use this feat only to summon outsiders of his chosen subtype.

**True Form (Ex)**

**Ability:** A pact wizard's familiar reveals its true form, automatically transforming into an
outsider improved familiar of the chosen subtype.

**Gained:** At 7th Level
