+++
id = "ref/arc-mesmerist/vox"
kind = "archetype"
title = "Vox"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Vox"
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
features = [
  { anchor = "spells" },
  { anchor = "compelling-voice" },
  { anchor = "wounding-words", level = 3 },
  { anchor = "subsonic-strike", level = 10 },
]
trades = [
  { replaces = "Towering ego", feature = "towering-ego", by = ["spells"] },
  { replaces = "Mesmerist trick normally gained at 10th level", feature = "mesmerist-tricks", levels = [10], by = ["spells"] },
  { replaces = "touch treatment (break enchantment)", feature = "touch-treatment", levels = [14], by = ["spells"] },
  { replaces = "Touch treatment (minor)", feature = "touch-treatment", levels = [3], by = ["wounding-words"] },
  { replaces = "touch treatment (moderate)", feature = "touch-treatment", levels = [6], by = ["wounding-words"] },
  { replaces = "Touch treatment (major)", feature = "touch-treatment", levels = [10], by = ["subsonic-strike"] },
  { alters = "Spellcasting", feature = "spells", by = ["spells"] },
  { alters = "Hypnotic stare", feature = "hypnotic-stare", by = ["compelling-voice"] },
]
+++

Most mesmerists practice their mental manipulation through their entrancing gaze, but others have
learned to practice their skill through the lilt and intonation of their voice. From sibilant
whispers to overwhelming imprecations that resonate with the force of pure will, a vox unleashes the
power of his mind with every silken syllable and shattering shout.

## Spells {#spells}

A vox adds the following spells to his class list: 1st—_ear-piercing scream_; 2nd—_cacophonous call,
disrupt silence_ (see page 212), _distracting cacophony, piercing shriek, sonic scream_; 4th—_shout,
sonic thrust, wall of sound_; 5th—_cacophonous call (mass), echolocation, resonating word_;
6th—_magnifying chime, shout (greater), sonic form._ Unlike most psychic spells, a vox's mesmerist
spells use both thought and verbal components; like a [bard](ref/class/bard), a vox cannot remove
the verbal components of his spells.

This alters the mesmerist's spellcasting and replaces towering ego, the mesmerist trick normally
gained at 10th level, and touch treatment (break enchantment).

## Compelling Voice (Su) {#compelling-voice}

A vox can focus the sound of his voice on one creature within 30 feet as a swift action, sapping
that target's willpower and rendering her more vulnerable to mind-affecting powers, rather than
using a stare like other mesmerists. A vox can use his compelling voice even while
[deafened](ref/misc/deafened), but it has a 20% chance to fail, just like casting a spell with a
verbal component. The target does not need to be able to understand what the vox is saying, but does
need to be able to hear the sound of the vox's voice (for instance, this ability cannot be used if
either the vox or his target is in an area of magical silence). Otherwise, the vox's compelling
voice has the effects of the standard mesmerist's hypnotic stare, and it gains further benefits as
normal from abilities like the painful stare and bold stare class features.

This ability alters hypnotic stare.

## Wounding Words (Su) {#wounding-words}

At 3rd level, a vox can focus the power of his voice to magnify the force of his blows in melee. As
a standard action, a vox can make a melee touch attack that deals 1d6 points of sonic damage plus 1
point per mesmerist level. Alternatively, he can make a single attack with a melee weapon as a
standard action, adding the listed sonic damage to the damage dealt by his weapon on a successful
attack. He can use this ability a number of times per day equal to 3 + his Charisma modifier.

If the target of the vox's wounding words is also the target of his compelling voice, that creature
must succeed at a Will save (DC = 10 + 1/2 the vox's mesmerist level + his Charisma modifier) or
take a -2 penalty on attack rolls, saving throws, skill checks, and ability checks for 1 round. This
penalty doesn't stack with the effects of the [Concussive Spell](ref/feat/concussive-spell)
metamagic feat.

This ability replaces touch treatment (minor) and touch treatment (moderate).

## Subsonic Strike (Su) {#subsonic-strike}

At 10th level, a vox is able to unleash a deadly flurry of his wounding words as a standard action.
He can target a number of creatures or objects equal to his Charisma modifier (minimum 1) within 30
feet, requiring a ranged touch attack against each target. If the target of his compelling voice is
within 30 feet, he can choose to instead target only that creature with a single ranged touch or
melee touch attack, dealing double normal damage on a successful attack.

Whatever choice he makes, the vox must expend one use of wounding words.

This ability replaces touch treatment (major).
