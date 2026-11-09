+++
id = "ref/spell/baleful-shadow-transmutation"
kind = "spell"
title = "Baleful Shadow Transmutation"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "baleful_shadow_transmutation", path = "json/spells12.json" },
]
[[sources]]
publication = "blood-of-shadows"
page = "30"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Druid", level = 7 },
  { class = "Investigator", level = 6 },
  { class = "Medium", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent"
saving_throw = "Will disbelief, then Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Alchemist, Arcanist, Bard, Investigator, Medium, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Witch, Wizard\
7: Druid
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will disbelief, then Fortitude negates
Spell resistance: yes
Target: one creature
Subschool: Shadow
Descriptors: shadow
:::

You infuse a target's shadow with energies from the Shadow Plane, shaping the shadow into one that
appears to belong to a different creature, and tricking the target into believing it actually is
that creature. When you cast this spell, choose one Huge or smaller creature of the animal type or
one Medium or Small creature of the humanoid type. If the chosen creature is ill suited to the
target's current environment, such as an aquatic creature not in water, the subject gains a +4 bonus
on all saving throws against baleful shadow transmutation. If the subject fails its Will save, it
believes that it is the chosen creature, causing it to lose its extraordinary, supernatural, and
[spell-like abilities](ref/umr/spell-like-abilities), lose its ability to cast spells (if it had the
ability), and gain the alignment, special abilities, and Intelligence, Wisdom, and Charisma scores
of its new form in place of its own. It retains any class features (other than spellcasting) that
aren't extraordinary, supernatural, or spell-like abilities.

When the subject is first targeted by this spell, and once every 24 hours thereafter, the subject
must attempt a Will save in order to disbelieve this effect. If the save succeeds, the spell's
effect ends. The first time the subject fails this save, it must also attempt a Fortitude save. If
it also fails this Fortitude save, the subject permanently assumes the form of the chosen animal or
humanoid, as per polymorph. This is a polymorph effect. Successfully disbelieving the spell returns
the subject to its true form. If the subject fails its Fortitude save against the effects of baleful
shadow transmutation, any further polymorph effects cast on the target automatically fail.

Incorporeal or gaseous creatures are immune to baleful shadow transmutation, and a creature with the
shapechanger subtype can revert to its natural form as a standard action.
