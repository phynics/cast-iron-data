+++
id = "ref/rule/plagued"
kind = "rule"
title = "Plagued"
source_ids = ["horror-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plagued", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Realms pg. 58-59\
Disease can become a corruption when it causes long-lasting and physical changes to the body.

### Catalyst

Suffering a magical disease for a prolonged period can induce the plagued corruption.

### Progression

You carry the symptoms and appearance of one suffering from a disease, even if you've been cured of
the illness that triggered your corruption or are otherwise normally immune to disease. Further,
once you gain the plagued corruption, you lose any immunity to disease and cannot gain such immunity
from magical spells or items or other effects. Only living creatures can gain this corruption.

Once per month, if you did not infect a number of creatures equal to or greater than your
manifestation level with a disease you are carrying, you must attempt a Fortitude saving throw (DC =
15 + your manifestation level). If you fail, the next time you rest, you immediately gain a new
disease of the GM's choosing (without a further saving throw) and black out, losing control to the
insidious delirium of the disease. You must seek out and infect any creature you can find before the
next sunrise. If you succeed on your Fortitude saving throw or are prevented from infecting anyone
for 1 day, the urge passes, but the DC of future saving throws to resist this temptation increases
by 2. This increase is cumulative, but resets when your corruption progresses. Innocents you infect
and then cure (or whose recovery you significantly assist, at the GM's discretion) do not count
toward this number, nor do those infected by others who were themselves infected before your
corruption reached its current stage.

**Corruption Stage 1**

**Details:** The first time your corruption progresses, any disease you suffer from becomes more
tenacious. You take a -2 penalty on all saving throws to resist contracting a new disease, and your
alignment shifts one step toward evil.

**Corruption Stage 2**

**Details:** The second time your corruption progresses, diseases you suffer from become difficult
to cure; the DC of a disease you are suffering from is increased by 10 for the purposes of caster
level checks for spells such as [remove disease](ref/spell/remove-disease) to cure you from its
effects. Your alignment shifts to evil.

**Corruption Stage 3**

**Details:** The third time your corruption progresses, your disease saps your free will and the GM
gains control of your character.

### Removing the Corruption

Curing the corruption requires curing not only the underlying diseases you suffer from, but also the
initial illness that triggered your corruption - this often necessitates the use of rare and
elaborate treatments.

### Manifestations

The following are manifestations of the plagued corruption.

**Accelerated Affliction**

**Flavor:** You can quicken diseases in others.

**Gift:** As a **swift action**, once per day per 2 manifestation levels you have (minimum once per
day), you can cause one creature within 30 feet suffering from any diseases to attempt a saving
throw against one randomly determined disease they are suffering. On a failed saving throw, they
immediately take that disease's damage. A successful save does not count toward the saving throws
required to recover from the disease.

**Stain:** You take a -2 penalty to any one ability score of your choice.

**Bodily Betrayal**

**Flavor:** Your body betrays you at the worst moments.

**Prereq:** Accelerated affliction

**Gift:** Once per day per manifestation level, you can make a touch attack on a creature and expose
it to any disease you are carrying.

**Stain:** Plague sores make injuries more acutely painful. You take a -2 penalty on attack rolls,
saving throws, and [concentration](ref/rule/concentration) checks for 1 round after you are dealt
lethal damage.

**False Health**

**Flavor:** You can feign health and hide your symptoms.

**Prereq:** Accelerated affliction

**Gift:** Once per day as a **swift action**, you can suppress the stain of your _accelerated
affliction_ for a number of hours equal to your manifestation level.

**Stain:** You take a -2 penalty on concentration checks while using false health.

**Fevered Dreams**

**Flavor:** Disease clouds your thoughts.

**Prereq:** Manifestation level 6th, infectious thoughts, miserable company

**Gift:** The dreams of victims of the diseases you spread are apparent to you. Once per day while
you rest, you can cause a number of sleeping victims of your disease up to your manifestation level
to suffer the effects of one of these spells of your choice: [dream](ref/spell/dream),
[fear](ref/spell/fear) (upon awakening), [nightmare](ref/spell/nightmare), or
[suggestion](ref/spell/suggestion) (upon awakening).

**Stain:** You sleep poorly. You must rest for 12 hours each night to gain the full benefits of
rest.

**Infectious Thoughts**

**Flavor:** Your thoughts spread like your disease.

**Prereq:** Manifestation level 3rd, miserable company

**Gift:** You can communicate telepathically with any creature within 10 feet suffering from any
disease.

At manifestation level 5th, the range increases to 30 feet.

At manifestation level 7th, the range is 100 feet.

At manifestation level 9th, the range is 1 mile.

**Stain:** Your ego becomes hard to contain. You take a -2 penalty on Will saving throws against
effects with the emotion descriptor.

At manifestation level 5th, the penalty doubles.

**Living Breath**

**Flavor:** The stink of disease carries on your breath.

**Prereq:** Manifestation level 5th, accelerated affliction, bodily betrayal

**Gift:** When you use your _bodily betrayal_ manifestation to expose a creature to a disease you
are carrying, your breath carries the disease as well, potentially infecting all creatures within a
10-foot radius. These creatures gain a +2 bonus on the saving throw to resist the disease you are
attempting to inflict with your _bodily betrayal._

**Stain:** The disease shortens your breath and stiffens your limbs. You take a -2 penalty on all
Strength- and Dexterity-based checks.

**Miserable Company**

**Flavor:** Your disease's symptoms become more apparent.

**Gift:** You gain a +2 bonus on [Heal](ref/skill/heal) checks to recognize or treat diseases and on
Charisma-based skill checks to influence creatures able to inflict disease or those suffering from a
disease.

At manifestation level 3rd, these bonuses double. Creatures with any diseases take a -2 penalty on
any saving throws against mind-affecting effects you create.

**Stain:** You remain infectious for 1d4 days even after you are cured of any infectious disease
(including your corruption plague), though you show no symptoms.

At manifestation level 3rd, you remain infectious for 1d8 days.

**Overwhelming Weakness**

**Flavor:** Disease saps your limbs of their strength.

**Gift:** Victims other than you who fail their initial saving throw against any disease effect you
create become sickened for 24 hours.

**Stain:** The disease makes your limbs weak. You take a -2 penalty to Strength. This penalty stacks
with the ability penalty from _accelerated affliction_ if you chose Strength as your penalty.

**Theft of Awareness**

**Flavor:** Your senses fail you, but the terrible disease you can inflict affords you access to the
senses of those who suffer from it.

**Prereq:** Manifestation level 7th, infectious thoughts, miserable company

**Gift:** As a **move action**, for as long as you concentrate, you can borrow the senses of any
creature suffering from a disease effect you created, as long as the creature is within range of
your _infectious thoughts._ Your body is effectively blind and deaf while you concentrate. The
target can resist this intrusion with a successful Will saving throw.

At manifestation level 9th, you can possess one such victim as per
[possession](ref/spell/possession) once per day as a **standard action** while you are already
sharing its senses.

**Stain:** Your senses falter. You take a -4 penalty on Perception checks and Sense Motive checks
while you are not using theft of awareness.
