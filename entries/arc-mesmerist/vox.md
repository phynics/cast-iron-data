+++
id = "ref/arc-mesmerist/vox"
kind = "archetype"
title = "Vox"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vox", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "39"

[fields]
kind = "archetype"
replaces = ["Towering ego, 10th-level mesmerist trick", "touch treatment (break enchantment)", "Touch treatment (minor)", "touch treatment (moderate)", "Touch treatment (major)"]
alters = ["Spellcasting", "Hypnotic stare"]
+++

Most mesmerists practice their mental manipulation through their entrancing gaze, but others have
learned to practice their skill through the lilt and intonation of their voice. From sibilant
whispers to overwhelming imprecations that resonate with the force of pure will, a vox unleashes the
power of his mind with every silken syllable and shattering shout.

**Spells**

**Alters:** Spellcasting

**Info:** A vox adds the following spells to his class list.

**Replaces:** Towering ego, 10th-level mesmerist trick, touch treatment (break enchantment)

**Spells:** Ear-piercing scream

**Spells:** Cacophonous call, disrupt silence, distracting cacophony, piercing shriek, sonic scream

**Spells:** Shout, sonic thrust, wall of sound

**Spells:** Mass cacophonous call, echolocation, resonating word

**Spells:** Magnifying chime, greater shout, sonic form

**Special:** Unlike most psychic spells, a vox's mesmerist spells use both thought and verbal
components; like a [bard](ref/class/bard), a vox cannot remove the verbal components of his spells.

**Compelling Voice (Su)**

**Alters:** Hypnotic stare

**Special:** A vox can use his _compelling voice_ even while [deafened](ref/misc/deafened), but it
has a 20% chance to fail, just like casting a spell with a verbal component. The target does not
need to be able to understand what the vox is saying, but does need to be able to hear the sound of
the vox's voice (for instance, this ability cannot be used if either the vox or his target is in an
area of magical silence). Otherwise, the vox's _compelling voice_ has the effects of the standard
mesmerist's _hypnotic stare,_ and it gains further benefits as normal from abilities like the
_painful stare_ and _bold stare_ class features.

**Swift:** A vox can focus the sound of his voice on one creature within 30 feet, sapping that
target's willpower and rendering her more vulnerable to mind-affecting powers, rather than using a
stare like other mesmerists.

**Wounding Words (Su)**

**Flavor:** A vox can focus the power of his voice to magnify the force of his blows in melee.

**Gained:** At 3rd Level

**Replaces:** Touch treatment (minor), touch treatment (moderate)

**Special:** If the target of the vox's _wounding words_ is also the target of his _compelling
voice,_ that creature must succeed at a Will save (DC = 10 + 1/2 the vox's mesmerist level + his
Charisma modifier) or take a -2 penalty on attack rolls, saving throws, skill checks, and ability
checks for 1 round. This penalty doesn't stack with the effects of the
[Concussive Spell](ref/feat/concussive-spell) metamagic feat.

**Standard:** A vox can either make a melee touch attack that deals 1d6 points of sonic damage plus
1 point per mesmerist level, or he can make a single attack with a melee weapon, adding the listed
sonic damage to the damage dealt by his weapon on a successful attack.

**Usage:** Charisma3 modifier times/day

**Subsonic Strike (Su)**

**Gained:** At 10th Level

**Replaces:** Touch treatment (major)^1^

**Special:** Whatever choice he makes, the vox must expend one use of _wounding words._

**Standard:** A vox is able to unleash a deadly flurry of his _wounding words_ at once. He can
target a number of creatures or objects equal to his Charisma modifier (minimum 1) within 30 feet,
requiring a ranged touch attack against each target. If the target of his _compelling voice_ is
within 30 feet, he can choose to instead target only that creature with a single ranged touch or
melee touch attack, dealing double normal damage on a successful attack.

^1^ It is unclear if this refers to only the 10th-level ability (greater), and/or if it affects the
14th-level ability (break enchantment). Consult your GM.
