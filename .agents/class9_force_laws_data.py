# -*- coding: utf-8 -*-
"""
Curriculum content for NCERT Class 9 Science Chapter 10: Force and Laws of Motion
20 Comprehensive slides with:
- 16 interactive content slides with 32 in-slide checkpoints (2 per content slide)
- 4 dedicated mastery quiz challenge slides with 40 questions total (10 per slide)
- Complete step-by-step solutions for all quiz questions
- Voiceover narration scripts for Prof. Sophia
"""

slides_data = [
    # Slide 1: Introduction to Force & Vector Nature
    {
        "id": 1,
        "title": "Introduction to Force & Vector Nature",
        "subtitle": "Push, Pull, Magnitude, Direction & Free Body Diagrams (C-2.1)",
        "content": """
<p class="lead-p">In everyday life, we observe objects at rest beginning to move, moving bodies slowing down, speeding up, or veering around corners. An external agency is required to cause these changes—this physical interaction is called <strong>Force</strong>.</p>

<div class="theory-box">
  <h4>1. Defining Force & Its Observable Effects</h4>
  <p>A <strong>force</strong> is a push, pull, or mutual interaction on an object resulting from its interaction with another entity. A force can:</p>
  <ul>
    <li><strong>Change the state of rest or motion:</strong> Push a stalled car to roll forward, or brake a bicycle to rest.</li>
    <li><strong>Alter the speed of an object:</strong> Accelerate a falling ball downwards or decelerate an upward throw.</li>
    <li><strong>Change the direction of motion:</strong> A cricket batsman deflecting an oncoming ball with a bat.</li>
    <li><strong>Change the shape or dimensions:</strong> Squeezing a rubber ball, stretching a spring, or flattening dough.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Vector Character of Force</h4>
    <p>Force possesses both <strong>magnitude</strong> (how strong it is) and <strong>direction</strong> (where it points). If you push a door with a force of $10\\text{ N}$ to open it, pushing in the opposite direction will slam it shut! Represented mathematically as $\\vec{F}$.</p>
  </div>
  <div class="card-item">
    <h4>SI Unit of Force: The Newton (N)</h4>
    <p>The standard International System (SI) unit of force is the <strong>Newton</strong>, symbolized as $\\text{N}$. Named in honour of Sir Isaac Newton, $1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2$. In CGS units, force is measured in dynes ($1\\text{ N} = 10^5\\text{ dynes}$).</p>
  </div>
</div>
""",
        "sim_type": "force_vector",
        "voice": "Welcome to the Force and Laws of Motion Master Laboratory! In this foundational session, we explore what force truly is: a push or pull that can initiate, stop, or redirect motion. Crucially, force is a vector quantity having both magnitude and direction. Let us experiment with our interactive vector simulator!",
        "checkpoints": [
            {
                "question": "Which of the following physical quantities is completely characterized only when both magnitude and direction are specified?",
                "options": ["Mass", "Force", "Speed", "Time"],
                "correct": 1,
                "explanation": "Force is a vector quantity requiring both magnitude (e.g. 15 N) and spatial direction (e.g. eastward). Mass, speed, and time are scalar quantities."
            },
            {
                "question": "What is the equivalent fundamental SI unit representation of 1 Newton (N)?",
                "options": ["1 kg·m/s", "1 kg·m/s²", "1 kg²/m·s", "1 g·cm/s²"],
                "correct": 1,
                "explanation": "From Newton's second law F = ma, 1 Newton equals 1 kilogram accelerated at 1 meter per second squared, or 1 kg·m/s²."
            }
        ]
    },

    # Slide 2: Balanced vs Unbalanced Forces
    {
        "id": 2,
        "title": "Balanced vs Unbalanced Forces",
        "subtitle": "Equilibrium, Net Force (ΣF), and Acceleration (C-2.1, C-8.1)",
        "content": """
<p class="lead-p">When multiple forces act simultaneously on a body, their combined influence is determined by their vector sum, known as the <strong>Net Force ($\\Sigma \\vec{F}$)</strong> or resultant force.</p>

<div class="theory-box">
  <h4>1. Balanced Forces ($\\Sigma \\vec{F} = 0$)</h4>
  <p>If the resultant of all forces acting on a body is zero, the forces are termed <strong>balanced forces</strong>:</p>
  <ul>
    <li>They <strong>cannot</strong> change the state of rest or uniform motion of an object.</li>
    <li>An object at rest remains at rest; an object moving at constant velocity continues moving at identical speed in a straight line.</li>
    <li>Balanced forces <strong>can</strong> alter the shape or size of an object (e.g., compressing a balloon between two hands with equal opposing forces).</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. Unbalanced Forces ($\\Sigma \\vec{F} \\neq 0$)</h4>
  <p>If the resultant of all forces acting on a body is non-zero, an <strong>unbalanced net force</strong> exists:</p>
  <ul>
    <li>An unbalanced force always produces an <strong>acceleration</strong> ($a = \\frac{\\Sigma F}{m}$) in the direction of the net force.</li>
    <li>It changes the object's speed, direction of motion, or both.</li>
    <li>To accelerate an object from rest, an external unbalanced force is strictly necessary.</li>
  </ul>
</div>
""",
        "sim_type": "balanced_tug_of_war",
        "voice": "Consider a block on a horizontal tabletop. When two opposite teams pull a rope with identical forces of 50 Newtons each, the net force is zero. The forces are balanced, and the rope remains stationary. But add just one more Newton to either side, and the forces become unbalanced, causing instant acceleration in the direction of the net force!",
        "checkpoints": [
            {
                "question": "When a wooden block on a table is pulled to the left with 35 N and to the right with 35 N simultaneously, the net force acting on the block is:",
                "options": ["70 N to the right", "35 N downward", "0 N (Balanced)", "1 N to the left"],
                "correct": 2,
                "explanation": "Forces acting in opposite directions along the same line subtract: 35 N - 35 N = 0 N. The forces are balanced, and no acceleration occurs."
            },
            {
                "question": "Which of the following can balanced forces cause on an object?",
                "options": ["A change in linear velocity", "A change in shape or size", "An acceleration from rest", "A change in direction of travel"],
                "correct": 1,
                "explanation": "Balanced forces have zero net force, so they cannot cause acceleration or velocity change. However, opposing balanced forces can compress, stretch, or deform an object's physical shape."
            }
        ]
    },

    # Slide 3: Force of Friction
    {
        "id": 3,
        "title": "The Force of Friction",
        "subtitle": "Microscopic Interlocking, Static vs Kinetic, & Resistance to Motion (C-2.1)",
        "content": """
<p class="lead-p">Why does a rolling ball on a grass lawn eventually grind to a halt without anyone touching it? The answer lies in contact resistance: the <strong>Force of Friction</strong>.</p>

<div class="theory-box">
  <h4>1. Nature and Direction of Friction</h4>
  <p><strong>Friction</strong> is an opposing contact force that arises between two surfaces in contact whenever one body moves or attempts to slide across another. It acts parallel to the contact interface and <strong>always opposes the relative motion</strong> (or impending motion) between surfaces.</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Microscopic Origin of Friction</h4>
    <p>Even polished surfaces possess microscopic hills and valleys (asperities). When two surfaces touch, these microscopic asperities interlock and form cold-welded junctions. To initiate motion, an applied force must shear these microscopic junctions.</p>
  </div>
  <div class="card-item">
    <h4>Classification of Friction</h4>
    <ul>
      <li><strong>Static Friction ($f_s$):</strong> Opposes impending motion when the body is at rest. Self-adjusting up to a maximum threshold called <em>limiting friction</em> ($f_{\\text{max}} = \\mu_s N$).</li>
      <li><strong>Kinetic / Sliding Friction ($f_k$):</strong> Resistance during active relative sliding. Slightly less than limiting static friction ($f_k < f_{\\text{max}}$).</li>
      <li><strong>Rolling Friction ($f_r$):</strong> Resistance when a cylinder or sphere rolls over a surface. Greatly reduced ($f_r \\ll f_k$), which is why wheels were humanity's greatest mechanical invention!</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "friction_breakaway",
        "voice": "Friction is a subtle contact force. When you gently push a heavy crate, it doesn't budge because static friction pushes back with an exactly equal opposing force. As you push harder, static friction grows until it hits its maximum limiting threshold. Once you break past this limit, kinetic friction takes over, and the crate begins to slide!",
        "checkpoints": [
            {
                "question": "What happens to the static frictional force between a stationary box and the floor as you increase your pushing force from 10 N to 20 N (before the box starts moving)?",
                "options": ["Static friction stays constant at 10 N", "Static friction increases to 20 N to maintain equilibrium", "Static friction drops to zero", "Static friction becomes negative"],
                "correct": 1,
                "explanation": "Static friction is a self-adjusting force. Up to its maximum limiting value, it increases in exact lockstep with the applied pushing force so the net horizontal force remains zero."
            },
            {
                "question": "Why are ball bearings used in bicycle hubs and automobile wheel axles?",
                "options": ["To increase sliding friction", "To replace sliding friction with much smaller rolling friction", "To eliminate the normal reaction force", "To increase the gravitational mass"],
                "correct": 1,
                "explanation": "Rolling friction is significantly smaller than sliding friction. By using spherical ball bearings, sliding contact is converted to rolling contact, dramatically reducing energy losses."
            }
        ]
    },

    # Slide 4: Galileo's Thought Experiment & Demise of Aristotelian Fallacy
    {
        "id": 4,
        "title": "Galileo's Inclined Plane & Demise of Aristotelian Fallacy",
        "subtitle": "The Revolutionary Thought Experiment Leading to Newton's First Law (C-2.1, C-8.2)",
        "content": """
<p class="lead-p">For nearly two thousand years, Western philosophy was dominated by <strong>Aristotle's fallacy</strong>: the belief that a constant external force is required to keep a body in uniform continuous motion. Galileo Galilei shattered this dogma through ingenious inclined plane thought experiments.</p>

<div class="theory-box">
  <h4>1. Galileo's Double Inclined Plane Observations</h4>
  <p>Galileo studied the motion of marble spheres rolling on smooth double inclined planes:</p>
  <ul>
    <li>A marble rolling down an inclined plane accelerates due to downward gravity.</li>
    <li>Climbing up the opposite incline, the marble decelerates until it reaches virtually the <strong>exact same vertical height</strong> from which it was released.</li>
    <li>When the slope of the second incline is reduced, the marble must travel a <strong>longer distance</strong> along the slope to reach that identical release height.</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. The Grand Deduction for a Horizontal Plane</h4>
  <p>Galileo asked: What if the second plane is made completely <strong>horizontal</strong> (slope angle $\\theta = 0^{\\circ}$)?</p>
  <p class="highlight-eq">$$\\text{If the second plane is horizontal, the marble will never reach its initial release height,}$$ $$\\text{and must continue moving indefinitely in a straight line at constant velocity!}$$</p>
  <p>In the real world, the marble stops only because of unavoidable contact friction and air resistance. In a frictionless ideal realm, <strong>no force is required to sustain uniform motion</strong>!</p>
</div>
""",
        "sim_type": "galileo_inclined_planes",
        "voice": "Galileo's thought experiment was one of the greatest leaps in scientific history. By releasing a marble down an incline and watching it climb an opposite ramp to the exact same vertical height, Galileo realized that if the second ramp is made perfectly horizontal, the ball must travel forward forever in an eternal quest to regain its height! Thus, uniform motion does not need a sustaining force.",
        "checkpoints": [
            {
                "question": "According to Galileo's thought experiment on a frictionless double inclined plane, if the second plane is made completely flat and horizontal, a released marble will:",
                "options": ["Stop immediately after reaching the base", "Travel a finite distance of 10 meters and halt", "Continue moving with constant velocity indefinitely", "Turn around and return to the first incline"],
                "correct": 2,
                "explanation": "Because the marble seeks its release height and a horizontal plane never rises, in the absence of friction the marble will continue moving forward indefinitely at constant velocity."
            },
            {
                "question": "What did Galileo demonstrate about the cause of an object slowing down in everyday life?",
                "options": ["Objects naturally want to be at rest because of Aristotle's natural state", "Retardation is caused by opposing contact friction, not an inherent desire to stop", "Mass decreases as an object travels forward", "Gravity pulls objects backward along a horizontal floor"],
                "correct": 1,
                "explanation": "Galileo proved that objects slow down and halt solely due to external resistive forces like friction and air drag. Without friction, motion continues indefinitely."
            }
        ]
    },

    # Slide 5: Newton's First Law of Motion & Inertia
    {
        "id": 5,
        "title": "Newton's First Law of Motion & Inertia",
        "subtitle": "The Law of Inertia: Inertia of Rest, Motion, & Direction (C-2.1)",
        "content": """
<p class="lead-p">Building upon Galileo's revolutionary insights, Sir Isaac Newton formulated the foundations of classical mechanics in his 1687 treatise <em>Philosophiae Naturalis Principia Mathematica</em>.</p>

<div class="theory-box">
  <h4>1. Statement of Newton's First Law of Motion</h4>
  <p class="highlight-eq">$$\\text{An object remains in a state of rest or of uniform motion in a straight line}$$ $$\\text{unless compelled to change that state by an applied external unbalanced force.}$$</p>
  <p>Newton's First Law is also universally known as the <strong>Law of Inertia</strong>. It asserts that bodies are inherently inert—they cannot self-initiate, alter, or terminate their state of motion.</p>
</div>

<div class="theory-box">
  <h4>2. The Three Manifestations of Inertia</h4>
  <div class="grid-3col">
    <div class="card-item">
      <h5>Inertia of Rest</h5>
      <p>Tendency of a stationary body to stay at rest. When a carpet is beaten with a stick, the carpet accelerates away while dust particles stay stationary due to inertia of rest and drop down under gravity.</p>
    </div>
    <div class="card-item">
      <h5>Inertia of Motion</h5>
      <p>Tendency of a moving body to maintain its forward speed. When a speeding bus applies sudden emergency brakes, passengers lunge forward because their upper bodies retain forward velocity.</p>
    </div>
    <div class="card-item">
      <h5>Inertia of Direction</h5>
      <p>Tendency to preserve straight-line direction. When a car negotiates a sharp curve, passengers lean radially outward because their bodies tend to continue traveling in a straight line.</p>
    </div>
  </div>
</div>
""",
        "sim_type": "coin_card_flick",
        "voice": "Newton's First Law reveals that matter possesses an intrinsic resistance to any change in its motion, called inertia. Consider the classic coin-on-a-card trick: when you flick the index card rapidly, the card slides away, but the heavy coin remains in place due to its inertia of rest, dropping straight down into the glass beaker below!",
        "checkpoints": [
            {
                "question": "When a horse suddenly begins galloping forward from rest, an inexperienced rider tends to fall backward. This everyday phenomenon is explained by:",
                "options": ["Inertia of direction", "Inertia of rest", "Newton's Third Law alone", "Inertia of motion"],
                "correct": 1,
                "explanation": "The lower part of the rider's body in contact with the saddle moves forward with the horse, while the upper body tends to remain at rest due to inertia of rest, causing a backward tilt."
            },
            {
                "question": "Why do safety seat belts in automobiles save lives during high-speed head-on collisions?",
                "options": ["They increase the car's engine power", "They prevent passengers from continuing forward at high speed due to inertia of motion", "They eliminate all frictional forces between tires and road", "They convert kinetic energy into gravitational mass"],
                "correct": 1,
                "explanation": "When a vehicle decelerates violently upon impact, passengers continue moving forward at the pre-collision velocity due to inertia of motion. Seat belts provide the necessary restraining force."
            }
        ]
    },

    # Slide 6: Inertia and Mass
    {
        "id": 6,
        "title": "Inertia and Mass",
        "subtitle": "Quantitative Measure of Inertia, Force Resistance, & Comparison (C-2.1)",
        "content": """
<p class="lead-p">While all matter possesses inertia, do all objects exhibit the exact same resistance to motion changes? Certainly not! A tennis ball is easily swatted, whereas kicking a boulder of identical volume will break your toe.</p>

<div class="theory-box">
  <h4>1. Mass as the Quantitative Measure of Inertia</h4>
  <p>The <strong>mass</strong> of a body is the quantitative measure of its inertia:</p>
  <ul>
    <li>The greater the mass of an object, the greater its inertia, and the greater the force required to produce a given acceleration.</li>
    <li>A light toy car ($m = 0.2\\text{ kg}$) can be halted effortlessly with one finger. A loaded freight train ($m = 5000\\text{ tonnes}$) traveling at the same modest speed requires kilometers of track and immense braking force to halt!</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Comparing Inertia in Common Pairs</h4>
    <ul>
      <li><strong>Football vs Stone:</strong> A stone of equal size has far greater density and mass, hence far greater inertia.</li>
      <li><strong>Bicycle vs Locomotive:</strong> The locomotive has thousands of times more mass, meaning enormous resistance to starting or stopping.</li>
      <li><strong>One Rupee Coin vs Five Rupee Coin:</strong> The heavier 5-rupee coin exhibits greater inertia.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Inertial Mass vs Gravitational Mass</h4>
    <p><strong>Inertial mass</strong> measures resistance to acceleration ($m_i = F/a$). <strong>Gravitational mass</strong> measures gravitational attraction ($m_g = W/g$). As Einstein later highlighted in General Relativity, experiments demonstrate that inertial mass and gravitational mass are strictly equivalent to extreme precision!</p>
  </div>
</div>
""",
        "sim_type": "mass_inertia_push",
        "voice": "Mass is the true quantitative measure of inertia. In our comparison track simulator, notice what happens when we apply an identical pushing force of 50 Newtons to a light 2-kilogram cart versus a heavy 20-kilogram iron block. The light cart accelerates rapidly, while the heavy block barely creeps forward due to its tenfold greater inertia!",
        "checkpoints": [
            {
                "question": "Which of the following objects has the greatest inertia?",
                "options": ["A rubber ball of mass 200 g", "A bicycle of mass 12 kg", "A car of mass 1200 kg", "A loaded train of mass 2,000,000 kg"],
                "correct": 3,
                "explanation": "Inertia is directly proportional to mass. The loaded train possesses the largest mass, therefore it exhibits the greatest inertia."
            },
            {
                "question": "If you apply an identical horizontal force of 20 N to an empty cardboard box (mass 1 kg) and a stone block (mass 10 kg), what is the ratio of their accelerations (a_box : a_stone)?",
                "options": ["1 : 1", "1 : 10", "10 : 1", "100 : 1"],
                "correct": 2,
                "explanation": "From a = F/m, a_box = 20/1 = 20 m/s², while a_stone = 20/10 = 2 m/s². The ratio of accelerations is 20 : 2 = 10 : 1."
            }
        ]
    },

    # Slide 7: Linear Momentum (p = mv)
    {
        "id": 7,
        "title": "Linear Momentum: The Quantity of Motion",
        "subtitle": "Combining Mass and Velocity, Vector Definition, and Units (C-2.1)",
        "content": """
<p class="lead-p">Why does a tiny bullet fired from a rifle easily pierce through thick timber, while a lead pellet of the same mass thrown gently by hand bounces off harmlessly? Conversely, why can a massive barge moving at barely 1 km/h crush a concrete pier? The answer requires combining mass and velocity: <strong>Momentum</strong>.</p>

<div class="theory-box">
  <h4>1. Definition of Linear Momentum ($\\vec{p}$)</h4>
  <p>The <strong>momentum</strong> of a body is defined as the product of its mass ($m$) and velocity ($\\vec{v}$):</p>
  <p class="highlight-eq">$$\\vec{p} = m \\cdot \\vec{v}$$</p>
  <ul>
    <li><strong>Vector Quantity:</strong> Momentum has both magnitude and direction. Its direction is <strong>identical to the direction of velocity</strong>.</li>
    <li><strong>SI Unit:</strong> Kilogram-meter per second ($\\text{kg}\\cdot\\text{m/s}$ or $\\text{N}\\cdot\\text{s}$).</li>
    <li>If a body is at rest ($v = 0$), its linear momentum is strictly zero, regardless of its mass.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Magnitude Proportionality</h4>
    <p>For a constant mass, momentum is directly proportional to velocity ($p \\propto v$). For objects moving at equal speed, momentum is directly proportional to mass ($p \\propto m$). Thus, a heavy truck at $20\\text{ m/s}$ has vastly more momentum than a car at $20\\text{ m/s}$.</p>
  </div>
  <div class="card-item">
    <h4>Stopping Force Relationship</h4>
    <p>To bring a moving body to rest, an opposing force must reduce its momentum to zero. A larger initial momentum requires either a much larger stopping force or a much longer duration of braking.</p>
  </div>
</div>
""",
        "sim_type": "momentum_visualizer",
        "voice": "Momentum, introduced by Newton as the quantity of motion, is the product of mass and velocity. Notice how a tiny 10-gram bullet traveling at 400 meters per second packs a momentum of 4 kilogram meters per second—the exact same momentum as a 4-kilogram medicine ball rolling at 1 meter per second! Both require identical stopping impulses.",
        "checkpoints": [
            {
                "question": "A cricket ball of mass 0.15 kg is bowled at a speed of 40 m/s. What is its linear momentum?",
                "options": ["0.15 kg·m/s", "6.0 kg·m/s", "60 kg·m/s", "266.7 kg·m/s"],
                "correct": 1,
                "explanation": "Linear momentum p = m · v = 0.15 kg × 40 m/s = 6.0 kg·m/s in the direction of the ball's motion."
            },
            {
                "question": "If an object's mass is doubled while its velocity is halved, what happens to its linear momentum?",
                "options": ["It quadruples", "It doubles", "It remains unchanged", "It decreases by half"],
                "correct": 2,
                "explanation": "New momentum p' = (2m) × (v/2) = m · v = p. The linear momentum remains completely unchanged."
            }
        ]
    },

    # Slide 8: Newton's Second Law of Motion
    {
        "id": 8,
        "title": "Newton's Second Law of Motion",
        "subtitle": "Rate of Change of Momentum, Mathematical Derivation (F = ma) (C-2.1)",
        "content": """
<p class="lead-p">While the First Law explains what happens when no net force acts, the <strong>Second Law of Motion</strong> provides the quantitative bridge between an applied unbalanced force and the resulting change in motion.</p>

<div class="theory-box">
  <h4>1. Formal Statement of Newton's Second Law</h4>
  <p class="highlight-eq">$$\\text{The rate of change of momentum of an object is directly proportional to}$$ $$\\text{the applied unbalanced force and takes place in the direction of the force.}$$</p>
</div>

<div class="theory-box">
  <h4>2. Mathematical Derivation of $F = ma$</h4>
  <p>Consider a body of mass $m$ moving with initial velocity $\\vec{u}$. When an unbalanced force $\\vec{F}$ is applied for time duration $t$, its velocity changes to $\\vec{v}$:</p>
  <ul>
    <li>Initial momentum: $p_1 = m \\cdot u$</li>
    <li>Final momentum after time $t$: $p_2 = m \\cdot v$</li>
    <li>Change in momentum: $\\Delta p = p_2 - p_1 = m(v - u)$</li>
    <li>Rate of change of momentum: $\\frac{\\Delta p}{t} = \\frac{m(v - u)}{t} = m \\cdot a$ &nbsp;&nbsp;(since $a = \\frac{v - u}{t}$)</li>
  </ul>
  <p>According to the Second Law: $F \\propto \\frac{\\Delta p}{t} \\implies F \\propto m \\cdot a \\implies F = k \\cdot m \\cdot a$</p>
  <p>By defining <strong>one unit of force</strong> as the force producing an acceleration of $1\\text{ m/s}^2$ in a mass of $1\\text{ kg}$, the constant of proportionality becomes $k = 1$!</p>
  <p class="highlight-eq">$$F = m \\cdot a$$</p>
</div>
""",
        "sim_type": "newton_second_law_cart",
        "voice": "Newton's Second Law is the crown jewel of dynamics: F equals m times a! Force equals mass times acceleration. It tells us that to accelerate a heavier body, you need proportionally more force; and for a given force, a lighter mass accelerates much faster. Let us test this live on our dynamic air-track cart simulator!",
        "checkpoints": [
            {
                "question": "A force of 25 N acts on a stationary cart of mass 5 kg for 3 seconds. What acceleration is produced in the cart?",
                "options": ["0.2 m/s²", "5.0 m/s²", "15.0 m/s²", "125.0 m/s²"],
                "correct": 1,
                "explanation": "From Newton's second law F = ma, the acceleration a = F / m = 25 N / 5 kg = 5.0 m/s²."
            },
            {
                "question": "Newton's First Law of Motion can be mathematically deduced from the Second Law F = ma by setting:",
                "options": ["m = 0", "F = 0, which implies a = 0 (velocity remains constant)", "a = infinity", "v = u + at"],
                "correct": 1,
                "explanation": "If the net force F = 0, then since mass m ≠ 0, acceleration a must be 0. Zero acceleration means velocity does not change: an object at rest stays at rest, and an object in motion maintains uniform velocity."
            }
        ]
    },

    # Slide 9: Impulse of Force & Everyday Applications
    {
        "id": 9,
        "title": "Impulse of Force & Everyday Applications",
        "subtitle": "Force-Time Cushioning, Catching Cricket Balls, & Airbags (C-2.1, C-8.1)",
        "content": """
<p class="lead-p">Why does a cricket fielder draw their hands backward while taking a high catch? Why do athletes land on sand pits rather than concrete slabs? The concept of <strong>Impulse</strong> explains these critical safety mechanics.</p>

<div class="theory-box">
  <h4>1. Defining Impulse ($J$)</h4>
  <p><strong>Impulse</strong> is the product of an applied force and the duration of time over which it acts:</p>
  <p class="highlight-eq">$$J = F \\cdot \\Delta t = \\Delta p = m(v - u)$$</p>
  <p>Impulse equals the total change in momentum! Rearranging for average force reveals the golden rule of impact mechanics:</p>
  <p class="highlight-eq">$$F = \\frac{\\Delta p}{\\Delta t}$$</p>
  <p>For a fixed change in momentum $\\Delta p$, <strong>increasing the time interval $\\Delta t$ dramatically reduces the impact force $F$</strong>!</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Everyday Cushioning Mechanics</h4>
    <ul>
      <li><strong>Catching a Cricket Ball:</strong> Pulling hands backward extends contact time $\\Delta t$, reducing impact force on the hands and preventing injury.</li>
      <li><strong>High Jump Pits:</strong> Landing on foam cushions or sand increases stopping time, keeping impact forces on joints safe.</li>
      <li><strong>Car Crumple Zones & Airbags:</strong> Modern cars deform on impact, prolonging collision duration so occupants experience survivable decelerations.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Karate Strike: Minimizing Time</h4>
    <p>A karate master does the exact opposite: striking a pile of tiles with lightning speed so contact time $\\Delta t$ is infinitesimal (milliseconds). This concentrates the momentum transfer into an enormous, shattering peak force!</p>
  </div>
</div>
""",
        "sim_type": "impulse_catcher",
        "voice": "The impulse equation reveals a life-saving secret: force equals change in momentum divided by time. When catching a fast cricket ball, if you keep your hands stiff, stopping time is tiny, producing a painful sting. By pulling your hands backward, you increase the stopping time, slashing the peak force by more than seventy percent!",
        "checkpoints": [
            {
                "question": "Why does a fielder pull their hands backward while catching a fast cricket ball?",
                "options": [
                    "To decrease the change in momentum",
                    "To increase the time duration of impact, thereby reducing the average force on hands",
                    "To increase the ball's final momentum",
                    "To decrease the ball's mass"
                ],
                "correct": 1,
                "explanation": "By pulling the hands back, the fielder increases the stopping time Δt. Since F = Δp / Δt, a larger Δt reduces the peak impact force on the palms."
            },
            {
                "question": "A rubber ball of mass 0.2 kg moving at 15 m/s strikes a wall and bounces back at 15 m/s. If the impact lasts 0.05 seconds, what is the average force exerted on the wall?",
                "options": ["60 N", "120 N", "30 N", "0 N"],
                "correct": 1,
                "explanation": "Initial momentum p₁ = 0.2 × 15 = 3 kg·m/s. Rebound momentum p₂ = 0.2 × (-15) = -3 kg·m/s. Change in momentum Δp = -3 - 3 = -6 kg·m/s. Magnitude of force F = |Δp| / Δt = 6 / 0.05 = 120 N."
            }
        ]
    },

    # Slide 10: Newton's Third Law of Motion
    {
        "id": 10,
        "title": "Newton's Third Law of Motion",
        "subtitle": "Action and Reaction, Paired Interactions, & Different Bodies (C-2.1)",
        "content": """
<p class="lead-p">Forces never occur in isolation as lonely entities. Whenever you push against a brick wall, the wall pushes back on your hands with equal vigor. This fundamental symmetry is articulated by <strong>Newton's Third Law of Motion</strong>.</p>

<div class="theory-box">
  <h4>1. Statement of Newton's Third Law</h4>
  <p class="highlight-eq">$$\\text{To every action, there is always an equal and opposite reaction.}$$</p>
  <p>Mathematically, if object $A$ exerts a force $\\vec{F}_{AB}$ on object $B$, then object $B$ simultaneously exerts a force $\\vec{F}_{BA}$ on object $A$ such that:</p>
  <p class="highlight-eq">$$\\vec{F}_{AB} = -\\vec{F}_{BA}$$</p>
</div>

<div class="theory-box">
  <h4>2. Critical Subtleties of the Third Law</h4>
  <ul>
    <li><strong>Forces Always Occur in Pairs:</strong> There is no such thing as an isolated single force in the universe.</li>
    <li><strong>Action and Reaction Act on DIFFERENT Bodies:</strong> Force $\\vec{F}_{AB}$ acts on body $B$, while force $\\vec{F}_{BA}$ acts on body $A$.</li>
    <li><strong>They NEVER Cancel Each Other:</strong> Because action and reaction act on separate bodies, they cannot form a balanced pair on a single object.</li>
    <li><strong>Simultaneous Occurrence:</strong> Neither force precedes the other; action and reaction arise and terminate at the exact same instant.</li>
  </ul>
</div>
""",
        "sim_type": "spring_balance_pair",
        "voice": "Newton's Third Law states that every action has an equal and opposite reaction. A vital trap students often fall into is asking: if action and reaction are equal and opposite, why don't they cancel each other out? The answer is profound: action and reaction act on two completely different objects! They cannot cancel because they act on separate bodies.",
        "checkpoints": [
            {
                "question": "Why do the action and reaction forces described in Newton's Third Law NOT cancel each other out?",
                "options": [
                    "Because they are not actually equal in magnitude",
                    "Because one acts slightly after the other",
                    "Because they act on two different bodies, not on the same body",
                    "Because one is a scalar and the other is a vector"
                ],
                "correct": 2,
                "explanation": "For two forces to balance and cancel, they must act on the same body. Action acts on body B, while reaction acts on body A; hence they act on distinct bodies and cannot cancel."
            },
            {
                "question": "Two spring balances A and B are hooked together. Balance A is fixed to a wall, while Balance B is pulled with a force of 40 N. What will be the reading on Balance A?",
                "options": ["0 N", "20 N", "40 N", "80 N"],
                "correct": 2,
                "explanation": "By Newton's Third Law, if balance B pulls balance A with 40 N, balance A pulls back on balance B with an equal force of 40 N. Both balances will read exactly 40 N."
            }
        ]
    },

    # Slide 11: Everyday Applications of Newton's Third Law
    {
        "id": 11,
        "title": "Everyday Applications of Newton's Third Law",
        "subtitle": "Walking, Rowing Boats, Rocket Propulsion, & Recoil (C-2.1, C-8.1)",
        "content": """
<p class="lead-p">From the simple act of taking a step to launching interplanetary probes into deep space, Newton's Third Law governs dynamic propulsion throughout the cosmos.</p>

<div class="grid-2col">
  <div class="card-item">
    <h4>1. Walking on the Ground</h4>
    <p>To walk forward, your shoe pushes backward and downward against the ground (<strong>Action</strong>). By the third law, the ground pushes forward and upward against your foot with an equal and opposite force (<strong>Reaction</strong>). On frictionless polished ice or banana peels, you cannot push backward, so no forward reaction force is generated, causing you to slip!</p>
  </div>
  <div class="card-item">
    <h4>2. Rowing a Boat</h4>
    <p>A rower pushes water backward with oars (<strong>Action</strong>). The displaced water pushes the oars and boat forward with an equal reaction force (<strong>Reaction</strong>). Stepping off a boat onto the shore pushes the boat backward into the water as you leap forward.</p>
  </div>
</div>

<div class="theory-box">
  <h4>3. Rocket and Jet Engine Propulsion</h4>
  <p>Inside a rocket combustion chamber, burning propellant produces high-pressure gas that is ejected downward through a nozzle at supersonic speed (<strong>Action force on gas</strong>). The escaping gas exerts an equal, upward reaction thrust on the rocket body (<strong>Reaction force on rocket</strong>). Crucially, rockets operate flawlessly in the vacuum of space because they do not push against atmospheric air—they push against their own expelled exhaust gases!</p>
</div>
""",
        "sim_type": "rocket_propulsion",
        "voice": "Think about how a rocket ascends into orbit. It does not push against the launch pad or atmospheric air. Inside the combustion chamber, burning gases are expelled downward at tremendous speeds. By Newton's Third Law, the exiting exhaust pushes back upward on the rocket with tremendous thrust, propelling it into space!",
        "checkpoints": [
            {
                "question": "Can a chemical rocket accelerate in the complete vacuum of outer space where there is no air to push against?",
                "options": [
                    "No, because rockets need atmospheric air to push against",
                    "Yes, because rocket thrust is the reaction force exerted by escaping exhaust gases on the rocket body",
                    "No, because gravity is zero in deep space",
                    "Only if solar wind is blowing"
                ],
                "correct": 1,
                "explanation": "Rockets accelerate in a vacuum because thrust is generated by Newton's Third Law: ejecting high-speed mass backward creates an equal forward reaction on the rocket, independent of surrounding air."
            },
            {
                "question": "When a swimmer pushes water backward with their hands and feet, what propels the swimmer forward?",
                "options": [
                    "The buoyant force alone",
                    "The reaction force exerted by the water pushing forward on the swimmer",
                    "The gravitational attraction of the pool floor",
                    "Surface tension of water"
                ],
                "correct": 1,
                "explanation": "Pushing water backward is the action force; the water exerting an equal forward force on the swimmer's body is the reaction force that produces forward acceleration."
            }
        ]
    },

    # Slide 12: Law of Conservation of Linear Momentum
    {
        "id": 12,
        "title": "Law of Conservation of Linear Momentum",
        "subtitle": "Derivation from 2nd & 3rd Laws, Isolated Systems (C-2.1, C-8.2)",
        "content": """
<p class="lead-p">When two bodies interact, collide, or explode apart, does the total motion of the system change? When no external force interferes, the answer is a profound <strong>NO</strong>: total linear momentum is strictly conserved.</p>

<div class="theory-box">
  <h4>1. Statement of Conservation of Momentum</h4>
  <p class="highlight-eq">$$\\text{In an isolated system (where net external force is zero), the total linear momentum}$$ $$\\text{of colliding or interacting bodies remains completely constant.}$$</p>
</div>

<div class="theory-box">
  <h4>2. Elegant Derivation from Newton's Laws</h4>
  <p>Consider two spheres of masses $m_1$ and $m_2$ with initial velocities $u_1$ and $u_2$ colliding head-on for a contact duration $\\Delta t$, separating with final velocities $v_1$ and $v_2$:</p>
  <ul>
    <li>Force exerted by sphere 1 on sphere 2: $F_{21} = m_2 \\cdot \\frac{v_2 - u_2}{\\Delta t}$ &nbsp;&nbsp;(Newton's 2nd Law)</li>
    <li>Force exerted by sphere 2 on sphere 1: $F_{12} = m_1 \\cdot \\frac{v_1 - u_1}{\\Delta t}$ &nbsp;&nbsp;(Newton's 2nd Law)</li>
    <li>By Newton's 3rd Law, these interaction forces are equal and opposite: $F_{21} = -F_{12}$</li>
  </ul>
  <p>Substituting expressions:</p>
  <p class="highlight-eq">$$m_2 \\frac{v_2 - u_2}{\\Delta t} = -m_1 \\frac{v_1 - u_1}{\\Delta t}$$</p>
  <p>Multiplying by $\\Delta t$ and rearranging terms:</p>
  <p class="highlight-eq">$$m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2$$</p>
  <p class="highlight-eq">$$\\Sigma \\vec{p}_{\\text{initial}} = \\Sigma \\vec{p}_{\\text{final}}$$</p>
</div>
""",
        "sim_type": "collision_carts",
        "voice": "The Law of Conservation of Momentum is one of nature's universal conservation laws. By combining Newton's Second and Third Laws, we prove that during any collision, the total momentum before impact precisely equals the total momentum after impact, provided no external unbalanced force acts!",
        "checkpoints": [
            {
                "question": "Under what condition is the total linear momentum of a system of interacting particles strictly conserved?",
                "options": [
                    "Only when all collisions are perfectly elastic",
                    "When the net external force acting on the system is zero",
                    "Only at zero degrees Celsius",
                    "When gravitational forces are doubled"
                ],
                "correct": 1,
                "explanation": "Conservation of momentum strictly requires an isolated system, meaning the vector sum of all external forces acting on the system must be zero (ΣF_ext = 0)."
            },
            {
                "question": "A cart of mass 2 kg moving at 6 m/s collides and locks together with a stationary cart of mass 4 kg. What is their combined final speed?",
                "options": ["1 m/s", "2 m/s", "3 m/s", "6 m/s"],
                "correct": 1,
                "explanation": "Initial momentum = (2 × 6) + (4 × 0) = 12 kg·m/s. After locking together, total mass = 2 + 4 = 6 kg. By conservation of momentum, 12 = 6 × v_final ⟹ v_final = 2 m/s."
            }
        ]
    },

    # Slide 13: Recoil Velocity of Firearms & Explosions
    {
        "id": 13,
        "title": "Recoil Velocity of Firearms & Explosions",
        "subtitle": "Derivation of Recoil Formula & Safety Mechanics (C-2.1, C-8.1)",
        "content": """
<p class="lead-p">When a firearm discharges a bullet, the shooter experiences a sharp backward kick known as <strong>recoil</strong>. This recoil is a direct manifestation of conservation of linear momentum.</p>

<div class="theory-box">
  <h4>1. Derivation of Recoil Velocity ($V_g$)</h4>
  <p>Consider a gun of mass $M$ loaded with a bullet of mass $m$. Before firing, both are at rest:</p>
  <ul>
    <li>Total initial momentum: $p_{\\text{initial}} = (M + m) \\cdot 0 = 0$</li>
    <li>Upon firing, the bullet emerges forward with velocity $v$. The gun kicks backward with recoil velocity $V_g$.</li>
    <li>Total final momentum: $p_{\\text{final}} = m \\cdot v + M \\cdot V_g$</li>
  </ul>
  <p>Since no external horizontal force acts on the gun-bullet system:</p>
  <p class="highlight-eq">$$p_{\\text{initial}} = p_{\\text{final}} \\implies 0 = m \\cdot v + M \\cdot V_g$$</p>
  <p class="highlight-eq">$$V_g = -\\frac{m \\cdot v}{M}$$</p>
  <p>The negative sign confirms that the gun moves in the <strong>opposite direction</strong> to the bullet!</p>
</div>

<div class="theory-box">
  <h4>2. Why Firearms Are Built Heavy</h4>
  <p>Because the gun's mass $M$ appears in the denominator, making the gun significantly heavier than the bullet ($M \\gg m$) ensures the recoil velocity $V_g$ remains small and manageable, protecting the shooter's shoulder from severe injury.</p>
</div>
""",
        "sim_type": "cannon_recoil",
        "voice": "Why does a heavy rifle kick backward when fired? Before pulling the trigger, total momentum is zero. When the light bullet shoots forward with massive velocity, the heavy rifle must recoil backward with equal and opposite momentum so the total system momentum remains zero! Because the rifle is much heavier, its recoil speed is relatively small.",
        "checkpoints": [
            {
                "question": "A bullet of mass 20 g (0.02 kg) is fired horizontally with a velocity of 300 m/s from a rifle of mass 3.0 kg. What is the recoil velocity of the rifle?",
                "options": ["-2.0 m/s", "-0.2 m/s", "+20 m/s", "-6.0 m/s"],
                "correct": 0,
                "explanation": "Using recoil formula V_g = -(m · v) / M = -(0.02 kg × 300 m/s) / 3.0 kg = -6.0 / 3.0 = -2.0 m/s (backward)."
            },
            {
                "question": "If a hunter fires a rifle while holding it loosely away from their shoulder rather than pressed firmly against it, the perceived kick is much more painful because:",
                "options": [
                    "The rifle mass is isolated, so it recoils at full speed and strikes the shoulder with high kinetic impact",
                    "The bullet speed decreases",
                    "Gravity doubles during firing",
                    "The momentum of the bullet changes direction"
                ],
                "correct": 0,
                "explanation": "Pressing the rifle firmly against the shoulder couples the rifle's mass to the shooter's body mass (M_total = M_rifle + M_body), dramatically slashing the recoil speed."
            }
        ]
    },

    # Slide 14: Experimental Apparatus & Data Collection
    {
        "id": 14,
        "title": "Experimental Apparatus & Data Collection",
        "subtitle": "Spring Balances, Air Tracks, Photogates, & Graphical Inferences (C-8.2)",
        "content": """
<p class="lead-p">Science progresses through rigorous quantitative instrumentation. In investigating forces and acceleration, physicists utilize specialized tools to isolate variables and eliminate experimental error.</p>

<div class="grid-2col">
  <div class="card-item">
    <h4>1. Linear Air Tracks & Photogates</h4>
    <p>A hollow aluminum rail perforated with tiny air jets suspends gliders on a cushion of air, reducing contact friction virtually to zero. Optoelectronic photogates record the exact microsecond a flag breaks an infrared beam, providing ultra-precise velocity and acceleration data.</p>
  </div>
  <div class="card-item">
    <h4>2. Calibrated Spring Balances</h4>
    <p>Spring balances operate on Hooke's Law ($F = k \\cdot x$), where spring extension $x$ is directly proportional to applied force $F$. Used in pairs to demonstrate Newton's Third Law and measure static friction breakaway thresholds.</p>
  </div>
</div>

<div class="theory-box">
  <h4>3. Graphical Verification of $F = ma$ and $p = mv$</h4>
  <div class="grid-2col">
    <div>
      <h5>Force vs Acceleration Graph ($F$ vs $a$)</h5>
      <p>Plotting applied force on the y-axis against acceleration on the x-axis yields a straight line passing through the origin. The <strong>slope of the line equals the inertial mass</strong> of the object:</p>
      <p class="highlight-eq">$$\\text{Slope} = \\frac{\\Delta F}{\\Delta a} = m$$</p>
    </div>
    <div>
      <h5>Momentum vs Velocity Graph ($p$ vs $v$)</h5>
      <p>Plotting linear momentum on the y-axis against velocity on the x-axis produces a linear graph whose <strong>slope represents the mass</strong> ($m = \\frac{\\Delta p}{\\Delta v}$).</p>
    </div>
  </div>
</div>
""",
        "sim_type": "virtual_air_track",
        "voice": "In modern physics laboratories, we eliminate friction using linear air tracks and measure motion with photogate sensors. When we plot applied force against acceleration, the data forms a perfect straight line passing through the origin. The slope of this line gives the exact inertial mass of the glider!",
        "checkpoints": [
            {
                "question": "In an experiment verifying Newton's Second Law, a student plots Force (F) on the vertical axis and Acceleration (a) on the horizontal axis. What physical property does the slope of this line represent?",
                "options": ["Velocity", "Inertial Mass", "Displacement", "Gravitational Constant"],
                "correct": 1,
                "explanation": "Since F = m · a, rearranging gives m = F / a. On a graph of F versus a, the slope ΔF / Δa directly represents the object's mass."
            },
            {
                "question": "Why is an air track preferred over a normal wooden ramp when verifying the conservation of momentum?",
                "options": [
                    "Because air tracks increase the gravitational pull",
                    "Because air cushion reduces external friction to near-zero, satisfying the isolated system condition",
                    "Because gliders become lighter on an air track",
                    "Because photogates only function with air"
                ],
                "correct": 1,
                "explanation": "Momentum is strictly conserved only when net external force is zero. An air track floats the gliders on air, virtually eliminating friction so external forces are negligible."
            }
        ]
    },

    # Slide 15: Kinematic Problem-Solving Workshop
    {
        "id": 15,
        "title": "Comprehensive Problem-Solving Workshop",
        "subtitle": "Combining Kinematic Equations with F = ma & Apparent Weight (C-8.1)",
        "content": """
<p class="lead-p">Mastery in dynamics requires connecting kinematic formulas ($v = u + at$, $s = ut + \\frac{1}{2}at^2$, $v^2 = u^2 + 2as$) with Newton's dynamic laws ($F = ma$).</p>

<div class="theory-box">
  <h4>1. Multi-Step Stopping Force Problem</h4>
  <p><strong>Problem:</strong> A car of mass $1000\\text{ kg}$ traveling at $72\\text{ km/h}$ is brought to rest over a distance of $50\\text{ m}$ by applying brakes. Calculate the required braking force.</p>
  <ul>
    <li>Convert speed to SI: $u = 72 \\times \\frac{5}{18} = 20\\text{ m/s}$, $v = 0\\text{ m/s}$, $s = 50\\text{ m}$</li>
    <li>Use third kinematic equation: $v^2 = u^2 + 2as \\implies 0 = 20^2 + 2 \\cdot a \\cdot 50$</li>
    <li>$100 a = -400 \\implies a = -4\\text{ m/s}^2$ (retardation)</li>
    <li>Apply Newton's Second Law: $F = m \\cdot a = 1000 \\times (-4) = -4000\\text{ N}$</li>
    <li><strong>Answer:</strong> The required braking force is $4000\\text{ N}$ directed opposite to motion.</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. Apparent Weight in an Elevator / Lift</h4>
  <p>A passenger of mass $m$ standing on a weighing scale inside a lift experiences normal floor reaction $N$:</p>
  <ul>
    <li><strong>Lift moving with constant velocity ($a = 0$):</strong> $N = mg$ (True weight).</li>
    <li><strong>Lift accelerating upward with acceleration $+a$:</strong> $N - mg = ma \\implies N = m(g + a)$ (Feels heavier).</li>
    <li><strong>Lift accelerating downward with acceleration $-a$:</strong> $mg - N = ma \\implies N = m(g - a)$ (Feels lighter).</li>
    <li><strong>Free-fall (cable snaps, $a = g$):</strong> $N = m(g - g) = 0$ (Complete weightlessness!).</li>
  </ul>
</div>
""",
        "sim_type": "elevator_scale",
        "voice": "By connecting kinematics with Newton's Second Law, we solve complex real-world challenges! Consider standing on a scale inside an elevator. When the elevator accelerates upward, the floor pushes up harder with normal force m times g plus a, making you feel heavier. If the elevator cable snaps and enters free fall, the scale reads zero—you experience weightlessness!",
        "checkpoints": [
            {
                "question": "A person of mass 60 kg stands on a weighing scale in an elevator accelerating upward at 2 m/s² (take g = 9.8 m/s²). What reading does the scale show?",
                "options": ["588 N", "468 N", "708 N", "120 N"],
                "correct": 2,
                "explanation": "In an upward accelerating elevator, apparent weight N = m(g + a) = 60 × (9.8 + 2.0) = 60 × 11.8 = 708 N."
            },
            {
                "question": "A bullet of mass 10 g leaves a rifle barrel of length 0.8 m with a muzzle speed of 400 m/s. Assuming uniform acceleration from rest, what is the average accelerating force on the bullet?",
                "options": ["100 N", "1,000 N", "2,000 N", "10,000 N"],
                "correct": 1,
                "explanation": "u = 0, v = 400 m/s, s = 0.8 m. Using v² = u² + 2as ⟹ 400² = 2 × a × 0.8 ⟹ 160,000 = 1.6 a ⟹ a = 100,000 m/s². Mass m = 0.01 kg. F = m × a = 0.01 × 100,000 = 1,000 N."
            }
        ]
    },

    # Slide 16: Indian Scientific Heritage & Modern Frontiers
    {
        "id": 16,
        "title": "Indian Scientific Heritage & Modern Frontiers",
        "subtitle": "Acharya Kanad's Vaisheshika Sutras & The Four Fundamental Forces (C-8.1)",
        "content": """
<p class="lead-p">The human quest to comprehend force and motion spans millennia—from ancient Indian philosophical atomism to modern relativistic and quantum field theories.</p>

<div class="theory-box">
  <h4>1. Ancient Indian Foundations: Acharya Kanad (~600 BCE)</h4>
  <p>Centuries before Galileo and Newton, the ancient Indian sage <strong>Acharya Kanad</strong> founded the <em>Vaisheshika</em> school of natural philosophy. In his <em>Vaisheshika Sutras</em>, Kanad categorized motion (*Karma*) and recognized the causes of physical action:</p>
  <ul>
    <li><strong>Vega (Impressed Motion / Momentum):</strong> Kanad identified *Vega* as the quality produced in an object by an applied impulse (*Prayatna*) that enables continued movement.</li>
    <li><strong>Samskara (Tendency / Inertia):</strong> Recognized that an object continues in its state of activity (*Vega*) until counteracted by opposing substances or contact resistance (*Samyoga*).</li>
    <li>Kanad systematically classified five fundamental modes of mechanical motion: upward throw (*Utksepana*), downward throw (*Avaksepana*), contraction (*Akuncana*), expansion (*Prasarana*), and transverse motion (*Gamana*).</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. Modern Scientific Frontier: The 4 Fundamental Forces & Relativity</h4>
  <div class="grid-2col">
    <div>
      <h5>The 4 Fundamental Forces of Nature</h5>
      <ol>
        <li><strong>Gravitational Force:</strong> Universal attraction between masses (weakest, infinite range).</li>
        <li><strong>Electromagnetic Force:</strong> Interactions between charges (manifests as contact friction, tension, normal force!).</li>
        <li><strong>Strong Nuclear Force:</strong> Binds quarks inside protons/neutrons (strongest force, subatomic range).</li>
        <li><strong>Weak Nuclear Force:</strong> Governs radioactive beta decay (extremely short range).</li>
      </ol>
    </div>
    <div>
      <h5>Relativistic Limit ($v \\to c$)</h5>
      <p>Newton's $F = ma$ is a low-speed approximation ($v \\ll c$). As velocities approach the speed of light ($c = 3 \\times 10^8\\text{ m/s}$), momentum becomes relativistic: $\\vec{p} = \\gamma m \\vec{v}$, where $\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}$. No amount of force can ever accelerate a massive object to the speed of light!</p>
    </div>
  </div>
</div>
""",
        "sim_type": "fundamental_forces",
        "voice": "Our exploration concludes with a historical bridge: in sixth century BCE India, Acharya Kanad formulated the concept of Vega, recognizing that an impressed action sustains motion until counteracted by contact forces. In the modern era, we discover that all everyday contact forces like friction and normal reaction are manifestations of the fundamental electromagnetic interaction!",
        "checkpoints": [
            {
                "question": "What ancient Indian philosophical term did Acharya Kanad use in the Vaisheshika Sutras to denote the impressed tendency or momentum that sustains motion?",
                "options": ["Pancha Mahabhuta", "Vega", "Rasa", "Prakriti"],
                "correct": 1,
                "explanation": "In the Vaisheshika Sutras, Acharya Kanad used the term 'Vega' to describe the impressed motion or momentum that sustains a body's continuous movement."
            },
            {
                "question": "To which of the four fundamental forces of nature do everyday contact forces like friction, tension, and normal reaction ultimately belong?",
                "options": ["Gravitational force", "Strong nuclear force", "Electromagnetic force", "Weak nuclear force"],
                "correct": 2,
                "explanation": "At the microscopic level, contact friction, string tension, and normal floor reactions arise from electrostatic repulsions between electrons in the outer shells of atoms, making them electromagnetic."
            }
        ]
    },

    # Slide 17: Quiz Challenge I: Foundational Laws & Inertia (Q1-10)
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: Forces & Inertia",
        "subtitle": "Questions 1–10 • Comprehensive Diagnostic with Step-by-Step Solutions",
        "content": "<p class=\"lead-p\">Test your mastery of force vectors, balanced vs unbalanced forces, friction types, Galileo's thought experiments, and the three manifestations of inertia. Click 'View Solution' on any question to examine detailed step-by-step reasoning.</p>",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge One! These ten questions test your grasp of balanced forces, friction, Galileo's inclined plane experiment, and the law of inertia. Give each question your best thought before checking the step-by-step solution modal.",
        "quiz_range": (1, 10)
    },

    # Slide 18: Quiz Challenge II: Newton's Second Law & Momentum (Q11-20)
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: Momentum & Second Law",
        "subtitle": "Questions 11–20 • Quantitative Calculations with Step-by-Step Solutions",
        "content": "<p class=\"lead-p\">Evaluate your calculation skills on linear momentum, rate of change of momentum, F = ma derivations, impulse mechanics, and impact-time cushioning. Click 'View Solution' for detailed mathematical workings.</p>",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge Two! Here we focus on the quantitative mathematics of Newton's Second Law, momentum calculations, impulse, and safety engineering. Work out the numbers carefully!",
        "quiz_range": (11, 20)
    },

    # Slide 19: Quiz Challenge III: Newton's Third Law & Momentum Conservation (Q21-30)
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Third Law & Conservation",
        "subtitle": "Questions 21–30 • Action-Reaction Pairs, Recoil, & Collisions",
        "content": "<p class=\"lead-p\">Assess your conceptual and numerical mastery of paired interactions, simultaneous action-reaction forces, collision momentum balance, and firearm recoil mechanics. Inspect each solution popup for clear explanations.</p>",
        "sim_type": "quiz_slide",
        "voice": "Quiz Challenge Three examines Newton's Third Law and the universal conservation of linear momentum. Remember the critical rule: action and reaction act on two different bodies and never cancel each other!",
        "quiz_range": (21, 30)
    },

    # Slide 20: Quiz Challenge IV: Advanced Problems & Frontiers (Q31-40)
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Advanced Dynamics",
        "subtitle": "Questions 31–40 • Integrated Kinematics, Apparent Weight, & Frontiers",
        "content": "<p class=\"lead-p\">The final test of your mechanics mastery! Tackle multi-step kinematic braking, elevator scale readings, connected masses, Indian historical heritage, and relativistic momentum limits. Click 'View Solution' for complete step-by-step derivations.</p>",
        "sim_type": "quiz_slide",
        "voice": "You have reached the final mastery challenge of Chapter 10! These ten multi-step questions integrate kinematics, elevator dynamics, and modern physics. Excellent work reaching the end of Force and Laws of Motion!",
        "quiz_range": (31, 40)
    }
]

# 40 Rigorous Quiz Questions
quiz_questions = [
    # Q1
    {
        "num": 1,
        "question": "An object moves with a constant velocity of 12 m/s along a straight, frictionless horizontal surface. What is the net external force acting on the object?",
        "options": ["12 N in the direction of motion", "0 N", "Depends on the mass of the object", "9.8 N downward"],
        "correct": 1,
        "solution": "Step 1: Understand Newton's First Law. An object moving with constant velocity has zero acceleration (a = 0).\nStep 2: Apply Newton's Second Law: F_net = m · a = m · 0 = 0 N.\nConclusion: When velocity is constant, the net force is strictly zero."
    },
    # Q2
    {
        "num": 2,
        "question": "A heavy wooden crate resting on a concrete floor does not move when pushed with a horizontal force of 40 N. What is the magnitude of the static frictional force opposing the push?",
        "options": ["0 N", "40 N", "Less than 40 N", "Greater than 40 N"],
        "correct": 1,
        "solution": "Step 1: The crate remains in static equilibrium (a = 0).\nStep 2: By Newton's First Law, horizontal forces must balance: F_applied - f_static = 0.\nStep 3: Therefore, f_static = F_applied = 40 N.\nConclusion: Static friction self-adjusts to exactly match the applied force until limiting friction is reached."
    },
    # Q3
    {
        "num": 3,
        "question": "When a tree branch is vigorously shaken, leaves and ripe fruits detach and fall to the ground. This phenomenon is primarily caused by:",
        "options": ["Inertia of motion of the leaves", "Inertia of rest of the leaves and fruits", "Newton's Third Law alone", "Centripetal acceleration"],
        "correct": 1,
        "solution": "Step 1: When the branch is shaken, the branch moves rapidly back and forth.\nStep 2: The leaves and fruits, due to their inertia of rest, tend to remain in their original stationary positions.\nStep 3: This differential displacement creates immense shear stress at the stalks, causing them to detach and fall under gravity."
    },
    # Q4
    {
        "num": 4,
        "question": "A passenger in a moving car is thrown outward while taking a sharp turn at high speed. This is an example of:",
        "options": ["Inertia of rest", "Inertia of motion", "Inertia of direction", "Gravitational deflection"],
        "correct": 2,
        "solution": "Step 1: An object in motion tends to continue traveling in a straight line unless acted upon by an external force (Inertia of Direction).\nStep 2: When the car veers into a curved path, the passenger's body tends to maintain its straight-line tangential path, manifesting as an apparent outward tilt relative to the car."
    },
    # Q5
    {
        "num": 5,
        "question": "In Galileo's double inclined plane experiment, what would happen to a marble released from a height h on an incline if the opposing plane has an angle of zero (horizontal) and friction is absent?",
        "options": ["It travels a distance equal to h and stops", "It continues moving at constant velocity indefinitely", "It slows down due to gravity", "It oscillates back and forth"],
        "correct": 1,
        "solution": "Step 1: On the second incline, the marble attempts to reach its release height h.\nStep 2: If the second plane is horizontal, it never rises to height h.\nStep 3: In the absence of friction, the marble must continue rolling forward at constant velocity indefinitely."
    },
    # Q6
    {
        "num": 6,
        "question": "Which of the following bodies has the greatest inertia?",
        "options": ["A five-rupee coin", "A one-rupee coin", "A 100-rupee note", "A postage stamp"],
        "correct": 0,
        "solution": "Step 1: Inertia is a direct quantitative property of mass.\nStep 2: Among the choices, a five-rupee coin has the highest mass (approximately 9 grams), compared to ~3.8 g for a one-rupee coin and fractions of a gram for paper notes/stamps.\nConclusion: The five-rupee coin possesses the greatest inertia."
    },
    # Q7
    {
        "num": 7,
        "question": "Two forces of 12 N and 5 N act concurrently on a 2 kg block at a 90° right angle to each other. What is the magnitude of the resulting acceleration?",
        "options": ["3.5 m/s²", "6.5 m/s²", "8.5 m/s²", "17.0 m/s²"],
        "correct": 1,
        "solution": "Step 1: Find the magnitude of the resultant force using vector addition for perpendicular vectors:\nF_net = √(F₁² + F₂²) = √(12² + 5²) = √(144 + 25) = √169 = 13 N.\nStep 2: Apply Newton's Second Law: a = F_net / m = 13 N / 2 kg = 6.5 m/s²."
    },
    # Q8
    {
        "num": 8,
        "question": "A force of 10 N acts on a body of mass 2 kg initially at rest. What distance does the body cover in the first 4 seconds?",
        "options": ["20 m", "40 m", "80 m", "160 m"],
        "correct": 1,
        "solution": "Step 1: Calculate acceleration: a = F / m = 10 N / 2 kg = 5 m/s².\nStep 2: Use kinematic equation s = ut + ½at².\nSince the body starts from rest, u = 0.\nStep 3: s = 0 + ½(5)(4²) = ½ × 5 × 16 = 40 m."
    },
    # Q9
    {
        "num": 9,
        "question": "Why does an athlete run a certain distance before taking a long jump?",
        "options": [
            "To gain inertia of rest",
            "To gain inertia of motion which aids in achieving a longer leap",
            "To decrease their mass",
            "To increase friction between shoes and runway"
        ],
        "correct": 1,
        "solution": "Step 1: Running before the jump imparts high horizontal forward velocity to the athlete's body.\nStep 2: At takeoff, this velocity is retained due to inertia of motion, which combines with vertical leap velocity to yield a significantly longer parabolic trajectory."
    },
    # Q10
    {
        "num": 10,
        "question": "If the action force acting on an object is 50 N directed due North, what is the reaction force?",
        "options": ["50 N directed due North", "50 N directed due South acting on the other body", "0 N", "100 N directed due South"],
        "correct": 1,
        "solution": "Step 1: According to Newton's Third Law, for every action there is an equal and opposite reaction.\nStep 2: The reaction force is strictly equal in magnitude (50 N), strictly opposite in direction (due South), and acts on the body that initiated the action."
    },

    # Q11
    {
        "num": 11,
        "question": "A 1500 kg automobile moving at 20 m/s is brought to rest in 5 seconds by the brakes. What is the average braking force applied?",
        "options": ["3000 N", "6000 N", "15,000 N", "30,000 N"],
        "correct": 1,
        "solution": "Step 1: Calculate acceleration: a = (v - u) / t = (0 - 20) / 5 = -4 m/s².\nStep 2: Calculate force: F = m · a = 1500 kg × (-4 m/s²) = -6000 N.\nConclusion: The magnitude of the braking force is 6000 N directed opposite to motion."
    },
    # Q12
    {
        "num": 12,
        "question": "What is the momentum of an elephant of mass 4000 kg strolling at a leisurely pace of 1.5 m/s?",
        "options": ["2667 kg·m/s", "6000 kg·m/s", "60,000 kg·m/s", "4000 kg·m/s"],
        "correct": 1,
        "solution": "Step 1: Formula for linear momentum: p = m · v.\nStep 2: Substitute values: p = 4000 kg × 1.5 m/s = 6000 kg·m/s in the direction of motion."
    },
    # Q13
    {
        "num": 13,
        "question": "A constant force acts on an object of mass 5 kg for a duration of 2 seconds, increasing its velocity from 3 m/s to 7 m/s. What is the magnitude of the applied force?",
        "options": ["5 N", "10 N", "20 N", "25 N"],
        "correct": 1,
        "solution": "Step 1: Find acceleration: a = (v - u) / t = (7 - 3) / 2 = 4 / 2 = 2 m/s².\nStep 2: Apply Newton's Second Law: F = m · a = 5 kg × 2 m/s² = 10 N."
    },
    # Q14
    {
        "num": 14,
        "question": "Which of the following graphs of Momentum (p) versus Velocity (v) for an object of constant mass is correct?",
        "options": [
            "A parabola opening upward",
            "A horizontal line parallel to the v-axis",
            "A straight line passing through the origin with slope equal to mass",
            "A hyperbola asymptotic to both axes"
        ],
        "correct": 2,
        "solution": "Step 1: The equation relating momentum and velocity is p = m · v.\nStep 2: For constant mass m, this is of the form y = mx, which is a straight line passing through the origin (0, 0) whose slope Δp/Δv equals the mass m."
    },
    # Q15
    {
        "num": 15,
        "question": "A hammer of mass 500 g (0.5 kg) moving at 50 m/s strikes a nail and drives it into wood, coming to rest in 0.01 seconds. What is the average force exerted by the hammer on the nail?",
        "options": ["250 N", "2500 N", "5000 N", "25,000 N"],
        "correct": 1,
        "solution": "Step 1: Initial momentum p₁ = 0.5 kg × 50 m/s = 25 kg·m/s.\nStep 2: Final momentum p₂ = 0.\nStep 3: Change in momentum Δp = 0 - 25 = -25 kg·m/s.\nStep 4: Average force F = |Δp| / Δt = 25 / 0.01 = 2500 N."
    },
    # Q16
    {
        "num": 16,
        "question": "A body of mass m is moving with speed v. If its kinetic energy is doubled, what happens to its linear momentum?",
        "options": ["It doubles", "It remains the same", "It increases by a factor of √2", "It quadruples"],
        "correct": 2,
        "solution": "Step 1: Relationship between kinetic energy KE and momentum p: KE = p² / (2m) ⟹ p = √(2m · KE).\nStep 2: If KE' = 2 · KE, then p' = √(2m · 2KE) = √2 · √(2m · KE) = √2 · p.\nConclusion: Linear momentum increases by a factor of √2 (approximately 1.414 times)."
    },
    # Q17
    {
        "num": 17,
        "question": "Why are ceramic teacups more likely to shatter when dropped onto a hard stone floor than when dropped from the same height onto a thick carpet?",
        "options": [
            "The stone floor increases the teacup's change in momentum",
            "The carpet increases the duration of impact, reducing the peak impact force",
            "The carpet absorbs all gravitational energy before impact",
            "The teacup's mass is greater on stone"
        ],
        "correct": 1,
        "solution": "Step 1: Dropped from the same height, the teacup reaches both surfaces with identical momentum and must be brought to rest (same Δp).\nStep 2: On stone, stopping time Δt is nearly zero (milliseconds), yielding an enormous peak force F = Δp/Δt that shatters the ceramic.\nStep 3: On carpet, the fibers compress, prolonging Δt and keeping the impact force below the fracture limit."
    },
    # Q18
    {
        "num": 18,
        "question": "A force of 5 N produces an acceleration of 8 m/s² on a mass m₁, and an acceleration of 24 m/s² on a mass m₂. What acceleration would the same force produce if both masses are tied together?",
        "options": ["4 m/s²", "6 m/s²", "12 m/s²", "16 m/s²"],
        "correct": 1,
        "solution": "Step 1: Find individual masses: m₁ = F / a₁ = 5 / 8 kg; m₂ = F / a₂ = 5 / 24 kg.\nStep 2: Total combined mass M = m₁ + m₂ = 5/8 + 5/24 = 15/24 + 5/24 = 20/24 = 5/6 kg.\nStep 3: Acceleration of combined mass: a = F / M = 5 / (5/6) = 5 × (6/5) = 6 m/s²."
    },
    # Q19
    {
        "num": 19,
        "question": "What is the SI unit of impulse?",
        "options": ["N/s", "N·s (or kg·m/s)", "N·m", "kg·m²/s"],
        "correct": 1,
        "solution": "Step 1: Impulse is defined as Force × time (J = F · Δt).\nStep 2: Therefore, its SI unit is Newton-second (N·s).\nStep 3: In fundamental units: 1 N·s = (1 kg·m/s²) · s = 1 kg·m/s, which is identical to the unit of linear momentum."
    },
    # Q20
    {
        "num": 20,
        "question": "A cricket ball of mass 160 g (0.16 kg) moving at 30 m/s is hit by a bat, returning directly along its original path at 20 m/s. If the contact lasts 0.02 s, what is the average force exerted by the bat?",
        "options": ["80 N", "200 N", "400 N", "800 N"],
        "correct": 2,
        "solution": "Step 1: Taking initial direction as positive: u = +30 m/s, v = -20 m/s.\nStep 2: Change in momentum Δp = m(v - u) = 0.16 × (-20 - 30) = 0.16 × (-50) = -8.0 kg·m/s.\nStep 3: Average force F = |Δp| / Δt = 8.0 / 0.02 = 400 N opposite to initial motion."
    },

    # Q21
    {
        "num": 21,
        "question": "When a person jumps out of a small rowing boat onto a river bank, what happens to the boat?",
        "options": [
            "The boat remains stationary",
            "The boat moves forward toward the bank",
            "The boat moves backward away from the bank into the river",
            "The boat sinks vertically"
        ],
        "correct": 2,
        "solution": "Step 1: To leap forward onto the bank, the person's feet push backward on the boat (Action).\nStep 2: By Newton's Third Law, the boat exerts an equal and opposite forward force on the person (Reaction).\nStep 3: As a result of the backward action force on the boat, the light boat accelerates backward away from the bank."
    },
    # Q22
    {
        "num": 22,
        "question": "A gun of mass 4 kg fires a bullet of mass 50 g (0.05 kg) with a muzzle velocity of 400 m/s. What is the recoil velocity of the gun?",
        "options": ["-2.5 m/s", "-5.0 m/s", "-10.0 m/s", "-20.0 m/s"],
        "correct": 1,
        "solution": "Step 1: Before firing, total momentum is zero: p_initial = 0.\nStep 2: By conservation of momentum: m_bullet · v_bullet + M_gun · V_recoil = 0.\nStep 3: (0.05 × 400) + (4 × V_recoil) = 0 ⟹ 20 + 4 V_recoil = 0 ⟹ V_recoil = -20 / 4 = -5.0 m/s (backward)."
    },
    # Q23
    {
        "num": 23,
        "question": "Why is it difficult for a fireman to hold a hose-pipe which ejects large streams of water at a high velocity?",
        "options": [
            "The hose becomes very heavy due to water weight",
            "The high-speed escaping water exerts an equal and opposite backward reaction force on the hose",
            "Friction between water and the nozzle turns into heat",
            "Atmospheric pressure pushes the hose backward"
        ],
        "correct": 1,
        "solution": "Step 1: The nozzle accelerates huge volumes of water forward at immense velocity (Action).\nStep 2: By Newton's Third Law, the exiting water stream exerts an equal and opposite backward reaction force on the hose.\nStep 3: The fireman must exert significant muscular force to counter this backward reaction thrust."
    },
    # Q24
    {
        "num": 24,
        "question": "Two objects of masses 100 g (0.1 kg) and 200 g (0.2 kg) are moving along the same line in the same direction with velocities of 2 m/s and 1 m/s respectively. They collide, and after collision, the first object moves at 1.67 m/s. What is the velocity of the second object?",
        "options": ["0.50 m/s", "1.165 m/s", "1.50 m/s", "2.00 m/s"],
        "correct": 1,
        "solution": "Step 1: Initial momentum = (0.1 × 2) + (0.2 × 1) = 0.2 + 0.2 = 0.40 kg·m/s.\nStep 2: Final momentum = (0.1 × 1.67) + (0.2 × v₂) = 0.167 + 0.2 v₂.\nStep 3: By conservation of momentum: 0.40 = 0.167 + 0.2 v₂ ⟹ 0.2 v₂ = 0.40 - 0.167 = 0.233 ⟹ v₂ = 0.233 / 0.2 = 1.165 m/s."
    },
    # Q25
    {
        "num": 25,
        "question": "A rocket of mass 1000 kg consumes propellant at a rate of 40 kg/s, ejecting exhaust gas at 2000 m/s relative to the rocket. What is the initial upward thrust force produced on the rocket?",
        "options": ["50 N", "20,000 N", "80,000 N", "800,000 N"],
        "correct": 2,
        "solution": "Step 1: Rocket thrust is given by the rate of momentum ejection: F_thrust = v_exhaust × (Δm / Δt).\nStep 2: Substitute values: F_thrust = 2000 m/s × 40 kg/s = 80,000 N.\nConclusion: The escaping gases exert an upward reaction thrust of 80,000 N."
    },
    # Q26
    {
        "num": 26,
        "question": "A horse pulls a cart forward. According to Newton's Third Law, the cart pulls the horse backward with an equal and opposite force. Why does the horse-cart system accelerate forward?",
        "options": [
            "Because the horse's pull on the cart is slightly greater than the cart's pull on the horse",
            "Because the forward friction/reaction force exerted by the ground on the horse's hooves exceeds the backward resistive forces on the cart",
            "Because Newton's Third Law does not apply to living animals",
            "Because the cart's wheels eliminate all mass"
        ],
        "correct": 1,
        "solution": "Step 1: Action-reaction between horse and cart are internal forces.\nStep 2: To find the acceleration of the horse-cart system, we analyze external horizontal forces on the system.\nStep 3: The horse pushes backward on the ground; the ground pushes forward on the horse's hooves (F_ground). The ground exerts backward rolling friction on the cart wheels (f_cart).\nStep 4: If F_ground > f_cart, the net external force is forward, causing the entire system to accelerate!"
    },
    # Q27
    {
        "num": 27,
        "question": "A stationary bomb of mass 12 kg explodes into two fragments of masses 4 kg and 8 kg. If the velocity of the 4 kg fragment is 20 m/s, what is the speed of the 8 kg fragment?",
        "options": ["5 m/s", "10 m/s", "15 m/s", "20 m/s"],
        "correct": 1,
        "solution": "Step 1: Before explosion, the bomb is at rest: p_initial = 0.\nStep 2: The explosion is driven by internal chemical forces, so total momentum is conserved.\nStep 3: p_final = m₁v₁ + m₂v₂ = 0 ⟹ (4 × 20) + (8 × v₂) = 0 ⟹ 80 + 8 v₂ = 0 ⟹ v₂ = -10 m/s.\nConclusion: The 8 kg piece flies in the opposite direction at a speed of 10 m/s."
    },
    # Q28
    {
        "num": 28,
        "question": "Can an internal force change the total linear momentum of an isolated system?",
        "options": [
            "Yes, if the internal force is very large",
            "No, because internal forces occur in equal and opposite pairs whose vector sum is strictly zero",
            "Yes, during an inelastic collision",
            "Only in a vacuum"
        ],
        "correct": 1,
        "solution": "Step 1: By Newton's Third Law, every internal force exerted by particle i on particle j is balanced by an equal and opposite internal force exerted by j on i (F_ij = -F_ji).\nStep 2: Summing all internal forces: Σ F_internal = 0.\nConclusion: Internal forces can alter individual constituent velocities, but can NEVER change the total momentum of the system."
    },
    # Q29
    {
        "num": 29,
        "question": "A girl of mass 40 kg jumps with a horizontal velocity of 5 m/s onto a stationary cart with frictionless wheels of mass 3 kg. What is her velocity as the cart starts moving?",
        "options": ["4.65 m/s", "5.00 m/s", "3.75 m/s", "2.50 m/s"],
        "correct": 0,
        "solution": "Step 1: Total initial momentum = (m_girl × v_girl) + (m_cart × v_cart) = (40 × 5) + (3 × 0) = 200 kg·m/s.\nStep 2: After jumping onto the cart, combined mass M = 40 + 3 = 43 kg.\nStep 3: By conservation of momentum: 200 = 43 × v_final ⟹ v_final = 200 / 43 ≈ 4.65 m/s."
    },
    # Q30
    {
        "num": 30,
        "question": "An astronaut of mass 80 kg floating freely in deep space throws a 0.5 kg wrench at 20 m/s away from their spacecraft. What is the astronaut's resulting recoil speed?",
        "options": ["0.125 m/s", "0.25 m/s", "1.25 m/s", "2.50 m/s"],
        "correct": 0,
        "solution": "Step 1: Initial momentum p_initial = 0.\nStep 2: By conservation of momentum: m_wrench · v_wrench + M_astro · V_astro = 0.\nStep 3: (0.5 × 20) + (80 × V_astro) = 0 ⟹ 10 + 80 V_astro = 0 ⟹ V_astro = -10 / 80 = -0.125 m/s."
    },

    # Q31
    {
        "num": 31,
        "question": "A student of mass 50 kg stands inside an elevator that accelerates downward at 3 m/s² (take g = 9.8 m/s²). What reading does a spring scale beneath their feet display?",
        "options": ["640 N", "490 N", "340 N", "150 N"],
        "correct": 2,
        "solution": "Step 1: In a downward accelerating frame, equation of motion is: mg - N = ma.\nStep 2: Rearranging for normal contact force N: N = m(g - a).\nStep 3: Substitute values: N = 50 kg × (9.8 - 3.0 m/s²) = 50 × 6.8 = 340 N.\nConclusion: The scale reads 340 N (the student feels noticeably lighter)."
    },
    # Q32
    {
        "num": 32,
        "question": "If the cable supporting an elevator snaps and the cabin falls freely under gravity, what will be the apparent weight of a passenger inside?",
        "options": ["Equal to their true weight mg", "Double their true weight", "Zero (Complete Weightlessness)", "Infinite"],
        "correct": 2,
        "solution": "Step 1: In free fall, downward acceleration a = g.\nStep 2: Apparent weight formula: N = m(g - a) = m(g - g) = 0 N.\nConclusion: The passenger and floor accelerate downward at the identical rate g; the floor exerts zero contact force on the passenger, producing complete weightlessness."
    },
    # Q33
    {
        "num": 33,
        "question": "A block of mass 10 kg is placed on a rough horizontal surface with coefficient of static friction μ_s = 0.4. If a horizontal pull of 30 N is applied, what is the frictional force acting on the block? (Take g = 9.8 m/s²)",
        "options": ["39.2 N", "30 N", "9.2 N", "0 N"],
        "correct": 1,
        "solution": "Step 1: Calculate normal reaction: N = mg = 10 × 9.8 = 98 N.\nStep 2: Calculate maximum limiting static friction: f_max = μ_s × N = 0.4 × 98 = 39.2 N.\nStep 3: Compare applied force F = 30 N with f_max. Since F < f_max, the block does NOT move!\nStep 4: Because the block is stationary, static friction self-adjusts to exactly balance the applied force: f_static = F_applied = 30 N."
    },
    # Q34
    {
        "num": 34,
        "question": "Two masses m₁ = 2 kg and m₂ = 3 kg are connected by a light inextensible string passing over a frictionless pulley (Atwood's machine). Taking g = 10 m/s², what is the acceleration of the system?",
        "options": ["1.0 m/s²", "2.0 m/s²", "5.0 m/s²", "10.0 m/s²"],
        "correct": 1,
        "solution": "Step 1: For Atwood's machine, the net pulling force is the difference in gravitational weights: F_net = (m₂ - m₁)g = (3 - 2) × 10 = 10 N.\nStep 2: The total mass accelerated is (m₁ + m₂) = 2 + 3 = 5 kg.\nStep 3: Acceleration a = F_net / M_total = 10 N / 5 kg = 2.0 m/s²."
    },
    # Q35
    {
        "num": 35,
        "question": "A bullet of mass 20 g moving at 250 m/s penetrates 12.5 cm (0.125 m) into a target before stopping. What is the average resistive force exerted by the target on the bullet?",
        "options": ["500 N", "2500 N", "5000 N", "10,000 N"],
        "correct": 2,
        "solution": "Step 1: u = 250 m/s, v = 0, s = 0.125 m.\nStep 2: Use kinematic relation v² = u² + 2as ⟹ 0 = 250² + 2a(0.125) ⟹ 0 = 62,500 + 0.25 a ⟹ a = -62,500 / 0.25 = -250,000 m/s².\nStep 3: Bullet mass m = 20 g = 0.02 kg.\nStep 4: Resistive force F = m · |a| = 0.02 kg × 250,000 m/s² = 5000 N."
    },
    # Q36
    {
        "num": 36,
        "question": "A vehicle of mass M is traveling at speed v. If the driver applies maximum braking and the vehicle stops in distance d, what would the stopping distance be if the initial speed were doubled to 2v under identical braking force?",
        "options": ["d", "2d", "4d", "8d"],
        "correct": 2,
        "solution": "Step 1: From kinematics, v² = u² + 2as ⟹ 0 = u² - 2ad ⟹ d = u² / (2a).\nStep 2: Since braking force F and mass M are unchanged, deceleration a = F/M is constant.\nStep 3: Stopping distance is directly proportional to the square of initial velocity: d ∝ u².\nStep 4: If u is doubled (2u), d' = (2u)² / 2a = 4 · [u² / 2a] = 4d."
    },
    # Q37
    {
        "num": 37,
        "question": "In the Vaisheshika philosophy of ancient India (~600 BCE), Acharya Kanad categorized 'Vega' as a quality of substances that:",
        "options": [
            "Destroys all atomic structure",
            "Acts as the impressed momentum that sustains continuous motion until opposed",
            "Creates gravitational attraction between planets",
            "Explains the emission of light from fire"
        ],
        "correct": 1,
        "solution": "Step 1: In Vaisheshika Sutras (Chapter 5), Acharya Kanad introduced 'Vega' (impressed motion/momentum).\nStep 2: Kanad observed that when an object is set into motion by an effort (prayatna), Vega is generated within it, which sustains motion in a given direction until counteracted by opposing contacts (friction/resistance)."
    },
    # Q38
    {
        "num": 38,
        "question": "Which of the four fundamental forces of nature is responsible for keeping the protons and neutrons tightly bound inside an atomic nucleus?",
        "options": ["Gravitational force", "Electromagnetic force", "Strong nuclear force", "Weak nuclear force"],
        "correct": 2,
        "solution": "Step 1: Protons are positively charged and experience intense electrostatic repulsion within the tiny femtometer scale of the nucleus.\nStep 2: The Strong Nuclear Force is an attractive, short-range fundamental interaction (~100 times stronger than electromagnetism) that overcomes this repulsion to bind protons and neutrons together."
    },
    # Q39
    {
        "num": 39,
        "question": "According to Einstein's Special Theory of Relativity, why can no massive object ever be accelerated to reach or exceed the speed of light (c)?",
        "options": [
            "Friction in outer space becomes infinite",
            "As velocity approaches c, relativistic momentum and effective inertial resistance approach infinity, requiring infinite force",
            "Gravity pulls the object backward into the past",
            "The object shrinks to zero mass"
        ],
        "correct": 1,
        "solution": "Step 1: In relativistic mechanics, momentum is p = γ m v, where the Lorentz factor γ = 1 / √(1 - v²/c²).\nStep 2: As v approaches c (v → c), √(1 - v²/c²) approaches 0, causing γ and momentum p to diverge to infinity (p → ∞).\nStep 3: Accelerating a particle to c would require an infinite impulse and infinite energy, establishing c as the ultimate cosmic speed limit."
    },
    # Q40
    {
        "num": 40,
        "question": "A 100 kg astronaut holds a 10 kg medicine ball while standing on frictionless ice. The astronaut throws the ball horizontally at 8 m/s. How much work was done by the astronaut's muscles during the throw?",
        "options": ["320 J", "352 J", "640 J", "704 J"],
        "correct": 1,
        "solution": "Step 1: By conservation of momentum, m_ball · v_ball + M_astro · V_astro = 0 ⟹ (10 × 8) + (100 × V_astro) = 0 ⟹ V_astro = -80 / 100 = -0.8 m/s.\nStep 2: Work done by muscles equals total kinetic energy generated:\nW = KE_ball + KE_astronaut.\nStep 3: KE_ball = ½ m v² = ½ × 10 × 8² = 5 × 64 = 320 J.\nStep 4: KE_astronaut = ½ M V² = ½ × 100 × (-0.8)² = 50 × 0.64 = 32 J.\nStep 5: Total work = 320 J + 32 J = 352 J."
    }
]

if __name__ == '__main__':
    assert len(slides_data) == 20, f"Expected 20 slides, got {len(slides_data)}"
    assert len(quiz_questions) == 40, f"Expected 40 quiz questions, got {len(quiz_questions)}"
    for i, q in enumerate(quiz_questions, 1):
        assert q["num"] == i, f"Question number mismatch: {q['num']} != {i}"
        assert len(q["options"]) == 4, f"Question {i} does not have 4 options"
        assert 0 <= q["correct"] <= 3, f"Question {i} invalid correct index"
    print("All 20 slides and 40 quiz questions verified successfully!")

